import os
from dotenv import load_dotenv
from supabase import create_client

load_dotenv()

supabase = create_client(os.getenv("SUPABASE_URL"), os.getenv("SUPABASE_SERVICE_KEY"))

def seed_companies():
    
    companies = [
{
    "company_name": "Bank of America Corporation",
    "domain": "bankofamerica.com",
    "industry": "Banking & financial services (consumer, commercial, wealth management, and investment banking)",
    "employee_count": "180000-220000",
    "revenue_range": ">$100B annual revenue; 2024 revenue was about $101.9B, and 2025 full-year net income reached $30.5B with Q4 2025 revenue of $28.4B (net of interest expense)",
    "hq_location": "Charlotte, North Carolina, United States",
    "founded_year": 1904,
    "funding_stage": "Public company listed on NYSE under ticker BAC",
    "crm_used": "Salesforce Service Cloud (used to manage Twitter-based customer service and social CRM interactions)",
    "survey_tools_used": [
        "Medallia Experience Cloud (enterprise CX and VoC platform deployed across branches, contact centers, digital banking, and employee experience since 2019)"
    ],
    "marketing_tools": [
        "unknown"
    ],
    "hr_tools": [
        "unknown"
    ],
    "tech_stack": [
        "Medallia Experience Cloud for omnichannel customer and employee feedback management across six countries",
        "Salesforce Service Cloud for Twitter-based and social media customer service CRM workflows",
        "Erica AI virtual financial assistant embedded in consumer and business channels, with 3.2B+ client interactions and ~2M uses per day as of 2025",
        "Extensive internal AI/ML stack with 270+ AI and machine learning models in production across marketing, risk, and operations",
        "CashPro digital banking platform for corporate and commercial clients, processing $1.2T in payments through the CashPro App in 2025"
    ],
    "uses_competitor_of_surveysparrow": True,
    "competitor_names": [
        "Medallia"
    ],
    "last_funding_amount": "unknown",
    "last_funding_date": "unknown",
    "recent_news": "Jan 2026: Reported full-year 2025 earnings of $30.5B, up 19% YoY, with Q4 2025 net income of $7.6B and revenue of $28.4B. 2025-2026: Updated Fast Facts show approximately 213,200 employees, 70M clients, and 94% of client interactions now digital. Sep 2025: Bloomberg reported a senior leadership shake-up framed as a succession-focused reorganization of top executives.",
    "hiring_for_roles": [
        "unknown"
    ],
    "leadership_changes": "September 2025: Bank of America announced a senior leadership shake-up that Bloomberg described as elevating trading leadership and positioning the bank for CEO succession, marking one of the most significant reorganizations of its top ranks in years.",
    "recent_product_launches": "Erica, launched in 2018, has evolved into a primary digital touchpoint integrated into both consumer banking and the CashPro app, handling over 3.2B interactions and solving 98% of inquiries without human intervention. The bank also built an AI-driven marketing simulator using ~30 internal AI models, improving marketing campaign conversion rates by roughly 60%.",
    "likely_pain_points": [
        "Coordinating real-time feedback across roughly 70M clients and multiple channels (branches, contact centers, web, mobile, Zelle, CashPro) is operationally complex",
        "Aligning Medallia's structured CX/EX data with conversational signals from Erica and other AI tools so surveys, proactive alerts, and AI-driven interactions share a single, consistent customer view",
        "Expanding feedback programs across six countries introduces continuous challenges around localization, differing regulatory requirements, and consistent action-planning from survey insights",
        "With approximately 213,200 employees and a history of senior leadership shake-ups aimed at succession, maintaining high employee engagement depends on robust, timely internal pulse and lifecycle surveys",
        "The bank's $13-13.5B annual tech spend and 270+ AI/ML models create a risk that feedback and survey signals become siloed from downstream AI decisioning",
        "Specialized feedback needs for segments like global corporate, wealth management, and high-touch B2B payments (e.g., CashPro and Global Payments Solutions) may require more tailored survey experiences than the core retail-focused Medallia programs"
    ]
},
{
    "company_name": "Calendly LLC",
    "domain": "calendly.com",
    "industry": "Scheduling automation / meeting lifecycle SaaS for sales, recruiting, customer success, and broader go-to-market teams",
    "employee_count": "650-750",
    "revenue_range": "Estimated $144M-$270M ARR (third-party estimates: ~$144.1M revenue and ~$270M ARR by 2023)",
    "hq_location": "Atlanta, Georgia, United States (remote-first company since 2021)",
    "founded_year": 2013,
    "funding_stage": "Late-stage private SaaS company; Series B, total funding ~$350M and valuation ~$3B as of January 2021",
    "crm_used": "unknown",
    "survey_tools_used": [
        "Sprig (used for targeted in-app onboarding surveys to capture thousands of new-user responses within hours)",
        "User Interviews Research Hub (used for research panel management and recruitment of follow-up interview participants)"
    ],
    "marketing_tools": [
        "unknown"
    ],
    "hr_tools": [
        "unknown"
    ],
    "tech_stack": [
        "React and TypeScript front-end with JavaScript, HTML5, and CSS3",
        "Backend services in Python (Flask), plus Java and Go for performance-critical microservices",
        "PostgreSQL as primary relational database",
        "Apache Spark and Apache Beam for big data processing",
        "Apache Airflow for workflow orchestration and scheduling",
        "AWS infrastructure, primarily EC2 for compute and S3 for storage",
        "Kubernetes for container orchestration",
        "Docker for containerization",
        "Jenkins and Buildkite for CI/CD pipelines",
        "Internal collaboration stack including Slack, Jira, Confluence, Google Workspace, and DocuSign"
    ],
    "uses_competitor_of_surveysparrow": True,
    "competitor_names": [
        "Sprig",
        "User Interviews"
    ],
    "last_funding_amount": "$350M Series B (growth + secondary liquidity round led by OpenView and ICONIQ Capital)",
    "last_funding_date": "January 2021",
    "recent_news": "Dec 2024: Calendly conducted a layoff of about 70 employees (~13% of workforce) across engineering, customer experience, marketing, and billing. Dec 4 2024: Appointed Shane Murphy-Reuter (ex-Webflow CMO and ex-ZoomInfo CMO) as President, Go-to-Market. Feb 2026: Published an 'AI Platform Excellence' blog describing a new internal AI platform and agentic infrastructure launched since August 2025.",
    "hiring_for_roles": [
        "Staff Product Manager, New Products (0-to-1 AI-powered product lines for solopreneurs and small businesses)",
        "Staff Product Manager, Scheduling / Core Product",
        "Senior Product Designer, AI Notetaker",
        "Senior Product Designer, Growth",
        "Senior Frontend Platform Engineer, App Platform",
        "Staff Full Stack Engineer, Contacts",
        "Senior Full Stack Engineer, Growth",
        "Machine Learning Engineer",
        "Engineering Manager, Platform Services / Ecosystems",
        "Senior FP&A Analyst and Corporate FP&A Manager",
        "Senior Manager, CX Operations - Systems & Analytics"
    ],
    "leadership_changes": "January 10 2023: Jessica Gilmartin joined as Chief Marketing Officer. December 4 2024: Shane Murphy-Reuter appointed President, Go-to-Market, overseeing sales, marketing, and customer experience as the company pivots to a broader multi-product, AI-powered platform.",
    "recent_product_launches": "2024-2026: AI Notetaker that attends meetings, captures context, tracks action items, and surfaces insights over time, built on an internal agentic AI platform rolled out from August 2025. 2024-2025: Product updates emphasize evolving from a single scheduling tool into a multi-product platform with AI-assisted scheduling, routing, and meeting lifecycle automation.",
    "likely_pain_points": [
        "Coordinating and analyzing high-volume user feedback across multiple research tools is complex: Sprig in-app surveys plus User Interviews creates challenges in unifying qualitative survey data with product analytics at scale",
        "Post-layoff morale and employee experience measurement is critical: successive workforce reductions in 2023 and 2024 increase the need for robust, recurring employee-pulse surveys in a remote-first culture",
        "Shifting from single-product PLG to multi-product AI-driven platform raises new segmentation and feedback needs across distinct personas",
        "GTM reorganization under a new President requires tight alignment of sales, marketing, and CX feedback into a unified system",
        "AI features like Notetaker inherently depend on high-quality labeled feedback to improve models, but existing tools may not fully cover continuous structured rating of AI output quality",
        "Internally they still need holistic visibility into post-meeting satisfaction for enterprise customers, which may not be fully met by their current research-focused stack"
    ]
},
{
    "company_name": "Notion Labs, Inc.",
    "domain": "notion.so",
    "industry": "Productivity and collaboration software / AI workspace and knowledge management platform for teams",
    "employee_count": "950-1050",
    "revenue_range": "Surpassed $600M in annual recurring revenue by late 2025, up from about $400M revenue in 2024 and over $500M ARR earlier in 2025",
    "hq_location": "San Francisco, California, United States (HQ moving to a 105,000 sq ft lease in the Monadnock Building at 685 Market St, downtown SF)",
    "founded_year": 2013,
    "funding_stage": "Late-stage private company; valued around $10B in its October 2021 round and an $11B valuation in a 2025 employee secondary share sale",
    "crm_used": "Salesforce (listed in Notion's marketing and sales tech stack for managing customer and sales workflows)",
    "survey_tools_used": [
        "Gainsight (used for customer health scoring and customer success, including survey-based signals across segments)",
        "Hotjar (used for product experience insights and in-the-moment user feedback and surveys on web properties)"
    ],
    "marketing_tools": [
        "Marketo (marketing automation and demand generation)",
        "Facebook Ads",
        "Google Ads",
        "LinkedIn Ads",
        "Twitter Ads",
        "Contentful (content management for marketing experiences)",
        "ZoomInfo (B2B data and prospecting)",
        "Intercom (in-product messaging and customer engagement)",
        "Zendesk (customer support and ticketing)"
    ],
    "hr_tools": [
        "Workday (core HR and back-office operations)",
        "Greenhouse (recruiting and applicant tracking)",
        "Rippling (HR, payroll, and IT administration)"
    ],
    "tech_stack": [
        "Node.js and Next.js for core application and web front-end",
        "TypeScript, JavaScript, HTML5, CSS3 for client-side development",
        "React as the primary UI library",
        "PostgreSQL as a core transactional data store",
        "Apache Kafka, Apache Spark, Apache Flink, Hadoop, Airflow, and dbt for data processing and pipelines",
        "Amazon Web Services (including EC2, S3, CloudFront, and broader AWS infrastructure)",
        "Docker and AWS Elastic Load Balancing for containerization and deployment",
        "Segment, Google Analytics, Amplitude, Hotjar, Facebook Pixel, and Tableau for analytics and product/marketing insights",
        "Workday, Greenhouse, NetSuite, Tesorio, and Rippling for back-office, finance, and people operations",
        "ProfitWell and Stripe for payments and subscription revenue analytics"
    ],
    "uses_competitor_of_surveysparrow": True,
    "competitor_names": [
        "Gainsight",
        "Hotjar"
    ],
    "last_funding_amount": "$270M secondary share sale (secondary market round)",
    "last_funding_date": "January 26, 2026",
    "recent_news": "September 18, 2025: CNBC reported Notion crossed $500M in annual revenue, driven by AI tools and a customizable AI agent. December 15, 2025: Forbes reported Notion's employee share sale at an $11B valuation, with the company surpassing $600M in ARR with about half of revenue from AI offerings and cash-flow positive. November 2024: Signed a 10-year lease for 105,000 sq ft in the Monadnock Building in downtown San Francisco.",
    "hiring_for_roles": [
        "AI Applications Engineer",
        "Data Engineer, Finance",
        "Data Engineer, Go-To-Market",
        "Engineering Manager, AI Search",
        "Software Engineer, Cloud Infrastructure",
        "Software Engineer, Datastore / Enterprise Data Platform",
        "AI Solutions Specialist",
        "Mid-Market Customer Success Manager",
        "Manager, Solutions Engineering - Enterprise",
        "Product Marketing Manager, IT Solutions / Enterprise Product Marketing Manager",
        "Global Head of GTM Recruiting and Senior GTM Recruiter roles in People/HR"
    ],
    "leadership_changes": "March 2023: Erica Anderson (previously CRO at GitHub) appointed as Chief Revenue Officer. September 2023: Rachel Hepworth announced as first Chief Marketing Officer. December 2023: Fuzzy Khosrowshahi (former creator of Google Sheets and SVP of Product Engineering at Slack) introduced as CTO. May 2025: Katy Shields (prior roles at DoorDash, VSCO, Google X/Waymo) hired as Chief People Officer.",
    "recent_product_launches": "2023-2024: Notion AI launched and expanded with AI writing assistant, AI autofill, and AI-powered Q&A over workspace content. 2024-2025: Customizable AI agent capable of generating documents by aggregating data from various sources, powered by models from OpenAI and Anthropic. 2024-2025: AI Meeting Notes, Enterprise Search, and Notion Mail rolled out as part of a unified AI workspace.",
    "likely_pain_points": [
        "Complex customer-health and feedback modeling: D-R-E-A-M health scoring framework still requires consistent, high-quality survey inputs and manual overrides to avoid misleading health scores across self-serve, SMB, and enterprise segments",
        "Coordinating product-feedback signals across Segment, Amplitude, Hotjar, Google Analytics, Gainsight, and internal telemetry into a single decision-ready view is an ongoing operational challenge",
        "Measuring satisfaction and outcomes for rapidly expanding AI features (Notion AI, AI agent, AI Meeting Notes, Enterprise Search, Notion Mail) across different customer cohorts",
        "Scaling enterprise and multi-product GTM feedback loops - existing tools may not fully cover qualitative deal-loss, implementation, and champion feedback at scale",
        "Employee experience visibility in a high-growth hybrid environment across multiple global offices (San Francisco, New York, Dublin, Hyderabad, Tokyo, Seoul)",
        "As Notion competes directly with Microsoft 365 and Google Workspace, deeply understanding why teams adopt or churn depends on sophisticated segmented survey programs"
    ]
},
{
    "company_name": "Miro",
    "domain": "miro.com",
    "industry": "Visual collaboration / online whiteboard and innovation workspace platform for distributed teams",
    "employee_count": "2500-3000",
    "revenue_range": "Estimated $500-665M in annual recurring revenue (ARR) as of 2024-2025, based on third-party and media estimates",
    "hq_location": "Co-headquartered in San Francisco, CA (201 Spear Street, Suite 1100) and Amsterdam, Netherlands",
    "founded_year": 2011,
    "funding_stage": "Late-stage private company; last primary round was a $400M Series C at a $17.5B valuation in January 2022",
    "crm_used": "Salesforce (listed in Miro's marketing and sales tech stack as a core CRM)",
    "survey_tools_used": [
        "Gainsight (customer success platform with survey and NPS capabilities, used in Miro's go-to-market stack)",
        "Hotjar (experience analytics and on-site survey tool in Miro's analytics stack)"
    ],
    "marketing_tools": [
        "Twitter Ads",
        "Contentful",
        "Salesforce",
        "Circle.so",
        "Zendesk",
        "HubSpot",
        "Ahrefs",
        "SEMrush",
        "Marketo",
        "Google Ads",
        "Workato",
        "Screaming Frog",
        "Gainsight",
        "LinkedIn Ads"
    ],
    "hr_tools": [
        "unknown"
    ],
    "tech_stack": [
        "Languages & frameworks: JavaScript, TypeScript, Java, Ruby, Kotlin, HTML5, CSS3, React, React Native, Next.js, Spring Boot, Ruby on Rails",
        "Development & DevOps: GitHub, Bitbucket, Git, Docker, Kubernetes, Bamboo, Terraform, Apache Maven, Webpack",
        "Hosting & infra: Amazon Web Services (including Amazon EC2), NGINX, Amazon S3, Amazon CloudFront, Amazon Route 53",
        "Data stores: PostgreSQL, Redis, Amazon S3",
        "Analytics: Google Tag Manager, Segment, Looker, Google Analytics, Hotjar, Matomo",
        "Monitoring: Sentry, New Relic, Pingdom",
        "Collaboration & productivity: Slack, Jira, Confluence, Asana, Google Workspace, DocuSign, Webex",
        "Payments & billing: Stripe"
    ],
    "uses_competitor_of_surveysparrow": True,
    "competitor_names": [
        "Gainsight",
        "Hotjar"
    ],
    "last_funding_amount": "$400M Series C primary funding round",
    "last_funding_date": "January 5, 2022",
    "recent_news": "October 2024: Launched AI-driven Innovation Workspace and Intelligent Canvas with over 30 new AI features. October 2025-February 2026: Announced reaching 100M users and 250,000 customer organizations globally. October-November 2024: Laid off roughly 18% of staff (~275 employees), its second major reduction after a February 2023 cut of 119 roles. September 2025: Named to the 2025 Forbes Cloud 100 list. January 14, 2025: Harold Klaje appointed as Chief Revenue Officer.",
    "hiring_for_roles": [
        "Strategic Account Executive (enterprise / strategic sales)",
        "Commercial Account Executive (multiple openings in Austin)",
        "Enterprise Account Executive (San Francisco)",
        "Head of Global Sales Development",
        "Business Development Representative (BDR) roles in Austin and remote",
        "Senior Threat Detection Engineer (security engineering)",
        "Full-Stack / Forward Deployed Engineer (customer-facing engineering)",
        "Enterprise Customer Success Manager (managing portfolios of 25-50 enterprise accounts)",
        "Regional Workplace Manager (office operations and workplace experience in Austin)"
    ],
    "leadership_changes": "February 2023: CEO Andrey Khusid announced a layoff of 119 employees (~7% of headcount). November 2023: Jeff Chow (former CEO and CPO of InVision) joined as Chief Product and Technology Officer. June 2024: Will Rahim serving as Chief Customer Officer. January 14, 2025: Harold Klaje appointed as Chief Revenue Officer.",
    "recent_product_launches": "October 2024: Launch of the Innovation Workspace and Intelligent Canvas with AI docs, prototyping, tables, Sidekicks, and Flows, plus deep integrations with Microsoft Copilot, Power BI, Adobe Express, Glean, and AWS. October 2025: At Canvas 25, announced 100M users and launched AI collaboration tools including Flows, Sidekicks, and Model Context Protocol (MCP) support.",
    "likely_pain_points": [
        "Complex feedback aggregation at massive scale: Miro serves over 100M users and 250,000 customer organizations, making it difficult to systematically capture and synthesize structured feedback across segments using only product analytics and a few survey tools",
        "Fragmented feedback tooling: internal stack includes Hotjar and Gainsight, plus promoted integrations with Qualtrics and Hotjar for customers, leading to fragmented feedback data spread across multiple systems",
        "Measuring the impact of AI Innovation Workspace features - consistently tracking user satisfaction and ROI for AI Canvas, Sidekicks, Flows, and Product Acceleration across enterprise accounts",
        "Post-layoff employee sentiment: two significant layoff waves (7% in early 2023 and ~18% in late 2024) increase the need for reliable recurring employee engagement and pulse surveys",
        "Enterprise GTM feedback loops: with a growing enterprise footprint and a new CRO, Miro needs structured scalable mechanisms to capture feedback from onboarding, renewals, and expansion cycles",
        "Tool-sprawl vs. consolidation narrative: Miro promotes tech stack consolidation messaging for customers but internally uses a wide range of tools, creating a continuing operational challenge"
    ]
},
{
    "company_name": "Toast, Inc.",
    "domain": "toasttab.com",
    "industry": "Restaurant technology / cloud-based point-of-sale and management platform for restaurants and hospitality",
    "employee_count": "6000-7000",
    "revenue_range": "ARR reached about $1.9B by Q2 2025 and exceeded $2.0B by year-end 2025 (26% YoY ARR growth), with FY2025 GAAP net income of $342M and Adjusted EBITDA of $633M",
    "hq_location": "333 Summer St, Boston, MA 02210, United States (global HQ), with additional hubs including San Francisco, Toronto, Dublin, Chicago, Omaha, and Chennai",
    "founded_year": 2011,
    "funding_stage": "Public company listed on NYSE under ticker TOST; before IPO raised ~$903M across 11 funding rounds, including a $400M Series F in February 2020 at a $4.9B valuation",
    "crm_used": "Salesforce (Sales Cloud, Service Cloud, Salesforce CPQ, Field Service, and Community/Experience Cloud used as the unified CRM and service platform across sales, support, and field operations)",
    "survey_tools_used": [
        "Qualtrics (enterprise survey and experience management platform in Toast's internal application utilities stack)",
        "UserTesting (used for structured UX research and qualitative feedback sessions)",
        "Toast Guest Feedback (proprietary real-time guest feedback suite embedded in Toast Go handhelds and Toast digital receipts for thumbs-up/down ratings and comments)"
    ],
    "marketing_tools": [
        "Marketo (marketing automation for campaigns and lead nurturing)",
        "Klaviyo (email marketing platform used for lifecycle and promotional campaigns)",
        "Amplitude (product analytics to measure feature usage and growth funnels)",
        "Appcues (in-app onboarding tours and feature discovery)",
        "Salesforce Marketing Cloud components such as Advertising Studio and Social Studio",
        "Mailgun (transactional and marketing email delivery)"
    ],
    "hr_tools": [
        "Remote (global employment/EOR platform used to support distributed hiring)"
    ],
    "tech_stack": [
        "Core application stack built with Java, Kotlin, JavaScript, HTML5, CSS3, Tailwind CSS, GraphQL, React, and jQuery",
        "Backend services running on Android-based POS clients with a cloud backbone on Amazon Web Services (AWS)",
        "Data layer using PostgreSQL, Amazon DynamoDB, RabbitMQ, Apache Pulsar, Splunk, and pgBouncer",
        "Application utilities including Okta (identity), Smartsheet (work management), UserTesting, JAMF (device management), and Qualtrics",
        "Salesforce and Salesforce Service Cloud as the primary CRM and service backbone, tightly integrated with Zendesk and QuickBooks via Workato",
        "Product and growth tooling including Amplitude, Appcues, Klaviyo for email campaigns",
        "Engineering tooling such as GitHub, Jenkins, Docker"
    ],
    "uses_competitor_of_surveysparrow": True,
    "competitor_names": [
        "Qualtrics",
        "UserTesting"
    ],
    "last_funding_amount": "unknown",
    "last_funding_date": "February 14, 2022 (Corporate Minority P2P round with undisclosed amount, following a $400M Series F in February 2020)",
    "recent_news": "February 2026: Toast reported Q4 and full-year 2025 results, with GPV up 23% YoY to $195.1B, ARR exceeding $2.0B (26% YoY growth), approximately 164,000 restaurant locations (+22% YoY), and FY2025 GAAP net income of $342M versus $19M in 2024. September 2025: At Goldman Sachs Communicopia + Technology Conference, highlighted 31% YoY gross profit growth in Q2, strong international traction, and expansion into enterprise brands like Dine Brands and Marriott.",
    "hiring_for_roles": [
        "Hybrid Development Representative (multiple markets; outbound sales and prospecting for restaurant customers)",
        "Senior Manager, CX Strategy & Analytics",
        "Manager, Customer Success - Mid-Market (MM)",
        "Product Designer, Ads & Insights",
        "Tech Lead / Staff Full Stack Engineer - Upsells Platform (building a generative AI-driven upsell suggestions platform)",
        "Full Stack and Backend Software Engineers across payments, platform, and restaurant experience teams"
    ],
    "leadership_changes": "September 4, 2023: Toast announced co-founder and COO Aman Narang would become CEO effective January 1, 2024, succeeding long-time CEO Chris Comparato, who moved to a board-only role.",
    "recent_product_launches": "2019-present: Toast Guest Feedback, a real-time feedback suite built into Toast Go handheld POS devices and digital receipts. 2025: Toast Go 3 hardware (~16% lighter), new KDS food-runner tracking features, and pilots of AI-driven dynamic pricing. 2025-2026: New Upsells platform using generative AI models to provide smart, real-time upsell suggestions to front-of-house staff.",
    "likely_pain_points": [
        "Coordinating guest feedback across 160,000+ restaurant locations: Guest Feedback currently focuses on quick thumbs-up/down ratings that generate large volumes of unstructured data needing normalization and analysis at scale",
        "Fragmented internal feedback stack: simultaneously operates its own guest feedback product and internally uses Qualtrics and UserTesting, increasing the risk that feedback lives in separate systems",
        "Measuring the impact of AI-driven upsell and pricing features requires continuous fine-grained evaluation not possible with generic survey flows",
        "Restaurant-level NPS/CSAT and churn risk: with ARR exceeding $2B and 160,000+ locations, small percentage changes in restaurant churn materially affect growth",
        "Employee and field-team experience visibility: Toast has grown to ~6,500 employees with global hubs and is actively reorganizing around AI initiatives",
        "Partner and ecosystem feedback across payments, lending (Toast Capital), payroll/HR, marketing, and numerous third-party integrations"
    ]
},
{
    "company_name": "Zapier",
    "domain": "zapier.com",
    "industry": "No-code automation / iPaaS platform connecting 7,000+ web apps for workflow automation",
    "employee_count": "1000-1300",
    "revenue_range": "Estimated $310M revenue in 2024, up from about $250.7M in 2023, with projections around $400M for 2025",
    "hq_location": "Fully remote company with a registered headquarters at 548 Market St #62411, San Francisco, CA 94104, United States",
    "founded_year": 2011,
    "funding_stage": "Profitable, late-stage private company; has raised only about $2.6M across early seed/angel rounds and a later secondary transaction, with a ~$5B valuation reported in 2021",
    "crm_used": "HubSpot CRM (HubSpot is Zapier's central source of truth for company data, used across Sales Hub, Marketing Hub, and Operations Hub)",
    "survey_tools_used": [
        "Gainsight Customer Communities (used to run and scale the Zapier Community, capture customer questions and experience signals, and power self-service support)"
    ],
    "marketing_tools": [
        "HubSpot Marketing Hub (used alongside Sales and Operations Hubs as the core marketing and CRM platform)"
    ],
    "hr_tools": [
        "unknown"
    ],
    "tech_stack": [
        "Backend built primarily with Python and Django",
        "Frontend using JavaScript, React, Redux, HTML5, and CSS3",
        "Infrastructure on AWS including Amazon EC2, AWS Lambda, and Amazon VPC",
        "Data stores including Amazon Redshift, MySQL, Memcached, Redis, McRouter, and Celery for asynchronous task processing",
        "Build and deployment tooling such as Jenkins, Terraform, Babel, Webpack, Gulp, Ansible",
        "Search and application utility layer using Elasticsearch",
        "Extensive product and GTM stack around HubSpot, Gainsight Customer Communities, and Zendesk"
    ],
    "uses_competitor_of_surveysparrow": True,
    "competitor_names": [
        "Gainsight Customer Communities"
    ],
    "last_funding_amount": "unknown",
    "last_funding_date": "January 14, 2021 (secondary market transaction; amount undisclosed)",
    "recent_news": "2024-2025: Multiple analyses report Zapier generated about $310M in revenue in 2024 and is projected to reach ~$400M in 2025, with a valuation around $5B. October-November 2025: Appointed Brandon Sammut as first Chief People & AI Transformation Officer, with internal stats indicating 97% of employees now use AI in daily work. September 2023: Announced general availability of Tables (an automation-first database) and introduced Canvas, an AI-powered flowchart tool.",
    "hiring_for_roles": [
        "Sr. Director, Engineering - Applied AI",
        "Campaign Marketing Manager (AI Enterprise)",
        "Principal Growth Marketer",
        "Data Engineer (Data team, remote in NAMER/EMEA)",
        "Applied AI Engineer",
        "Engineer, Backend (Events Team)",
        "Engineer, Full Stack (Revenue Zone)",
        "Sr. Product Manager - AI Capabilities",
        "Account Executive, Large Enterprise",
        "Manager & Sr. Manager roles in Mid-Market and Enterprise Sales",
        "Sr. Frontend Engineer (Enterprise zone)",
        "Sr. Manager, AI & Machine Learning"
    ],
    "leadership_changes": "October-November 2025: Zapier elevated Brandon Sammut into a new C-suite role as Chief People & AI Transformation Officer, explicitly tying people leadership to AI transformation. Co-founder Wade Foster remains CEO, supported by co-founders Bryan Helmig (CTO) and Mike Knoop (Head of Zapier AI), and CFO Rajiv Krishnarao.",
    "recent_product_launches": "September 2023: General availability of Zapier Tables, an automation-first database. September 2023: Launch of Canvas, an AI-powered flowchart tool for mapping end-to-end business processes and turning them into Zaps. 2023-2025: AI-first product direction including AI workflow drafting, enhanced visual editor supporting multi-path workflows, and stronger admin controls for enterprise governance.",
    "likely_pain_points": [
        "Unifying customer feedback across HubSpot, Gainsight Customer Communities, and support channels is complex: synthesizing structured CRM data, community signals (125,000 monthly visitors, 240,000 page views), and support interactions into a single feedback view is non-trivial",
        "At Zapier's scale (millions of users, 100,000+ paying customers, 3M+ companies), systematically capturing and segmenting customer sentiment by use case, industry, and plan level goes beyond what community analytics alone can provide",
        "Measuring satisfaction and outcomes for new AI features (Tables, Canvas, AI-generated workflows) requires continuous feedback loops distinguishing between core automation users and new AI-first users",
        "Employee-experience visibility in a fully remote, AI-transforming org across 40+ countries requires robust recurring internal feedback and pulse surveys",
        "As Zapier intensifies its enterprise push, it needs tighter GTM feedback loops on enterprise requirements, onboarding, and renewal risks beyond what HubSpot CRM notes and community posts can capture",
        "Internal reliance on multiple platforms (HubSpot, Gainsight Communities, Zendesk) creates ongoing challenge to avoid fragmented feedback silos"
    ]
},
{
    "company_name": "Duolingo, Inc.",
    "domain": "duolingo.com",
    "industry": "EdTech / mobile-first language and multi-subject learning platform (languages, math, music, chess)",
    "employee_count": "700-900",
    "revenue_range": "Approximately $1.0-1.04B revenue in FY2025, up ~39% YoY from $748M in 2024",
    "hq_location": "5900 Penn Avenue, Pittsburgh, Pennsylvania 15206, United States",
    "founded_year": 2011,
    "funding_stage": "Public company listed on NASDAQ under ticker DUOL; raised about $183M in venture funding before its 2021 IPO",
    "crm_used": "Salesforce (listed in Duolingo's marketing and sales tech stack)",
    "survey_tools_used": [
        "unknown"
    ],
    "marketing_tools": [
        "Facebook Ads",
        "Google Ads",
        "Sprout Social",
        "Pardot / Salesforce Marketing Cloud Account Engagement",
        "Zendesk",
        "Salesforce (used across sales and marketing operations)"
    ],
    "hr_tools": [
        "Workday (core HRIS)",
        "Greenhouse (ATS used alongside Workday)",
        "Paycor",
        "Gem (talent sourcing)",
        "Prelude (interview scheduling)"
    ],
    "tech_stack": [
        "Languages & frameworks: Python, Java, JavaScript, Kotlin, Swift, C, C++, Scala, R, Flask, Backbone.js, HTML5, CSS3",
        "Back-end services originally in Python with core session generator and engine rewritten in Scala running on the JVM",
        "Application hosting on Amazon Web Services (EC2, S3, AWS ELB, Route 53) plus Microsoft Azure and NGINX",
        "Data stores: Amazon S3, MySQL, PostgreSQL, Amazon DynamoDB, Google BigQuery",
        "Analytics: Google Analytics, Google Tag Manager, Facebook Pixel",
        "Monitoring & performance: New Relic",
        "Security & utilities: OneTrust, HackerOne, Jupyter, Airtable, Shopify",
        "Collaboration & productivity: Google Workspace, Slack, Jira, Confluence, Asana, Zoom, DocuSign"
    ],
    "uses_competitor_of_surveysparrow": False,
    "competitor_names": [],
    "last_funding_amount": "$35M primary capital raise in Series H at a $2.4B valuation (pre-IPO); IPO then raised about $520.8M in July 2021",
    "last_funding_date": "July 28, 2021 (IPO); last private round was November 18, 2020 (Series H)",
    "recent_news": "August 6, 2025: Reported Q2 2025 results with 41% total revenue growth, 46% subscription revenue growth, and record profitability, highlighting the Energy mechanic and a Chess course. January 12, 2026: Announced CFO transition - Matthew Skaruppa stepping down, board member Gillian Munson appointed as new CFO. 2024-2026: Repositioning as a multi-subject learning platform extending into math, music, and chess with Max-style AI capabilities.",
    "hiring_for_roles": [
        "AI Product Engineer, Math",
        "Staff AI Research Engineer",
        "Senior Data Scientist",
        "Senior Software Engineer, Backend",
        "Senior iOS Software Engineer",
        "Senior Site Reliability Engineer",
        "Group Product Manager, Growth",
        "Director of Product Design",
        "Senior Product Designer, Music",
        "Learning Designer, Math",
        "Director of Payroll (People Operations / HR)",
        "Associate Product Manager, Recent Grad",
        "Software Engineer, New Graduate"
    ],
    "leadership_changes": "January 12, 2026: CFO Matthew Skaruppa will step down and be succeeded by board member and Audit Committee Chair Gillian Munson as Chief Financial Officer. Co-founder Luis von Ahn remains CEO while co-founder Severin Hacker serves as CTO.",
    "recent_product_launches": "2023-2025: Expanded beyond languages by launching dedicated courses in Math and Music inside the main app, and in 2025 began rolling out a Chess course. 2023-2024: Introduced the Energy feature for daily learning pacing. 2024-2026: Rolling out AI-powered learning experiences using generative models to power conversational speaking practice, faster content creation, and more adaptive exercises.",
    "likely_pain_points": [
        "Coordinating and interpreting user feedback at massive scale: 130M+ MAUs and 46M+ DAUs, making it challenging to capture structured sentiment signals across cohorts, devices, and subjects using only in-app telemetry and app-store reviews",
        "Measuring learning outcomes and satisfaction for new subjects like math, music, and chess requires more granular subject-specific feedback loops beyond generic engagement metrics",
        "Evaluating AI-driven learning experiences: increasingly relying on AI to generate exercises and power conversational practice, creating an ongoing need for structured feedback on AI output accuracy and user trust",
        "Balancing gamification with perceived educational rigor: must continuously test whether changes to streaks, leaderboards, and reward systems are improving long-term learning satisfaction or just short-term engagement",
        "Understanding cohort-level sentiment as the company optimizes for profitability through price increases and cost discipline, which can introduce churn risks among price-sensitive learners",
        "Employee experience and change management as headcount grew from ~500 in 2022 to ~830 by 2025, with hybrid expectations centered on Pittsburgh and other hubs"
    ]
},
{
    "company_name": "ZoomInfo Technologies Inc.",
    "domain": "zoominfo.com",
    "industry": "B2B go-to-market / sales and marketing intelligence software platform",
    "employee_count": "3000-3200",
    "revenue_range": "Approximately $1.25B GAAP revenue in FY2025 (+3% YoY). GAAP operating income $225.7M; adjusted operating income $445.9M",
    "hq_location": "Vancouver, Washington, United States (global headquarters; moving into a new 366,000 sq ft Terminal 1 HQ building on the Columbia River waterfront)",
    "founded_year": 2007,
    "funding_stage": "Public company listed on NASDAQ under ticker GTM (formerly ZI). Last noted financing was post-IPO equity",
    "crm_used": "unknown",
    "survey_tools_used": [],
    "marketing_tools": [],
    "hr_tools": [],
    "tech_stack": [
        "Snowflake as the primary data warehouse (ZoomInfo describes itself as a warehouse-first company)",
        "Databricks as a serverless MLOps and data processing platform",
        "Airflow for data orchestration on AWS, with similar orchestration on GCP",
        "AWS as a core cloud provider for data platform and application infrastructure",
        "GCP used alongside AWS for parts of the data platform and orchestration",
        "Monte Carlo for data observability across the enterprise data platform",
        "Atlan for data cataloging and data discovery",
        "Internal ZoomInfo Data Platform (ZDP) and Enterprise Data Platform (EDP)"
    ],
    "uses_competitor_of_surveysparrow": False,
    "competitor_names": [],
    "last_funding_amount": "unknown",
    "last_funding_date": "unknown",
    "recent_news": "February 9, 2026: Reported Q4 and full-year 2025 results with GAAP revenue of $319.1M in Q4 2025 (+3% YoY) and full-year 2025 GAAP revenue of $1,249.5M (+3% YoY), GAAP operating income of $225.7M, and unlevered free cash flow of $454.9M. August 4, 2024: Appointed two new independent directors, Domenic Maida and Owen Wurzbacher, to its Board to strengthen AI and data expertise. April 14, 2025: Major ZoomInfo Copilot updates including automatic account tracking, expanded AI emailer for renewals and upsells, and deal-risk alerts.",
    "hiring_for_roles": [
        "Senior Data Engineering Analyst",
        "Partner Solutions Engineer III",
        "Senior Principal Software Engineer / Principal Software Engineer (distributed systems, APIs, data pipelines using ML and LLMs)",
        "Senior Software Engineer (backend, Java/Node.js)",
        "Senior Sales Development Representative - Enterprise Customer (multiple locations)",
        "SMB / Mid-Market Account Executive roles",
        "Customer Success Manager III and ZTS Customer Success Manager III (enterprise and strategic accounts)",
        "Senior Product Manager roles including Context Engineering and Predictive Analytics"
    ],
    "leadership_changes": "August 4, 2024: Appointed Domenic Maida (former Bloomberg Chief Data Officer) and investor Owen Wurzbacher as independent directors, while Todd Crockett stepped down. Founder Henry Schuck continues as CEO and Chairman, publicly positioning ZoomInfo as an AI-powered GTM platform.",
    "recent_product_launches": "2024-2025: ZoomInfo Copilot launched and expanded - an AI assistant embedded in GTM Workspace with AI-generated emails, meeting prep summaries, risk alerts, buying-signal feeds, and CRM-embedded signals for Salesforce and HubSpot. 2024-2026: GTM Studio and GTM Workspace as a unified execution layer including a Waterfall Enrichment engine that queries 25-40+ third-party vendors in parallel.",
    "likely_pain_points": [
        "Customer experience and NPS improvement at scale: own public NPS via Comparably sits in the mid-20s with roughly one-third of customers classified as detractors",
        "Fragmented feedback across multiple surfaces: customer sentiment and product feedback scattered across in-app usage, support channels, community reviews, and sales interactions, making it difficult to maintain a single structured view",
        "Measuring satisfaction and ROI for new AI features (Copilot, Waterfall Enrichment, GTM Studio) requires targeted cohort-based surveys that can segment by industry, motion, and maturity",
        "Internal employee sentiment during efficiency-driven changes: headcount declined about 9.35% year-over-year to 3,180 employees as of December 31, 2025",
        "Aligning GTM and product teams around unified feedback signals: internally synthesizing feedback from sales, CS, product analytics, and Comparably into prioritized product roadmaps is a complex ongoing challenge",
        "Customer-facing proof of value and outcome reporting for Copilot and GTM Studio requires survey-style feedback to validate AI-driven workflows"
    ]
},
{
    "company_name": "Gusto, Inc.",
    "domain": "gusto.com",
    "industry": "HR and payroll technology / people platform for small businesses (payroll, benefits, HR, compliance)",
    "employee_count": "2000-2500",
    "revenue_range": ">$500M revenue in FY2023 (reported May 2024); 401(k) ARR grew ~50% YoY and Gusto Money ARR >140% YoY in 2024",
    "hq_location": "525 20th Street, San Francisco, CA 94107, United States (flagship HQ with additional offices in Denver, New York, and Istanbul)",
    "founded_year": 2011,
    "funding_stage": "Late-stage private unicorn (Series E+); total funding ~$746M, last major round $425M Series E in June 2021 at ~$9.5B valuation; June 2025 tender offer of $200M+ for employee liquidity",
    "crm_used": "unknown",
    "survey_tools_used": [],
    "marketing_tools": [],
    "hr_tools": [],
    "tech_stack": [
        "Languages & frameworks: Ruby on Rails, Bootstrap, JavaScript, Python, HTML5, Java, ES6, CSS3, PHP, Ruby, Kotlin, Swift, GraphQL",
        "Development & DevOps: Kubernetes, Terraform",
        "Libraries: React",
        "Application hosting: Apex, NGINX",
        "Data stores: Apache Spark, Hadoop",
        "Analytics: Google Analytics, Mixpanel, Amplitude",
        "Monitoring: Bugsnag, New Relic",
        "Assets and media: Amazon CloudFront",
        "Communications: Mailgun, Mandrill"
    ],
    "uses_competitor_of_surveysparrow": False,
    "competitor_names": [],
    "last_funding_amount": "$200 million+ tender offer (employee liquidity round)",
    "last_funding_date": "June 2025",
    "recent_news": "June 2025: Launched a $200M+ tender offer for employee liquidity. September 2024: Introduced Gus, an AI assistant for small business owners that answers questions, provides personalized insights, and executes tasks like PTO approvals and salary changes with user confirmation. 2023-2024: Expanded 401(k) business with ~50% YoY ARR growth and Gusto Money spending accounts with >140% YoY ARR growth, while surpassing $500M total revenue in FY2023.",
    "hiring_for_roles": [
        "Senior Product Manager, Time Tools",
        "Technical Enterprise Client Success Manager - Symmetry",
        "Senior Product Manager, Benefits & PEO (multiple roles)",
        "Senior Product Manager, Unified Service Platform",
        "Senior Product Design Lead, Payments & Risk Platform",
        "Senior Accountant (Platform Accounting)",
        "Program Manager",
        "Tools Administration Lead"
    ],
    "leadership_changes": "2012-present: Co-founders Josh Reeves (CEO), Edward Kim (CTO), and Tomer London (CPO) continue to lead Gusto, with Reeves guiding the evolution from payroll to a full people platform.",
    "recent_product_launches": "September 2024: Gusto launched Gus, an AI assistant that provides personalized insights, answers compliance/tax questions, and executes tasks like salary changes or PTO approvals with final user confirmation. 2023-2024: Expanded embedded payroll (Gusto 27) to 186K small businesses through partners, grew 401(k) business, and launched Gusto Money spending accounts.",
    "likely_pain_points": [
        "Customer feedback management across payroll, benefits, and HR workflows: serves 300K+ SMBs with embedded payroll in 186K businesses, generating diverse feedback that needs to be unified and prioritized beyond basic support tickets",
        "Measuring satisfaction for AI features like Gus: the AI assistant handles sensitive tasks (salary changes, PTO), requiring continuous structured feedback on accuracy, trust, and user value",
        "SMB customer health and churn prevention: with rapid growth in 401(k) and Gusto Money, must track segmented NPS and satisfaction to identify at-risk accounts",
        "Employee experience in a high-growth, distributed workforce across San Francisco, Denver, New York, and Istanbul",
        "Partner and embedded ecosystem feedback: Gusto 27 partners represent 186K businesses, creating a need for structured feedback loops on API reliability, onboarding ease, and partner satisfaction",
        "Compliance and regulatory sentiment: as a payroll/HR platform handling sensitive data for SMBs, must continuously gauge customer confidence in compliance features through targeted surveys"
    ]
},
{
    "company_name": "Lenskart Solutions Limited",
    "domain": "lenskart.com",
    "industry": "Omnichannel D2C eyewear retail (prescription eyewear, sunglasses, contact lenses, eye checkups, and accessories)",
    "employee_count": "17000-18000",
    "revenue_range": "FY2025 operating revenue ~$794M (~\u20b96,652 crore), up 22.5% YoY from FY2024. FY25 net profit \u20b9297 crore (first profitable year). International revenue ~$300M, India ~$455M",
    "hq_location": "Sector 43, Golf Course Road, Gurugram, Haryana 122002, India (global HQ). Additional hubs in Singapore and Dubai",
    "founded_year": 2010,
    "funding_stage": "Late-stage unicorn; total funding ~$2.12B. Last formal round: Series I ($500M from ADIA in March 2023, $100M from ChrysCapital in June 2023). DRHP filed with SEBI in July 2025 for ~$257M IPO (fresh issue). Valuation ~$5B as of secondary trades",
    "crm_used": "CleverTap (primary customer engagement and CRM platform for omnichannel marketing automation, unifying online and offline customer data, and orchestrating campaigns across push notifications, email, SMS, and WhatsApp at scale)",
    "survey_tools_used": [
        "CleverTap NPS (built-in NPS survey feature within CleverTap's Web Pop-up & In-App Messaging)",
        "WebEngage (used for customer engagement and retention journeys)"
    ],
    "marketing_tools": [
        "CleverTap (omnichannel marketing automation across push, email, SMS, WhatsApp, and in-app across 40M+ users)",
        "WebEngage (engagement journey orchestration, retargeting, and lifecycle automation)",
        "Google Analytics (web digital analytics)",
        "Power BI (business intelligence and visualization for marketing and operations analytics)"
    ],
    "hr_tools": [
        "unknown"
    ],
    "tech_stack": [
        "Cloud infrastructure: AWS (primary cloud), with data lake built on AWS S3 and compute on reserved/spot EC2 instances in private subnets",
        "Container orchestration: Kubernetes (Kops on AWS), Helm for templated deployment, Rook for storage",
        "CI/CD: Internally built CI/CD pipelines on top of git, integrated with Helm and Kubernetes",
        "Data engineering: Amazon Redshift, Amazon Airflow (MWAA), Apache Spark, Hadoop, MongoDB, Python, R, SQL",
        "Analytics and ML: AWS ML stack, Python (scikit-learn, TensorFlow/Keras), R, automation frameworks for personalization and demand forecasting",
        "Visualization: Power BI",
        "Customer engagement: CleverTap, WebEngage"
    ],
    "uses_competitor_of_surveysparrow": True,
    "competitor_names": [
        "CleverTap (includes built-in NPS survey capability)",
        "WebEngage (includes in-app survey and NPS journey features)"
    ],
    "last_funding_amount": "~\u20b990 crore (undisclosed round led by Radhakishan Damani)",
    "last_funding_date": "October 2025",
    "recent_news": "July 2025: Filed DRHP with SEBI to raise \u20b92,150 crore via an IPO (fresh issue); the DRHP disclosed FY2025 net profit of \u20b9297 crore, a sharp turnaround from a \u20b910 crore net loss in FY24. November 2024: Formally launched Japan's OWNDAYS eyewear products in India following its ~$400M majority stake acquisition in OWNDAYS. December 2025: Board governance update - new Company Secretary and Chief Compliance Officer appointed, signaling compliance strengthening ahead of IPO.",
    "hiring_for_roles": [
        "Fresher Trainee Optometrist - multiple store locations across India",
        "Store Manager - multiple cities",
        "Full Stack Developer (Python) - Gurugram",
        "Zonal Manager - retail operations",
        "Remote Optometry Lead",
        "IT Lead",
        "Corporate Sales Manager",
        "Optometrist Trainer",
        "Data Engineer - Gurugram (Amazon Redshift, AWS, Airflow, MongoDB, Spark)"
    ],
    "leadership_changes": "Co-founder Peyush Bansal continues as CEO and Chief People Officer, supported by CFO Mukti Hariharan and COO/CBO Oliver Kaye. December 2025: Ashish Kumar Srivastava appointed new Company Secretary and Chief Compliance Officer as part of compliance restructuring ahead of IPO.",
    "recent_product_launches": "November 2024: Launch of OWNDAYS premium Japanese eyewear products in India. FY2024-FY2025: Expansion of Lenskart Gold membership program to 68 lakh members (+27% YoY). FY2025 ongoing: AI-powered 3D virtual try-on embedded in app and website, personalized recommendation engine, and continued expansion of omnichannel stores (282 new India stores, 52 new international stores in FY2025).",
    "likely_pain_points": [
        "Structured post-purchase feedback at scale: ~99 lakh annual transacting customers in India alone, but relies on CleverTap's lightweight in-app NPS widget rather than a full-featured multi-touchpoint survey platform",
        "Omnichannel experience consistency feedback: with 1,500+ stores across India, Singapore, Dubai, and Southeast Asia (OWNDAYS), customer experience varies by channel with no systematic mechanism to compare CX quality across all touchpoints",
        "IPO-readiness and investor-grade CX metrics: institutional investors will scrutinize NPS, CSAT, and customer retention data; CleverTap's lightweight built-in NPS cannot fully bridge this gap",
        "Employee feedback for a 17,000+ person hybrid workforce across offices, stores, and manufacturing sites in multiple languages",
        "Partner and franchise feedback: mix of company-owned and franchise stores requires capturing structured feedback from franchise partners on support quality, marketing, and supply chain reliability",
        "Post-eye-checkup service quality measurement: free home eye checkups and in-store optometry services require a flexible multilingual survey experience that in-app NPS prompts alone cannot provide"
    ]
},
{
    "company_name": "Urban Company Limited",
    "domain": "urbancompany.com",
    "industry": "Tech-enabled home services marketplace connecting customers with trained service professionals (beauty & spa, cleaning, plumbing, painting, appliance repair, and more)",
    "employee_count": "1300-1500",
    "revenue_range": "FY2025 consolidated revenue ~$137M (~\u20b91,144.5 crore), up 38.2% YoY from FY24. FY25 consolidated net profit \u20b9239.8 crore (first profitable year; FY24 was a \u20b992.7 crore net loss)",
    "hq_location": "DLF Phase 1, Gurugram, Haryana 122002, India",
    "founded_year": 2014,
    "funding_stage": "Listed company (NSE: URBANCO; BSE listed). IPO listed September 17, 2025 at \u20b9161-162/share (issue price \u20b993-103), subscribed ~103x. Total pre-IPO funding ~$453M; last major primary raise was the Series F of $255M in June 2021",
    "crm_used": "MoEngage (customer engagement and CRM platform for retention and multi-channel automation)",
    "survey_tools_used": [
        "Unknown (no dedicated third-party survey/feedback platform publicly documented; NPS tracking documented internally at ~20-25%, with internal targets of moving it to ~35%)"
    ],
    "marketing_tools": [
        "MoEngage (omnichannel campaign automation: push notifications, email, SMS, WhatsApp, in-app messaging)",
        "Rocketium (creative automation for reducing marketing campaign production lead times by 8x)",
        "Tableau (data visualization and marketing analytics dashboards)",
        "ELK Stack / Elasticsearch (application and search analytics)"
    ],
    "hr_tools": [
        "unknown"
    ],
    "tech_stack": [
        "Frontend: ReactJS, AngularJS, Swift (iOS), Java (Android)",
        "Backend: Node.js, Python, Java, Scala, NGINX, Redis",
        "Infrastructure: AWS (primary cloud), microservices architecture with Kubernetes, Helm charts, event-driven design",
        "Messaging/queue: Apache Kafka (event streaming), RabbitMQ-style priority queues",
        "Databases: PostgreSQL, Amazon Redshift (analytics warehouse), Snowflake (data lake/warehouse)",
        "AI/ML: AI-powered partner-customer matchmaking engine, Azure AI (face and ID verification for service partner onboarding)",
        "In-app communication: ejabberd (XMPP-based in-app chat)",
        "Data and analytics: HDFS, Airflow, ELK Stack, Tableau",
        "Marketing automation: MoEngage"
    ],
    "uses_competitor_of_surveysparrow": False,
    "competitor_names": [],
    "last_funding_amount": "$63M secondary round",
    "last_funding_date": "2024 (exact month undisclosed)",
    "recent_news": "September 17, 2025: Listed on NSE and BSE at ~57-58% premium over issue price on an IPO subscribed ~103x. October 2025: Reported FY2025 consolidated net profit of \u20b9239.8 crore (vs. \u20b992.7 crore net loss in FY24) and 38.2% YoY revenue growth. May 2025: Partnered with Noon to offer home services in the UAE and Saudi Arabia.",
    "hiring_for_roles": [
        "SDE 2 Backend - software engineering roles in microservices and platform",
        "AI Visual Systems Builder",
        "Category Manager",
        "Manager, Business Growth",
        "Customer Support Executive",
        "Senior Manager, Controllership & Accounting",
        "Business Development Associate - Mumbai (hybrid)",
        "Operations Executive",
        "Talent Acquisition Specialist and HR Generalist"
    ],
    "leadership_changes": "2025: Post-IPO formalization of board structure - Abhiraj Singh Bhal (co-founder) formally designated as Chairman & Managing Director, Varun Khaitan as Director & COO, and Raghav Chandra as Director & CTPO. All three co-founders remained in top operating roles through IPO.",
    "recent_product_launches": "2024-2025: Launched branded product lines including water purifiers and wall panels, and expanded house painting category with proprietary materials. 2025: International expansion through Noon partnership (UAE and Saudi Arabia). FY2024-FY2025: UC Membership and subscription tiers expanded; income from services contributed 73.4% of FY25 revenue (+29% YoY).",
    "likely_pain_points": [
        "NPS improvement from a documented low base: overall NPS is ~20-25% with internal target of 35% - requires structured systematic feedback collection and closed-loop processes that MoEngage's built-in surveys cannot fully address at scale",
        "Dual-sided marketplace feedback management: every transaction involves a customer and a service partner; capturing and reconciling feedback from both sides across 47,888 average monthly active partners is a structural challenge",
        "Post-IPO investor-grade CX and EX reporting: now faces investor scrutiny on structured CX metrics (NPS, CSAT, churn) and employee sentiment data",
        "International expansion and multi-language feedback: operates in India (50+ cities), UAE, Saudi Arabia, and Singapore across Arabic, English, and Hindi",
        "Service partner satisfaction and attrition: 47,888 monthly active partners - regularly measuring partner satisfaction and earnings perception is critical for supply retention",
        "Real-time CSAT after each service transaction: capturing structured CSAT within minutes of each job completion and routing alerts to operations managers is a sophisticated closed-loop feedback use case that MoEngage's campaign tools are not purpose-built to handle"
    ]
},
{
    "company_name": "Zepto (Kiranakart Technologies Private Limited)",
    "domain": "zepto.com",
    "industry": "Quick commerce (q-commerce) - 10-minute grocery, FMCG, and food delivery via a dark-store network in India",
    "employee_count": "5600-5900",
    "revenue_range": "FY2025 revenue ~$1.3B (~\u20b911,110 crore), up 150% YoY from \u20b94,454 crore in FY24. Annualized GOV ~$3B. FY25 losses significantly reduced with improved unit economics",
    "hq_location": "Bengaluru, Karnataka, India (moved from Mumbai in 2024)",
    "founded_year": 2021,
    "funding_stage": "Late-stage unicorn; total funding >$1.5B. Last round: $450M pre-IPO round led by CalPERS and General Catalyst at $7B valuation, closed October 2025. IPO filing planned for 2026",
    "crm_used": "CleverTap (primary customer engagement and retention CRM platform; CMO publicly described CleverTap as a 'key pillar of Zepto's growth')",
    "survey_tools_used": [
        "CleverTap built-in NPS and in-app surveys (CleverTap's native NPS survey feature; no separate standalone survey platform publicly documented)"
    ],
    "marketing_tools": [
        "CleverTap (omnichannel campaign automation: push, email, SMS, WhatsApp, in-app messaging, customer journey orchestration)",
        "MoEngage / WebEngage (job ads requiring experience with all three major Indian engagement platforms suggest evaluation or parallel use)"
    ],
    "hr_tools": [
        "unknown"
    ],
    "tech_stack": [
        "Microservices architecture using Kubernetes and Argo CD for container orchestration and GitOps deployments",
        "Internal developer portal built on Backstage for unified developer experience across hundreds of services",
        "Apache Kafka for real-time event streaming (tracking fleet movement, orders, customer and supplier events at sub-second latency)",
        "ClickHouse for lightning-fast OLAP and analytical queries on real-time operational data",
        "Databricks (Spark/MLflow) for ML workloads, batch analytics, and data transformation pipelines",
        "Apache Airflow (MWAA) for data pipeline orchestration tightly integrated with Databricks",
        "Amazon Web Services (primary cloud provider; under active cost optimization as of October 2025)",
        "Unity Catalog (Databricks) for data access control, governance, and budget guardrails across 300+ internal users",
        "CleverTap for customer engagement, CRM, and in-app notifications"
    ],
    "uses_competitor_of_surveysparrow": True,
    "competitor_names": [
        "CleverTap (includes built-in NPS/in-app survey capabilities)"
    ],
    "last_funding_amount": "$450M pre-IPO round (~$300M primary + ~$170M ESOP pool expansion)",
    "last_funding_date": "October 17, 2025",
    "recent_news": "October 2025: Raised $450M at a $7B valuation, immediately followed by a cost-efficiency drive that removed ~300 employees from payroll (total ~1,000 impacted since early 2025), with CEO Aadit Palicha announcing a freeze on hiring and active reduction of AWS and software costs. July 2025: Filed FY2025 financials confirming \u20b911,110 crore revenue (150% YoY growth) and sharply reduced losses. December 2024: Officially launched Zepto Cafe as a separate app with 30,000 daily orders and 100+ new cafes per month.",
    "hiring_for_roles": [
        "Senior Product Manager - New Category (Bengaluru; 0-to-1 product launches in emerging categories)",
        "Product Manager II - Search & Recommendations (Bengaluru)",
        "Product Manager / Senior Product Manager - Shopping Experience",
        "Senior Manager - Consumer CRM (responsible for CleverTap, MoEngage, WebEngage campaigns and engagement strategy)"
    ],
    "leadership_changes": "2021-present: Co-founder Aadit Palicha (CEO) and co-founder Kaivalya Vohra (CTO) continue to lead Zepto. October 2025: Palicha emphasized a shift to cost discipline - cutting AWS and software spend, freezing hiring, and replacing functions with automation in customer support.",
    "recent_product_launches": "2024: Zepto Pass membership launched (free delivery subscription with 4M+ subscribers by April 2024); Zepto Cafe officially launched nationwide in November 2024 with a dedicated app and 30,000+ daily orders. 2024-2025: Zepto Supersaver (deep discount vertical) introduced to differentiate from Blinkit and Swiggy Instamart. 2025: Rapid dark-store expansion with 100+ cafes per month.",
    "likely_pain_points": [
        "Post-delivery CSAT at scale without a dedicated platform: processes millions of 10-minute deliveries daily but relies on CleverTap's lightweight in-app NPS widget which lacks multi-question contextual CSAT flows to distinguish delivery speed, product quality, packaging damage, and substitution accuracy",
        "Cafe and new-category feedback isolation: Zepto Cafe and Supersaver require completely different satisfaction dimensions than core grocery delivery, yet feedback is presumably lumped into the same CleverTap NPS framework",
        "Pre-IPO NPS/CSAT benchmarking pressure: with an IPO targeted for 2026, institutional investors will demand structured, auditable CX and employee experience metrics that CleverTap's in-app NPS alone cannot provide",
        "Employee sentiment during cost-cutting and automation: ~1,000 employees impacted since early 2025; tracking remaining employee morale through formal pulse surveys is critical for retention",
        "Dark-store operations and delivery partner feedback: ~500+ dark stores and thousands of delivery partners need structured feedback on infrastructure, inventory accuracy, and working conditions via mobile-first survey flows",
        "Cost pressure creating software vendor consolidation risk: CEO explicitly directed teams to cut cloud and software costs; any new platform would need a clear ROI case"
    ]
},
{
    "company_name": "Swiggy (Bundl Technologies Private Limited)",
    "domain": "swiggy.com",
    "industry": "Food delivery, quick commerce (Instamart), and hyperlocal on-demand delivery platform operating across India",
    "employee_count": "7000-8000",
    "revenue_range": "FY2025 consolidated revenue ~$1.82B (~\u20b915,227 crore), up 35% YoY from \u20b911,247 crore in FY24. Net loss \u20b93,116.79 crore in FY25 (widened YoY due to Instamart expansion). Q4 FY25 revenue \u20b94,410 crore (+45% YoY)",
    "hq_location": "Embassy Tech Village, Outer Ring Road, Devarabisanahalli, Bengaluru, Karnataka 560103, India",
    "founded_year": 2014,
    "funding_stage": "Public company listed on NSE and BSE (ticker: SWIGGY) since November 2024; raised ~$1.37B in IPO. Total VC funding pre-IPO was ~$3.6B",
    "crm_used": "MoEngage (flagship MoEngage customer for push notifications and multi-channel engagement; used to orchestrate customer journey campaigns across channels)",
    "survey_tools_used": [
        "CleverTap (used for real-time analytics and customer engagement experimentation including push A/B testing)",
        "Unknown dedicated survey platform (no standalone third-party survey/feedback tool publicly documented beyond MoEngage and CleverTap's built-in features)"
    ],
    "marketing_tools": [
        "MoEngage (primary customer engagement platform for push notifications, email, SMS, WhatsApp, and in-app journey orchestration)",
        "CleverTap (real-time analytics, A/B testing, and data-driven campaign strategy)",
        "Sumo Logic (centralized log management and real-time observability platform)"
    ],
    "hr_tools": [
        "unknown"
    ],
    "tech_stack": [
        "Languages: Java, Scala, Python, Go, Rust, Node.js (backend); ReactJS (frontend); Kotlin (Android), Swift (iOS)",
        "Infrastructure: AWS (primary IaaS); Kubernetes for container orchestration",
        "Databases: MySQL, PostgreSQL, ScyllaDB",
        "Caches: Redis, Aerospike (high-throughput real-time caching for order and delivery state)",
        "Observability/Logging: Sumo Logic (enterprise-grade log ingest and analysis across 300+ engineers)",
        "Customer engagement: MoEngage (primary), CleverTap (analytics and experimentation layer)",
        "CI/CD: Jenkins, ArgoCD, Terraform, Kubernetes GitOps pipelines"
    ],
    "uses_competitor_of_surveysparrow": True,
    "competitor_names": [
        "CleverTap (includes built-in NPS and in-app survey capabilities)",
        "MoEngage (includes in-app and push-based survey and feedback features)"
    ],
    "last_funding_amount": "~$1.37B IPO primary raise (November 2024)",
    "last_funding_date": "November 13, 2024 (IPO listing date)",
    "recent_news": "January 2025: Launched SNACC, a standalone app promising 15-minute delivery of quick bites, beverages, and meals. May 2025: Reported Q4 FY25 results - full-year revenue \u20b915,227 crore (+35% YoY) but net loss widened to \u20b93,116.79 crore, driven by aggressive Instamart dark store expansion. July 2025: Reshuffled post-IPO board, appointing Faraz Khalid (CEO of Noon, UAE) as Additional Non-Executive Independent Director.",
    "hiring_for_roles": [
        "Product Manager II",
        "Senior Software Engineer",
        "Account Manager",
        "Area Sales Manager",
        "Key Account Manager I",
        "Sales Manager I and Sales Manager II",
        "Analyst - Finance",
        "Data Analyst and Data Engineer",
        "User Experience Designer / Product Designer",
        "Assistant Manager - Influencer Marketing",
        "Warehouse Lead - SLP"
    ],
    "leadership_changes": "July 2025: Board restructuring post-IPO - Faraz Khalid appointed as Additional Non-Executive Independent Director; VC nominee directors Sumer Juneja (Norwest Venture Partners) and Anand Daniel (Accel India) resigned. Founder & Group CEO Sriharsha Majety, Co-founder Nandan Reddy, and CFO Rahul Bothra continue in executive roles.",
    "recent_product_launches": "October 2024: Swiggy Bolt launched as an in-app feature for 15-minute food delivery from restaurants within 2 km radius. January 2025: SNACC launched as a standalone app for 15-minute delivery of quick bites, beverages, and ready meals. FY2024-FY2025: Instamart dark-store network aggressively expanded, adding 100+ new cities in FY25.",
    "likely_pain_points": [
        "Post-delivery feedback fragmentation across 5 verticals (Food Delivery, Instamart, Bolt, SNACC, and Dineout): each has distinct satisfaction dimensions and MoEngage/CleverTap are not purpose-built to route structured CSAT appropriately by vertical",
        "Widening losses require precision CX data for retention ROI: must demonstrate retention economics through structured customer satisfaction data that quantifies the revenue impact of CX interventions",
        "Restaurant and dark-store partner satisfaction at scale: hundreds of thousands of restaurant partners and Instamart dark-store vendors require a dedicated B2B survey program not covered by consumer-facing engagement tools",
        "Delivery partner (Swiggy Gig) experience and churn: capturing structured feedback on earnings clarity, app usability, safety, and grievance handling through short mobile-first Hindi/regional-language surveys",
        "Employee engagement amid rapid headcount scaling and losses: added 2,000 employees in FY25 while operating at a \u20b93,100+ crore annual loss and expanding into 100+ new cities",
        "SNACC and Bolt product-market fit validation: both new products launched without public mention of structured in-app feedback or NPS tracking specific to these verticals"
    ]
},
{
    "company_name": "CRED (Dreamplug Technologies Private Limited)",
    "domain": "cred.club",
    "industry": "Fintech / members-only premium credit card payments, financial services, rewards, and lifestyle platform for India's top-10% credit card holders",
    "employee_count": "750-850",
    "revenue_range": "FY2025 operating revenue ~$327M (~\u20b92,735 crore), up 16% YoY from \u20b92,397 crore in FY24. Net loss \u20b91,457 crore in FY25 (down 11.5% YoY). Gross margin ~70%. ARPU ~\u20b92,000. Monthly transacting users (MTUs) 1.26 crore",
    "hq_location": "Bengaluru, Karnataka, India",
    "founded_year": 2018,
    "funding_stage": "Late-stage unicorn (private). Total funding >$1B across 9 rounds. Last round: $72M down round in May 2025 at a $3.64B valuation - a 43% decline from $6.4B Series F valuation in 2022",
    "crm_used": "unknown",
    "survey_tools_used": [
        "unknown"
    ],
    "marketing_tools": [
        "unknown"
    ],
    "hr_tools": [
        "unknown"
    ],
    "tech_stack": [
        "Cloud infrastructure: AWS (primary cloud provider)",
        "Microservices architecture using event-driven design patterns",
        "Event streaming: Apache Kafka (used for order management, reward event sourcing, and inter-service communication)",
        "Caching & state: Redis (for stateless JWT token revocation lists, static user data caching)",
        "Search: Elasticsearch (for offer engine and pre-indexed queries)",
        "Data engineering: BigQuery (analytics warehouse), dbt (data transformation), Python (pipeline logic)",
        "AI/ML: Internal ML platform for personalization, segmentation, and churn models; LLM agent integrations in data workflows",
        "Security/identity: OAuth 2.0, AWS KMS/Secrets Manager, edge caching (Cloudflare/Fastly)"
    ],
    "uses_competitor_of_surveysparrow": False,
    "competitor_names": [],
    "last_funding_amount": "$72M (down round)",
    "last_funding_date": "May 2025",
    "recent_news": "January 2026: Reported FY2025 financials - operating revenue \u20b92,735 crore (+16% YoY), net loss \u20b91,457 crore (down 11.5% YoY), total payment value \u20b98.5 lakh crore (+23% YoY), 1.26 crore MTUs, and managed lending AUM of \u20b922,000 crore. 45% of active members used 3+ products. Company targeting full profitability in FY26. May 2025: Closed a $72M down round at $3.64B valuation.",
    "hiring_for_roles": [
        "Data Engineer (Pipelines, ETL, BigQuery, Python) - hybrid in San Francisco or London",
        "Unknown roles in product and engineering at Bengaluru HQ (active hiring inferred from job board activity)"
    ],
    "leadership_changes": "2018-present: Kunal Shah has been the sole founder and CEO since inception, with no public C-suite departures or appointments documented in 2024-2025. The company maintains a lean, founder-led structure with ~800 employees.",
    "recent_product_launches": "FY2024-FY2025: CRED Money (personal finance management), CRED Cash+ (revolving credit), PPI wallet, and credit score tracking and management tools. FY2023: CRED Garage launched as a vehicle management and insurance marketplace (Sep 2023). FY2023-FY2025: CRED expanded its insurance marketplace within CRED Garage.",
    "likely_pain_points": [
        "Structured member feedback across 5+ product verticals (bill payments, lending, CRED Money, insurance/Garage, travel/Escapes, shopping): understanding satisfaction specific to each product requires multi-touchpoint segmented survey infrastructure that push notifications alone cannot provide",
        "Churn prevention among premium, high-ARPU members: even modest churn among India's top-10% credit card holders materially impacts the \u20b92,000 ARPU and \u20b922,000 crore AUM",
        "Down round and profitability pressure: the 43% valuation haircut and stated goal of FY26 profitability means CRED must demonstrate clear ROI from every product expansion using structured customer feedback data",
        "Loan and credit product satisfaction and complaint management: with \u20b922,000 crore in managed lending AUM, subject to RBI's grievance redressal requirements",
        "Employee engagement at a lean, high-performance scale-up: ~800 employees managing \u20b92,735 crore revenue and multiple simultaneous product launches with no publicly documented internal employee survey program",
        "No documented external survey platform: unlike larger Indian consumer tech companies, CRED has no publicly confirmed third-party survey tool in its stack"
    ]
},
{
    "company_name": "Monzo Bank Limited",
    "domain": "monzo.com",
    "industry": "Digital challenger bank / neobank - UK-regulated retail and business banking (current accounts, savings, lending, investments, Flex BNPL, business accounts)",
    "employee_count": "3900-4100",
    "revenue_range": "FY2025 (year ending March 31, 2025) revenue \u00a31.2 billion (+48% YoY from \u00a3880M in FY24). Adjusted pre-tax profit \u00a3113.9M (8x YoY increase). Customer deposits \u00a316.6B (+48%). Weekly active users 6.9M (+28% YoY). 12M+ total customers",
    "hq_location": "Broadwalk House, 5 Appold Street, London EC2A 2AG, United Kingdom. Additional office in Dublin, Ireland",
    "founded_year": 2015,
    "funding_stage": "Late-stage private unicorn; planning IPO. Total funding ~$1.5B since inception. Most recent rounds: \u00a3340M ($430M) March 2024 at $5B valuation and \u00a3150M ($190M) May 2024 at $5.2B valuation. IPO expected in 2026 under new CEO Diana Layfield",
    "crm_used": "unknown",
    "survey_tools_used": [
        "Typeform (historically used; Monzo terminated the contract following a data breach in June 2018. Not confirmed as active in 2024-2026)",
        "CMA-mandated Independent Service Quality Survey (annual external survey; not an internal platform choice)"
    ],
    "marketing_tools": [
        "unknown"
    ],
    "hr_tools": [
        "unknown"
    ],
    "tech_stack": [
        "Backend: Go (Golang) - primary microservices language used by the majority of Monzo's 300+ backend engineers",
        "Mobile: Swift (iOS), Kotlin (Android)",
        "Frontend: React",
        "Containerisation and orchestration: Docker, Kubernetes",
        "Data stack: BigQuery (data warehouse), dbt (data transformation and modelling), Looker (BI and analytics), Python ML microservices using Sanic (custom-built model serving)",
        "Cloud: Google Cloud Platform (primary; BigQuery, Colab, and data tooling are GCP-native); AWS used secondarily",
        "SAP (cloud partnership for business banking operations and scale)",
        "Apple Pay integration for Monzo Flex BNPL"
    ],
    "uses_competitor_of_surveysparrow": False,
    "competitor_names": [],
    "last_funding_amount": "\u00a3150M ($190M)",
    "last_funding_date": "May 2024",
    "recent_news": "February 2026: CEO TS Anil stepped down after five years; former Google and Standard Chartered executive Diana Layfield took over as Group CEO, with Shelley Malton joining as incoming COO. June 2025: Reported FY2025 results - \u00a31.2B revenue (+48% YoY), \u00a3113.9M adjusted pre-tax profit (8x YoY), 12.2M customers (+25%), and 6.9M weekly active users (+28%). October 2024: Launched Monzo Business Team, a \u00a325/month premium SMB plan as business customer count surpassed 500,000.",
    "hiring_for_roles": [
        "Lead Product Manager (multiple squads)",
        "Senior Product Manager - European Union (Dublin office)",
        "Senior User Research Manager",
        "Staff Technical Program Manager - Platform",
        "Senior Lead Product Designer - Operations",
        "Product Director - Customer Support",
        "Product Director - Operations",
        "Senior Engineer II - Backend (Go)",
        "iOS Engineer",
        "Customer Operations / Disputes Specialist and Vulnerable Customer Advisor",
        "Credit Risk Oversight Manager and Senior Credit Analyst - Financial Health",
        "Senior Financial Crime Risk Manager (12-Month FTC)",
        "Governance Lead - Marketing"
    ],
    "leadership_changes": "February 2026: Diana Layfield (former President EMEA at Google, Group Head of Retail Banking at Standard Chartered) succeeded TS Anil as Group CEO. Anil transitioned to an advisory role. October 2025: Shelley Malton announced as incoming Chief Operating Officer. The dual CEO + COO transition represents Monzo's most significant executive change since founding.",
    "recent_product_launches": "October 2024: Monzo Business Team plan launched (\u00a325/month, expense cards for up to 15 employees, bulk payments, payment approvals). 2024: Monzo Flex BNPL integrated with Apple Pay; pension consolidation feature; mortgage tracking dashboard; fraud protection enhancements. 2024-2026: International expansion in progress - Ireland office growing toward 70 employees by mid-2027; US expansion activity ongoing.",
    "likely_pain_points": [
        "Post-Typeform gap - no confirmed enterprise survey platform since 2018: 6+ years of customer and employee feedback at scale likely relies on ad-hoc or fragmented tooling, a significant structural gap for a 4,000-employee, 12M+ customer bank",
        "CEO and COO transition creates urgent feedback monitoring need: with a brand new CEO (Diana Layfield) and COO (Shelley Malton) both onboarding in early 2026, understanding employee sentiment and culture health is critical",
        "Pre-IPO NPS and CSAT auditability: Monzo is widely expected to IPO in 2026; institutional investors will expect auditable time-series CX metrics that the CMA-mandated annual survey cannot adequately provide",
        "Measuring satisfaction across rapidly expanding product lines (personal accounts, joint accounts, Flex/BNPL, savings, investments, pension tracking, Monzo Business Lite/Pro/Team, international accounts)",
        "Business customer feedback at scale: 500,000+ SMB accounts with newly launched premium Team tier requires a B2B-grade survey approach fundamentally different from consumer feedback workflows",
        "International expansion feedback: actively expanding into Ireland, US, and continental Europe, requiring localised satisfaction feedback in multiple languages"
    ]
},
{
    "company_name": "Revolut Ltd",
    "domain": "revolut.com",
    "industry": "Global digital bank / neobank - retail and business banking, payments, FX, wealth/investments, crypto, insurance, and lending across 48+ countries",
    "employee_count": "12500-13200",
    "revenue_range": "FY2024 (year ended December 31, 2024) revenue $4.0B (\u00a33.1B), up 72% YoY from $2.2B in 2023. Profit before tax $1.4B (+149% YoY). Net profit $1.0B (26% margin). Business banking division reached $1B annualised revenue. 65M+ global customers by end-2025",
    "hq_location": "7 Westferry Circus, Canary Wharf, London E14 4HD, United Kingdom (global HQ). Major engineering and operations hubs in Krakow, Moscow, Vilnius, and Bengaluru",
    "founded_year": 2015,
    "funding_stage": "Late-stage private company; planning IPO likely in 2026. Total funding >$3.3B. Latest round: Secondary share sale at $75B valuation in November 2025 (led by Coatue, Greenoaks, Dragoneer, Fidelity, Andreessen Horowitz, NVIDIA's NVentures, Franklin Templeton, T. Rowe Price). Previous secondary in August 2024 at $45B",
    "crm_used": "unknown",
    "survey_tools_used": [
        "unknown"
    ],
    "marketing_tools": [
        "unknown"
    ],
    "hr_tools": [
        "unknown"
    ],
    "tech_stack": [
        "Languages & frameworks: Java, Kotlin (Android), Swift (iOS), Python, Scala, Node.js, JavaScript, TypeScript, HTML5, CSS3",
        "Frontend: React, Redux",
        "Application hosting: Google Cloud Platform (primary cloud), NGINX",
        "Development and CI/CD: Git, Bitbucket, Docker, Terraform, Ansible, Babel, Yarn, ESLint, Prettier, Jest, Cypress",
        "Monitoring and observability: New Relic",
        "Design: Figma",
        "IDE and developer tooling: IntelliJ IDEA, WebStorm"
    ],
    "uses_competitor_of_surveysparrow": False,
    "competitor_names": [],
    "last_funding_amount": "Undisclosed amount in secondary share sale (employee and investor liquidity)",
    "last_funding_date": "November 2025",
    "recent_news": "November 2025: Completed a secondary share sale at a $75B valuation - up from $45B in August 2024 - making it the most valuable European private tech company. 2025: Grew headcount from 8,000 (start of 2024) to over 13,000 by end-2025, receiving over 1.6 million job applications in 2025. July 2025: Announced a 400+ role recruitment drive in Western Europe to build out a new French entity. November 2024: Revealed 2025 product vision including a new AI-powered financial assistant, branded ATMs, and mortgages.",
    "hiring_for_roles": [
        "Head of Marketing - CEE (Central and Eastern Europe)",
        "Head of Growth - UAE",
        "Marketing Manager (multiple markets)",
        "Events Manager",
        "Growth Partnerships Manager",
        "Product Owner (Technical) - Crypto",
        "Product Strategy Manager - India hub",
        "Senior Software Engineers across payments, crypto, wealth, and platform teams"
    ],
    "leadership_changes": "2024-2025: Victor Stinga formally took on the role of Group CFO (confirmed in November 2025 funding announcement), succeeding a period of CFO turnover. Co-founder Nik Storonsky continues as Group CEO and Vlad Yatsenko as Co-Founder and CTO. Pierre Decote serves as Group Chief Risk & Compliance Officer.",
    "recent_product_launches": "January 2025: Revolut Robo-Advisor launched in Singapore with zero management fees until April 2025. 2024: Revolut Business crossed $1B in annualised revenue; new Business Team features and first Business credit product launched in Europe; branded ATM roll-out started in Spain. 2024-2025: Expanded into 10+ new markets and rolled out AI-powered financial assistant features to consumer accounts.",
    "likely_pain_points": [
        "No confirmed enterprise survey/feedback platform at hyper-scale: serves 65M+ customers across 48 countries with no publicly documented VoC platform - a major gap at $4B revenue and 13,000 employees",
        "Pre-IPO CX metrics auditability requirement: with a $75B valuation and IPO widely anticipated in 2026, will face institutional investor scrutiny on structured NPS, CSAT, and churn driver data",
        "Employee experience at extreme scale-up velocity: added ~5,000 employees in 2025 alone (8,000 to 13,000) - onboarding satisfaction and culture health are nearly impossible to track without a formal employee pulse program",
        "Localised feedback across 48+ markets and 20+ languages: distinct regulatory requirements, product configurations, and cultural expectations across all markets requires a scalable multilingual survey platform",
        "Measuring satisfaction for new AI and wealth features: AI financial assistant, Robo-Advisor, and expanded wealth products are high-trust, high-stakes features where in-app star ratings are insufficient",
        "Business banking partner and SME satisfaction: Revolut Business has 500,000+ SMB customers and $1B+ annualised revenue; B2B relationship NPS requires a fundamentally different mechanism than consumer in-app prompts"
    ]
},
{
    "company_name": "Wise plc (formerly TransferWise)",
    "domain": "wise.com",
    "industry": "Global fintech / cross-border payments and multi-currency banking - retail and business international money transfers, Wise Account (40+ currencies), Wise Business, Assets, debit cards, and Wise Platform (B2B infrastructure for banks and enterprises)",
    "employee_count": "6000-7000",
    "revenue_range": "FY2025 (year ended March 31, 2025) revenue \u00a31.21B (~$1.54B), up 15% YoY from \u00a31.05B in FY24. Underlying profit before tax \u00a3282.1M (+17% YoY). Gross profit \u00a31,307.8M at 75% gross margin. Free cash flow \u00a3615.4M. 15.6M active customers (+21% YoY). Cross-border volume \u00a3145.2B (+23% YoY)",
    "hq_location": "6 Broad Court, London WC2B 5QZ, United Kingdom. Key engineering hubs in Tallinn (Estonia), Singapore, Austin (TX), Sao Paulo, Tokyo, and Budapest",
    "founded_year": 2011,
    "funding_stage": "Public company listed on the London Stock Exchange (LSE: WISE) since July 2021, via a direct listing. Total pre-IPO funding was ~$396M. Market cap approximately \u00a38-9B as of early 2026",
    "crm_used": "unknown",
    "survey_tools_used": [
        "unknown"
    ],
    "marketing_tools": [
        "unknown"
    ],
    "hr_tools": [
        "unknown"
    ],
    "tech_stack": [
        "Languages & frameworks: Java (primary backend microservices), Groovy, Spring Boot, HTML5",
        "Frontend: React, AngularJS",
        "Application servers: Apache Tomcat, Apache HTTP Server",
        "Event streaming and stream processing: Apache Kafka (event bus for 400+ microservices), Kafka Streams with a custom DSL and ~300 stateful stream processing applications holding 50TB of state",
        "Container orchestration: Kubernetes",
        "Containerisation: Docker",
        "Data analytics: Python (analytics platform engineering roles active in 2026)",
        "Design: Figma"
    ],
    "uses_competitor_of_surveysparrow": False,
    "competitor_names": [],
    "last_funding_amount": "unknown",
    "last_funding_date": "July 2021 (LSE direct listing; no secondary raises publicly confirmed since)",
    "recent_news": "June 2025: Reported FY2025 results - revenue \u00a31.21B (+15%), underlying profit before tax \u00a3282.1M (+17%), 15.6M active customers (+21%), cross-border volume \u00a3145.2B (+23%), and gross profit margin of 75%. Also guided for medium-term underlying income growth of 15-20% CAGR. 2025-2026: Expanding Wise Assets into APAC markets with dedicated hiring for an Assets Expansion Lead.",
    "hiring_for_roles": [
        "Principal / Product Lead - Account Management",
        "Senior Business Development Manager - Online Platforms",
        "Senior Software Engineer I - Analytics Platform (Python)",
        "Learning and Development Specialist - Payment Operations",
        "SEO Senior Content Specialist - German",
        "B2B Content Marketing Manager",
        "Lead Product Analyst - Onboarding",
        "Card Fraud Analyst (Acquiring)",
        "Senior Analyst - Marketing Analytics",
        "Wise Assets Expansion Lead - APAC",
        "Regulatory Compliance Officer - Assets",
        "Due Diligence Agent - Platform"
    ],
    "leadership_changes": "2011-present: Co-founder Kristo Kaarmann continues as CEO; co-founder Taavet Hinrikus stepped back from an executive role but remains on the board. May 2023: CFO Matt Briers announced retirement (completed March 2024) and CEO Kaarmann briefly went on leave due to a UK tax-related regulatory matter; CTO Harsh Sinha served as interim CEO. 2024: A new CFO was appointed following Briers' departure.",
    "recent_product_launches": "2021-2025 (ongoing): Wise Assets - a multi-currency investment feature backed by a BlackRock-managed MSCI World Index fund, now expanding into APAC. 2023-2025: Wise Platform - a B2B API infrastructure product enabling banks and enterprises to embed Wise's cross-border payments rails. 2024-2025: Wise Business expanded with higher transfer limits, multi-user access, and new integrations with accounting platforms; over 500,000 SMB and enterprise Business accounts active globally.",
    "likely_pain_points": [
        "No confirmed enterprise survey platform at 6,500 employees and 15.6M customers: customer and employee satisfaction insights likely rely on fragmented in-app ratings, app store feedback, and possibly bespoke internal tooling",
        "Measuring cross-product satisfaction across personal accounts, Business, Assets, and Platform: four distinct product lines with different customer types (individuals, SMBs, banks, enterprises) requires a dedicated multi-touchpoint survey infrastructure",
        "B2B customer and partner experience for Wise Platform: enterprise bank and fintech API customers have high expectations for onboarding quality, API reliability, and support responsiveness - this B2B relationship NPS feedback loop is likely underdeveloped",
        "Employee experience across 11 global locations in 17+ countries with distinct cultural norms and language differences requires consistent multilingual employee pulse and lifecycle surveys",
        "Post-CFO transition and regulatory scrutiny change management: ongoing employee sentiment monitoring around stability and confidence in leadership requires structured feedback channels",
        "Localised onboarding and verification satisfaction: customers who fail or are delayed in onboarding across 160+ countries are a known churn risk, requiring targeted micro-survey flows that in-app star ratings cannot provide"
    ]
},
{
    "company_name": "Grab Holdings Limited",
    "domain": "grab.com",
    "industry": "Southeast Asian super-app platform - ride-hailing, food delivery (GrabFood), grocery (GrabMart), digital payments and financial services (GrabFin/OVO), advertising, and enterprise mobility (Grab for Business)",
    "employee_count": "12500-13000",
    "revenue_range": "FY2025 full-year revenue ~$3.3B (est. based on Q4 2025 of $906M and 19% YoY growth trajectory); FY2024 full-year revenue $2,797M (+19% YoY). First full-year net profit reported in FY2025. On-Demand GMV Q4 2025 was a record $6.1B",
    "hq_location": "3 Media Close, One-North, Singapore 138498 (global HQ)",
    "founded_year": 2012,
    "funding_stage": "Public company listed on NASDAQ (ticker: GRAB) since December 2021 via SPAC merger with Altimeter Growth Corp. Pre-IPO total funding was >$12B. Market cap ~$23.3B as of late 2024",
    "crm_used": "Salesforce (Grab for Business B2B sales and enterprise account management; listed as required CRM expertise for commercial and enterprise key account roles)",
    "survey_tools_used": [
        "unknown"
    ],
    "marketing_tools": [
        "SmartRecruiters (used as Grab's career site and ATS platform for all global job listings)"
    ],
    "hr_tools": [
        "SmartRecruiters (ATS for recruiting globally)"
    ],
    "tech_stack": [
        "Backend languages: Go (Golang, primary for microservices and data platform SDKs), Java/Kotlin (server-side), Python (ML, analytics)",
        "Mobile: Swift (iOS), Kotlin/Java (Android)",
        "Event streaming: Apache Kafka on Kubernetes (EKS) using Strimzi - Grab's 'Coban' real-time data platform supports all products; 3-replica clusters spanning 3 AWS AZs",
        "Stream processing: Apache Flink",
        "Container orchestration: Kubernetes on AWS EKS with Strimzi",
        "Cloud infrastructure: AWS (primary; EC2, EBS, EKS, load balancers, VPC)",
        "ML/AI serving: NVIDIA Triton Inference Server (TIS) deployed via custom Triton Server Manager",
        "ML platform CI/CD: GitLab",
        "Observability: StarRocks (real-time OLAP database)",
        "Secret management: Hashicorp Vault",
        "AI-assisted development: Cursor AI coding assistant (scaled from pilot to daily use across Grab's engineering team in 2025)"
    ],
    "uses_competitor_of_surveysparrow": False,
    "competitor_names": [],
    "last_funding_amount": "unknown",
    "last_funding_date": "December 2021 (SPAC IPO listing on NASDAQ)",
    "recent_news": "February 10, 2026: Reported Q4 and full-year 2025 results - Q4 revenue $906M (+19% YoY), Q4 adjusted EBITDA $148M (+54%), Q4 On-Demand GMV a record $6.1B. Full-year 2025 marks Grab's first ever net profitable year. MTUs crossed 50 million. Board authorised a new $500M share repurchase program. April 2025: Released two new AI products - AI Merchant Assistant and AI Driver Companion.",
    "hiring_for_roles": [
        "Lead Software Engineer - Backend AI",
        "Senior Software Engineer - Fullstack AI Assisted and Agentic Product Development",
        "Senior Software Engineer - Backend (Streaming Data/Flink)",
        "Lead Data Engineer - Autonomy",
        "Lead Simulation Engineer",
        "Senior Machine Learning Engineer",
        "Senior Software Engineer - Mobile Android (Consumer Experience)",
        "Senior Product Analyst",
        "Enterprise Key Accounts Manager - Grab for Business Thailand",
        "Head - Ads Strategy",
        "Manager - GrabFin Regional Strategy & Partnerships",
        "People Operations Business Partner",
        "Lead Technical Program Manager (multiple roles)"
    ],
    "leadership_changes": "April 2025: CFO Peter Oey and Group VP Marketing Cheryl Goh elevated to non-independent board directors - significant governance maturation for a post-SPAC NASDAQ-listed company. September 2025: John Pierantoni designated as Chief Accounting Officer; Liam Barker formally became Group General Counsel. Co-founder and Group CEO Anthony Tan and President Ming Maa continue in their roles.",
    "recent_product_launches": "April 2025: AI Merchant Assistant launched - generative AI tool helping food delivery merchants optimise menus, promotional copy, and listing rankings. April 2025: AI Driver Companion launched - real-time in-app AI assistant providing drivers with trip guidance, earnings tips, and navigation assistance. 2024-2025: Grab for Business significantly expanded with new enterprise key accounts.",
    "likely_pain_points": [
        "Omni-vertical customer satisfaction fragmentation: operates five distinct verticals (Mobility, Food, Mart, Financial Services, and Ads) accessed by 50M+ MTUs through a single app; in-app star ratings conflate ride quality with food delivery freshness and payment success",
        "Driver and merchant partner experience monitoring: hundreds of thousands of driver-partners and merchant-partners across 8 Southeast Asian countries need structured B2B-side feedback collection that Salesforce CRM notes alone cannot provide",
        "First-full-year-profitability pressure and retention economics: FY2025 was Grab's first profitable year; institutional investor scrutiny requires demonstrable CX improvement trajectory data",
        "Multi-country, multi-language feedback infrastructure: operates across 8 countries spanning Bahasa Indonesia, Malay, Thai, Vietnamese, Tagalog, Khmer, Burmese, and English",
        "GrabFin (financial services) compliance-grade customer feedback: provides loans, insurance, and investment products in jurisdictions where regulators (MAS, OJK, Bank Negara) require evidence of complaints management and customer satisfaction tracking",
        "Grab for Business (B2B) enterprise customer satisfaction: serves enterprise clients with corporate travel, expense management, and voucher programs; B2B account health requires structured survey flows different from consumer app interactions"
    ]
},
{
    "company_name": "Bukalapak (PT Bukalapak.com Tbk)",
    "domain": "bukalapak.com",
    "industry": "Indonesian technology company - pivoted from e-commerce marketplace to virtual products, gaming (Itemku), MSME digitisation (Mitra Bukalapak), investment platform, and retail digital services. Physical goods marketplace formally discontinued March 2025",
    "employee_count": "500-600",
    "revenue_range": "FY2024 annual revenue IDR 4.46 trillion (~$278M, +0.5% YoY). Q1 2025 revenue IDR 1.46 trillion (+25% QoQ). Company reported first significant net profit of IDR 2.9 trillion in Q3 2025. Cash reserves IDR 19 trillion (~$1.19B)",
    "hq_location": "Jl. Kemang Timur Raya No. 14, Mampang Prapatan, Jakarta Selatan 12730, Indonesia",
    "founded_year": 2010,
    "funding_stage": "Publicly listed on IDX (Indonesian Stock Exchange, ticker: BUKA) since August 2021 via Indonesia's largest tech IPO at the time, raising IDR 21.9 trillion (~$1.5B) at a ~$6B valuation. Significant shareholders include Ant Group (~23%), GIC (~10%), and Microsoft (~2%). No new primary funding rounds since IPO",
    "crm_used": "unknown",
    "survey_tools_used": [
        "unknown"
    ],
    "marketing_tools": [
        "unknown"
    ],
    "hr_tools": [
        "unknown"
    ],
    "tech_stack": [
        "Cloud infrastructure: Microsoft Azure (primary) and Google Cloud Platform (secondary)",
        "APIs: GraphQL (used for both frontend data fetching and inter-service communication)",
        "Frontend: HTML5; React (inferred from standard tech profiles)",
        "Backend: Custom tribe-based data platform - each business unit (tribe) runs its own ETL processes on a shared infrastructure",
        "Data platform: Self-serve ETL with team-level ownership across business units"
    ],
    "uses_competitor_of_surveysparrow": False,
    "competitor_names": [],
    "last_funding_amount": "IDR 21.9 trillion (~$1.5B) IPO primary raise",
    "last_funding_date": "August 2021 (IDX IPO listing)",
    "recent_news": "March 2025: Officially discontinued its physical goods marketplace - the company now focuses exclusively on Mitra Bukalapak (MSME digitisation), Gaming (led by Itemku), Investment (mutual funds, securities), and Virtual Products. Q3 2025: Reported IDR 2.9 trillion net profit and headcount reduction from 1,018 (Dec 2024) to 543 - a 47% workforce cut. Q1 2025: Revenue grew 37% QoQ and contribution margin nearly doubled (+95% QoQ) under CEO Willix Halim's 'lean and focused' strategy.",
    "hiring_for_roles": [
        "Senior Category Specialist - Gaming",
        "Senior Business Development Specialist",
        "Offline Business Development Senior Manager",
        "Relationship Manager - Investment Solution",
        "Business Process & Compliance Specialist",
        "Risk Management Manager",
        "Head of Legal Transaction",
        "Tax Manager",
        "Associate Reporting Manager - Finance",
        "Payment Integrity Intern",
        "IT Support Specialist"
    ],
    "leadership_changes": "February 2022: Willix Halim (formerly COO) formally appointed as CEO, replacing Rachmat Kaimuddin who resigned to serve in government. 2024-2025: No new C-suite appointments publicly documented; the lean management structure under Willix Halim has been stable throughout the restructuring.",
    "recent_product_launches": "January 2025: Mitra Bukalapak continued expanding its MSME agent network (warkop and warung operators) offering digital financial services to Indonesia's offline micro-merchants. 2024-2025: Gaming vertical (Itemku - Indonesia's dominant gaming marketplace for in-game items, gift cards, and top-ups) formally integrated as a core growth pillar.",
    "likely_pain_points": [
        "Post-restructuring employee morale and sentiment monitoring: workforce cut by ~47% between December 2024 and Q3 2025 (from 1,018 to 543), requiring a structured pulse survey program to measure surviving employee sentiment and burnout risk",
        "Mitra Bukalapak agent satisfaction at grassroots scale: hundreds of thousands of Indonesian warung owners are low-literacy, mobile-first, Bahasa Indonesia-speaking micro-entrepreneurs for whom standard survey platforms require significant localisation and accessibility design",
        "Gaming platform (Itemku) buyer and seller NPS: as gaming becomes a primary revenue driver, understanding buyer satisfaction with digital item delivery and seller experience with listings and payouts requires structured NPS and CSAT flows",
        "Investor (investment platform) user trust and satisfaction: OJK (Indonesia's financial regulator) requirements for investor suitability and complaint handling make structured post-onboarding and post-transaction surveys both a compliance need and a retention tool",
        "Virtual products post-transaction CSAT: digital top-ups are high-volume, low-margin, instant-delivery transactions where failure rates and wrong denomination errors are the primary churn triggers"
    ]
},
{
    "company_name": "Shopee (Shopee Pte. Ltd., wholly owned subsidiary of Sea Limited)",
    "domain": "shopee.com",
    "industry": "E-commerce marketplace and digital commerce platform - Southeast Asia's largest e-commerce platform (SEA + Taiwan), spanning marketplace, Shopee Live (livestream commerce), Shopee Ads, ShopeeFood (select markets), and integrated digital financial services via Monee/ShopeePay",
    "employee_count": "13400-13800",
    "revenue_range": "Shopee (Sea e-commerce segment) FY2025 revenue $16.6B (+33.9% YoY). GMV $127.4B (+26.8% YoY). Orders 13.9 billion (+27.5% YoY). ~400 million active buyers and 20 million sellers served in 2025. Sea group FY2025 revenue $22.9B (+36.3%). Sea group net income $1.6B (3.6x YoY growth)",
    "hq_location": "1 Fusionopolis Place, #17-10 Galaxis, Singapore 138522. Additional major offices in Shenzhen, Jakarta, Kuala Lumpur, Bangkok, Manila, Ho Chi Minh City, and Taipei",
    "founded_year": 2015,
    "funding_stage": "Subsidiary of NYSE-listed Sea Limited (ticker: SE); Sea Limited has been publicly traded since October 2017. Current Sea market cap ~$80B as of March 2026",
    "crm_used": "unknown",
    "survey_tools_used": [
        "unknown"
    ],
    "marketing_tools": [
        "unknown"
    ],
    "hr_tools": [
        "SeaTalk - Sea's own proprietary enterprise communication and HR platform, used internally across Shopee, Garena, and Monee"
    ],
    "tech_stack": [
        "Frontend: React (UI), Redux (state management), Webpack (bundling), Jest/Enzyme (testing)",
        "Backend: Java (scalable services and microservices), PHP (web layer), Python (ML, data analysis, recommendation systems)",
        "Databases: MySQL (structured transactional data), Redis (distributed caching), MongoDB (unstructured/catalogue data)",
        "Real-time processing: Apache Kafka (event bus), Apache Spark (large-scale batch and stream analytics)",
        "CI/CD: Jenkins, GitLab CI",
        "Containerisation: Docker + Kubernetes",
        "Internal communication and HR platform: SeaTalk (proprietary app covering team messaging, meeting management, HR functions across Sea group)",
        "AI/ML: Custom personalisation and recommendation models; LLM-based customer service agents in development"
    ],
    "uses_competitor_of_surveysparrow": False,
    "competitor_names": [],
    "last_funding_amount": "unknown",
    "last_funding_date": "unknown",
    "recent_news": "March 2026: Sea Limited reported full-year 2025 results - Shopee GMV $127.4B (+26.8%), e-commerce revenue $16.6B (+33.9%), group net income $1.6B (3.6x YoY). Guided for 25% GMV growth in 2026. January 2026: Monee partnered with Episode Six to launch the ShopeePay Unlimited Card across Southeast Asia beginning in Thailand. 2025: AI transformation accelerated with active hiring for PM - AI Agent & Chatbot Intelligence (Regional Operations) and AI Strategy Business PM.",
    "hiring_for_roles": [
        "Product Manager - AI Agent & Chatbot Intelligence, Regional Operations",
        "Lead Product Manager - Return & Refund (AI Strategies)",
        "AI Strategy Business Product Manager - SG Product",
        "Data Product Manager - Marketplace Intelligence & Data",
        "Technical Product Manager - Data Infrastructure",
        "Business Product Manager - Regional Operations",
        "Product Manager - Campaign Management, Buyer & Marketing",
        "Product Manager - Notifications, Buyer & Marketing",
        "Product Manager - Order Checkout, Buyer & Marketing",
        "Product Manager - Order Fulfillment, Buyer & Marketing",
        "Marketing (289 openings), Operations (1,271 openings), People (106 openings) at Malaysia office alone"
    ],
    "leadership_changes": "August 2022: Chris Feng stepped down as Shopee CEO citing personal reasons. Post-2022: Sea group has not publicly named a standalone Shopee CEO; operations appear to be run through Forrest Li (Group CEO) and the regional president structure. No major Shopee-level C-suite appointments publicly announced in 2024-2025.",
    "recent_product_launches": "2024-2025: Shopee Live (livestream commerce) scaled into a major GMV driver across Southeast Asia. 2025-2026: ShopeePay Unlimited Card (powered by Monee and Episode Six) launched in Thailand with multi-country Southeast Asia rollout underway. 2025: Shopee Premium (luxury/premium brand channel) and Shopee Ads platform continued expansion; AI-powered customer service chatbots deployed at scale.",
    "likely_pain_points": [
        "No confirmed enterprise survey platform across 400M buyers and 20M sellers: buyer satisfaction signals across 9 markets likely rely on in-app star ratings, app store reviews, and internal data queries - creating blind spots for qualitative feedback at scale",
        "Seller NPS and merchant experience across 20M sellers of highly varying sophistication: understanding seller satisfaction with listing tools, fee structures, logistics, and dispute resolution is a critical supply-side retention challenge",
        "AI chatbot and digital customer service satisfaction measurement: actively replacing human agents with LLM-powered AI chatbots; measuring whether AI-resolution journeys satisfy buyers and tracking deflection-quality tradeoffs requires systematic CSAT surveys",
        "Multi-country, multi-language CX consistency: operates in 8+ countries with distinct languages, consumer expectations, and regulatory requirements",
        "ShopeePay and Monee financial service satisfaction and compliance: the ShopeePay Unlimited Card rollout creates new regulatory obligations for financial complaint management and customer satisfaction tracking",
        "SeaTalk employee experience surveys for 13,000+ staff: no evidence that SeaTalk includes a robust employee pulse survey or lifecycle feedback capability"
    ]
},
{
    "company_name": "Razorpay Software Private Limited",
    "domain": "razorpay.com",
    "industry": "Full-stack financial services platform for businesses - payment gateway, payment links, subscriptions, Magic Checkout, business banking (RazorpayX), payroll (Opfin), corporate cards, loyalty, POS, and Optimizer (multi-gateway routing)",
    "employee_count": "3500-4500",
    "revenue_range": "FY2025 consolidated revenue ~$453M (~\u20b93,783 crore), up 65% YoY from \u20b92,296 crore in FY24. Gross profit \u20b91,277 crore (+41% YoY). Post-ESOP and restructuring net loss \u20b91,209 crore (one-time costs from reverse flip to India in May 2025). Online payments business EBITDA-positive per CEO Harshil Mathur",
    "hq_location": "SJR Cyber, No. 22 Laskar Hosur Road, Adugodi, Bengaluru, Karnataka 560030, India. Reverse-flipped to India in May 2025",
    "founded_year": 2014,
    "funding_stage": "Late-stage unicorn (private). Total funding >$800M. Last valued at ~$7B (Series F, $375M, December 2021 from GIC, Peak XV, Alkeon Capital, TCV). IPO in active preparation: invited merchant bank bids January 2026, targeting ~$700M+ raise. IPO expected end-2026 or early 2027",
    "crm_used": "Salesforce Sales Cloud (used by Razorpay's B2B merchant sales team to manage lead assignment, account management, and pipeline; documented to reduce turnaround time from lead capture to close)",
    "survey_tools_used": [
        "unknown"
    ],
    "marketing_tools": [
        "MoEngage (primary merchant engagement platform - email, WhatsApp, SMS automated flows; documented case study shows MoEngage Flows drove merchant retention up by 25%)"
    ],
    "hr_tools": [
        "Opfin / RazorpayX Payroll (Razorpay's own payroll and HR platform - used internally as a flagship dogfooding deployment)"
    ],
    "tech_stack": [
        "Mobile: React Native, TypeScript",
        "API layer: GraphQL, Apollo Studio",
        "CI/CD: Bitrise (mobile), internal Devstack (cloud-native local development ecosystem using Kubernetes, Helm, Helmfile, and Traefik 2.0)",
        "Containerisation and orchestration: Docker, Kubernetes",
        "Error monitoring: Sentry",
        "Backend: Java, Go, PHP, Python",
        "Cloud: AWS (primary; LocalStack for local AWS emulation in Devstack; EC2, S3, Lambda)",
        "Observability: OpenTelemetry",
        "Merchant engagement: MoEngage",
        "Sales CRM: Salesforce Sales Cloud",
        "Push/OTP delivery: Firebase"
    ],
    "uses_competitor_of_surveysparrow": False,
    "competitor_names": [],
    "last_funding_amount": "$375M (Series F)",
    "last_funding_date": "December 2021",
    "recent_news": "January-February 2026: Formally initiated IPO proceedings, inviting investment bank bids targeting ~$700M+ in fresh capital; Kotak Mahindra Bank and Axis Capital are leading contenders. October 2025: Filed FY2025 financials - \u20b93,783 crore revenue (+65% YoY), gross profit \u20b91,277 crore (+41%), net loss \u20b91,209 crore (post-ESOP/restructuring one-off). CEO confirmed core payments business is EBITDA-positive. February 2025: Razorpay FTX 2025 event unveiled Magic Checkout + Appmaker integration, OTP Assist, RazorpayX DuplicateShield, and Smart Collect 2.0.",
    "hiring_for_roles": [
        "Staff Software Engineer",
        "Staff Software Engineer (Platform)",
        "Software Engineering Manager",
        "Lead Solutions Engineer",
        "Lead DevOps Engineer",
        "Lead Analytics Specialist",
        "Lead Product Designer",
        "Product Designer II",
        "Manager - Ad Sales (Enterprise Sales)",
        "Manager Key Accounts - GTM Startup Accounts",
        "Senior Associate / Team Lead - Banking Operations",
        "Analyst - Finance Operations (Refunds)",
        "Communications Designer"
    ],
    "leadership_changes": "June 2022: Co-founder Shashank Kumar transitioned from CTO to Managing Director; former AWS executive Murali Brahmadesam appointed as CTO. May 2025: Reverse flip to India completed, formalising Razorpay Software Pvt. Ltd. as the parent entity - a governance milestone in IPO preparation.",
    "recent_product_launches": "February 2025 (FTX 2025): Magic Checkout + Appmaker (Shopify mobile commerce with up to 50% conversion lift), OTP Assist (automated OTP retrieval), RazorpayX DuplicateShield (AI-powered duplicate debit detection), RazorpayX DirectToPhone Payouts, Smart Collect 2.0, and RazorpayX Corporate Card. October 2024 (Sprint 2024): Razorpay Optimizer (multi-gateway payment routing that boosts success rate by up to 10%).",
    "likely_pain_points": [
        "No confirmed standalone survey or feedback platform despite 10M+ merchants: relies solely on MoEngage for email/SMS/WhatsApp engagement with no documented CX/NPS measurement layer - merchant churn signals are detected reactively",
        "Pre-IPO merchant NPS benchmarking is now strategically critical: with a $700M+ IPO targeted for end-2026 or early 2027, institutional investors will scrutinise merchant satisfaction and NPS trajectories",
        "Multi-product satisfaction differentiation: serves merchants through 7+ distinct products (Payment Gateway, Magic Checkout, RazorpayX banking, Payroll, POS, Optimizer, Loyalty) requiring multi-touchpoint segmented CSAT",
        "Merchant onboarding drop-off and dissatisfaction measurement: no public data exists on merchant onboarding satisfaction or support CSAT after activation",
        "Employee experience at scale and during IPO preparation: 4,000 employees, recently completed reverse flip, March 2025 conversion to public limited entity, and active IPO preparation creating employee anxiety",
        "RazorpayX business banking customer satisfaction and RBI compliance: as a regulated payment aggregator (PA licence), structured post-interaction CSAT and complaint-rate monitoring is a compliance and audit readiness requirement"
    ]
},
{
    "company_name": "Delta Air Lines, Inc.",
    "domain": "delta.com",
    "industry": "Commercial aviation - passenger air transportation, cargo, loyalty (SkyMiles), maintenance (Delta TechOps), refining (Monroe Energy/Trainer Refinery), and managed travel services operating across 300+ destinations in 60+ countries",
    "employee_count": "102500-103500",
    "revenue_range": "FY2025 total operating revenue $63.4B (up 2.9% YoY from $61.6B in FY24). Operating income $5.8B (9.2% margin). Pre-tax income $6.2B (9.8% margin). EPS $7.66. Operating cash flow $8.3B",
    "hq_location": "1030 Delta Boulevard, Atlanta, Georgia 30354, United States",
    "founded_year": 1924,
    "funding_stage": "Public company listed on NYSE (ticker: DAL). Market cap ~$42B as of early March 2026",
    "crm_used": "Salesforce Service Cloud + Experience Cloud (with LWC-based Experience Cloud portal, CTI integration, MuleSoft API integration to backend systems, and Salesforce Einstein Analytics for operational insights)",
    "survey_tools_used": [
        "Medallia Experience Cloud (deployed since September 2015 - Delta's primary enterprise CX platform for measuring customer satisfaction across the entire travel journey; provides real-time actionable feedback to 80,000+ employees daily; doubled survey response rates vs. previous solution at launch)"
    ],
    "marketing_tools": [
        "Salesforce Marketing Cloud (integrated with Harmonizer for real-time document exchange with alliance partners)",
        "Medallia Experience Cloud (also used for experience-driven marketing insights and loyalty experience measurement for SkyMiles)"
    ],
    "hr_tools": [
        "unknown"
    ],
    "tech_stack": [
        "CRM and Service: Salesforce Service Cloud, Experience Cloud (with Lightning Web Components), MuleSoft (API middleware integration layer), Salesforce Einstein Analytics, Copado (CI/CD for Salesforce deployments)",
        "CX/Feedback: Medallia Experience Cloud (enterprise VoC, NPS, CSAT across all customer touchpoints globally)",
        "Marketing: Salesforce Marketing Cloud (with Harmonizer for alliance data exchange)",
        "In-flight entertainment: Delta Sync (proprietary IFE platform; new version with 4K HDR QLED displays, Bluetooth, AI-personalised content launching 2026 in partnership with Thales)",
        "AI tools: AI-powered personalisation and operational insights via Delta Sync, CES 2025 AI innovation showcase"
    ],
    "uses_competitor_of_surveysparrow": True,
    "competitor_names": [
        "Medallia (enterprise CX, NPS, and feedback management platform deployed at scale since 2015)"
    ],
    "last_funding_amount": "unknown",
    "last_funding_date": "unknown",
    "recent_news": "March 5, 2026: Delta announced sweeping C-suite leadership changes - longtime COO John Laughter stepped down after three decades; Peter Carter elevated to President; Ranjan Goswami named new Chief Marketing and Product Officer (replacing departing Alicia Tillman). January 2026: Reported full-year 2025 results - revenue $63.4B, pre-tax income $6.2B, EPS $7.66. January 2025 (CES 2025): Delta unveiled next-generation Delta Sync IFE system (4K HDR QLED + AI personalisation) and Uber Eats SkyMiles integration.",
    "hiring_for_roles": [
        "Intern - Airport Customer Service, Product Analyst and Management (Summer 2026)",
        "Manager - Flight Offer and Catalog Systems",
        "IT Network Engineer",
        "Senior Business Analyst",
        "Senior Decision Scientist - Operations Research",
        "Data Analyst - TechOps Business Performance",
        "Senior Engineer - Enabling Technologies",
        "Program Manager - Commercial Analysis and Data Strategy",
        "Program Manager - Global Benefits",
        "Sourcing Manager - TechOps Supply Chain",
        "Graduate Intern - Sustainability / Sustainable Skies Lab (Summer 2026)"
    ],
    "leadership_changes": "March 5, 2026: Major executive restructuring announced by CEO Ed Bastian - COO John Laughter (30+ year veteran) retiring; Peter Carter elevated to President overseeing enterprise strategy, international portfolio, and sustainability; Ranjan Goswami appointed Chief Marketing and Product Officer, replacing CMO Alicia Tillman who departed for external leadership roles. CEO Ed Bastian and CFO Dan Janki continue in their positions.",
    "recent_product_launches": "CES 2025 (January 2025): Delta Sync next-gen IFE - 4K HDR QLED seatback displays with Bluetooth, AI-driven personalised content, accessibility features launching on new aircraft from 2026 via Thales partnership. SkyMiles + Uber Eats integration: Members earn 1 mile per dollar on eligible Uber Eats orders. Airbus ZEROe collaboration: Partnership to explore hydrogen-powered aircraft concepts.",
    "likely_pain_points": [
        "Medallia contract renewal and competitive evaluation window: Delta has used Medallia since 2015 (10+ years); the March 2026 leadership transition (new CMO+CPO Ranjan Goswami) creates a realistic near-term contract review window as new leaders typically audit the incumbent vendor stack",
        "New CMO/CPO Ranjan Goswami onboarding: a new Chief Marketing and Product Officer typically audits CX and VoC infrastructure within the first 90-180 days and may seek to rationalise or modernise the existing Medallia setup",
        "Employee experience measurement at 103,000-person scale during restructuring: simultaneous COO retirement, President elevation, and CMO departure in March 2026 - Medallia's primary deployment is customer-facing, not employee-focused",
        "Delta Sync IFE personalisation feedback loop: new AI-personalised in-flight entertainment launching from 2026 requires structured in-flight micro-surveys - a novel aircraft-specific feedback use case the ground-based Medallia deployment was not designed to serve",
        "Operational disruption CSAT measurement: capturing real-time post-disruption CSAT and recovery satisfaction at scale where delta-level granularity matters more than Medallia's standard batch-survey cadence",
        "Digital channel and AI tool satisfaction: measuring whether digital-first passengers are satisfied with AI-driven interactions vs. human agent touchpoints requires in-app and post-chat CSAT surveys tightly integrated with Salesforce Service Cloud - potentially a gap between the Medallia system and the Salesforce-native workflow"
    ]
},
{
    "company_name": "Walmart Inc.",
    "domain": "walmart.com",
    "industry": "World's largest omnichannel retailer - brick-and-mortar grocery and general merchandise (4,600+ US stores, 600+ Sam's Club locations, 10,000+ international stores), e-commerce (Walmart.com, Walmart+), advertising (Walmart Connect), financial services, healthcare, and connected TV advertising (Vizio/SmartCast)",
    "employee_count": "2000000-2105000",
    "revenue_range": "FY2025 (year ended January 31, 2025) total revenue $681.0B (+5.1% YoY). Net sales $674.5B. Gross profit $163.1B (24.1% margin). Operating income $29.3B (+8.6%). Net income $20.2B (+23.9%). eCommerce net sales grew ~21% YoY in US. Sam's Club comparable sales +4.7%",
    "hq_location": "702 SW 8th Street, Bentonville, Arkansas 72716, United States",
    "founded_year": 1962,
    "funding_stage": "Public company listed on NYSE (ticker: WMT). Market cap ~$760B as of early March 2026. World's largest company by revenue (Fortune Global 500 #1 in 2025)",
    "crm_used": "Salesforce Commerce Cloud and Order Management (via Walmart Commerce Technologies partnership - powers omnichannel fulfillment, pickup, and GoLocal delivery logistics)",
    "survey_tools_used": [
        "Medallia Experience Cloud - Walmart Mexico (Walmart MX) is a confirmed Medallia customer; used for retail CX and NPS measurement, featured in a 'Redefining Customer Experience: Walmart's Winning Strategies' showcase in March 2026"
    ],
    "marketing_tools": [
        "Walmart Connect (proprietary retail media advertising platform managing sponsored product ads, display, CTV, and omnichannel marketing; expanded significantly with Vizio SmartCast/WatchFree+ integration post-December 2024 acquisition)",
        "Vizio SmartCast OS / WatchFree+ streaming (18M+ active accounts; uses ACR data from Vizio for hyper-targeted CTV ad products)",
        "Salesforce Marketing Cloud (used as part of the Salesforce Commerce Cloud partnership)"
    ],
    "hr_tools": [
        "unknown"
    ],
    "tech_stack": [
        "Commerce and fulfillment: Walmart Commerce Technologies (proprietary store fulfilment and GoLocal delivery technology; commercially licensed to third-party retailers via Salesforce AppExchange)",
        "Advertising: Walmart Connect (retail media network) integrated with Vizio SmartCast OS and WatchFree+ (ACR data-driven CTV advertising)",
        "CX measurement: Medallia Experience Cloud (Mexico and likely other markets)",
        "AI and data: Walmart Global Tech operates a large-scale proprietary AI and data platform (Walmart Data Ventures) for demand forecasting, pricing, personalisation, and advertising targeting",
        "Membership platform: Walmart+ (subscription loyalty and delivery program) and Sam's Club membership system"
    ],
    "uses_competitor_of_surveysparrow": True,
    "competitor_names": [
        "Medallia (deployed at Walmart Mexico for retail CX and NPS; featured in March 2026 Walmart CX showcase)"
    ],
    "last_funding_amount": "unknown",
    "last_funding_date": "unknown",
    "recent_news": "January 2026: Announced sweeping C-suite leadership changes - new CEO John Furner (succeeding Doug McMillon who retired); Seth Dallaire elevated to EVP and Chief Growth Officer overseeing Walmart Connect, Walmart+, Data Ventures, Vizio, and global Marketplace; David Guggina appointed President & CEO of Walmart U.S.; Chris Nicholas named President & CEO of Walmart International; Latriece Watkins named President & CEO of Sam's Club. December 2024: Walmart completed the $2.3B acquisition of Vizio.",
    "hiring_for_roles": [
        "Senior Manager, Business Development - Inbound Channel (Walmart India/Flipkart Wholesale)",
        "Director - Fashion, Kids",
        "Data Analyst II (MS Excel, Power BI, SQL)",
        "Senior Resolution Coordinator - Customer Support",
        "Senior Seller Consultants - Strategic Sellers",
        "Software Engineer (Walmart Global Tech - multiple disciplines)",
        "Data Scientist / ML Engineer (Walmart Global Tech - AI/data platform)",
        "Human Resources Specialist, Recruiter, Marketing Manager, Project Manager, Account Manager (corporate roles globally)"
    ],
    "leadership_changes": "November 2025: Doug McMillon (CEO since 2014) announced retirement; John Furner named successor CEO. January 2026: Furner introduced a comprehensive organizational restructuring - Seth Dallaire elevated to enterprise-wide CGO; David Guggina appointed President & CEO of Walmart U.S.; Chris Nicholas appointed President & CEO of Walmart International; Latriece Watkins appointed President & CEO of Sam's Club - the most significant leadership reorganisation in a decade.",
    "recent_product_launches": "December 2024: Vizio acquisition completed ($2.3B); Vizio converted to Walmart-exclusive private label brand, with SmartCast OS and WatchFree+ integrated into Walmart Connect CTV advertising platform. 2025: Walmart+ membership expanded with new Vizio SmartCast and Paramount+ bundle benefits. 2025-2026: Walmart Data Ventures launched new B2B data products enabling brand suppliers to access anonymised Walmart shopper data.",
    "likely_pain_points": [
        "Post-CEO transition CX and EX measurement under new leadership: with a brand new CEO and near-complete C-suite restructuring in January 2026, each new business unit head will seek to establish CX and employee satisfaction baselines for their domains - only Walmart MX confirmed to have Medallia",
        "Medallia deployment gap - only Mexico confirmed: no public evidence of Medallia being deployed in Walmart U.S. (4,600 stores), Sam's Club, Flipkart (India), or Walmart Canada - a significant gap for a $681B revenue business",
        "Vizio integration customer satisfaction measurement: 18M active SmartCast accounts interact with a new product ecosystem daily; measuring SmartCast user satisfaction, ad experience perception, and content quality feedback requires a distinct survey/feedback infrastructure",
        "Sam's Club member NPS and renewal prediction: fee-based membership model where NPS and member satisfaction directly predict renewal rates - capturing structured feedback at key moments in a form that predicts churn risk",
        "2.1 million associate employee experience and frontline pulse surveys: 1.6M US associates in hourly retail, distribution, and logistics roles with limited desktop access require mobile-first, short-form surveys",
        "Supplier and marketplace seller satisfaction: measuring seller satisfaction with onboarding, catalogue management, ad tools, and logistics through structured B2B NPS and CSAT surveys is an important supply-side retention lever"
    ]
},
{
    "company_name": "KFC (operated and franchised by Yum! Brands, Inc.)",
    "domain": "kfc.com",
    "industry": "Quick-service restaurant (QSR) - global fried chicken fast-food chain operating company-owned and franchise restaurants across 150+ countries",
    "employee_count": "810500-825000",
    "revenue_range": "KFC brand revenue (Yum! Brands segment) approximately $6.8B annually. Yum! Brands total company revenue FY2025: ~$7.5B (based on Q3 2025 of $1.98B +8.2% YoY). KFC global system sales grew 6% in Q3 2025; same-store sales +3% globally. Digital sales exceeded $10B systemwide in Q3 2025, surpassing 50% digital mix across all brands",
    "hq_location": "KFC brand HQ: 1441 Gardiner Lane, Louisville, Kentucky 40213, USA. Yum! Brands corporate HQ: 1441 Gardiner Lane, Louisville, Kentucky 40213, USA",
    "founded_year": 1952,
    "funding_stage": "Subsidiary of Yum! Brands, Inc. (NYSE: YUM), a public company. Market cap ~$35B",
    "crm_used": "Salesforce Sales Cloud (Yum! Brands selected Salesforce Sales Cloud in 2021 for Sales Automation, CRM, and Sales Engagement, displacing a legacy system)",
    "survey_tools_used": [
        "Qualtrics XM Platform (primary enterprise CX and feedback platform for KFC globally - Qualtrics powers a global omnichannel experience management program with post-transaction surveys; feedback volume increased 300% after implementation; dashboards are role-segmented for restaurant managers, market managers, and executives; also uses Qualtrics XM Discover for unstructured text analytics on delivery platform reviews across 1,000+ UK locations)"
    ],
    "marketing_tools": [
        "Salesforce Marketing Cloud (integrated with Salesforce Sales Cloud for franchise and B2B partner marketing)",
        "Qualtrics XM Discover (text analytics and social listening for unstructured customer feedback, NLP on delivery partner reviews)",
        "Byte by Yum (proprietary AI-backed digital and marketing technology platform including digital menu boards, kiosk ordering, kitchen display systems, and loyalty/digital ordering; used across 25,000+ global restaurants)"
    ],
    "hr_tools": [
        "unknown"
    ],
    "tech_stack": [
        "Byte by Yum (Yum!'s proprietary SaaS restaurant technology platform - integrates kitchen management, POS, order management, digital menu boards, AI-driven operations, loyalty, and delivery across KFC, Taco Bell, Pizza Hut, and Habit Burger; used by 25,000+ global restaurants)",
        "Qualtrics XM Platform + XM Discover (global CX measurement, post-transaction surveys, text analytics, role-segmented dashboards)",
        "Salesforce Sales Cloud (CRM and sales engagement for corporate and franchise sales teams)",
        "Digital ordering: Mobile apps, third-party delivery platform integrations (Uber Eats, DoorDash, Just Eat); digital mix surpassed 50% of all orders systemwide in 2025",
        "Self-service kiosks and kitchen display systems deployed at 16+ Next Generation KFC test locations in the US"
    ],
    "uses_competitor_of_surveysparrow": True,
    "competitor_names": [
        "Qualtrics (XM Platform + XM Discover - fully deployed as KFC's global omnichannel CX survey, feedback, and text analytics platform; 300% feedback volume increase documented post-implementation)"
    ],
    "last_funding_amount": "unknown",
    "last_funding_date": "unknown",
    "recent_news": "October 2025: Chris Turner became CEO of Yum! Brands (succeeding David Gibbs, who retired), effective October 1; Turner was the CFO since 2019 and primary champion of Yum!'s technology investments including Byte by Yum. November 2025: Yum! Brands Q3 2025 earnings - revenue $1.98B (+8.2% YoY); digital sales $10B (>50% of total); company announced exploration of strategic options for Pizza Hut. December 2024: KFC launched 'Next Generation KFC' test at 16 US restaurants, featuring digital menu boards, ordering kiosks, and upgraded kitchen display systems.",
    "hiring_for_roles": [
        "unknown"
    ],
    "leadership_changes": "June-October 2025: Chris Turner elevated from CFO/Chief Franchise Officer to Group CEO of Yum! Brands, effective October 1, 2025. David Gibbs retired from CEO role after six years and serves as an advisor through 2026. April 2025: New President of KFC U.S. appointed, credited with marketing strategy adjustment and spicy wings launch that drove 2% SSS growth in the US.",
    "recent_product_launches": "December 2024-2025: KFC Next Generation restaurant format \u2014 digital menu boards, kiosk ordering, upgraded kitchen display systems, Original Recipe Tenders, Classic and Spicy Twister Wraps, frozen beverages; rolled out across 16 US test locations with improved customer satisfaction and speed scores.[web:1050] December 2025: Five new menu items launched (Chicken Teriyaki Bowl, Chicken Caesar Salad, Brussels Bites, Puffies, additional items) across select markets.[web:1055] February 2025: Byte by Yum platform formally announced as an integrated SaaS suite covering all QSR technology needs across all Yum! brands; 25,000+ restaurants already using at least one component globally.[web:1053]",
    "likely_pain_points": [
        "Qualtrics contract renewal review under new CEO Chris Turner: Turner became CEO in October 2025, and as the architect of Yum!'s technology strategy (including Byte by Yum and digital sales growth), he will likely review all major platform contracts within 12\u201318 months. Qualtrics enterprise contracts are large, expensive, and multi-year; a new CEO with a technology background may evaluate whether a more integrated or cost-effective alternative fits the evolving Byte by Yum ecosystem.[web:1049][web:1054][web:1047]",
        "Qualtrics + Byte by Yum integration complexity: Byte by Yum is Yum!'s proprietary POS, KMS, and digital ordering platform, while Qualtrics runs CX measurement separately; bridging real-time operational data from Byte (order accuracy, drive-thru speed, kitchen status) with customer satisfaction signals in Qualtrics requires integration work that is not natively built \u2014 a gap that a survey tool with deeper QSR operational integrations could exploit.[web:1047][web:1053]",
        "Pizza Hut strategic review creates platform consolidation opportunity: Yum! is exploring strategic options for Pizza Hut (possible sale/restructuring), which means the Qualtrics deployment may be renegotiated at the brand level; if Pizza Hut is sold or spun off, the Qualtrics contract scope (and cost) would be renegotiated, potentially creating a window for alternative vendors to bid on one or more brand segments.[web:1045][web:1052]",
        "Franchise operator feedback and training quality surveys: KFC is 98%+ franchised globally; measuring franchisee satisfaction with corporate support, training quality, marketing campaigns, technology onboarding, and new restaurant design rollout requires a B2B franchise-facing survey program separate from the consumer CX tools \u2014 no such tool is publicly documented alongside the Qualtrics consumer deployment.[web:1047][web:1043]",
        "Employee experience at Next Generation restaurants during digital transformation: The Next Generation KFC rollout (kiosks, kitchen display systems, new menu) is being tested at 16+ US locations; capturing frontline employee satisfaction, training readiness, and technology adoption friction through short, mobile-first pulse surveys during this rollout would help optimize the format before system-wide expansion \u2014 an employee-experience survey use case not covered by the consumer-focused Qualtrics XM deployment.[web:1050][web:1047]"
    ]
},
{
    "company_name": "Marriott International, Inc.[web:1066][web:1067]",
    "domain": "marriott.com",
    "industry": "Global hospitality \u2014 hotel franchising, licensing, and management across 30+ brands, 9,000+ properties, 1.7M rooms in 141 countries; includes luxury, premium, select, and midscale segments, plus Marriott Bonvoy loyalty platform (271M members).[web:1066][web:1059][web:1065]",
    "employee_count": -1000,
    "revenue_range": "FY2025 revenue $25.7B (+2.4% YoY from $25.1B in FY2024). Net income ~$2.5B. Marriott Bonvoy added ~43M new members in 2025, reaching 271M total at year-end. Pipeline of 3,900+ hotels (680,000+ rooms). Total room count grew to 9,400+ properties globally.[web:1059][web:1058][web:1060]",
    "hq_location": "7750 Wisconsin Avenue, Bethesda, Maryland 20814, United States.[web:1066]",
    "founded_year": 1927,
    "funding_stage": "Public company listed on NASDAQ (ticker: MAR). Market cap ~$60.7B as of early 2026.[web:1058]",
    "crm_used": "Salesforce Service Cloud, Experience Cloud (Salesforce-powered global customer recognition platform launched 2018; integrated across all call centres, web, mobile, and in-hotel channels to provide personalised guest recognition for Marriott Bonvoy members; covers 30 brands globally; enables associates to see full guest profile and loyalty status in real time).[web:1063][web:1068]",
    "survey_tools_used": [
        "Medallia Experience Cloud \u2014 'guestVoice' program (Marriott's primary enterprise guest feedback and VoC platform; Medallia is deployed globally to surface the voice of the customer to associates at all organisational levels; used by properties worldwide; hundreds of thousands of guests have received direct responses through the platform; drives customer loyalty and hotel performance benchmarking).[web:1067][web:1062]"
    ],
    "marketing_tools": [
        "Salesforce Marketing Cloud (integrated with Service Cloud and Experience Cloud for personalised omnichannel loyalty marketing across Marriott Bonvoy's 271M members \u2014 email, mobile, SMS, and in-app messaging).[web:1063][web:1068]",
        "Medallia guestVoice (text analytics and guest sentiment insights used to inform marketing and loyalty strategy).[web:1067]"
    ],
    "hr_tools": [
        "unknown"
    ],
    "tech_stack": [
        "CRM and Guest Recognition: Salesforce Service Cloud, Experience Cloud, Marketing Cloud (global customer recognition platform covering all 30 brands; real-time personalisation for 271M loyalty members; Apple Business Chat integration in mobile app).[web:1063][web:1068]",
        "Guest Feedback / VoC: Medallia Experience Cloud (guestVoice \u2014 global enterprise VoC program; post-stay surveys, real-time guest alerting, associate dashboards, and response management).[web:1067][web:1062]",
        "Mobile App: Marriott Bonvoy app (digital key, mobile check-in, room requests, upgrades, dining reservations; deep Salesforce CRM integration).[web:1063][web:1068]"
    ],
    "uses_competitor_of_surveysparrow": True,
    "competitor_names": [
        "Medallia (guestVoice \u2014 deployed globally across Marriott's 9,000+ properties for guest feedback, NPS, and VoC management; deep integration with associate workflows at the property level).[web:1067][web:1062]"
    ],
    "last_funding_amount": "unknown",
    "last_funding_date": "unknown",
    "recent_news": "February 2026: Marriott reported FY2025 results \u2014 revenue $25.7B, 271M Bonvoy members (+43M YoY), 9,400+ total properties, pipeline of 3,900+ hotels (680,000+ rooms). Described 2025 as a 'landmark year' driven by citizenM acquisition, midscale expansion, and luxury acceleration.[web:1059][web:1065] January 2026: Marriott announced a strategic realignment of its regional leadership structure \u2014 Neal Jones appointed President EMEA (reporting to CEO Anthony Capuano); Federico Greppi appointed President CALA; both join the executive leadership team as part of a geographic growth strategy.[web:1069] July 2025: Marriott completed the acquisition of the citizenM brand (35+ hotels, ~9,000 rooms globally), integrating it into Marriott Bonvoy in Q4 2025 \u2014 marking entry into the affordable design hotel segment.[web:1065] May 2025: 'Series by Marriott' new collection brand globally launched \u2014 a midscale/upscale collection enabling regionally-established independent hotel brands to join Marriott Bonvoy while retaining their independent identity.[web:1070] July 2025: CFO Leeny Oberg (26 years at Marriott) announced retirement effective March 31, 2026; Kathleen Mason (EVP and Controller) and Brad Hill (EVP Development) joined the executive team as planned successors for CFO and Development roles.[web:1064]",
    "hiring_for_roles": [
        "unknown"
    ],
    "leadership_changes": "July 2025: CFO Leeny Oberg announced retirement (effective March 31, 2026); Kathleen Mason named incoming CFO; Brad Hill named EVP Development. Both report to CEO Anthony Capuano.[web:1064] January 2026: Strategic regional restructuring \u2014 Neal Jones elevated to President EMEA; Federico Greppi appointed President CALA; both new roles report to Capuano and sit on the executive leadership team.[web:1069] CEO Anthony Capuano (appointed 2021) continues in his role; no CEO change indicated.[web:1066][web:1069]",
    "recent_product_launches": "May 2025: Series by Marriott \u2014 new global collection brand for midscale/upscale regionally distinctive hotels to join Marriott Bonvoy while maintaining independent identity; designed to accelerate pipeline in underserved markets globally.[web:1070] July 2025: citizenM brand acquisition completed \u2014 35+ hotels, ~9,000 rooms, affordable design-led properties integrated into Marriott Bonvoy Q4 2025; adds sub-luxury urban segment previously absent from Marriott portfolio.[web:1065] 2025: Marriott Bonvoy app continued upgrades \u2014 digital key improvements, AI-powered room upgrade suggestions, and expanded dining reservation integrations through the Salesforce-powered guest recognition platform.[web:1063][web:1065]",
    "likely_pain_points": [
        "Medallia contract review window \u2014 CFO and Development head transition: With CFO Leeny Oberg retiring in March 2026 and Kathleen Mason stepping into the CFO role, Marriott's technology vendor contracts and ROI assessments will be reviewed by new financial leadership within the first 12\u201318 months. Enterprise Medallia agreements of Marriott's scale are multi-million dollar, multi-year commitments; new CFO leadership often triggers budget scrutiny on large platform vendors.[web:1064][web:1067]",
        "Franchise owner and property manager feedback gap: Marriott is 98%+ asset-light and managed/franchised \u2014 meaning 9,000+ independent property owners and general managers are Marriott's primary B2B relationship; measuring franchisee satisfaction with corporate support quality, brand standards, technology tools (PMS upgrades, Salesforce CRM rollout), and training effectiveness requires a structured B2B NPS and relationship survey program, distinct from the consumer-facing Medallia guestVoice deployment.[web:1063][web:1067]",
        "citizenM and Series by Marriott onboarding satisfaction: Two newly launched brand integrations (citizenM Q4 2025, Series by Marriott from May 2025) are onboarding hotel owners and operators onto Marriott's platforms; capturing structured feedback from newly integrated property teams on the onboarding process quality, system ease-of-use, and Bonvoy integration experience is a near-term operational need not covered by the consumer-facing guestVoice program.[web:1065][web:1070]",
        "Bonvoy member satisfaction differentiation across 30 brands and 141 countries: With 271M Bonvoy members (+43M in 2025 alone), understanding satisfaction differences between luxury guests (Ritz-Carlton, St. Regis), midscale guests (Fairfield, Series by Marriott), and design-first guests (citizenM) requires brand-segmented, multilingual NPS and CSAT programs with granular analytics \u2014 a use case where Medallia's enterprise pricing and complexity may be disproportionate for individual brand teams seeking agility.[web:1059][web:1065][web:1067]",
        "Associate (employee) experience at 414,000 hospitality workers: Marriott's frontline hospitality associates \u2014 housekeepers, front desk staff, F&B employees \u2014 are geographically dispersed across 141 countries and largely without desk access; capturing their satisfaction, safety culture, and manager quality through short, mobile-first, multilingual pulse surveys is a structural employee experience gap not addressed by the consumer-focused Medallia and Salesforce deployments.[web:1060][web:1066]",
        "Regional leadership restructuring change management: January 2026 saw new Presidents for EMEA and CALA, with reporting structures and team compositions changing; measuring employee sentiment and alignment with new regional leaders through structured pulse surveys in the first 90\u2013180 days of the transition is an HR and leadership effectiveness priority not currently served by any documented internal survey tool.[web:1069][web:1064]"
    ]
},
{
    "company_name": "Lowe's Companies, Inc.[web:1076][web:1078]",
    "domain": "lowes.com",
    "industry": "Home improvement retail \u2014 brick-and-mortar and e-commerce stores selling building materials, appliances, tools, lumber, plumbing, flooring, and home d\u00e9cor; serving DIY consumers and Professional contractors (Pro) across ~1,700 US stores.[web:1078][web:1079]",
    "employee_count": -5000,
    "revenue_range": "FY2025 (year ended Jan 31, 2025) revenue ~$83.7B. Q3 FY2025 (ended Nov 1, 2024) net sales $20.8B. Q2 FY2025 net sales ~$24.0B (+1.1% YoY). Online sales grew 7.5% YoY in Q2. Net income FY2025 ~$7B. Market cap ~$132B.[web:1074][web:1083][web:1076][web:1078]",
    "hq_location": "1000 Lowe's Boulevard, Mooresville, North Carolina 28117, United States.[web:1076]",
    "founded_year": 1946,
    "funding_stage": "Public company listed on NYSE (ticker: LOW). Market cap ~$132B.[web:1076]",
    "crm_used": "Salesforce (actively used as part of Lowe's SaaS integration stack alongside Marketo; Salesforce appears in Lowe's documented technology architecture).[web:1077]",
    "survey_tools_used": [
        "unknown"
    ],
    "marketing_tools": [
        "Marketo (marketing automation; listed in Lowe's documented SaaS stack alongside Salesforce).[web:1077]",
        "Lowe's Rewards loyalty program (proprietary loyalty platform generating repeat buying data; expanded in 2025 as a core engagement tool for DIY customers).[web:1083]",
        "MyLowe's Pro Rewards (relaunched loyalty program for contractors \u2014 faster rewards, easier redemption \u2014 launched early 2025 replacing MVP Pro Rewards).[web:1079]"
    ],
    "hr_tools": [
        "unknown"
    ],
    "tech_stack": [
        "AI/ML inference: OpenAI GPT endpoints (GenAI for customer-facing applications), Azure ML (classical ML workloads for pricing, demand forecasting), NVIDIA Jetson + custom computer vision detectors (edge AI in stores for inventory and loss prevention).[web:1077][web:1081]",
        "Data platform: Palantir Foundry (enterprise data lakehouse and AI application platform; real-time inventory streams and loyalty CDP), Snowflake (data warehouse), Databricks (with Autoloader).[web:1077]",
        "MLOps: GitHub \u2192 Argo \u2192 Azure ML automated pipeline; bias and drift testing; Grafana + Prometheus for CV model monitoring; custom drift alerts for ML and LLM outputs.[web:1077]",
        "Integration and ETL: MuleSoft Anypoint, Fivetran, Airbyte, Workato, Tray.io, Zapier, Hevo Data, Segment, Estuary Flow; AWS Lambda, Azure Data Factory, Snowflake Snowpipe, Debezium (CDC for OLTP sync).[web:1077]",
        "SaaS apps: Salesforce, Marketo, Stripe.[web:1077]",
        "Security: Zero-trust APIs, role-based model access, prompt-safety filters for LLM outputs.[web:1077]",
        "OpenAI partnership: Expanded November 2025 to build AI tools across guided selling, store associate productivity, and supply-chain operations.[web:1081]"
    ],
    "uses_competitor_of_surveysparrow": False,
    "competitor_names": [],
    "last_funding_amount": "unknown",
    "last_funding_date": "unknown",
    "recent_news": "November 2025: Lowe's announced a deepened partnership with OpenAI to build AI-powered tools for customer-facing guided selling, store associate productivity, and supply-chain operations, positioning itself as what its CDO Seemantini Godbole called an 'elite tier AI enterprise.' Digital sales growth of 7.5% YoY was specifically attributed to enhanced AI-powered digital tools.[web:1081][web:1083] November 2025: Q3 FY2025 results \u2014 $20.8B net sales; adjusted diluted EPS increased 5.9% YoY to $3.06; Pro segment and online sales continued to outperform DIY walk-in traffic as the housing market remains under pressure from high mortgage rates.[web:1073][web:1074] December 2024: Lowe's 2024 Investor Day \u2014 announced MyLowe's Pro Rewards relaunch (for small-to-medium contractors), expansion of Palantir Foundry AI applications to all stores, guided selling tools for associates via AI, and third-party marketplace integration for store associates to sell items not stocked in-store.[web:1079][web:1077]",
    "hiring_for_roles": [
        "unknown"
    ],
    "leadership_changes": "CEO Marvin Ellison (appointed May 2018) continues in role; no CEO change announced or indicated through early 2026.[web:1078] CDO/CIO Seemantini Godbole continues as Chief Digital and Information Officer, driving the AI-first technology agenda.[web:1079][web:1081] No major C-suite changes documented in 2024\u20132025.",
    "recent_product_launches": "Early 2025: MyLowe's Pro Rewards relaunched \u2014 redesigned loyalty program for small-to-medium contractors replacing MVP Pro Rewards; rewards faster to earn, easier to redeem; supports 'Total Home' strategy of growing Pro customer share.[web:1079][web:1083] December 2024 (Investor Day launch): Third-party marketplace for in-store associates \u2014 store associates can now search and sell items from Lowe's online marketplace not stocked at their physical location; guided AI selling tools for associates deployed systemwide.[web:1079][web:1077] 2025: Palantir Foundry rollout to all ~1,700 US stores for real-time inventory optimisation, computer vision-based loss prevention (NVIDIA Jetson edge devices), and AI-powered supply chain operations.[web:1077]",
    "likely_pain_points": [
        "No confirmed enterprise survey platform despite 270,000 employees and 170M+ annual customer transactions: Lowe's has no publicly documented NPS, CSAT, or employee survey platform \u2014 relying on Palantir Foundry behavioral data, loyalty program signals, and app store reviews as proxies for customer satisfaction; structured feedback infrastructure is a notable gap at $83.7B revenue and 1,700 stores.[web:1077][web:1083][web:1076]",
        "Pro contractor NPS and MyLowe's Pro Rewards adoption feedback: The relaunched MyLowe's Pro Rewards program (2025) targets small-to-medium contractors \u2014 a commercially critical but notoriously hard-to-retain B2B segment; measuring whether the new rewards structure actually improves contractor satisfaction, redemption rates, and switching intention requires structured relationship NPS and post-interaction CSAT that the loyalty platform alone cannot provide.[web:1079][web:1083]",
        "AI tool satisfaction among 270,000 store associates: Lowe's is deploying GenAI guided selling tools, computer vision edge devices, and AI-powered marketplace search to store associates systemwide; measuring whether associates find these tools helpful, understand them, and trust them \u2014 and identifying training gaps \u2014 requires a structured, mobile-first, short-form pulse survey program that none of Lowe's documented tools (Palantir, OpenAI, Azure ML, Marketo) is designed to provide.[web:1081][web:1077]",
        "Measuring satisfaction gaps between Pro and DIY segments: Lowe's 'Total Home' strategy simultaneously serves professional contractors (Pro) and DIY homeowners \u2014 two segments with very different satisfaction drivers (Pro: job site delivery, dedicated account managers, credit terms; DIY: product discovery, installation help, return ease); disentangling their respective NPS scores and pain points requires segmented, multi-touchpoint survey architecture not covered by the Salesforce/Palantir stack.[web:1079][web:1083]",
        "Housing market headwinds and SSS softness \u2014 urgent feedback loop on pricing and assortment: With same-store sales pressured by high mortgage rates and declining large-ticket discretionary home improvement projects, Lowe's needs real-time survey data on why shoppers are deferring purchases (price sensitivity? project confidence? competing offers?) to inform tactical pricing, promotion, and assortment decisions \u2014 a business decision-support use case for quick, targeted surveys that behavioral analytics alone miss.[web:1074][web:1076]",
        "Frontline employee experience during technology transformation: Headcount has declined from 340,000 (2022) to 270,000 (2025) while the workload per associate has intensified with AI tool rollouts; systematically tracking frontline morale, technology adoption readiness, and manager effectiveness through pulse surveys at a 270,000-person scale is a structural EX gap \u2014 especially relevant as OpenAI partnership tools roll out to all 1,700 stores.[web:1081][web:1077]"
    ]
},
{
    "company_name": "WeWork Inc.[web:1085][web:1097]",
    "domain": "wework.com",
    "industry": "Flexible workspace and coworking \u2014 provides private offices, hot desks, dedicated desks, meeting rooms, event spaces, and space management software (WeWork Workplace) to individuals, startups, and enterprise companies in Class A commercial buildings globally.[web:1085][web:1093][web:1098]",
    "employee_count": -500,
    "revenue_range": "Exact post-bankruptcy revenue not publicly disclosed (WeWork became private post-June 2024 emergence). Pre-bankruptcy FY2023 revenue was ~$3.4B. Post-restructuring: company reached positive EBITDA in late 2024/early 2025; $80\u2013100M capital investment in location upgrades planned for 2025; operating ~600 global locations (170 owned US/Canada + franchise/partner network).[web:1089][web:1094][web:1095]",
    "hq_location": "75 Varick Street, New York, NY 10013, United States.[web:1085][web:1097]",
    "founded_year": 2010,
    "funding_stage": "Private company. Emerged from Chapter 11 bankruptcy on June 11, 2024 after shedding ~$4B in debt, renegotiating 190+ leases, and raising $400M in new equity capital. Total pre-bankruptcy funding was >$22B (primarily from SoftBank). Now privately held by post-reorganization equity holders; not publicly traded.[web:1092][web:1086][web:1095]",
    "crm_used": "Salesforce (WeWork operates in Salesforce Tower, San Francisco, and Salesforce is part of its documented SaaS stack for member/enterprise sales CRM management).[web:1095][web:1096]",
    "survey_tools_used": [
        "unknown"
    ],
    "marketing_tools": [
        "Looker (BI dashboards \u2014 scheduled report delivery to teams for coworking metrics, occupancy, and member analytics).[web:1096]",
        "Anaplan (financial planning, budgeting, and forecasting across locations and P&L lines).[web:1096]"
    ],
    "hr_tools": [
        "unknown"
    ],
    "tech_stack": [
        "WeWork Workplace (proprietary SaaS space management software \u2014 desk booking, room reservations, occupancy analytics, hybrid work planning; integrated into the WeWork App as of March 2024; available as standalone B2B SaaS to non-WeWork tenants via the Coworking Partner Network).[web:1093][web:1098]",
        "WeWork App (unified member app \u2014 space booking, building access, visitor management, amenity reservations, Workplace integrations).[web:1098]",
        "Salesforce (CRM for enterprise sales pipeline and account management).[web:1095][web:1096]",
        "Looker (BI and data dashboards for occupancy, membership, and operational reporting).[web:1096]",
        "Anaplan (financial planning and forecasting across global location portfolio).[web:1096]"
    ],
    "uses_competitor_of_surveysparrow": False,
    "competitor_names": [],
    "last_funding_amount": "$400M (new equity capital raised as part of Chapter 11 emergence).[web:1092][web:1094]",
    "last_funding_date": "June 2024 (bankruptcy emergence).[web:1092]",
    "recent_news": "June 2025: WeWork confirmed to Bisnow and Inman that it has returned to profitability \u2014 positive EBITDA achieved for the first time in years; the company is debt-free, invested $80\u2013100M in location upgrades in 2025, and entered a partnership with the Ritz-Carlton Leadership Center to improve hospitality training across its workforce.[web:1089][web:1094] May 2025: WeWork reported positive EBITDA for the prior six-month period (H2 2024), operating ~600 global locations (170 owned US/Canada locations + global franchise/partner network across 37 countries); cash flow slightly negative due to planned capital reinvestment in physical upgrades.[web:1095] October 2024: WeWork launched its Coworking Partner Network \u2014 an affiliate program giving WeWork Workplace software users access to 75+ third-party Vast Coworking Group locations (Venture X, Office Evolution, Intelligent Office) across 50+ new US/Canada markets, expanding the addressable footprint without taking on new leases.[web:1093]",
    "hiring_for_roles": [
        "unknown"
    ],
    "leadership_changes": "June 2024: CEO David Tolley stepped down upon WeWork's emergence from Chapter 11. John Santora (nearly five decades in commercial real estate, formerly Chairman at CBRE) appointed as new CEO \u2014 signalling a pivot to operational discipline and real estate credibility over hypergrowth culture.[web:1092][web:1097] No further documented C-suite changes in 2025.[web:1097]",
    "recent_product_launches": "March 2024: WeWork App 2.0 launched \u2014 integrated WeWork Workplace (space management software) directly into the member-facing app, creating a single hub for booking, building access, occupancy planning, and hybrid work management.[web:1098] October 2024: Coworking Partner Network launched \u2014 affiliate marketplace giving WeWork Workplace software subscribers access to 75+ Vast Coworking Group locations in 50+ new North American markets not served by WeWork-owned locations.[web:1093] 2025: $80\u2013100M investment in physical location upgrades (renovations, amenity improvements, design refresh) across the global portfolio; partnership with Ritz-Carlton Leadership Center for hospitality training across all WeWork staff.[web:1094]",
    "likely_pain_points": [
        "Member satisfaction and retention as the primary post-bankruptcy growth lever: WeWork's turnaround thesis depends entirely on retaining existing members and demonstrating that its product has improved since bankruptcy; yet there is no publicly documented NPS or structured CSAT program to measure whether the $80\u2013100M in location upgrades, hospitality training, and WeWork App improvements are actually improving member satisfaction \u2014 a critical blind spot when occupancy rate is the single most important financial metric.[web:1089][web:1094][web:1095]",
        "Coworking Partner Network member experience consistency: WeWork's new affiliate model extends its Workplace software to 75+ third-party Vast Coworking Group locations (Venture X, Office Evolution, Intelligent Office) where WeWork does not control the physical experience; tracking member satisfaction and Net Promoter Score at affiliate locations versus owned locations requires a standardised post-visit survey program that WeWork Workplace (a booking tool) was not designed to deliver.[web:1093][web:1098]",
        "Enterprise member onboarding and renewal NPS: WeWork's commercial pivot targets large enterprise accounts (companies needing 50\u2013500+ desks); measuring enterprise account manager satisfaction, contract renewal intent, and onboarding quality through structured B2B relationship NPS surveys is a standard enterprise customer success practice \u2014 yet no such tool is documented in WeWork's post-bankruptcy stack.[web:1094][web:1097]",
        "Employee experience and culture rebuilding post-bankruptcy: WeWork went from a 14,000-person workforce (2019 peak) to roughly 2,300 today, having conducted multiple rounds of mass layoffs; the surviving team is small, under new leadership (CEO Santora since June 2024), and operating in a radically different cost-conscious culture; measuring employee engagement, trust in leadership, and psychological safety through formal pulse surveys is operationally important for retention of the remaining talent.[web:1085][web:1092][web:1097]",
        "Hospitality training effectiveness measurement: WeWork's June 2025 partnership with the Ritz-Carlton Leadership Center to improve hospitality training is a direct signal that service quality is a strategic focus; measuring training effectiveness, customer-facing associate confidence, and behaviour change through pre/post training surveys is a standard L&D practice that the new Ritz-Carlton partnership likely requires but no tool is documented for.[web:1094][web:1089]"
    ]
},
{
    "company_name": "Beyond, Inc. (formerly Overstock.com; operates bedbathandbeyond.com and beyond.com)[web:1113][web:1107]",
    "domain": "bedbathandbeyond.com",
    "industry": "Online-only home furnishings and goods e-commerce retailer \u2014 furniture, bedding, bath, kitchen, d\u00e9cor, and home improvement products sold via bedbathandbeyond.com and beyond.com.[web:1107][web:1113]",
    "employee_count": -100,
    "revenue_range": "FY2023 revenue ~$1.6B (post-rebrand). FY2022 revenue ~$1.9B. Revenue has been declining due to housing market softness and macro headwinds. Company is publicly traded (NASDAQ: BYON) but has been loss-making since the rebrand.[web:1113]",
    "hq_location": "799 West Coliseum Way, Midvale, Utah 84047, United States.[web:1113]",
    "founded_year": 1999,
    "funding_stage": "Public company listed on NASDAQ (ticker: BYON). Original Bed Bath & Beyond (the brick-and-mortar) was founded in 1971 and existed from 1971\u20132023 before full liquidation.[web:1100][web:1113]",
    "crm_used": "unknown",
    "survey_tools_used": [
        "unknown"
    ],
    "marketing_tools": [
        "unknown"
    ],
    "hr_tools": [
        "unknown"
    ],
    "tech_stack": [
        "unknown"
    ],
    "uses_competitor_of_surveysparrow": False,
    "competitor_names": [],
    "last_funding_amount": "unknown",
    "last_funding_date": "unknown",
    "recent_news": "The original Bed Bath & Beyond (brick-and-mortar) filed Chapter 11 bankruptcy on April 23, 2023, liquidated all ~480 US stores and ~174 Canadian stores, and the last physical location closed July 30, 2023.[web:1100][web:1101][web:1103] Overstock.com acquired the BB&B brand IP, domain, trademarks, customer database, and loyalty program data for $21.5M in a bankruptcy court-supervised auction on June 27, 2023.[web:1107][web:1109] Overstock relaunched bedbathandbeyond.com in August 2023 and renamed its entire corporate entity to Beyond, Inc. (BYON) in January 2024.[web:1113]",
    "hiring_for_roles": [
        "unknown"
    ],
    "leadership_changes": "The original Bed Bath & Beyond's final CEO was Sue Gove (appointed June 2022, resigned upon bankruptcy filing April 2023). The current bedbathandbeyond.com entity (Beyond, Inc.) is led by Adrianne Lee as CEO and Jonathan Johnson (who championed the acquisition) previously served as CEO; Johnson stepped down in September 2023.[web:1113]",
    "recent_product_launches": "unknown",
    "likely_pain_points": []
},
{
    "company_name": "Exxon Mobil Corporation[web:1124][web:1128]",
    "domain": "exxonmobil.com",
    "industry": "Integrated energy \u2014 upstream oil and gas exploration and production, downstream refining, chemicals, lubricants (Mobil 1), and low carbon solutions (carbon capture and storage, hydrogen, biofuels) globally.[web:1124][web:1122][web:1123]",
    "employee_count": -1000,
    "revenue_range": "FY2025 total revenue ~$324B. Full-year 2025 earnings $28.8B. Q4 2025 earnings $6.5B. Distributed $37.2B to shareholders in 2025 (dividends + buybacks). Free cash flow $5.6B in Q4 2025.[web:1115][web:1128]",
    "hq_location": "22777 Springwoods Village Parkway, Spring, Texas 77389, United States (relocated from Irving, TX to Spring, TX in 2023).[web:1124]",
    "founded_year": 1999,
    "funding_stage": "Public company listed on NYSE (ticker: XOM). Market cap ~$642B (as of March 2026). Standard Oil heritage dating to 1870; current ExxonMobil formed by Exxon\u2013Mobil merger in 1999.[web:1116][web:1124]",
    "crm_used": "Salesforce Sales Cloud (selected in 2024, replacing legacy CRM; go-live 2024; covers Sales Automation, CRM, and Sales Engagement across ExxonMobil's commercial and B2B sales teams).[web:1121][web:1125]",
    "survey_tools_used": [
        "unknown"
    ],
    "marketing_tools": [
        "unknown"
    ],
    "hr_tools": [
        "unknown"
    ],
    "tech_stack": [
        "CRM/Sales: Salesforce Sales Cloud (2024 go-live; replaces legacy CRM; integrates with existing ERP and compliance systems).[web:1121][web:1125]",
        "ERP: SAP (widely used across ExxonMobil's global operations for finance, supply chain, plant maintenance, and HR; standard in the energy sector at ExxonMobil's scale).[web:1125]",
        "AI/Digital: ExxonMobil has a significant internal data science and AI function (Upstream data analytics, reservoir simulation, refinery optimisation); cloud infrastructure partners include Microsoft Azure and AWS (inferred from enterprise energy sector norms and Salesforce/SAP integrations).[web:1125][web:1122]"
    ],
    "uses_competitor_of_surveysparrow": False,
    "competitor_names": [],
    "last_funding_amount": "unknown",
    "last_funding_date": "unknown",
    "recent_news": "January 30, 2026: ExxonMobil reported FY2025 results \u2014 full-year earnings $28.8B; distributed $37.2B to shareholders; Q4 2025 earnings $6.5B, free cash flow $5.6B; structural cost savings of $11.3B achieved since 2019 with $2.7B delivered in 2025.[web:1115][web:1128] November 2025: Jon Gibbs (President, Global Projects) promoted to Senior President, ExxonMobil Global Operations effective January 1, 2026; Staale Knudsen appointed President of Global Projects.[web:1126] December 2024: Dan Ammann succeeded Liam Mallon as President, ExxonMobil Upstream Company; Bartley Engle appointed President, Low Carbon Solutions effective January 2025, as ExxonMobil accelerates its carbon capture, hydrogen, and biofuels strategy.[web:1122]",
    "hiring_for_roles": [
        "unknown"
    ],
    "leadership_changes": "January 2025: Dan Ammann (former GM/Cruise CEO) became President of ExxonMobil Upstream Company, succeeding Liam Mallon (retired after 34 years); Bartley Engle appointed President of Low Carbon Solutions.[web:1122] January 2026: Jon Gibbs elevated to Senior President, ExxonMobil Global Operations; Staale Knudsen appointed President, ExxonMobil Global Projects Company.[web:1126] CEO Darren Woods continues in his role (appointed 2017). CFO Kathryn Mikells continues in her role.[web:1124]",
    "recent_product_launches": "2024\u20132025: ExxonMobil Low Carbon Solutions expanded its carbon capture and storage (CCS) network (Denbury acquisition, $4.9B in 2023, completed 2024; largest CO2 pipeline and injection network in the US). Biofuels scale-up at Strathcona, Canada (2,000 barrels/day low carbon hydrogen for oil sands operations). ExxonMobil Proxxima \u2014 new thermosetting resin and advanced materials product line for lightweight, high-strength industrial applications.[web:1123][web:1124]",
    "likely_pain_points": [
        "Fresh Salesforce Sales Cloud deployment creates integration-layer opportunity: ExxonMobil went live on Salesforce Sales Cloud in 2024, replacing legacy CRM across commercial and B2B sales teams; enterprise CRM deployments at this scale (58,000 employees, ~$324B revenue) routinely require 12\u201324 months of process optimisation, and closing-the-loop with B2B customer satisfaction surveys (post-contract NPS, account health CSAT) is a natural adjacency to the new Salesforce investment.[web:1121][web:1125]",
        "B2B customer satisfaction for Mobil-branded lubricants and specialty chemicals: ExxonMobil's downstream and chemicals division serves millions of B2B accounts (fleet operators, OEMs, industrial manufacturers) with Mobil 1 and Mobil Delvac lubricants, as well as Proxxima advanced materials; measuring distributor NPS, OEM technical support CSAT, and post-delivery satisfaction at scale across these commercial accounts is a known gap for enterprise energy companies that primarily rely on field sales teams and transactional data.[web:1124][web:1121]",
        "Low Carbon Solutions customer and partner feedback: ExxonMobil's fastest-growing business unit (CCS, hydrogen, biofuels) works with industrial emitters, government agencies, and project partners in novel ways; measuring partner satisfaction with project development processes, regulatory navigation support, and technical collaboration quality through structured B2B surveys is a strategic priority as this division competes for long-term CCS infrastructure contracts.[web:1122][web:1123]",
        "Employee engagement during sustained workforce reduction: ExxonMobil's headcount has fallen from 75,000 (2014) to 58,000 (2025), representing a 23% reduction over a decade including continued cuts in 2025 (-2,900 employees); systematically monitoring employee morale, retention risk, and alignment with the company's evolving low-carbon strategy through formal employee survey programs is critical to retaining technical and operational talent in a highly competitive energy talent market.[web:1116][web:1122]",
        "Retail fuel and convenience customer satisfaction (Exxon and Mobil stations): ExxonMobil operates and franchises thousands of Exxon and Mobil branded service stations globally; capturing post-visit CSAT from fuel and convenience retail customers at scale (mobile-friendly, frictionless, multilingual) and benchmarking performance across company-owned vs. franchised stations is a consumer CX gap with clear commercial value \u2014 yet no survey platform is publicly documented for this use case.[web:1124]"
    ]
},
]
    
    # Using upsert to avoid duplicate errors if run multiple times
    supabase.table("company_intelligence").upsert(companies, on_conflict="domain").execute()
    print(f"{len(companies)} companies seeded")

if __name__ == "__main__":
    seed_companies()
