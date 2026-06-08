import os
import json
import re
import google.generativeai as genai
from dotenv import load_dotenv

from tools.supabase_tools import (
    get_lead, get_company_intelligence, get_lead_context,
    get_product_features, get_transcript,
    write_lead_context, advance_pipeline
)
from tools.chroma_tools import embed_lead_context, recall_won_deals

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def ask_gemini(prompt: str) -> str:
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(
        prompt
    )
    return response.text

def parse_json(text: str) -> dict:
    clean = re.sub(r"```json|```", "", text).strip()
    return json.loads(clean)

def run_discovery_intelligence_agent(lead_id: str):
    lead = get_lead(lead_id)
    transcript = get_transcript(lead_id)
    icp_context = get_lead_context(lead_id, "icp_alignment")
    scoring_context = get_lead_context(lead_id, "lead_scoring")
    company = get_company_intelligence(lead.get("domain", ""))
    features = get_product_features()
    
    # Recall similar won deals
    query_text = f"{company.get('company_name')} {company.get('industry')} {icp_context.get('pain_point_matches', [])}"
    similar_deals = recall_won_deals(query_text)

    prompt = f"""
    You are the Discovery Intelligence Agent for SurveySparrow.

    You have:
    1. The full sales call transcript
    2. The ICP Alignment Agent's analysis
    3. The Lead Scoring Agent's analysis
    4. The company's intelligence profile
    5. SurveySparrow's full product feature list
    6. Similar past deals from memory

    Your job:
    - Extract the exact needs the customer expressed on the call
    - Confirm or update the buying intent from previous analysis
    - Map their specific needs to SurveySparrow's features
    - Identify the top 3–5 demo focus areas for the Presales team
    - Write a clear presales handoff note

    Return JSON with:
    "exact_customer_needs" (list of strings),
    "confirmed_buying_intent" (string),
    "feature_recommendations" (list of strings - SurveySparrow features that match),
    "demo_focus_areas" (list of strings),
    "presales_handoff_note" (string),
    "recommended_pricing_tier" (string)

    Write as if handing off to a Presales engineer
    who will run the demo tomorrow.
    Be specific about what to show and in what order.

    Transcript: {transcript}
    ICP Context: {icp_context}
    Lead Scoring Context: {scoring_context}
    Company Intelligence: {company}
    Our Product Features: {features}
    Similar Past Deals: {similar_deals}

    Return JSON only. No preamble.
    """

    response = ask_gemini(prompt)
    context = parse_json(response)

    write_lead_context(lead_id, "discovery_intelligence", context)

    # Embedding logic based on AGENTS.md
    embedding_text = f"""
    Company: {company.get('company_name')} | Industry: {company.get('industry')}
    Employees: {company.get('employee_count')} | Funding: {company.get('funding_stage')}
    Survey Tools: {company.get('survey_tools_used')} | CRM: {company.get('crm_used')}
    ICP Score: {icp_context.get('icp_alignment_score')}
    Buying Intent: {icp_context.get('buying_intent_summary')}
    Pain Points: {icp_context.get('pain_point_matches')}
    Fit Score: {scoring_context.get('fit_score')} | Label: {scoring_context.get('lead_label')}
    Signal Strength: {scoring_context.get('buying_signal_strength')}
    Exact Needs: {context.get('exact_customer_needs')}
    Features Recommended: {context.get('feature_recommendations')}
    """

    embed_lead_context(lead_id, embedding_text)

    advance_pipeline(lead_id, "ready_for_presales", "discovery_intelligence_agent")
