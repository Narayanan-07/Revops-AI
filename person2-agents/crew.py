import os
from dotenv import load_dotenv

# We will import the agent entrypoints once they are created
from agents.icp_alignment import run_icp_alignment_agent
from agents.discovery_intelligence import run_discovery_intelligence_agent

load_dotenv()

def trigger_agent(lead_id: str, stage: str):
    """
    stage: icp_alignment | discovery_intelligence
    Called by Person 1's FastAPI webhook receivers.
    Internally chains: icp_alignment → lead_scoring automatically.
    """
    if stage == "icp_alignment":
        print(f"Triggering ICP Alignment Agent for lead {lead_id}...")
        run_icp_alignment_agent(lead_id)
    elif stage == "discovery_intelligence":
        print(f"Triggering Discovery Intelligence Agent for lead {lead_id}...")
        run_discovery_intelligence_agent(lead_id)

