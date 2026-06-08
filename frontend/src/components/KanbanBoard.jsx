import React, { useState } from 'react';
import LeadCard from './LeadCard';
import LeadDrawer from './LeadDrawer';

// Palette is white / black / orange / green only. Stage accents:
//  - orange  → in-progress stages
//  - zinc    → awaiting (waiting on a human)
//  - green   → ready for presales (the goal)
const COLUMNS = [
  { id: 'icp_alignment', title: 'ICP Alignment', accent: 'border-t-orange-400', badge: 'bg-orange-100 text-orange-700' },
  { id: 'lead_scoring', title: 'Lead Scoring', accent: 'border-t-orange-500', badge: 'bg-orange-100 text-orange-700' },
  { id: 'awaiting_transcript', title: 'Awaiting Transcript', accent: 'border-t-zinc-400', badge: 'bg-zinc-200 text-zinc-700' },
  { id: 'discovery_intelligence', title: 'Discovery Intelligence', accent: 'border-t-orange-600', badge: 'bg-orange-100 text-orange-800' },
  { id: 'ready_for_presales', title: 'Ready for Presales', accent: 'border-t-green-500', badge: 'bg-green-100 text-green-700' },
];

export default function KanbanBoard({ leads, loading }) {
  const [selectedLead, setSelectedLead] = useState(null);

  if (loading && !Object.values(leads).flat().length) {
    return (
      <div className="flex items-center justify-center p-20 text-[var(--color-ink-soft)] ml-4">
        <div className="flex flex-col items-center gap-4">
          <div className="w-8 h-8 rounded-full border-2 border-orange-500 border-t-transparent animate-spin" />
          <p>Connecting to RevOps AI Core…</p>
        </div>
      </div>
    );
  }

  return (
    <>
      <div className="w-full flex gap-6 overflow-x-auto pb-8 custom-scrollbar min-h-screen px-4">
        {COLUMNS.map((col) => {
          const columnItems = leads[col.id] || [];

          return (
            <div
              key={col.id}
              className={`flex flex-col w-[320px] shrink-0 bg-[var(--color-surface-2)] rounded-2xl border border-[var(--color-border)] border-t-4 ${col.accent} shadow-sm relative overflow-hidden`}
            >
              {/* Header */}
              <div className="px-4 py-3 border-b border-[var(--color-border)] flex items-center justify-between sticky top-0 bg-[var(--color-surface-2)]/90 backdrop-blur-md z-10">
                <h3 className={`font-black uppercase tracking-wider text-xs px-2.5 py-1 rounded-md ${col.badge}`}>
                  {col.title}
                </h3>
                <span className="text-xs font-mono font-bold text-[var(--color-ink-soft)] bg-black/5 px-2 py-0.5 rounded-full">
                  {columnItems.length}
                </span>
              </div>

              {/* Cards */}
              <div className="flex-1 overflow-y-auto custom-scrollbar p-3 space-y-3 relative z-0 min-h-[150px]">
                {columnItems.length > 0 ? (
                  columnItems.map((item) => (
                    <LeadCard key={item.id} item={item} onClick={setSelectedLead} />
                  ))
                ) : (
                  <div className="h-full flex items-center justify-center text-[12px] text-[var(--color-ink-soft)] uppercase font-medium tracking-wide border border-dashed border-[var(--color-border)] rounded-xl mt-4 py-8 mb-4">
                    No leads in this stage
                  </div>
                )}
              </div>
            </div>
          );
        })}
      </div>

      <LeadDrawer
        isOpen={!!selectedLead}
        onClose={() => setSelectedLead(null)}
        selectedItem={selectedLead}
      />
    </>
  );
}
