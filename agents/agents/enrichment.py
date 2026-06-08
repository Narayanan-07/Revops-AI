import os
import json
import re
from google import genai
from google.genai import types
from dotenv import load_dotenv

from tools.supabase_tools import (
    get_lead, get_company_intelligence, upsert_company_intelligence,
)

load_dotenv()

# Uses the new google-genai client (same SDK as the lead_scoring agent) because
# Google Search grounding is only exposed through this client.
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def ask_gemini_grounded(prompt: str) -> str:
    """Ask Gemini with live Google Search grounding enabled."""
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
        config=types.GenerateContentConfig(
            tools=[types.Tool(google_search=types.GoogleSearch())],
            temperature=0.2,
        ),
    )
    return response.text


def parse_json(text: str) -> dict:
    """Grounded responses often wrap JSON in prose or code fences. Strip fences,
    then fall back to grabbing the outermost {...} block."""
    clean = re.sub(r"```json|```", "", text).strip()
    try:
        return json.loads(clean)
    except json.JSONDecodeError:
        start = clean.find("{")
        end = clean.rfind("}")
        if start != -1 and end != -1 and end > start:
            return json.loads(clean[start:end + 1])
        raise


def run_enrichment_agent(company_name: str, domain: str) -> dict:
    """Research a company live from the web and persist a company_intelligence
    row (cached by domain). Returns the stored profile."""
    prompt = f"""
    You are the Enrichment Agent for SurveySparrow — an AI-powered omnichannel
    experience management / survey platform.

    Research the following company using live web search and build a structured
    intelligence profile. SurveySparrow competitors include SurveyMonkey,
    Qualtrics, Typeform, Google Forms, Medallia, Jotform, Microsoft Forms.

    Company name: {company_name}
    Domain: {domain}

    Find and infer (use real, current web data — do not invent specifics):
    - industry, employee_count (as a range string), revenue_range, hq_location,
      founded_year (integer), funding_stage
    - crm_used, survey_tools_used, marketing_tools, hr_tools, tech_stack
    - whether they already use a SurveySparrow competitor, and which ones
    - last_funding_amount, last_funding_date
    - recent_news, hiring_for_roles, leadership_changes, recent_product_launches
    - likely_pain_points that SurveySparrow could solve

    Return JSON with EXACTLY these keys:
    "company_name" (string),
    "domain" (string, the domain above),
    "industry" (string),
    "employee_count" (string),
    "revenue_range" (string),
    "hq_location" (string),
    "founded_year" (integer or null),
    "funding_stage" (string),
    "crm_used" (string),
    "survey_tools_used" (list of strings),
    "marketing_tools" (list of strings),
    "hr_tools" (list of strings),
    "tech_stack" (list of strings),
    "uses_competitor_of_surveysparrow" (boolean),
    "competitor_names" (list of strings),
    "last_funding_amount" (string),
    "last_funding_date" (string),
    "recent_news" (string),
    "hiring_for_roles" (list of strings),
    "leadership_changes" (string),
    "recent_product_launches" (string),
    "likely_pain_points" (list of strings)

    Use empty string "" or empty list [] when something genuinely cannot be found.
    Return JSON only. No preamble.
    """

    response = ask_gemini_grounded(prompt)
    profile = parse_json(response)

    # Guarantee the keys we key/route on are always present and correct.
    profile["domain"] = domain
    profile.setdefault("company_name", company_name)

    return upsert_company_intelligence(profile)


def ensure_company_intelligence(lead_id: str) -> dict:
    """Called before ICP Alignment. If we already have intelligence for the
    lead's domain, reuse it; otherwise enrich live from the web."""
    lead = get_lead(lead_id)
    domain = lead.get("domain", "")
    company_name = lead.get("company_name", "")

    existing = get_company_intelligence(domain)
    if existing:
        print(f"[enrichment] Cache hit for {domain}")
        return existing

    print(f"[enrichment] No record for {domain} — enriching from the web...")
    return run_enrichment_agent(company_name, domain)
