import React from 'react';
import StatsBar from '../components/StatsBar';
import KanbanBoard from '../components/KanbanBoard';
import { useLeads } from '../hooks/useLeads';

export default function KanbanPage() {
  const { leads, loading } = useLeads();

  return (
    <>
      <StatsBar leads={leads} />
      <div className="flex-1 w-full px-6">
        <KanbanBoard leads={leads} loading={loading} />
      </div>
    </>
  );
}
