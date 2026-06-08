import React from 'react';
import { Users, UserCheck, UserX, Target, BarChart3 } from 'lucide-react';
import clsx from 'clsx';

export default function StatsBar({ leads }) {
  const totalLeads =
    (leads.icp_alignment?.length || 0) +
    (leads.lead_scoring?.length || 0) +
    (leads.discovery_intelligence?.length || 0) +
    (leads.ready_for_presales?.length || 0) +
    (leads.not_a_lead?.length || 0);

  const goodLeadsCount =
    (leads.discovery_intelligence?.length || 0) +
    (leads.ready_for_presales?.length || 0) +
    (leads.lead_scoring?.filter((l) => l.lead_context?.some((c) => c.lead_label === 'GOOD_LEAD')).length || 0);

  const notALeadCount = leads.not_a_lead?.length || 0;
  const readyForPresalesCount = leads.ready_for_presales?.length || 0;

  const seen = new Set();
  let totalFitScore = 0;
  let leadsWithFitScore = 0;
  Object.values(leads).flat().forEach((lead) => {
    if (seen.has(lead.id)) return;
    seen.add(lead.id);
    const scoringContext = lead.lead_context?.find((c) => c.stage === 'lead_scoring');
    if (scoringContext && scoringContext.fit_score != null) {
      totalFitScore += scoringContext.fit_score;
      leadsWithFitScore++;
    }
  });
  const avgFitScore = leadsWithFitScore > 0 ? Math.round(totalFitScore / leadsWithFitScore) : 0;

  return (
    <div className="flex items-center justify-between border border-[var(--color-border)] bg-[var(--color-surface)] px-6 py-4 shadow-sm mb-6 rounded-xl sticky top-0 z-10 w-full mx-auto max-w-[1600px] mt-4">
      <div className="flex items-center gap-6 divide-x divide-[var(--color-border)]">
        <StatItem icon={<Users className="w-5 h-5 text-orange-500" />} label="Total Leads" value={totalLeads} />
        <StatItem icon={<UserCheck className="w-5 h-5 text-green-600" />} label="Good Leads" value={goodLeadsCount} className="pl-6" />
        <StatItem icon={<UserX className="w-5 h-5 text-zinc-700" />} label="Not a Lead" value={notALeadCount} className="pl-6" />
        <StatItem icon={<Target className="w-5 h-5 text-green-600" />} label="Ready for Presales" value={readyForPresalesCount} className="pl-6" />
        <StatItem
          icon={<BarChart3 className={clsx('w-5 h-5', avgFitScore >= 60 ? 'text-green-600' : 'text-orange-500')} />}
          label="Avg Fit Score"
          value={avgFitScore}
          className="pl-6"
        />
      </div>

      <div className="flex items-center gap-2 text-xs text-[var(--color-ink-soft)] font-medium">
        <span className="flex h-2 w-2 relative">
          <span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-green-400 opacity-75" />
          <span className="relative inline-flex rounded-full h-2 w-2 bg-green-500" />
        </span>
        Live Updates Connected
      </div>
    </div>
  );
}

function StatItem({ icon, label, value, className }) {
  return (
    <div className={clsx('flex items-center gap-3', className)}>
      <div className="p-2 bg-[var(--color-surface-2)] rounded-md border border-[var(--color-border)]">
        {icon}
      </div>
      <div>
        <p className="text-xs text-[var(--color-ink-soft)] font-medium tracking-wide uppercase">{label}</p>
        <p className="text-xl font-semibold text-[var(--color-ink)] tracking-tight">{value}</p>
      </div>
    </div>
  );
}
