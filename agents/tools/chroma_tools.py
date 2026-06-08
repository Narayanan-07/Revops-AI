import os
import chromadb
from dotenv import load_dotenv

load_dotenv()

persist_dir = os.getenv("CHROMA_PERSIST_DIR", "./chroma_store")
client = chromadb.PersistentClient(path=persist_dir)

def embed_lead_context(lead_id: str, text: str):
    collection = client.get_or_create_collection("lead_contexts")
    
    # Using python hash to generate a unique string ID. 
    # In a production environment, MD5 or similar might be preferred
    doc_id = f"lead_{lead_id}_{abs(hash(text))}"
    
    collection.add(
        documents=[text],
        ids=[doc_id]
    )

def recall_similar_leads(query_text: str, n_results: int = 3):
    collection = client.get_or_create_collection("lead_contexts")
    count = collection.count()
    if count == 0:
        return []
    results = collection.query(
        query_texts=[query_text],
        n_results=min(n_results, count)
    )
    return results["documents"][0] if results["documents"] else []

def recall_won_deals(query_text: str, n_results: int = 3):
    collection = client.get_or_create_collection("won_deal_patterns")
    count = collection.count()
    if count == 0:
        return []
    results = collection.query(
        query_texts=[query_text],
        n_results=min(n_results, count)
    )
    return results["documents"][0] if results["documents"] else []
