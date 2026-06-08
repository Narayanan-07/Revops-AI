import React from 'react';
import { X, CheckCircle2, TrendingUp, AlertTriangle, FileText } from 'lucide-react';
import clsx from 'clsx';

export default function LeadDrawer({ isOpen, onClose, selectedItem }) {
  if (!isOpen || !selectedItem) return null;

  const { leads, lead_context } = selectedItem;

  const agent1 = lead_context?.find((c) => c.stage === 'icp_alignment' || c.updated_by_agent === 'icp_alignment_agent');
  const agent2 = lead_context?.find((c) => c.stage === 'lead_scoring' || c.updated_by_agent === 'lead_scoring_agent');
  const agent3 = lead_context?.find((c) => c.stage === 'discovery_intelligence' || c.updated_by_agent === 'discovery_intelligence_agent');

  const notALead = agent2?.lead_label === 'NOT_A_LEAD';

  return (
    <>
      {/* Backdrop */}
      <div className="fixed inset-0 bg-black/30 backdrop-blur-sm z-40 transition-opacity duration-300" onClick={onClose} />

      {/* Drawer */}
      <div
        className={clsx(
          'fixed top-0 right-0 h-full w-[500px] max-w-full bg-[var(--color-page)] border-l border-[var(--color-border)] shadow-2xl z-50',
          'transform transition-transform duration-500 ease-in-out flex flex-col',
          isOpen ? 'translate-x-0' : 'translate-x-full'
        )}
      >
        {/* Header */}
        <div className="flex items-center justify-between p-6 border-b border-[var(--color-border)] sticky top-0 bg-[var(--color-surface)]/95 backdrop-blur-md z-10">
          <div>
            <h2 className="text-xl font-bold tracking-tight text-[var(--color-ink)] mb-1">
              {leads?.company_name || 'Unknown Company'}
            </h2>
            <a
              href={`https://${leads?.domain}`}
              target="_blank"
              rel="noreferrer"
              className="text-sm text-orange-600 hover:text-orange-700 transition-colors flex items-center gap-1.5"
            >
              {leads?.domain}
            </a>
          </div>
          <button
            onClick={onClose}
            className="p-2 bg-black/5 hover:bg-black/10 rounded-full transition-colors text-[var(--color-ink-soft)] hover:text-[var(--color-ink)]"
          >
            <X className="w-5 h-5" />
          </button>
        </div>

        {/* Content */}
        <div className="flex-1 overflow-y-auto custom-scrollbar p-6 space-y-6">

          {/* Agent 1 */}
          <SectionBlock title="ICP Alignment Agent" icon={<CheckCircle2 className="w-4 h-4" />} accent="orange" active={!!agent1}>
            {agent1 ? (
              <div className="space-y-4 text-sm mt-4 text-[var(--color-ink-soft)]">
                <ScoreRow label="ICP Score" value={agent1.icp_alignment_score} />
                <div>
                  <h4 className="font-bold text-[var(--color-ink)] mb-1">Buying Intent</h4>
                  <p className="italic bg-[var(--color-surface-2)] p-3 rounded-lg border border-[var(--color-border)]">{agent1.buying_intent_summary || 'N/A'}</p>
                </div>
                <ListDisplay title="Pain Points" items={agent1.pain_point_matches} />
                <ListDisplay title="Firmographic" items={agent1.firmographic_signals} />
                <ListDisplay title="Technographic" items={agent1.technographic_signals} />
                <ListDisplay title="Chronographic" items={agent1.chronographic_signals} />
                <ListDisplay title="Gaps" items={agent1.icp_gaps} tone="warn" />
              </div>
            ) : <Pending text="Processing…" />}
          </SectionBlock>

          {/* Agent 2 */}
          <SectionBlock title="Lead Scoring Agent" icon={<TrendingUp className="w-4 h-4" />} accent={notALead ? 'zinc' : 'green'} active={!!agent2}>
            {agent2 ? (
              <div className="space-y-4 text-sm mt-4 text-[var(--color-ink-soft)]">
                <ScoreRow label="Fit Score" value={agent2.fit_score} />
                <div className="flex gap-2 flex-wrap">
                  <span className={clsx(
                    'px-2.5 py-1 rounded-md text-xs font-bold uppercase tracking-wider border',
                    notALead ? 'bg-zinc-900 border-zinc-800 text-white' : 'bg-green-100 border-green-200 text-green-700'
                  )}>
                    {notALead ? 'Not a Lead' : 'Good Lead'}
                  </span>
                  <span className="px-2.5 py-1 rounded-md bg-[var(--color-surface-2)] border border-[var(--color-border)] text-xs font-bold uppercase tracking-wider text-[var(--color-ink-soft)] flex items-center gap-1.5">
                    Signal: <span className="text-[var(--color-ink)]">{agent2.buying_signal_strength || 'medium'}</span>
                  </span>
                </div>
                <div>
                  <h4 className="font-bold text-[var(--color-ink-soft)] mb-2 text-xs uppercase tracking-widest">Reasoning</h4>
                  <p className="leading-relaxed whitespace-pre-line text-xs">{agent2.scoring_reasoning || 'N/A'}</p>
                </div>
                <ListDisplay title="Risk Factors" items={agent2.risk_factors} tone="warn" />
                <ListDisplay title="Similar Won Deals" items={agent2.similar_won_deals} tone="good" />
              </div>
            ) : <Pending text="Pending scoring…" />}
          </SectionBlock>

          {/* Agent 3 */}
          <SectionBlock title="Discovery Intelligence Agent" icon={<FileText className="w-4 h-4" />} accent="orange" active={!!agent3}>
            {agent3 ? (
              <div className="space-y-4 text-sm mt-4 text-[var(--color-ink-soft)]">
                <ListDisplay title="Exact Needs" items={agent3.exact_customer_needs} />
                <ListDisplay title="Feature Recommendations" items={agent3.feature_recommendations} tone="good" />
                <ListDisplay title="Demo Focus" items={agent3.demo_focus_areas} numbered />
                {agent3.confirmed_buying_intent && (
                  <div>
                    <h4 className="font-bold text-[var(--color-ink-soft)] mb-2 text-xs uppercase tracking-widest">Confirmed Intent</h4>
                    <p className="italic bg-[var(--color-surface-2)] p-3 rounded-lg border border-[var(--color-border)]">{agent3.confirmed_buying_intent}</p>
                  </div>
                )}
                {agent3.recommended_pricing_tier && (
                  <div className="flex items-center justify-between p-3 rounded-lg bg-green-50 border border-green-200">
                    <span className="font-bold text-green-700 text-xs uppercase tracking-wider">Recommended Tier</span>
                    <span className="font-bold text-green-800 bg-green-100 px-2 py-1 rounded">{agent3.recommended_pricing_tier}</span>
                  </div>
                )}
                <div>
                  <h4 className="font-bold text-[var(--color-ink-soft)] mb-2 text-xs uppercase tracking-widest flex items-center gap-2">
                    <AlertTriangle className="w-3.5 h-3.5 text-orange-500" />
                    Presales Handoff Note
                  </h4>
                  <div className="bg-orange-50 border border-orange-200 p-4 rounded-xl text-[var(--color-ink)] leading-relaxed text-sm whitespace-pre-line">
                    {agent3.presales_handoff_note || 'N/A'}
                  </div>
                </div>
              </div>
            ) : <Pending text="Appears after a transcript is uploaded and processed." />}
          </SectionBlock>
        </div>
      </div>
    </>
  );
}

