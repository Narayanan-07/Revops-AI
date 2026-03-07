import { useState, useEffect, useCallback } from 'react';
import { supabase } from '../supabaseClient';

export function useLeads() {
  const [leads, setLeads] = useState({
    icp_alignment: [],
    lead_scoring: [],
    awaiting_transcript: [],
    discovery_intelligence: [],
    ready_for_presales: [],
    not_a_lead: []
  });

  const [loading, setLoading] = useState(true);

  const fetchAll = useCallback(async () => {
    try {
      const { data, error } = await supabase
        .from('pipeline')
        .select('*, leads(*), lead_context(*)');
        
      if (error) {
        console.error('Error fetching leads:', error);
        return;
      }

      const grouped = {
        icp_alignment: [], 
        lead_scoring: [],
        awaiting_transcript: [], 
        discovery_intelligence: [],
        ready_for_presales: [], 
        not_a_lead: []
      };

      data?.forEach(item => {
        // Map not_a_lead strictly if lead_context decides it, or if it's the pipeline stage
        // Wait, TASK.md says: NOT_A_LEAD cards appear in Lead Scoring column with red styling.
        // Wait, "Pipeline Stages — Exact Strings" has "not_a_lead" as a pipeline stage. 
        // "not_a_lead -> Disqualified by Agent 2". But the task says "NOT_A_LEAD cards appear in Lead Scoring column with red styling." Let's keep them in lead_scoring if requested, or map properly.
        // I will group by current_stage but if current_stage is not_a_lead, I'll put it in lead_scoring, or I can just keep it in grouped.not_a_lead and render grouped.not_a_lead inside the lead_scoring column.
        
        if (item.current_stage) {
          if (grouped[item.current_stage]) {
            grouped[item.current_stage].push(item);
          }
        }
      });

      // Sort by latest moved_at for each column
      Object.keys(grouped).forEach(key => {
        grouped[key].sort((a, b) => new Date(b.moved_at) - new Date(a.moved_at));
      });

      setLeads(grouped);
    } catch (err) {
      console.error('Failed to fetch leads:', err);
    } finally {
      setLoading(false);
    }
  }, []);

  useEffect(() => {
    fetchAll();

    const channel = supabase.channel('live')
      .on('postgres_changes', { event: '*', schema: 'public', table: 'pipeline' }, fetchAll)
      .on('postgres_changes', { event: '*', schema: 'public', table: 'lead_context' }, fetchAll)
      .subscribe();

    return () => {
      supabase.removeChannel(channel);
    };
  }, [fetchAll]);

  return { leads, loading, refetch: fetchAll };
}
