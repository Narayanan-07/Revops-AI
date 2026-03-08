import React from 'react';
import { X, CheckCircle2, TrendingUp, AlertTriangle, FileText, Bot } from 'lucide-react';
import clsx from 'clsx';

export default function LeadDrawer({ isOpen, onClose, selectedItem }) {
  if (!isOpen || !selectedItem) return null;

  const { leads, lead_context } = selectedItem;
  
  // Extract contexts
  const agent1 = lead_context?.find(c => c.stage === 'icp_alignment' || c.updated_by_agent === 'icp_alignment_agent');
  const agent2 = lead_context?.find(c => c.stage === 'lead_scoring' || c.updated_by_agent === 'lead_scoring_agent');
  const agent3 = lead_context?.find(c => c.stage === 'discovery_intelligence' || c.updated_by_agent === 'discovery_intelligence_agent');

  return (
    <>
      {/* Backdrop */}
      <div 
        className="fixed inset-0 bg-black/50 backdrop-blur-sm z-40 transition-opacity duration-300"
        onClick={onClose}
      />

      {/* Drawer */}
      <div 
        className={clsx(
          "fixed top-0 right-0 h-full w-[500px] max-w-full bg-[var(--color-board-bg)] border-l border-[var(--color-border)] shadow-2xl z-50",
          "transform transition-transform duration-500 ease-in-out flex flex-col",
          isOpen ? "translate-x-0" : "translate-x-full"
        )}
      >
        {/* Header */}
        <div className="flex items-center justify-between p-6 border-b border-[var(--color-border)] sticky top-0 bg-[var(--color-board-bg)]/95 backdrop-blur-md z-10">
          <div>
            <h2 className="text-xl font-bold tracking-tight text-white mb-1">
              {leads?.company_name || 'Unknown Company'}
            </h2>
            <a 
              href={`https://${leads?.domain}`} 
              target="_blank" 
              rel="noreferrer"
              className="text-sm text-indigo-400 hover:text-indigo-300 transition-colors flex items-center gap-1.5"
            >
              {leads?.domain}
            </a>
          </div>
          <button 
            onClick={onClose}
            className="p-2 bg-white/5 hover:bg-white/10 rounded-full transition-colors text-gray-400 hover:text-white"
          >
            <X className="w-5 h-5" />
          </button>
        </div>

        {/* Scrollable Content */}
        <div className="flex-1 overflow-y-auto custom-scrollbar p-6 space-y-8">

          {/* Agent 1 Block */}
          <SectionBlock 
            title="ICP Alignment Agent" 
            icon={<CheckCircle2 className="w-4 h-4" />}
            color="text-purple-400"
            bgColor="bg-purple-900/20 border-purple-500/20"
            agent={agent1}
          >
            {agent1 ? (
              <div className="space-y-4 text-sm mt-4 text-gray-300">
                <div className="flex items-center justify-between border-b border-white/5 pb-3">
                  <span className="font-semibold text-gray-400 uppercase tracking-wider text-xs">ICP Score</span>
                  <span className="text-xl font-bold text-white">{agent1.icp_alignment_score || 0}<span className="text-xs text-gray-500 font-normal">/100</span></span>
                </div>
                <div>
                  <h4 className="font-bold text-white mb-1">Buying Intent</h4>
                  <p className="italic bg-black/20 p-3 rounded-lg border border-white/5">{agent1.buying_intent_summary || 'N/A'}</p>
                </div>
                <ListDisplay title="Pain Points" items={agent1.pain_point_matches} />
                <ListDisplay title="Firmographic" items={agent1.firmographic_signals} />
                <ListDisplay title="Technographic" items={agent1.technographic_signals} />
                <ListDisplay title="Chronographic" items={agent1.chronographic_signals} />
                <ListDisplay title="Gaps" items={agent1.icp_gaps} isError />
              </div>
            ) : (
              <p className="text-center text-gray-500 text-sm py-4 italic">Processing...</p>
            )}
          </SectionBlock>

          {/* Agent 2 Block */}
          <SectionBlock 
            title="Lead Scoring Agent" 
            icon={<TrendingUp className="w-4 h-4" />}
            color={agent2?.lead_label === 'NOT_A_LEAD' ? 'text-red-400' : 'text-blue-400'}
            bgColor={agent2?.lead_label === 'NOT_A_LEAD' ? 'bg-red-900/20 border-red-500/20' : 'bg-blue-900/20 border-blue-500/20'}
            agent={agent2}
          >
            {agent2 ? (
              <div className="space-y-4 text-sm mt-4 text-gray-300">
                <div className="flex items-center justify-between border-b border-white/5 pb-3">
                  <span className="font-semibold text-gray-400 uppercase tracking-wider text-xs">Fit Score</span>
                  <span className="text-xl font-bold text-white tracking-tight">
                    {agent2.fit_score || 0}<span className="text-xs text-gray-500 font-normal">/100</span>
                  </span>
                </div>
                <div className="flex gap-2 mb-2">
                  <span className={clsx(
                    "px-2.5 py-1 rounded-md text-xs font-bold uppercase tracking-wider border",
                    agent2.lead_label === 'NOT_A_LEAD' ? "bg-red-500/10 border-red-500/30 text-red-500" : "bg-emerald-500/10 border-emerald-500/30 text-emerald-400"
                  )}>
                    {agent2.lead_label === 'NOT_A_LEAD' ? '🔴 NOT A LEAD' : '🟢 GOOD LEAD'}
                  </span>
                  <span className="px-2.5 py-1 rounded-md bg-white/5 border border-white/10 text-xs font-bold uppercase tracking-wider text-gray-300 flex items-center gap-1.5">
                    Signal: <span className="text-white">{agent2.buying_signal_strength || 'medium'}</span>
                  </span>
                </div>
                <div>
                  <h4 className="font-bold text-white mb-2 text-xs uppercase tracking-widest text-gray-500">Reasoning</h4>
                  <p className="leading-relaxed whitespace-pre-line text-xs">{agent2.scoring_reasoning || 'N/A'}</p>
                </div>
                <ListDisplay title="Risk Factors" items={agent2.risk_factors} isWarning />
                <ListDisplay title="Similar Won Deals" items={agent2.similar_won_deals} />
              </div>
            ) : (
              <p className="text-center text-gray-500 text-sm py-4 italic">Pending scoring...</p>
            )}
          </SectionBlock>

          {/* Agent 3 Block */}
          <SectionBlock 
            title="Discovery Intelligence Agent" 
            icon={<FileText className="w-4 h-4" />}
            color="text-amber-400"
            bgColor="bg-amber-900/20 border-amber-500/20"
            agent={agent3}
          >
            {agent3 ? (
              <div className="space-y-4 text-sm mt-4 text-gray-300">
                <ListDisplay title="Exact Needs" items={agent3.exact_customer_needs} />
                <ListDisplay title="Feature Recommendations" items={agent3.feature_recommendations} />
                <ListDisplay title="Demo Focus" items={agent3.demo_focus_areas} numbered highlight />
                {agent3.confirmed_buying_intent && (
                  <div className="mb-4">
                    <h4 className="font-bold text-white mb-2 text-xs uppercase tracking-widest text-gray-500">Confirmed Intent</h4>
                    <p className="italic bg-black/20 p-3 rounded-lg border border-white/5">{agent3.confirmed_buying_intent}</p>
                  </div>
                )}
                
                  {agent3.recommended_pricing_tier && (
                    <div className="flex items-center justify-between p-3 rounded-lg bg-emerald-500/10 border border-emerald-500/20 mb-4">
                      <span className="font-bold text-emerald-500 text-xs uppercase tracking-wider">Recommended Tier</span>
                      <span className="font-bold text-white bg-emerald-500/20 px-2 py-1 rounded shadow-sm">{agent3.recommended_pricing_tier}</span>
                    </div>
                  )}
                
                <div>
                  <h4 className="font-bold text-white mb-2 text-xs uppercase tracking-widest text-gray-500 flex items-center gap-2">
                    <AlertTriangle className="w-3.5 h-3.5 text-amber-500" />
                    Presales Handoff Note
                  </h4>
                  <div className="bg-black/30 border border-amber-500/20 p-4 rounded-xl text-amber-100/80 leading-relaxed text-sm whitespace-pre-line shadow-[inset_0_2px_10px_rgba(0,0,0,0.2)]">
                    {agent3.presales_handoff_note || 'N/A'}
                  </div>
                </div>
              </div>
            ) : (
              <p className="text-center text-gray-500 text-[13px] py-4 italic leading-relaxed">
                Appears after transcript processing.
                <br/>Requires transcript via webapp/database.
              </p>
            )}
          </SectionBlock>
        </div>
      </div>
    </>
  );
}

