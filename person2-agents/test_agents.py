from supabase import create_client
import os
from dotenv import load_dotenv

load_dotenv()

supabase_url = os.getenv("SUPABASE_URL", "")
supabase_key = os.getenv("SUPABASE_SERVICE_KEY", "")

if not supabase_url or not supabase_key:
    print("Warning: Missing Supabase credentials in .env")

# To test everything locally the user needs to provide their Supabase URL and keys in the .env file.
supabase = create_client(supabase_url, supabase_key) if supabase_url and supabase_key else None

if supabase:
    print("Inserting test lead manually...")
    result = supabase.table("leads").insert({
        "company_name": "Swiggy (Bundl Technologies Private Limited)",
        "domain": "swiggy.com",
        "message": " ",
        "source": "web_form"
    }).execute()
    lead_id = result.data[0]["id"]
    print(f"Test lead: {lead_id}")

    # Trigger Agent 1
    from crew import trigger_agent
    trigger_agent(lead_id, "icp_alignment")
    
    print("Check Supabase: lead_context should have icp_alignment + lead_scoring rows")
    print("Pipeline should show awaiting_transcript or not_a_lead")
else:
    print("Did not insert lead because of missing Supabase credentials.")
