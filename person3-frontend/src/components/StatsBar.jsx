import React from 'react';
import { Users, UserCheck, UserX, Target, BarChart3 } from 'lucide-react';
import clsx from 'clsx';

export default function StatsBar({ leads }) {
  // Compute metrics
  const totalLeads = 
    leads.icp_alignment.length + 
    leads.lead_scoring.length + 
    leads.awaiting_transcript.length + 
    leads.discovery_intelligence.length + 
    leads.ready_for_presales.length + 
    leads.not_a_lead.length;

  const goodLeadsCount = 
    leads.awaiting_transcript.length + 
    leads.discovery_intelligence.length + 
    leads.ready_for_presales.length +
    leads.lead_scoring.filter(l => l.lead_context?.some(c => c.lead_label === 'GOOD_LEAD')).length;

  const notALeadCount = leads.not_a_lead.length;
  const readyForPresalesCount = leads.ready_for_presales.length;

  // Compute average fit score
  let totalFitScore = 0;
  let leadsWithFitScore = 0;

  // Flatten all contexts to find fit scores
  Object.values(leads).flat().forEach(lead => {
    // Agent 2 creates Contexts with fit_score
    const scoringContext = lead.lead_context?.find(c => c.stage === 'lead_scoring');
    if (scoringContext && scoringContext.fit_score != null) {
      totalFitScore += scoringContext.fit_score;
      leadsWithFitScore++;
    }
  });

  const avgFitScore = leadsWithFitScore > 0 ? Math.round(totalFitScore / leadsWithFitScore) : 0;

  return (
    <div className="flex items-center justify-between border-b border-[var(--color-border)] bg-[var(--color-card-bg)] px-6 py-4 shadow-sm mb-6 rounded-lg sticky top-0 z-10 w-full mx-auto max-w-[1600px] mt-4">
      <div className="flex items-center gap-6 divide-x divide-[var(--color-border)]">
        
        <StatItem 
          icon={<Users className="w-5 h-5 text-blue-400" />} 
          label="Total Leads" 
          value={totalLeads} 
        />
        
        <StatItem 
          icon={<UserCheck className="w-5 h-5 text-emerald-400" />} 
          label="Good Leads" 
          value={goodLeadsCount} 
          className="pl-6"
        />

        <StatItem 
          icon={<UserX className="w-5 h-5 text-red-400" />} 
          label="Not a Lead" 
          value={notALeadCount} 
          className="pl-6"
        />

        <StatItem 
          icon={<Target className="w-5 h-5 text-purple-400" />} 
          label="Ready for Presales" 
          value={readyForPresalesCount} 
          className="pl-6"
        />

        <StatItem 
          icon={<BarChart3 className={clsx("w-5 h-5", avgFitScore >= 60 ? "text-emerald-400" : "text-yellow-400")} />} 
          label="Avg Fit Score" 
          value={avgFitScore} 
          className="pl-6"
        />
      </div>
      
      <div className="flex items-center gap-2 text-xs text-gray-400 font-medium">
        <span className="flex h-2 w-2 relative">
          <span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-emerald-400 opacity-75"></span>
          <span className="relative inline-flex rounded-full h-2 w-2 bg-emerald-500"></span>
        </span>
        Live Updates Connected
      </div>
    </div>
  );
}

function StatItem({ icon, label, value, className }) {
  return (
    <div className={clsx("flex items-center gap-3", className)}>
      <div className="p-2 bg-[var(--color-board-bg)] rounded-md shadow-inner border border-white/5">
        {icon}
      </div>
      <div>
        <p className="text-xs text-gray-400 font-medium tracking-wide uppercase">{label}</p>
        <p className="text-xl font-semibold text-white tracking-tight">{value}</p>
      </div>
    </div>
  );
}
