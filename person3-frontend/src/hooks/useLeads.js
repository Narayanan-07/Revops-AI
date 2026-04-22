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
      // lead_context is FK'd to leads, not pipeline — must be nested under leads
      const { data, error } = await supabase
        .from('pipeline')
        .select('*, leads(*, lead_context(*))');

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

      const STAGE_ORDER = {
        'icp_alignment': 0,
        'lead_scoring': 1,
        'awaiting_transcript': 2,
        'discovery_intelligence': 3,
        'ready_for_presales': 4,
        'not_a_lead': -1
      };

      data?.forEach(item => {
        // Flatten lead_context from nested leads onto the item directly
        if (item.leads && item.leads.lead_context) {
          item.lead_context = item.leads.lead_context;
        }

        const stage = item.current_stage;
        const order = STAGE_ORDER[stage] ?? 0;

        if (order === -1) {
          // NOT_A_LEAD: still show in ICP + Lead Scoring columns for visibility
          grouped.icp_alignment.push(item);
          grouped.lead_scoring.push(item);
          grouped.not_a_lead.push(item);
        } else {
          // Show card in every column the lead has reached
          if (order >= 0) grouped.icp_alignment.push(item);
          if (order >= 1) grouped.lead_scoring.push(item);
          if (order === 2) grouped.awaiting_transcript.push(item); // needs transcript
          if (order >= 3) grouped.discovery_intelligence.push(item);
          if (order >= 4) grouped.ready_for_presales.push(item);
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
