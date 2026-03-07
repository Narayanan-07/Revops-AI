-- ============================================
-- STATIC TABLES
-- ============================================

CREATE TABLE IF NOT EXISTS company_profile (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  company_name TEXT NOT NULL,
  product_name TEXT NOT NULL,
  product_description TEXT,
  value_proposition TEXT,
  pricing_model TEXT,
  target_company_size TEXT,
  target_industries TEXT[],
  target_roles TEXT[],
  geographies TEXT[],
  created_at TIMESTAMPTZ DEFAULT now()
);

CREATE TABLE IF NOT EXISTS icp_criteria (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  criterion TEXT NOT NULL,
  weight INTEGER DEFAULT 5,
  category TEXT,
  created_at TIMESTAMPTZ DEFAULT now()
);

CREATE TABLE IF NOT EXISTS product_features (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  feature_name TEXT NOT NULL,
  feature_description TEXT,
  pain_point_solved TEXT,
  use_case TEXT,
  created_at TIMESTAMPTZ DEFAULT now()
);

CREATE TABLE IF NOT EXISTS won_deals (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  company_name TEXT,
  industry TEXT,
  employee_count INTEGER,
  pain_points TEXT[],
  features_that_closed TEXT[],
  deal_size TEXT,
  created_at TIMESTAMPTZ DEFAULT now()
);

CREATE TABLE IF NOT EXISTS lost_deals (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  company_name TEXT,
  industry TEXT,
  why_lost TEXT,
  competitor_chosen TEXT,
  created_at TIMESTAMPTZ DEFAULT now()
);

CREATE TABLE IF NOT EXISTS company_intelligence (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  company_name TEXT NOT NULL,
  domain TEXT UNIQUE NOT NULL,
  industry TEXT,
  employee_count TEXT,
  revenue_range TEXT,
  hq_location TEXT,
  founded_year INTEGER,
  funding_stage TEXT,
  crm_used TEXT,
  survey_tools_used TEXT[],
  marketing_tools TEXT[],
  hr_tools TEXT[],
  tech_stack TEXT[],
  uses_competitor_of_surveysparrow BOOLEAN DEFAULT false,
  competitor_names TEXT[],
  last_funding_amount TEXT,
  last_funding_date TEXT,
  recent_news TEXT,
  hiring_for_roles TEXT[],
  leadership_changes TEXT,
  recent_product_launches TEXT,
  likely_pain_points TEXT[],
  created_at TIMESTAMPTZ DEFAULT now()
);

-- ============================================
-- DYNAMIC TABLES
-- ============================================

CREATE TABLE IF NOT EXISTS leads (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  company_name TEXT NOT NULL,
  domain TEXT NOT NULL,
  message TEXT,
  source TEXT DEFAULT 'web_form',
  created_at TIMESTAMPTZ DEFAULT now()
);

CREATE TABLE IF NOT EXISTS transcripts (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  lead_id UUID REFERENCES leads(id) ON DELETE CASCADE,
  transcript_text TEXT NOT NULL,
  inserted_at TIMESTAMPTZ DEFAULT now()
);

CREATE TABLE IF NOT EXISTS lead_context (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  lead_id UUID REFERENCES leads(id) ON DELETE CASCADE,
  stage TEXT CHECK (stage IN (
    'icp_alignment', 'lead_scoring', 'discovery_intelligence'
  )),

  -- Agent 1: ICP Alignment Agent
  icp_alignment_score INTEGER CHECK (icp_alignment_score BETWEEN 0 AND 100),
  buying_intent_summary TEXT,
  pain_point_matches TEXT[],
  firmographic_signals TEXT[],
  technographic_signals TEXT[],
  chronographic_signals TEXT[],
  icp_gaps TEXT[],

  -- Agent 2: Lead Scoring Agent
  fit_score INTEGER CHECK (fit_score BETWEEN 0 AND 100),
  lead_label TEXT CHECK (lead_label IN ('GOOD_LEAD', 'NOT_A_LEAD')),
  buying_signal_strength TEXT CHECK (buying_signal_strength IN ('high', 'medium', 'low')),
  risk_factors TEXT[],
  similar_won_deals TEXT[],
  scoring_reasoning TEXT,

  -- Agent 3: Discovery Intelligence Agent
  exact_customer_needs TEXT[],
  confirmed_buying_intent TEXT,
  feature_recommendations TEXT[],
  demo_focus_areas TEXT[],
  presales_handoff_note TEXT,
  recommended_pricing_tier TEXT,

  updated_by_agent TEXT CHECK (updated_by_agent IN (
    'icp_alignment_agent', 'lead_scoring_agent', 'discovery_intelligence_agent'
  )),
  timestamp TIMESTAMPTZ DEFAULT now()
);

CREATE TABLE IF NOT EXISTS pipeline (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  lead_id UUID REFERENCES leads(id) ON DELETE CASCADE UNIQUE,
  current_stage TEXT CHECK (current_stage IN (
    'icp_alignment',
    'lead_scoring',
    'awaiting_transcript',
    'discovery_intelligence',
    'ready_for_presales',
    'not_a_lead'
  )),
  moved_at TIMESTAMPTZ DEFAULT now(),
  moved_by TEXT
);

-- ============================================
-- ENABLE REALTIME
-- ============================================

-- Safely drop first if re-creating the publication (or just use standard Postgres procedures to add tables)
-- ALTER PUBLICATION supabase_realtime ADD TABLE leads;
-- ALTER PUBLICATION supabase_realtime ADD TABLE lead_context;
-- ALTER PUBLICATION supabase_realtime ADD TABLE pipeline;
-- ALTER PUBLICATION supabase_realtime ADD TABLE transcripts;
