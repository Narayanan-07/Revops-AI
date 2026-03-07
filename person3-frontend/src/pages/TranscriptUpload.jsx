import React, { useState } from 'react';
import { useLeads } from '../hooks/useLeads';
import { supabase } from '../supabaseClient';
import { Building2, Flame, Bot, CheckCircle2, AlertCircle } from 'lucide-react';
import clsx from 'clsx';

export default function TranscriptUpload() {
  const { leads, loading } = useLeads();
  const [transcripts, setTranscripts] = useState({});
  const [submitting, setSubmitting] = useState({});
  const [success, setSuccess] = useState({});

  // Only show leads in awaiting_transcript stage
  const awaitingLeads = leads.awaiting_transcript || [];

  const handleTextChange = (leadId, text) => {
    setTranscripts(prev => ({ ...prev, [leadId]: text }));
  };

  const handleSubmit = async (leadId) => {
    const text = transcripts[leadId];
    if (!text?.trim()) return;

    setSubmitting(prev => ({ ...prev, [leadId]: true }));
    
    try {
      const { error } = await supabase.from('transcripts').insert({
        lead_id: leadId,
        transcript_text: text
      });

      if (error) throw error;

      setSuccess(prev => ({ ...prev, [leadId]: true }));
      // Disable after successful submission
    } catch (err) {
      console.error('Failed to submit transcript:', err);
      alert('Failed to submit transcript. Check console.');
    } finally {
      setSubmitting(prev => ({ ...prev, [leadId]: false }));
    }
  };

  if (loading) {
    return (
      <div className="flex items-center justify-center p-20 text-gray-400 animate-pulse w-full">
        Fetching leads awaiting transcripts...
      </div>
    );
  }

  return (
    <div className="w-full max-w-5xl mx-auto py-8 px-6 pb-24 overflow-y-auto custom-scrollbar h-full">
      <div className="mb-8">
        <h2 className="text-2xl font-bold tracking-tight text-white flex items-center gap-3">
          Upload Sales Transcripts
          <span className="px-2.5 py-1 rounded-md text-xs font-bold uppercase tracking-wider bg-yellow-500/10 text-yellow-500 border border-yellow-500/20">
            {awaitingLeads.length} Pending
          </span>
        </h2>
        <p className="text-gray-400 mt-2 text-sm leading-relaxed">
          Paste the call transcripts for qualified leads below. 
          Agent 3 (Discovery Intelligence) will automatically analyze the call, extract exact customer needs, recommend features, and write the presales handoff note.
        </p>
      </div>

      {awaitingLeads.length === 0 ? (
        <div className="flex flex-col items-center justify-center p-16 border border-dashed border-white/10 rounded-2xl bg-white/5 mt-8">
          <CheckCircle2 className="w-12 h-12 text-emerald-500/50 mb-4" />
          <h3 className="text-lg font-bold text-gray-300">No transcripts pending</h3>
          <p className="text-sm text-gray-500 mt-1">All qualified leads have been processed.</p>
        </div>
      ) : (
        <div className="space-y-6">
          {awaitingLeads.map((item) => {
            const leadData = item.leads;
            const scoringContext = item.lead_context?.find(c => c.stage === 'lead_scoring');
            const alignmentContext = item.lead_context?.find(c => c.stage === 'icp_alignment');
            
            const fitScore = scoringContext?.fit_score || 0;
            const intentSummary = alignmentContext?.buying_intent_summary || 'No intent captured yet.';
            const leadId = item.lead_id;

            const isSuccess = success[leadId];
            const isSubmitting = submitting[leadId];
            const currentText = transcripts[leadId] || '';

            return (
              <div key={leadId} className="bg-[var(--color-card-bg)] border border-[var(--color-border)] rounded-xl overflow-hidden shadow-lg transition-all hover:border-indigo-500/50 relative group">
                
                {/* Header */}
                <div className="bg-[#121319] px-6 py-4 border-b border-white/5 flex items-start justify-between">
                  <div>
                    <h3 className="text-xl font-bold text-white flex items-center gap-2">
                      {leadData?.company_name}
                      <a href={`https://${leadData?.domain}`} target="_blank" rel="noreferrer" className="text-xs text-indigo-400 hover:text-indigo-300 font-normal flex items-center gap-1">
                        <Building2 className="w-3 h-3" /> {leadData?.domain}
                      </a>
                    </h3>
                    <p className="text-sm text-gray-400 italic mt-2 line-clamp-2 max-w-2xl border-l-2 border-indigo-500 pl-3 py-0.5">
                      "{intentSummary}"
                    </p>
                  </div>

                  <div className="flex flex-col items-end gap-2 shrink-0">
                    <div className="flex items-center gap-3">
                      <div className="text-right">
                        <p className="text-[10px] text-gray-500 font-bold uppercase tracking-wider">Fit Score</p>
                        <p className={clsx(
                          "text-lg font-medium tracking-tight",
                          fitScore >= 60 ? "text-emerald-400" : "text-yellow-400"
                        )}>
                          {fitScore}/100
                        </p>
                      </div>
                    </div>
                  </div>
                </div>

                {/* Body form */}
                <div className="p-6">
                  {isSuccess ? (
                    <div className="flex items-center gap-3 p-4 bg-emerald-500/10 border border-emerald-500/20 rounded-lg text-emerald-400">
                      <Bot className="w-5 h-5" />
                      <div>
                        <p className="font-bold text-sm">Transcript submitted successfully.</p>
                        <p className="text-xs text-emerald-500/70 mt-0.5">Agent 3 is now analyzing the call. This lead will disappear from this queue shortly.</p>
                      </div>
                    </div>
                  ) : (
                    <div className="space-y-4">
                      <label className="block text-sm font-medium text-gray-300">
                        Paste Call Transcript:
                      </label>
                      <textarea
                        value={currentText}
                        onChange={(e) => handleTextChange(leadId, e.target.value)}
                        placeholder="[00:00:00] Rep: Hey, thanks for joining..."
                        className="w-full h-48 bg-black/40 border border-white/10 rounded-lg p-4 text-sm text-gray-300 font-mono placeholder:text-gray-600 focus:outline-none focus:border-indigo-500 focus:ring-1 focus:ring-indigo-500 transition-all custom-scrollbar resize-y"
                        disabled={isSubmitting}
                      />
                      <div className="flex justify-end">
                        <button
                          onClick={() => handleSubmit(leadId)}
                          disabled={isSubmitting || !currentText.trim()}
                          className={clsx(
                            "flex items-center gap-2 px-6 py-2.5 rounded-lg text-sm font-bold tracking-wide transition-all",
                            !currentText.trim() 
                              ? "bg-white/5 text-gray-500 cursor-not-allowed" 
                              : isSubmitting 
                                ? "bg-indigo-500/50 text-white cursor-wait" 
                                : "bg-indigo-600 hover:bg-indigo-500 text-white shadow-lg hover:shadow-indigo-500/25"
                          )}
                        >
                          {isSubmitting ? 'Submitting...' : 'Submit Transcript'}
                        </button>
                      </div>
                    </div>
                  )}
                </div>

              </div>
            );
          })}
        </div>
      )}
    </div>
  );
}
