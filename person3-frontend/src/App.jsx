import React from 'react';
import StatsBar from './components/StatsBar';
import KanbanBoard from './components/KanbanBoard';
import { useLeads } from './hooks/useLeads';
import { Target } from 'lucide-react';

function App() {
  const { leads, loading } = useLeads();

  return (
    <div className="min-h-screen bg-[var(--color-board-bg)] text-white overflow-hidden flex flex-col font-sans selection:bg-indigo-500/30">
      
      {/* Top Navigation / Brand */}
      <header className="h-14 border-b border-[var(--color-border)] bg-[var(--color-board-bg)]/80 backdrop-blur-md flex items-center px-6 sticky top-0 z-40">
        <div className="flex items-center gap-2">
          <div className="w-8 h-8 rounded-lg bg-indigo-500 flex items-center justify-center shadow-[0_0_15px_rgba(99,102,241,0.5)]">
            <Target className="w-5 h-5 text-white" />
          </div>
          <h1 className="font-bold text-lg tracking-tight bg-gradient-to-r from-white to-gray-400 bg-clip-text text-transparent">
            RevOps AI
          </h1>
          <span className="ml-2 px-2 py-0.5 rounded text-[10px] font-black tracking-widest bg-white/10 text-gray-400 uppercase">
            Jury Demo
          </span>
        </div>
      </header>

      {/* Main Content Area */}
      <main className="flex-1 w-full max-w-[1700px] mx-auto overflow-hidden flex flex-col pt-2 relative">
        <StatsBar leads={leads} />
        <div className="flex-1 w-full px-6">
          <KanbanBoard leads={leads} loading={loading} />
        </div>
      </main>

    </div>
  );
}

export default App;
