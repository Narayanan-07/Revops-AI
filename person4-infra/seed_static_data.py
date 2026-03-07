import os
from dotenv import load_dotenv
from supabase import create_client

load_dotenv()

supabase = create_client(os.getenv("SUPABASE_URL"), os.getenv("SUPABASE_SERVICE_KEY"))

def seed_static_data():
    print("Seeding static data...")
    # 1. SurveySparrow Company Profile
    supabase.table("company_profile").insert({
        
    "company_name": "SurveySparrow",
    "product_name": "SurveySparrow (multi-product suite: SurveySparrow, ThriveSparrow, SparrowDesk, SparrowGenie)",
    "product_description": "AI-powered omnichannel experience management platform for collecting and acting on customer, employee, and NPS feedback through conversational surveys — now expanded into employee experience (ThriveSparrow), AI-first customer support (SparrowDesk), and RFP automation (SparrowGenie)",
    "value_proposition": "Higher response rates through conversational UI, unified CX+EX platform, powerful AI automation, white-labeling, 1500+ integrations, and multi-product suite covering the full feedback-to-action loop",
    "pricing_model": "Response-volume based tiered plans (not per user) — Basic at $19/mo (2,500 responses) to Professional at $249/mo (50,000 responses); Enterprise/NPS+CX Suite at custom pricing. Avg real-world contract ~$4,112",
    "target_company_size": "SMB to mid-market (50–2,000 employees core); enterprise tier available",
    "target_industries": ["SaaS", "Fintech", "Retail", "Healthcare", "BFSI", "HR Tech", "EdTech"],
    "target_roles": ["VP CX", "Head of HR", "VP Product", "Chief People Officer", "Head of Operations"],
    "geographies": ["India", "US", "UK", "SEA", "Middle East"],
    "founded": "2017",
    "headquarters": "Palo Alto, California, USA (operations in Cochin, India)",
    "employees": "~400",
    "revenue": "~$48M ARR (estimated)",
    "funding": "$1.4M seed",
    "customers": "100,000+ across 149 countries"

    }).execute()

    # 2. ICP Criteria
    icp = [
        {"criterion": "B2B company with 50+ employees", "weight": 10, "category": "firmographic"},
        {"criterion": "Has a CX or EX feedback program", "weight": 9, "category": "behavioral"},
        {"criterion": "Currently using Typeform, SurveyMonkey or Google Forms", "weight": 9, "category": "technographic"},
        {"criterion": "Series A or above funding", "weight": 8, "category": "firmographic"},
        {"criterion": "Hiring for CX, HR or Ops roles", "weight": 8, "category": "chronographic"},
        {"criterion": "Has NPS or CSAT tracking need", "weight": 9, "category": "behavioral"},
        {"criterion": "Uses a CRM (HubSpot, Salesforce, Zoho)", "weight": 7, "category": "technographic"},
        {"criterion": "Rapid growth or recent funding", "weight": 7, "category": "chronographic"},
        {"criterion": "Multiple markets or geographies", "weight": 6, "category": "firmographic"},
    ]
    supabase.table("icp_criteria").insert(icp).execute()

    # 3. Product Features
    features = [
        {"feature_name": "Conversational Surveys", "feature_description": "Chat-like survey UI with high response rates", "pain_point_solved": "Low survey response rates", "use_case": "NPS, CSAT, onboarding surveys"},
        {"feature_name": "360° Assessments", "feature_description": "Employee performance and peer feedback", "pain_point_solved": "No structured employee feedback process", "use_case": "HR, L&D teams"},
        {"feature_name": "NPS Tracking", "feature_description": "Real-time NPS dashboard with alerts", "pain_point_solved": "No unified NPS program", "use_case": "CX teams"},
        {"feature_name": "Offline Surveys", "feature_description": "Surveys work without internet connection", "pain_point_solved": "Field teams can't collect feedback offline", "use_case": "Retail, field ops"},
        {"feature_name": "White-labeling", "feature_description": "Full brand customization of surveys", "pain_point_solved": "Generic survey tools break brand experience", "use_case": "Agencies, enterprise"},
        {"feature_name": "Workflow Automation", "feature_description": "Auto-trigger actions based on survey responses", "pain_point_solved": "Manual follow-up after feedback collection", "use_case": "CX ops, HR ops"},
        {"feature_name": "HubSpot Integration", "feature_description": "Native two-way sync with HubSpot CRM", "pain_point_solved": "Feedback data siloed from CRM", "use_case": "Sales + CX teams"},
    ]
    supabase.table("product_features").insert(features).execute()

    # 4. Won Deals
    won = [
        {"company_name": "DiDi", "industry": "Mobility/Tech", "employee_count": 16000, "pain_points": ["Scale feedback across markets", "Low response rates"], "features_that_closed": ["Conversational Surveys", "Workflow Automation"], "deal_size": "Enterprise"},
        {"company_name": "FedEx", "industry": "Logistics", "employee_count": 500000, "pain_points": ["Employee engagement at scale", "Offline feedback"], "features_that_closed": ["360 Assessments", "Offline Surveys"], "deal_size": "Enterprise"},
        {"company_name": "Paysafe", "industry": "Fintech", "employee_count": 3400, "pain_points": ["NPS program", "CX measurement"], "features_that_closed": ["NPS Tracking", "HubSpot Integration"], "deal_size": "Mid-market"},
        {"company_name": "Deloitte Digital", "industry": "Professional Services", "employee_count": 415000, "pain_points": ["360 feedback", "White-label surveys"], "features_that_closed": ["360 Assessments", "White-labeling"], "deal_size": "Enterprise"},
    ]
    supabase.table("won_deals").insert(won).execute()

    print("✅ Static data seeded successfully")

if __name__ == "__main__":
    seed_static_data()
