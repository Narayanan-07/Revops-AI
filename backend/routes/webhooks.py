import sys
import os
from fastapi import APIRouter, BackgroundTasks
from typing import Any, Dict

router = APIRouter()

# Add agents to Python path so we can import crew.py
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../agents")))

try:
    from crew import trigger_agent
except Exception as e:
    print(f"FAILED TO IMPORT CREW: {e}")
    def trigger_agent(lead_id, stage):
        print(f"[MOCK] trigger_agent called with lead_id={lead_id}, stage={stage}")


@router.post("/trigger/icp-alignment")
async def trigger_icp_alignment(payload: Dict[str, Any], background_tasks: BackgroundTasks):
    """Called by Supabase webhook on leads INSERT. record.id = lead UUID."""
    record = payload.get("record", {})
    lead_id = record.get("id")
    if lead_id:
        background_tasks.add_task(trigger_agent, lead_id, "icp_alignment")
    return {"status": "ok"}


@router.post("/trigger/discovery-intelligence")
async def trigger_discovery(payload: Dict[str, Any], background_tasks: BackgroundTasks):
    """Called by Supabase webhook on transcripts INSERT.
    record.id = transcript UUID (NOT the lead).
    record.lead_id = the actual lead UUID we need."""
    record = payload.get("record", {})
    lead_id = record.get("lead_id")
    if lead_id:
        background_tasks.add_task(trigger_agent, lead_id, "discovery_intelligence")
    return {"status": "ok"}
