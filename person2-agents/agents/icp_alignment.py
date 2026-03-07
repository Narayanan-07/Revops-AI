import os
import json
import re
from google import genai
from dotenv import load_dotenv

from tools.supabase_tools import (
    get_lead, get_company_intelligence, get_icp_criteria,
    get_company_profile, get_product_features,
    write_lead_context, advance_pipeline
)
from tools.chroma_tools import embed_lead_context

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

def run_icp_alignment_agent(lead_id: str):
    lead = get_lead(lead_id)
    company = get_company_intelligence(lead.get("domain", ""))
    icp = get_icp_criteria()
    profile = get_company_profile()
    features = get_product_features()

    prompt = f"""
    You are the ICP Alignment Agent for SurveySparrow — an AI-powered
    omnichannel experience management platform.

    You have:
    1. An incoming lead's company data (from our pre-loaded intelligence DB)
    2. SurveySparrow's ICP criteria with weights
    3. SurveySparrow's company profile and product features

    Your job:
    - Analyze how well this company aligns with SurveySparrow's ICP
    - Extract buying intent signals from their firmographic data
      (company size, industry, funding stage, revenue)
    - Extract buying intent signals from technographic data
      (what survey tools they use, their CRM, HR tools)
    - Extract buying intent signals from chronographic data
      (recent news, hiring signals, leadership changes, funding)
    - Identify which of their likely pain points SurveySparrow can solve
    - Identify gaps — what we don't know yet

    Return JSON with:
    "icp_alignment_score" (0-100),
    "buying_intent_summary" (string),
    "pain_point_matches" (list of strings),
    "firmographic_signals" (list of strings),
    "technographic_signals" (list of strings),
    "chronographic_signals" (list of strings),
    "icp_gaps" (list of strings)

    Be specific. Use only data provided. Do not hallucinate.
    Write as if briefing a Sales rep before their first call.

    Lead: {lead}
    Company Intelligence: {company}
    Our ICP Criteria: {icp}
    Our Company Profile: {profile}
    Our Product Features: {features}

    Return JSON only. No preamble.
    """

    response = ask_gemini(prompt)
    context = parse_json(response)

    write_lead_context(lead_id, "icp_alignment", context)

    embedding_text = f"""
    Company: {company.get('company_name')} | Industry: {company.get('industry')}
    Employees: {company.get('employee_count')} | Funding: {company.get('funding_stage')}
    Survey Tools: {company.get('survey_tools_used')} | CRM: {company.get('crm_used')}
    ICP Score: {context.get('icp_alignment_score')}
    Buying Intent: {context.get('buying_intent_summary')}
    Pain Points: {context.get('pain_point_matches')}
    """

    embed_lead_context(lead_id, embedding_text)

    advance_pipeline(lead_id, "lead_scoring", "icp_alignment_agent")

    from agents.lead_scoring import run_lead_scoring_agent
    run_lead_scoring_agent(lead_id)