function SectionBlock({ title, icon, color, bgColor, agent, children }) {
  return (
    <div className="relative">
      <div className={clsx(
        "absolute -left-3 top-0 bottom-0 w-[2px] rounded-full opacity-50", 
        agent ? color.replace('text-', 'bg-') : 'bg-gray-800'
      )} />
      <div className={clsx("rounded-xl border p-5 transition-all", agent ? bgColor : "bg-white/5 border-white/5")}>
        <div className="flex items-center gap-2.5 mb-2 font-bold uppercase tracking-wider text-[11px]">
          <span className={clsx("p-1.5 rounded-md", agent ? "bg-black/20" : "bg-white/5 text-gray-500")}>
            {icon && React.cloneElement(icon, { className: clsx('w-4 h-4', agent ? color : 'text-gray-500') })}
          </span>
          <span className={agent ? color : 'text-gray-500'}>{title}</span>
        </div>
        {children}
      </div>
    </div>
  );
}

function ListDisplay({ title, items, isWarning = false, isError = false, highlight = false, numbered = false }) {
  if (!items || items.length === 0) return null;
  
  return (
    <div className="mb-4">
      <h4 className="font-bold text-white mb-1.5 text-xs uppercase tracking-widest text-gray-500">{title}</h4>
      {numbered ? (
        <ol className="space-y-1.5 list-decimal list-outside pl-4 text-[13px] leading-snug">
          {items.map((item, i) => (
            <li key={i} className={clsx(highlight ? "text-indigo-200" : "text-gray-300", "pl-1")}>
              {item}
            </li>
          ))}
        </ol>
      ) : (
        <ul className="space-y-1.5">
          {items.map((item, i) => (
            <li key={i} className="flex items-start gap-2 text-[13px] leading-snug">
               <span className={clsx(
                 "mt-1 w-1.5 h-1.5 rounded-full shrink-0",
                 isError ? "bg-red-500" : isWarning ? "bg-yellow-500" : highlight ? "bg-indigo-400" : "bg-gray-600"
               )} />
               <span className={clsx(
                 isError ? "text-red-200" : isWarning ? "text-yellow-200" : highlight ? "text-indigo-100" : "text-gray-300"
               )}>
                 {item}
               </span>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}
