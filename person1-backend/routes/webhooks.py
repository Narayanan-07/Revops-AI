import sys
import os
from fastapi import APIRouter
from pydantic import BaseModel
from typing import Any, Dict

router = APIRouter()

# Add person2-agents to path to import crew
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../person2-agents")))

try:
    from crew import trigger_agent
except ImportError:
    # Handle missing trigger_agent module gracefully for Person 1 independent testing
    def trigger_agent(lead_id, stage):
        print(f"[MOCK] trigger_agent called with lead_id={lead_id}, stage={stage}")

@router.post("/trigger/icp-alignment")
async def trigger_icp_alignment(payload: Dict[str, Any]):
    record = payload.get("record", {})
    lead_id = record.get("id")
    if lead_id:
        trigger_agent(lead_id, "icp_alignment")
    return {"status": "ok"}

@router.post("/trigger/discovery-intelligence")
async def trigger_discovery(payload: Dict[str, Any]):
    record = payload.get("record", {})
    lead_id = record.get("lead_id")
    if lead_id:
        trigger_agent(lead_id, "discovery_intelligence")
    return {"status": "ok"}
