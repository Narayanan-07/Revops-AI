import os
import json
import re
from google import genai
from dotenv import load_dotenv

from tools.supabase_tools import (
    get_company_intelligence, get_lead_context,
    get_won_deals, get_lost_deals, get_lead,
    write_lead_context, advance_pipeline
)
from tools.chroma_tools import embed_lead_context, recall_similar_leads

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def ask_gemini(prompt: str) -> str:
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    return response.text

def parse_json(text: str) -> dict:
    clean = re.sub(r"```json|```", "", text).strip()
    return json.loads(clean)

def run_lead_scoring_agent(lead_id: str):
    lead = get_lead(lead_id)
    icp_context = get_lead_context(lead_id, "icp_alignment")
    company = get_company_intelligence(lead.get("domain", ""))
    
    # Recall similar past leads
    query_text = f"{company.get('company_name')} {company.get('industry')} {icp_context.get('pain_point_matches', [])}"
    similar_leads = recall_similar_leads(query_text)

    won_deals = get_won_deals()
    lost_deals = get_lost_deals()

    prompt = f"""
    You are the Lead Scoring Agent for SurveySparrow.

    You have:
    1. The ICP Alignment Agent's full analysis
    2. The company's intelligence profile
    3. SurveySparrow's historical won and lost deal patterns
    4. Similar past leads recalled from memory

    Your job:
    - Score this lead from 0–100 on likelihood to buy SurveySparrow
    - Classify as GOOD_LEAD or NOT_A_LEAD
      (GOOD_LEAD = score >= 60, NOT_A_LEAD = score < 60)
    - Assess buying signal strength: high / medium / low
    - Identify risk factors that could prevent a deal
    - Reference similar past deals that were won or lost

    Return JSON with:
    "fit_score" (integer 0-100),
    "lead_label" ("GOOD_LEAD" or "NOT_A_LEAD"),
    "buying_signal_strength" ("high", "medium", or "low"),
    "risk_factors" (list of strings),
    "similar_won_deals" (list of strings),
    "scoring_reasoning" (string)

    If NOT_A_LEAD, explain clearly why in scoring_reasoning.

    ICP Analysis: {icp_context}
    Company Intelligence: {company}
    Historical Won Deals: {won_deals}
    Historical Lost Deals: {lost_deals}
    Similar Past Leads: {similar_leads}

    Return JSON only. No preamble.
    """

    response = ask_gemini(prompt)
    context = parse_json(response)

    write_lead_context(lead_id, "lead_scoring", context)

    # Embedding logic based on AGENTS.md
    embedding_text = f"""
    Company: {company.get('company_name')} | Industry: {company.get('industry')}
    Employees: {company.get('employee_count')} | Funding: {company.get('funding_stage')}
    Survey Tools: {company.get('survey_tools_used')} | CRM: {company.get('crm_used')}
    ICP Score: {icp_context.get('icp_alignment_score')}
    Buying Intent: {icp_context.get('buying_intent_summary')}
    Pain Points: {icp_context.get('pain_point_matches')}
    Fit Score: {context.get('fit_score')} | Label: {context.get('lead_label')}
    Signal Strength: {context.get('buying_signal_strength')}
    """

    embed_lead_context(lead_id, embedding_text)

    label = context.get('lead_label')
    if label == "GOOD_LEAD":
        advance_pipeline(lead_id, "awaiting_transcript", "lead_scoring_agent")
    else:
        advance_pipeline(lead_id, "not_a_lead", "lead_scoring_agent")
