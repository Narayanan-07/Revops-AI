import React from 'react';
import clsx from 'clsx';
import { formatDistanceToNow } from 'date-fns';
import { Bot, MapPin, Building2, Flame, AlertTriangle, FileText } from 'lucide-react';
import ScoreBar from './ScoreBar';

export default function LeadCard({ item, onClick }) {
  const { leads: leadData, lead_context: contexts, current_stage } = item;
  
  // Find relevant contexts
  const alignmentContext = contexts?.find(c => c.stage === 'icp_alignment');
  const scoringContext = contexts?.find(c => c.stage === 'lead_scoring');
  
  const icpScore = alignmentContext?.icp_alignment_score || 0;
  const fitScore = scoringContext?.fit_score || 0;
  const signalStrength = scoringContext?.buying_signal_strength || 'medium';
  
  // Is this actually marked as NOT_A_LEAD by Agent 2?
  const isNotALead = current_stage === 'not_a_lead' || scoringContext?.lead_label === 'NOT_A_LEAD';

  const intentSummary = alignmentContext?.buying_intent_summary || 'No intent captured yet.';
  const painPoints = alignmentContext?.pain_point_matches || [];
  const topPainPoints = painPoints.slice(0, 2); // Get top 2
  
  const getScoreColor = (score) => {
    if (score >= 71) return 'text-emerald-400';
    if (score >= 41) return 'text-yellow-400';
    return 'text-red-400';
  };
  
  // Helpers
  const formatTime = (iso) => {
    if (!iso) return 'Unknown time';
    try {
      return formatDistanceToNow(new Date(iso), { addSuffix: true });
    } catch {
      return 'Unknown time';
    }
  };

  const getSignalColor = (signal) => {
    if (signal === 'high') return 'bg-emerald-500/10 text-emerald-400 border-emerald-500/20';
    if (signal === 'medium') return 'bg-yellow-500/10 text-yellow-400 border-yellow-500/20';
    return 'bg-red-500/10 text-red-500 border-red-500/20';
  };

  return (
    <div 
      onClick={() => onClick(item)}
      className={clsx(
        "group relative flex flex-col p-4 rounded-xl cursor-pointer transition-all duration-300",
        "border backdrop-blur-sm shadow-sm hover:shadow-md",
        "hover:-translate-y-1",
        isNotALead 
          ? "bg-red-950/20 border-red-500/30 hover:bg-red-950/40 hover:border-red-500/50" 
          : "bg-[var(--color-card-bg)] border-[var(--color-border)] hover:border-indigo-500/50"
      )}
    >
      {/* Decorative Gradient Background on Hover */}
      {!isNotALead && (
        <div className="absolute inset-0 bg-gradient-to-br from-indigo-500/5 via-transparent to-transparent opacity-0 group-hover:opacity-100 transition-opacity rounded-xl pointer-events-none" />
      )}

      {/* Header */}
      <div className="flex justify-between items-start mb-2 relative z-10">
        <div>
          <h3 className={clsx(
            "font-semibold text-[15px] truncate",
            isNotALead ? "text-red-300" : "text-gray-100"
          )}>
            {leadData?.company_name || 'Unknown Company'}
          </h3>
          <div className="flex items-center gap-2 mt-1">
            <span className="inline-flex items-center gap-1 bg-white/5 px-2 py-0.5 rounded text-[10px] font-medium text-gray-300 border border-white/10 uppercase tracking-widest">
              Source: {leadData?.source ? leadData.source.replace(/_/g, ' ') : 'Web Form'}
            </span>
            <div className="flex items-center gap-1 text-xs text-gray-400">
              <Building2 className="w-3.5 h-3.5" />
              <span className="truncate max-w-[120px]">{leadData?.domain || 'unknown.com'}</span>
            </div>
          </div>
        </div>
        
        {isNotALead ? (
          <span className="inline-flex items-center rounded-sm bg-red-500/20 px-2 py-1 text-[10px] font-black tracking-widest uppercase text-red-500 border border-red-500/30">
            NOT A LEAD
          </span>
        ) : (
          <span className="inline-flex items-center rounded-sm bg-emerald-500/20 px-2 py-1 text-[10px] font-black tracking-widest uppercase text-emerald-400 border border-emerald-500/30 shadow-[0_0_10px_rgba(52,211,153,0.1)]">
            GOOD LEAD
          </span>
        )}
      </div>

      <div className="w-full h-px bg-white/5 my-3 relative z-10" />

      {/* Scores & Signals (Only if not a disqualified lead or if we want to show anyway) */}
      {!isNotALead && (
        <div className="space-y-2 mb-3 relative z-10 p-2 rounded-lg bg-black/20 border border-white/5">
          {(icpScore > 0 || fitScore > 0) ? (
            <>
              {icpScore > 0 && <ScoreBar label="ICP Score" score={icpScore} colorClass={getScoreColor(icpScore)} />}
              {fitScore > 0 && <ScoreBar label="Fit Score" score={fitScore} colorClass={getScoreColor(fitScore)} />}
            </>
          ) : (
            <div className="text-[10px] text-gray-500 italic text-center py-1">Scoring pending...</div>
          )}
        </div>
      )}

      {/* Signal Strength Badge */}
      {!isNotALead && scoringContext && signalStrength && (
        <div className="mb-3 relative z-10 flex">
          <span className={clsx(
            "inline-flex items-center gap-1.5 px-2.5 py-1 rounded-md text-[10px] font-bold uppercase tracking-wider border",
            getSignalColor(signalStrength)
          )}>
            <Flame className="w-3.5 h-3.5" />
            Signal: {signalStrength}
          </span>
        </div>
      )}

      {/* Content Section: Summary & Pain Points */}
      <div className="mb-4 relative z-10 flex-1">
        {isNotALead ? (
          <div className="text-xs leading-relaxed text-red-300/80 bg-red-950/30 p-2.5 rounded-lg border border-red-500/20">
            <div className="font-bold flex items-center gap-1.5 text-red-400 mb-1 tracking-wide uppercase text-[10px]">
              <AlertTriangle className="w-3 h-3" /> Agent Reasoning
            </div>
            {scoringContext?.scoring_reasoning ? 
              (scoringContext.scoring_reasoning.length > 150 
                ? scoringContext.scoring_reasoning.substring(0, 150) + '...' 
                : scoringContext.scoring_reasoning) 
              : 'Disqualified by agent logic.'}
          </div>
        ) : (
          <div className="space-y-3">
            <p className="text-[13px] leading-relaxed text-gray-300">
              "{intentSummary.length > 120 ? intentSummary.substring(0, 120) + '...' : intentSummary}"
            </p>
            {topPainPoints.length > 0 && (
              <div className="space-y-1">
                {topPainPoints.map((pp, idx) => (
                  <div key={idx} className="flex items-start gap-1.5 text-xs text-gray-400">
                    <AlertTriangle className="w-3 h-3 text-amber-500/70 shrink-0 mt-0.5" />
                    <span className="line-clamp-1">{pp}</span>
                  </div>
                ))}
              </div>
            )}
          </div>
        )}
      </div>

      {/* Footer */}
      <div className="flex items-center justify-between text-[10px] text-gray-500 pt-3 border-t border-white/5 relative z-10">
        
        <div className="flex items-center gap-2">
          {/* Status Badge */}
          {!isNotALead && (
             <span className={clsx(
               "px-2 py-0.5 rounded-full font-bold uppercase tracking-widest text-[9px]",
               current_stage === 'icp_alignment' ? 'bg-purple-500/10 text-purple-400 border border-purple-500/20' :
               current_stage === 'lead_scoring' ? 'bg-blue-500/10 text-blue-400 border border-blue-500/20' :
               current_stage === 'awaiting_transcript' ? 'bg-yellow-500/10 text-yellow-500 border border-yellow-500/20' :
               current_stage === 'discovery_intelligence' ? 'bg-amber-500/10 text-amber-500 border border-amber-500/20' :
               current_stage === 'ready_for_presales' ? 'bg-emerald-500/10 text-emerald-400 border border-emerald-500/20' :
               'bg-gray-800 text-gray-400'
             )}>
               {current_stage.replace(/_/g, ' ')}
             </span>
          )}
        </div>

        <div className="flex items-center gap-2 flex-col items-end">
          <div className="flex items-center gap-1.5 font-medium">
            <Bot className="w-3 h-3" />
            {item.moved_by ? item.moved_by.replace(/_/g, ' ').toUpperCase() : 'SYSTEM'}
          </div>
          <div className="font-mono opacity-60">{formatTime(item.moved_at)}</div>
        </div>
      </div>
    </div>
  );
}
