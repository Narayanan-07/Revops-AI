from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from database import supabase

router = APIRouter()

class LeadForm(BaseModel):
    company_name: str
    domain: str
    message: str

@router.post("/submit/lead")
async def submit_lead(data: LeadForm):
    # 1. Check domain exists
    exists = supabase.table("company_intelligence").select("id").eq("domain", data.domain).execute()
    if not exists.data:
        # Returning dictionary instead of raising HTTP exception per TASK_PERSON1.md exactly
        return {"status": "error", "message": "Company not in database"}

    # 2. Save lead
    result = supabase.table("leads").insert({
        "company_name": data.company_name,
        "domain": data.domain,
        "message": data.message,
        "source": "web_form"
    }).execute()
    
    return {"status": "ok", "lead_id": result.data[0]["id"]}
