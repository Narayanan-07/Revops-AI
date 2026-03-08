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