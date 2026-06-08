import React from 'react';
import clsx from 'clsx';
import { formatDistanceToNow } from 'date-fns';
import { Bot, Building2, Flame, AlertTriangle } from 'lucide-react';
import ScoreBar from './ScoreBar';

export default function LeadCard({ item, onClick }) {
  const { leads: leadData, lead_context: contexts, current_stage } = item;

  const alignmentContext = contexts?.find((c) => c.stage === 'icp_alignment');
  const scoringContext = contexts?.find((c) => c.stage === 'lead_scoring');

  const icpScore = alignmentContext?.icp_alignment_score || 0;
  const fitScore = scoringContext?.fit_score || 0;
  const signalStrength = scoringContext?.buying_signal_strength || 'medium';

  const isNotALead = current_stage === 'not_a_lead' || scoringContext?.lead_label === 'NOT_A_LEAD';

  const intentSummary = alignmentContext?.buying_intent_summary || 'No intent captured yet.';
  const topPainPoints = (alignmentContext?.pain_point_matches || []).slice(0, 2);

  // Palette: green (strong) → orange (mid/weak). No red.
  const getScoreColor = (score) => (score >= 60 ? 'text-green-600' : 'text-orange-500');

  const getSignalColor = (signal) => {
    if (signal === 'high') return 'bg-green-100 text-green-700 border-green-200';
    if (signal === 'medium') return 'bg-orange-100 text-orange-700 border-orange-200';
    return 'bg-zinc-100 text-zinc-600 border-zinc-200';
  };

  const formatTime = (iso) => {
    if (!iso) return 'Unknown time';
    try { return formatDistanceToNow(new Date(iso), { addSuffix: true }); }
    catch { return 'Unknown time'; }
  };

  const stageBadge = (stage) =>
    stage === 'ready_for_presales'
      ? 'bg-green-100 text-green-700 border border-green-200'
      : stage === 'awaiting_transcript'
        ? 'bg-zinc-100 text-zinc-600 border border-zinc-200'
        : 'bg-orange-100 text-orange-700 border border-orange-200';

  return (
    <div
      onClick={() => onClick(item)}
      className={clsx(
        'group relative flex flex-col p-4 rounded-xl cursor-pointer transition-all duration-300 border shadow-sm hover:shadow-md hover:-translate-y-1',
        isNotALead
          ? 'bg-zinc-900 border-zinc-800 hover:border-zinc-700 text-zinc-100'
          : 'bg-[var(--color-surface)] border-[var(--color-border)] hover:border-orange-300'
      )}
    >
      {/* Header */}
      <div className="flex justify-between items-start mb-2">
        <div className="min-w-0">
          <h3 className={clsx('font-semibold text-[15px] truncate', isNotALead ? 'text-white' : 'text-[var(--color-ink)]')}>
            {leadData?.company_name || 'Unknown Company'}
          </h3>
          <div className="flex items-center gap-2 mt-1">
            <span className={clsx(
              'inline-flex items-center gap-1 px-2 py-0.5 rounded text-[10px] font-medium uppercase tracking-widest border',
              isNotALead ? 'bg-white/5 text-zinc-400 border-white/10' : 'bg-black/5 text-[var(--color-ink-soft)] border-[var(--color-border)]'
            )}>
              {leadData?.source ? leadData.source.replace(/_/g, ' ') : 'Web Form'}
            </span>
            <div className={clsx('flex items-center gap-1 text-xs', isNotALead ? 'text-zinc-400' : 'text-[var(--color-ink-soft)]')}>
              <Building2 className="w-3.5 h-3.5" />
              <span className="truncate max-w-[110px]">{leadData?.domain || 'unknown.com'}</span>
            </div>
          </div>
        </div>

        {isNotALead ? (
          <span className="inline-flex items-center rounded bg-white/10 px-2 py-1 text-[10px] font-black tracking-widest uppercase text-zinc-200 border border-white/15">
            Not a Lead
          </span>
        ) : (
          <span className="inline-flex items-center rounded bg-green-100 px-2 py-1 text-[10px] font-black tracking-widest uppercase text-green-700 border border-green-200">
            Good Lead
          </span>
        )}
      </div>

      <div className={clsx('w-full h-px my-3', isNotALead ? 'bg-white/10' : 'bg-[var(--color-border)]')} />

      {/* Scores */}
      {!isNotALead && (
        <div className="space-y-2 mb-3 p-2 rounded-lg bg-[var(--color-surface-2)] border border-[var(--color-border)]">
          {icpScore > 0 || fitScore > 0 ? (
            <>
              {icpScore > 0 && <ScoreBar label="ICP Score" score={icpScore} colorClass={getScoreColor(icpScore)} />}
              {fitScore > 0 && <ScoreBar label="Fit Score" score={fitScore} colorClass={getScoreColor(fitScore)} />}
            </>
          ) : (
            <div className="text-[10px] text-[var(--color-ink-soft)] italic text-center py-1">Scoring pending…</div>
          )}
        </div>
      )}

      {/* Signal */}
      {!isNotALead && scoringContext && signalStrength && (
        <div className="mb-3 flex">
          <span className={clsx('inline-flex items-center gap-1.5 px-2.5 py-1 rounded-md text-[10px] font-bold uppercase tracking-wider border', getSignalColor(signalStrength))}>
            <Flame className="w-3.5 h-3.5" />
            Signal: {signalStrength}
          </span>
        </div>
      )}

      {/* Body */}
      <div className="mb-4 flex-1">
        {isNotALead ? (
          <div className="text-xs leading-relaxed text-zinc-300 bg-white/5 p-2.5 rounded-lg border border-white/10">
            <div className="font-bold flex items-center gap-1.5 text-zinc-200 mb-1 tracking-wide uppercase text-[10px]">
              <AlertTriangle className="w-3 h-3" /> Agent Reasoning
            </div>
            {scoringContext?.scoring_reasoning
              ? (scoringContext.scoring_reasoning.length > 150
                  ? scoringContext.scoring_reasoning.substring(0, 150) + '…'
                  : scoringContext.scoring_reasoning)
              : 'Disqualified by agent logic.'}
          </div>
        ) : (
          <div className="space-y-3">
            <p className="text-[13px] leading-relaxed text-[var(--color-ink-soft)]">
              "{intentSummary.length > 120 ? intentSummary.substring(0, 120) + '…' : intentSummary}"
            </p>
            {topPainPoints.length > 0 && (
              <div className="space-y-1">
                {topPainPoints.map((pp, idx) => (
                  <div key={idx} className="flex items-start gap-1.5 text-xs text-[var(--color-ink-soft)]">
                    <AlertTriangle className="w-3 h-3 text-orange-500 shrink-0 mt-0.5" />
                    <span className="line-clamp-1">{pp}</span>
                  </div>
                ))}
              </div>
            )}
          </div>
        )}
      </div>

      {/* Footer */}
      <div className={clsx('flex items-center justify-between text-[10px] pt-3 border-t', isNotALead ? 'border-white/10 text-zinc-400' : 'border-[var(--color-border)] text-[var(--color-ink-soft)]')}>
        <div className="flex items-center gap-2">
          {!isNotALead && (
            <span className={clsx('px-2 py-0.5 rounded-full font-bold uppercase tracking-widest text-[9px]', stageBadge(current_stage))}>
              {current_stage.replace(/_/g, ' ')}
            </span>
          )}
        </div>
        <div className="flex flex-col items-end gap-1">
          <div className="flex items-center gap-1.5 font-medium">
            <Bot className="w-3 h-3" />
            {item.moved_by ? item.moved_by.replace(/_/g, ' ').toUpperCase() : 'SYSTEM'}
          </div>
          <div className="font-mono opacity-70">{formatTime(item.moved_at)}</div>
        </div>
      </div>
    </div>
  );
}
