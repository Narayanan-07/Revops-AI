import React, { useState, useRef } from 'react';
import { useLeads } from '../hooks/useLeads';
import { Building2, Bot, CheckCircle2, UploadCloud, FileText, X } from 'lucide-react';
import clsx from 'clsx';

const ACCEPTED = '.txt,.vtt,.srt,.md,.pdf,.docx';

export default function TranscriptUpload() {
  const { leads, loading } = useLeads();
  const [transcripts, setTranscripts] = useState({});
  const [files, setFiles] = useState({});
  const [submitting, setSubmitting] = useState({});
  const [success, setSuccess] = useState({});

  const awaitingLeads = leads.awaiting_transcript || [];

  const handleTextChange = (leadId, text) =>
    setTranscripts((prev) => ({ ...prev, [leadId]: text }));

  const handleFile = (leadId, file) =>
    setFiles((prev) => ({ ...prev, [leadId]: file || null }));

  const handleSubmit = async (leadId) => {
    const text = transcripts[leadId];
    const file = files[leadId];
    if (!text?.trim() && !file) return;

    setSubmitting((prev) => ({ ...prev, [leadId]: true }));

    try {
      const body = new FormData();
      body.append('lead_id', leadId);
      if (text?.trim()) body.append('text', text);
      if (file) body.append('file', file);

      const res = await fetch(`${import.meta.env.VITE_BACKEND_URL}/submit/transcript`, {
        method: 'POST',
        body,
      });
      const data = await res.json();
      if (!res.ok || data.status === 'error') throw new Error(data.message || 'Upload failed');

      setSuccess((prev) => ({ ...prev, [leadId]: true }));
    } catch (err) {
      console.error('Failed to submit transcript:', err);
      alert('Failed to submit transcript. Check the console.');
    } finally {
      setSubmitting((prev) => ({ ...prev, [leadId]: false }));
    }
  };

  if (loading) {
    return (
      <div className="flex items-center justify-center p-20 text-[var(--color-ink-soft)] w-full">
        Fetching leads awaiting transcripts…
      </div>
    );
  }

  return (
    <div className="w-full max-w-5xl mx-auto py-8 px-6 pb-24 overflow-y-auto custom-scrollbar h-full">
      <div className="mb-8">
        <h2 className="text-2xl font-bold tracking-tight text-[var(--color-ink)] flex items-center gap-3">
          Upload Sales Transcripts
          <span className="px-2.5 py-1 rounded-md text-xs font-bold uppercase tracking-wider bg-orange-100 text-orange-700 border border-orange-200">
            {awaitingLeads.length} Pending
          </span>
        </h2>
        <p className="text-[var(--color-ink-soft)] mt-2 text-sm leading-relaxed">
          Paste the call transcript or upload a file (.txt, .vtt, .srt, .pdf, .docx) for each qualified lead.
          The Discovery Intelligence agent then extracts customer needs, recommends features, and writes the presales handoff note.
        </p>
      </div>

      {awaitingLeads.length === 0 ? (
        <div className="flex flex-col items-center justify-center p-16 border border-dashed border-[var(--color-border)] rounded-2xl bg-[var(--color-surface)] mt-8">
          <CheckCircle2 className="w-12 h-12 text-green-500 mb-4" />
          <h3 className="text-lg font-bold text-[var(--color-ink)]">No transcripts pending</h3>
          <p className="text-sm text-[var(--color-ink-soft)] mt-1">All qualified leads have been processed.</p>
        </div>
      ) : (
        <div className="space-y-6">
          {awaitingLeads.map((item) => {
            const leadData = item.leads;
            const scoringContext = item.lead_context?.find((c) => c.stage === 'lead_scoring');
            const alignmentContext = item.lead_context?.find((c) => c.stage === 'icp_alignment');

            const fitScore = scoringContext?.fit_score || 0;
            const intentSummary = alignmentContext?.buying_intent_summary || 'No intent captured yet.';
            const leadId = item.lead_id;

            const isSuccess = success[leadId];
            const isSubmitting = submitting[leadId];
            const currentText = transcripts[leadId] || '';
            const currentFile = files[leadId];

            return (
              <div key={leadId} className="bg-[var(--color-surface)] border border-[var(--color-border)] rounded-xl overflow-hidden shadow-sm transition-all hover:border-orange-300">

                {/* Header */}
                <div className="bg-[var(--color-surface-2)] px-6 py-4 border-b border-[var(--color-border)] flex items-start justify-between">
                  <div>
                    <h3 className="text-xl font-bold text-[var(--color-ink)] flex items-center gap-2">
                      {leadData?.company_name}
                      <a href={`https://${leadData?.domain}`} target="_blank" rel="noreferrer" className="text-xs text-orange-600 hover:text-orange-700 font-normal flex items-center gap-1">
                        <Building2 className="w-3 h-3" /> {leadData?.domain}
                      </a>
                    </h3>
                    <p className="text-sm text-[var(--color-ink-soft)] italic mt-2 line-clamp-2 max-w-2xl border-l-2 border-orange-400 pl-3 py-0.5">
                      "{intentSummary}"
                    </p>
                  </div>
                  <div className="text-right shrink-0">
                    <p className="text-[10px] text-[var(--color-ink-soft)] font-bold uppercase tracking-wider">Fit Score</p>
                    <p className={clsx('text-lg font-bold tracking-tight', fitScore >= 60 ? 'text-green-600' : 'text-orange-500')}>
                      {fitScore}/100
                    </p>
                  </div>
                </div>

                {/* Body */}
                <div className="p-6">
                  {isSuccess ? (
                    <div className="flex items-center gap-3 p-4 bg-green-50 border border-green-200 rounded-lg text-green-700">
                      <Bot className="w-5 h-5" />
                      <div>
                        <p className="font-bold text-sm">Transcript submitted successfully.</p>
                        <p className="text-xs text-green-600 mt-0.5">Discovery Intelligence is now analyzing the call. This lead will leave the queue shortly.</p>
                      </div>
                    </div>
                  ) : (
                    <div className="space-y-4">
                      <FileDrop
                        leadId={leadId}
                        file={currentFile}
                        onFile={(f) => handleFile(leadId, f)}
                        disabled={isSubmitting}
                      />

                      <div className="flex items-center gap-3 text-[11px] uppercase tracking-widest text-[var(--color-ink-soft)] font-bold">
                        <span className="h-px flex-1 bg-[var(--color-border)]" /> or paste <span className="h-px flex-1 bg-[var(--color-border)]" />
                      </div>

                      <textarea
                        value={currentText}
                        onChange={(e) => handleTextChange(leadId, e.target.value)}
                        placeholder="[00:00:00] Rep: Hey, thanks for joining…"
                        className="w-full h-40 bg-white border border-[var(--color-border)] rounded-lg p-4 text-sm text-[var(--color-ink)] font-mono placeholder:text-stone-400 focus:outline-none focus:border-orange-500 focus:ring-1 focus:ring-orange-300 transition-all custom-scrollbar resize-y"
                        disabled={isSubmitting}
                      />

                      <div className="flex justify-end">
                        <button
                          onClick={() => handleSubmit(leadId)}
                          disabled={isSubmitting || (!currentText.trim() && !currentFile)}
                          className={clsx(
                            'flex items-center gap-2 px-6 py-2.5 rounded-lg text-sm font-bold tracking-wide transition-all',
                            !currentText.trim() && !currentFile
                              ? 'bg-stone-200 text-stone-400 cursor-not-allowed'
                              : isSubmitting
                                ? 'bg-orange-300 text-white cursor-wait'
                                : 'bg-orange-500 hover:bg-orange-600 text-white shadow-md'
                          )}
                        >
                          {isSubmitting ? 'Submitting…' : 'Submit Transcript'}
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

function FileDrop({ leadId, file, onFile, disabled }) {
  const inputRef = useRef(null);

  if (file) {
    return (
      <div className="flex items-center justify-between gap-3 p-3 rounded-lg border border-green-200 bg-green-50">
        <div className="flex items-center gap-2 text-sm text-green-800 min-w-0">
          <FileText className="w-4 h-4 shrink-0" />
          <span className="truncate font-medium">{file.name}</span>
        </div>
        <button onClick={() => onFile(null)} disabled={disabled} className="p-1 rounded hover:bg-green-100 text-green-700 shrink-0">
          <X className="w-4 h-4" />
        </button>
      </div>
    );
  }

  return (
    <>
      <input
        ref={inputRef}
        id={`file-${leadId}`}
        type="file"
        accept={ACCEPTED}
        className="hidden"
        disabled={disabled}
        onChange={(e) => onFile(e.target.files?.[0] || null)}
      />
      <button
        type="button"
        onClick={() => inputRef.current?.click()}
        disabled={disabled}
        className="w-full flex flex-col items-center justify-center gap-2 py-6 rounded-lg border border-dashed border-[var(--color-border)] bg-[var(--color-surface-2)] hover:border-orange-400 hover:bg-orange-50 transition-colors text-[var(--color-ink-soft)]"
      >
        <UploadCloud className="w-6 h-6 text-orange-500" />
        <span className="text-sm font-semibold text-[var(--color-ink)]">Click to upload a transcript file</span>
        <span className="text-xs">.txt, .vtt, .srt, .pdf, .docx</span>
      </button>
    </>
  );
}
