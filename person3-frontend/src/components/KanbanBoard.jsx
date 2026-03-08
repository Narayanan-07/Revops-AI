import React, { useState } from 'react';
import LeadCard from './LeadCard';
import LeadDrawer from './LeadDrawer';

const COLUMNS = [
  { id: 'icp_alignment', title: 'ICP Alignment', color: 'border-purple-500/50', bgTitle: 'bg-purple-500/10 text-purple-400' },
  { id: 'lead_scoring', title: 'Lead Scoring', color: 'border-blue-500/50', bgTitle: 'bg-blue-500/10 text-blue-400' },
  { id: 'awaiting_transcript', title: 'Awaiting Transcript', color: 'border-yellow-500/50', bgTitle: 'bg-yellow-500/10 text-yellow-500' },
  { id: 'discovery_intelligence', title: 'Discovery Intelligence', color: 'border-amber-500/50', bgTitle: 'bg-amber-500/10 text-amber-500' },
  { id: 'ready_for_presales', title: 'Ready for Presales', color: 'border-emerald-500/50', bgTitle: 'bg-emerald-500/10 text-emerald-400' },
];

export default function KanbanBoard({ leads, loading }) {
  const [selectedLead, setSelectedLead] = useState(null);

  if (loading && !Object.values(leads).flat().length) {
    return (
      <div className="flex items-center justify-center p-20 text-gray-400 ml-4 animate-pulse">
        <div className="flex flex-col items-center gap-4">
          <div className="w-8 h-8 rounded-full border-2 border-indigo-500 border-t-transparent animate-spin" />
          <p>Connecting to RevOps AI Core...</p>
        </div>
      </div>
    );
  }

  return (
    <>
      <div className="w-full flex gap-6 overflow-x-auto pb-8 custom-scrollbar min-h-screen px-4">
        {COLUMNS.map((col) => {
          let columnItems = leads[col.id] || [];
          
          return (
            <div 
              key={col.id} 
              className="flex flex-col w-[320px] shrink-0 bg-[#0c0d11] rounded-2xl border border-white/5 shadow-xl relative overflow-hidden"
            >
              {/* Header */}
              <div className={`px-4 py-3 border-b border-white/5 flex items-center justify-between sticky top-0 bg-[#0c0d11]/80 backdrop-blur-md z-10 ${col.color} border-t-2`}>
                <h3 className={`font-black uppercase tracking-wider text-xs px-2.5 py-1 rounded-md ${col.bgTitle}`}>
                  {col.title}
                </h3>
                <span className="text-xs font-mono font-bold text-gray-500 bg-white/5 px-2 py-0.5 rounded-full">
                  {columnItems.length}
                </span>
              </div>
              
              {/* Cards Container */}
              <div className="flex-1 overflow-y-auto custom-scrollbar p-3 space-y-3 relative z-0 min-h-[150px]">
                {columnItems.length > 0 ? (
                  columnItems.map((item) => (
                    <LeadCard 
                      key={item.id} 
                      item={item} 
                      onClick={setSelectedLead}
                    />
                  ))
                ) : (
                  <div className="h-full flex items-center justify-center text-[12px] text-gray-500 uppercase font-medium tracking-wide border border-dashed border-white/5 rounded-xl mt-4 py-8 mb-4">
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
