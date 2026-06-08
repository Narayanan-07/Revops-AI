# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

**RevOps AI** (internal name "ContextBridge" / "7th-dimension") is an AI-powered Revenue Operations pipeline for **SurveySparrow**. When a prospect submits a "Request a Demo" form (company name + work email), an Enrichment Agent researches the company live from the web, then three sequential Gemini agents qualify the lead and — after a sales-call transcript is uploaded — produce a presales intelligence brief. State lives in Supabase (Postgres + Realtime); a React Kanban board visualizes the pipeline in real time.

The repo is organized by layer: `backend/`, `agents/`, `frontend/`, `infra/`.

## Architecture (the parts that span files)

The whole system is an event-driven chain wired through **Supabase database webhooks**, not direct service-to-service calls. Understanding the trigger flow is essential:

```
Form submit (company_name + email) ─POST /submit/lead─> domain = email's domain; leads INSERT
   └─(Supabase webhook)─> POST /trigger/icp-alignment ─> trigger_agent(lead_id,"icp_alignment")
        ├─> Agent 0 (Enrichment): ensure_company_intelligence(lead_id)
        │       cache hit on company_intelligence.domain? reuse : research live (Gemini + Google Search) → upsert
        └─> Agent 1 (ICP Alignment) ─inline call─> Agent 2 (Lead Scoring)
                                                       ├─ GOOD_LEAD (score≥60) → pipeline=awaiting_transcript
                                                       └─ NOT_A_LEAD (<60)     → pipeline=not_a_lead
Transcript: frontend POSTs (paste text OR uploaded file) ─> POST /submit/transcript ─> transcripts INSERT
   └─(Supabase webhook)─> POST /trigger/discovery-intelligence ─> trigger_agent(lead_id,"discovery_intelligence")
        └─> Agent 3 (Discovery Intelligence) → pipeline=ready_for_presales
```

Key cross-cutting facts that aren't obvious from any single file:

- **The form takes company name + work email, not a raw domain.** `backend/routes/form.py` derives `domain` from the email (`email.split("@")[-1]`) and stores both on the `leads` row. There is **no domain gate** — any company is accepted.
- **Enrichment runs before ICP.** `crew.py::trigger_agent(..., "icp_alignment")` first calls `ensure_company_intelligence(lead_id)` (in `agents/agents/enrichment.py`): if the domain already has a `company_intelligence` row it's reused, otherwise the Enrichment Agent researches it live with **Gemini + Google Search grounding** and upserts the row (keyed on `domain`). This is what makes the pipeline work for arbitrary companies, not just seeded ones.
- **Agent 2 has no webhook.** It is called inline at the end of `icp_alignment.py` (`run_lead_scoring_agent(lead_id)`). Only Agents 1 and 3 are webhook-triggered. `crew.py::trigger_agent(lead_id, stage)` only knows two stages: `icp_alignment` and `discovery_intelligence`.
- **The backend imports the agents by `sys.path` hack.** `backend/routes/webhooks.py` appends `../../agents` to `sys.path` and imports `crew`. Agents therefore run **in-process inside the FastAPI worker** as background tasks — there is no separate agent server. If the import fails, a mock `trigger_agent` is substituted (silent no-op printing to stdout) — watch for "FAILED TO IMPORT CREW" on startup.
- **One `lead_context` table, one row per agent per lead, distinguished by `stage`.** All three agents' output columns live in the same flat table; columns for the other stages are left NULL. `write_lead_context` always INSERTs (never updates) and derives `updated_by_agent = f"{stage}_agent"`.
- **`pipeline` is upserted on `lead_id`** (`on_conflict="lead_id"`) — exactly one row per lead, mutated in place via `advance_pipeline`. `pipeline.current_stage` is the single source of truth for the Kanban.
- **The frontend never queries `lead_context` directly.** `useLeads.js` does `from('pipeline').select('*, leads(*, lead_context(*))')` and then flattens `item.leads.lead_context` onto `item.lead_context`. Realtime subscriptions on `pipeline` and `lead_context` re-fetch everything on any change.
- **Kanban columns are cumulative, computed client-side** from a `STAGE_ORDER` map in `useLeads.js` (icp_alignment=0 … ready_for_presales=4, not_a_lead=-1). A lead appears in every column up to its current stage. `not_a_lead` is special-cased to appear only in ICP Alignment + Lead Scoring.
- **Transcripts go through the backend now.** `frontend/.../TranscriptUpload.jsx` POSTs `multipart/form-data` to `POST /submit/transcript` (`backend/routes/transcript.py`) with pasted `text` and/or an uploaded `file`. The backend extracts text (txt/vtt/srt/md decoded; pdf via `pdfplumber`; docx via `python-docx`) and inserts the `transcripts` row (service key). It no longer inserts directly via the Supabase JS client.
- **The seed data (~25 companies) is now just a warm cache.** `company_intelligence` rows are reused when present; unknown domains are enriched on demand. Pre-seeding is optional, not required.
- **ChromaDB is local & filesystem-backed** (`./chroma_store`, in the agents process CWD). Collections: `lead_contexts` (all agents write; Agent 2 reads via `recall_similar_leads`) and `won_deal_patterns` (Agent 3 reads via `recall_won_deals`). Note: `won_deal_patterns` is read but nothing in this repo seeds it, so recalls return `[]` until populated.

