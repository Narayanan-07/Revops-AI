import os
from dotenv import load_dotenv
from supabase import create_client

load_dotenv()

supabase = None
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_SERVICE_KEY")
if url and key:
    supabase = create_client(url, key)

def get_lead(lead_id: str) -> dict:
    result = supabase.table("leads").select("*").eq("id", lead_id).execute()
    return result.data[0] if result.data else {}

def get_company_intelligence(domain: str) -> dict:
    result = supabase.table("company_intelligence").select("*").eq("domain", domain).execute()
    return result.data[0] if result.data else {}

def get_icp_criteria() -> list:
    result = supabase.table("icp_criteria").select("*").execute()
    return result.data if result.data else []

def get_company_profile() -> dict:
    result = supabase.table("company_profile").select("*").execute()
    return result.data[0] if result.data else {}

def get_product_features() -> list:
    result = supabase.table("product_features").select("*").execute()
    return result.data if result.data else []

def get_won_deals() -> list:
    result = supabase.table("won_deals").select("*").execute()
    return result.data if result.data else []

def get_lost_deals() -> list:
    result = supabase.table("lost_deals").select("*").execute()
    return result.data if result.data else []

def get_transcript(lead_id: str) -> str:
    result = supabase.table("transcripts").select("*").eq("lead_id", lead_id).execute()
    return result.data[0]["transcript_text"] if result.data else ""

def get_lead_context(lead_id: str, stage: str) -> dict:
    result = supabase.table("lead_context").select("*").eq("lead_id", lead_id).eq("stage", stage).execute()
    return result.data[0] if result.data else {}

def write_lead_context(lead_id: str, stage: str, data: dict) -> None:
    payload = data.copy()
    payload["lead_id"] = lead_id
    payload["stage"] = stage
    payload["updated_by_agent"] = f"{stage}_agent"
    supabase.table("lead_context").insert(payload).execute()

def advance_pipeline(lead_id: str, stage: str, agent: str):
    supabase.table("pipeline").upsert({
        "lead_id": lead_id,
        "current_stage": stage,
        "moved_at": "now()",
        "moved_by": agent
    }, on_conflict="lead_id").execute()


# Columns that exist on company_intelligence. Used to filter out any
# extra keys the enrichment model may invent before we write the row.
COMPANY_INTELLIGENCE_COLUMNS = {
    "company_name", "domain", "industry", "employee_count", "revenue_range",
    "hq_location", "founded_year", "funding_stage", "crm_used",
    "survey_tools_used", "marketing_tools", "hr_tools", "tech_stack",
    "uses_competitor_of_surveysparrow", "competitor_names",
    "last_funding_amount", "last_funding_date", "recent_news",
    "hiring_for_roles", "leadership_changes", "recent_product_launches",
    "likely_pain_points",
}


def upsert_company_intelligence(profile: dict) -> dict:
    """Insert or update a company_intelligence row, keyed on the unique domain.
    Only known columns are written so the enrichment agent can be loose with
    its JSON. Returns the stored row."""
    row = {k: v for k, v in profile.items() if k in COMPANY_INTELLIGENCE_COLUMNS}

    # Coerce a couple of typed columns so Postgres doesn't reject the write.
    if "founded_year" in row:
        try:
            row["founded_year"] = int(row["founded_year"])
        except (TypeError, ValueError):
            row.pop("founded_year")
    if "uses_competitor_of_surveysparrow" in row:
        row["uses_competitor_of_surveysparrow"] = bool(row["uses_competitor_of_surveysparrow"])

    result = supabase.table("company_intelligence").upsert(
        row, on_conflict="domain"
    ).execute()
    return result.data[0] if result.data else row