const ACCENTS = {
  orange: { text: 'text-orange-600', bar: 'bg-orange-500', box: 'bg-orange-50 border-orange-200' },
  green: { text: 'text-green-700', bar: 'bg-green-500', box: 'bg-green-50 border-green-200' },
  zinc: { text: 'text-zinc-800', bar: 'bg-zinc-700', box: 'bg-zinc-100 border-zinc-200' },
};

function SectionBlock({ title, icon, accent = 'orange', active, children }) {
  const a = ACCENTS[accent] || ACCENTS.orange;
  return (
    <div className="relative">
      <div className={clsx('absolute -left-3 top-0 bottom-0 w-[2px] rounded-full', active ? a.bar : 'bg-[var(--color-border)]')} />
      <div className={clsx('rounded-xl border p-5', active ? a.box : 'bg-[var(--color-surface)] border-[var(--color-border)]')}>
        <div className="flex items-center gap-2.5 mb-2 font-bold uppercase tracking-wider text-[11px]">
          <span className={clsx('p-1.5 rounded-md bg-white', active ? a.text : 'text-[var(--color-ink-soft)]')}>
            {icon && React.cloneElement(icon, { className: clsx('w-4 h-4', active ? a.text : 'text-[var(--color-ink-soft)]') })}
          </span>
          <span className={active ? a.text : 'text-[var(--color-ink-soft)]'}>{title}</span>
        </div>
        {children}
      </div>
    </div>
  );
}

function ScoreRow({ label, value }) {
  return (
    <div className="flex items-center justify-between border-b border-[var(--color-border)] pb-3">
      <span className="font-semibold text-[var(--color-ink-soft)] uppercase tracking-wider text-xs">{label}</span>
      <span className="text-xl font-bold text-[var(--color-ink)]">
        {value || 0}<span className="text-xs text-[var(--color-ink-soft)] font-normal">/100</span>
      </span>
    </div>
  );
}

function Pending({ text }) {
  return <p className="text-center text-[var(--color-ink-soft)] text-[13px] py-4 italic leading-relaxed">{text}</p>;
}

function ListDisplay({ title, items, tone = 'neutral', numbered = false }) {
  if (!items || items.length === 0) return null;

  const dot = tone === 'warn' ? 'bg-orange-500' : tone === 'good' ? 'bg-green-500' : 'bg-zinc-400';

  return (
    <div>
      <h4 className="font-bold text-[var(--color-ink-soft)] mb-1.5 text-xs uppercase tracking-widest">{title}</h4>
      {numbered ? (
        <ol className="space-y-1.5 list-decimal list-outside pl-4 text-[13px] leading-snug text-[var(--color-ink)]">
          {items.map((item, i) => <li key={i} className="pl-1">{item}</li>)}
        </ol>
      ) : (
        <ul className="space-y-1.5">
          {items.map((item, i) => (
            <li key={i} className="flex items-start gap-2 text-[13px] leading-snug text-[var(--color-ink)]">
              <span className={clsx('mt-1.5 w-1.5 h-1.5 rounded-full shrink-0', dot)} />
              <span>{item}</span>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}