## Gotchas specific to this codebase

- **Two different Gemini SDKs are mixed (intentionally).** Agents 1 & 3 use the legacy `google.generativeai` (`genai.GenerativeModel("gemini-1.5-flash")`). Agent 2 and the Enrichment Agent use the new `google-genai` client (`from google import genai; genai.Client(...)`, `gemini-2.5-flash`). The Enrichment Agent *requires* the new SDK because Google Search grounding (`types.Tool(google_search=...)`) is only exposed there. Both packages are in `requirements.txt` (`google-generativeai` + `google-genai`).
- **`employee_count` type mismatch:** `company_intelligence.employee_count` is `TEXT` in `schema.sql`, while `won_deals.employee_count` is `INTEGER`.
- **Enrichment is the slowest, most failure-prone step.** It does a live grounded web search; `parse_json()` in `enrichment.py` is more forgiving than the others (falls back to grabbing the outer `{...}`), and `upsert_company_intelligence` filters to known columns and coerces `founded_year`/`uses_competitor_of_surveysparrow`. If enrichment throws, the whole chain for that lead aborts.
- **JSON parsing is brittle:** every agent ends its prompt with "Return JSON only. No preamble." and uses `parse_json()` which strips ```` ```json ```` fences then `json.loads()`. Malformed model output throws and aborts the chain.
- **No auth anywhere.** Backend uses the Supabase service key; frontend uses the anon key with open RLS. Webhooks are unauthenticated.

## Repository layout

| Dir | Tier | Entry points |
|---|---|---|
| `backend/` | FastAPI (Python) | `main.py` (CORS enabled); routes `form.py` (`POST /submit/lead`), `transcript.py` (`POST /submit/transcript`, file/text), `webhooks.py` (the two `/trigger/*` endpoints); `database.py` (Supabase client singleton) |
| `agents/` | Agent logic (Python) | `crew.py` (dispatcher), `agents/{enrichment,icp_alignment,lead_scoring,discovery_intelligence}.py`, `tools/{supabase_tools,chroma_tools}.py`, `test_agents.py` |
| `frontend/` | React 19 + Vite 6 + Tailwind v4 | `src/App.jsx` routes `/` (LeadForm), `/kanban` (KanbanPage), `/transcripts` (TranscriptUpload); `src/hooks/useLeads.js` is the data core |
| `infra/` | DB schema + seeds | `schema.sql`, `seed_static_data.py`, `seed_company_intelligence.py` |

## Commands

All Python services share the root `requirements.txt`. There is a `venv/` at the repo root. Shell is PowerShell on Windows.

```powershell
# One-time: activate the venv and install deps
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt

# Database setup (run schema.sql in the Supabase SQL editor first, then seed)
# If upgrading an existing DB, also run: ALTER TABLE leads ADD COLUMN IF NOT EXISTS email TEXT;
cd infra
python seed_static_data.py
python seed_company_intelligence.py

# Backend (serves API + runs agents in-process as background tasks)
cd backend
uvicorn main:app --reload --port 8000

# Agents — no server. Smoke-test the full chain end-to-end:
cd agents
python test_agents.py   # inserts a Swiggy lead → enrichment (cache hit) → Agent 1 → Agent 2 inline

# Frontend
cd frontend
npm install
npm run dev       # Vite dev server
npm run build     # production build
npm run lint      # ESLint
npm run preview   # preview built output
```

There is no Python test framework configured; `test_agents.py` is a manual end-to-end script (requires a live Supabase + Gemini key). There are no frontend tests.

## Environment variables

Each Python service loads its own `.env` (via `load_dotenv()`); the frontend uses Vite `VITE_` vars.

- `backend/.env`, `agents/.env`, `infra/.env`: `SUPABASE_URL`, `SUPABASE_SERVICE_KEY` (agents also need `GEMINI_API_KEY`, optional `CHROMA_PERSIST_DIR`).
- `frontend/.env`: `VITE_SUPABASE_URL`, `VITE_SUPABASE_ANON_KEY`, `VITE_BACKEND_URL`.

## Supabase webhooks (must be configured in the dashboard)

| Event | Table | POST URL |
|---|---|---|
| INSERT | `leads` | `<backend>/trigger/icp-alignment` |
| INSERT | `transcripts` | `<backend>/trigger/discovery-intelligence` |

Realtime must be enabled on `pipeline`, `lead_context`, `leads`, `transcripts` (`ALTER PUBLICATION supabase_realtime ADD TABLE ...`; see commented lines at the bottom of `schema.sql`).

## Frontend theme

The UI is a **light theme with a deliberately restricted palette: white, black, orange, green only** (no red/blue/purple). Honor this when adding UI:
- **orange** (`orange-*`, `--color-brand`) → brand, primary actions, in-progress stages, caution/warnings
- **green** (`green-*`, `--color-success`) → success, GOOD_LEAD, positive signals, "ready for presales"
- **black/zinc** → text and the NOT_A_LEAD / disqualified treatment (a dark card, not red)
- **white/stone** → surfaces; semantic tokens (`--color-page/-surface/-surface-2/-border/-ink/-ink-soft`) live in `src/index.css` `@theme`.
