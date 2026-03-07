import React from 'react';
import clsx from 'clsx';
import { formatDistanceToNow } from 'date-fns';
import { Bot, MapPin, Building2, Flame } from 'lucide-react';

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
          <div className="flex items-center gap-1.5 text-xs text-gray-400 mt-1">
            <Building2 className="w-3.5 h-3.5" />
            <span className="truncate max-w-[120px]">{leadData?.domain || 'unknown.com'}</span>
          </div>
        </div>
        
        {isNotALead && (
          <span className="inline-flex items-center rounded-full bg-red-500/20 px-2 py-0.5 text-xs font-semibold text-red-400 shadow-[0_0_10px_rgba(239,68,68,0.2)]">
            🔴 NOT
          </span>
        )}
      </div>

      <div className="w-full h-px bg-white/5 my-3 relative z-10" />

      {/* Scores & Signals */}
      <div className="grid grid-cols-2 gap-3 mb-3 relative z-10">
        <div>
          <p className="text-[10px] text-gray-500 font-bold uppercase tracking-wider mb-1">ICP Score</p>
          <p className="text-sm font-medium text-white flex items-baseline gap-1">
            {icpScore} <span className="text-[10px] text-gray-500">/100</span>
          </p>
        </div>
        <div>
          <p className="text-[10px] text-gray-500 font-bold uppercase tracking-wider mb-1">Fit Score</p>
          <p className={clsx(
            "text-sm font-medium flex items-baseline gap-1",
            fitScore >= 60 ? "text-emerald-400" : (fitScore > 0 ? "text-red-400" : "text-gray-400")
          )}>
            {fitScore || '-'} <span className="text-[10px] text-gray-500">/100</span>
          </p>
        </div>
      </div>

      {scoringContext && !isNotALead && (
        <div className="mb-3 relative z-10">
          <span className={clsx(
            "inline-flex items-center gap-1 px-2 py-1 rounded-md text-[10px] font-bold uppercase tracking-wider border",
            getSignalColor(signalStrength)
          )}>
            <Flame className="w-3 h-3" />
            Signal: {signalStrength}
          </span>
        </div>
      )}

      {/* Summary */}
      <div className="mb-4 relative z-10 flex-1">
        <p className={clsx(
          "text-xs leading-relaxed italic line-clamp-2",
          isNotALead ? "text-red-400/80" : "text-gray-400"
        )}>
          "{intentSummary.length > 80 ? intentSummary.substring(0, 80) + '...' : intentSummary}"
        </p>
      </div>

      {/* Footer */}
      <div className="flex items-center justify-between text-[10px] text-gray-500 pt-3 border-t border-white/5 relative z-10">
        <div className="flex items-center gap-1.5 font-medium">
          <Bot className="w-3.5 h-3.5" />
          {item.moved_by ? item.moved_by.replace(/_/g, ' ').toUpperCase() : 'SYSTEM'}
        </div>
        <div className="font-mono">{formatTime(item.moved_at)}</div>
      </div>
    </div>
  );
}
