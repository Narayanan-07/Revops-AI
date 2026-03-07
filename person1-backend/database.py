from supabase import create_client, Client
import os
from dotenv import load_dotenv

load_dotenv()

def get_supabase() -> Client:
    url = os.getenv("SUPABASE_URL", "")
    key = os.getenv("SUPABASE_SERVICE_KEY", "")
    
    if not url or not key:
        print("Warning: SUPABASE_URL or SUPABASE_SERVICE_KEY not set in .env")
        
    return create_client(url, key)

supabase: Client = get_supabase()
