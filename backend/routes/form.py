from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional
from database import supabase

router = APIRouter()


class LeadForm(BaseModel):
    company_name: str
    email: str
    message: Optional[str] = ""


def domain_from_email(email: str) -> str:
    """Use the work-email domain as the company's web domain."""
    return email.split("@")[-1].strip().lower()


@router.post("/submit/lead")
async def submit_lead(data: LeadForm):
    """Accept ANY company. The domain is derived from the submitter's work
    email; if that company isn't already in company_intelligence, the
    Enrichment Agent researches it live before ICP analysis runs.

    Inserting the lead fires the Supabase webhook -> /trigger/icp-alignment,
    which now runs: enrichment -> ICP alignment -> lead scoring.
    """
    email = data.email.strip()
    if "@" not in email or "." not in email.split("@")[-1]:
        return {"status": "error", "message": "Please enter a valid work email"}

    domain = domain_from_email(email)

    result = supabase.table("leads").insert({
        "company_name": data.company_name,
        "domain": domain,
        "email": email,
        "message": data.message or "",
        "source": "web_form",
    }).execute()

    return {"status": "ok", "lead_id": result.data[0]["id"], "domain": domain}
