import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import {
  Building2, Mail, MessageSquare, ArrowRight, Loader2,
  CheckCircle2, AlertCircle, BarChart3, Sparkles, Target,
} from 'lucide-react';
import clsx from 'clsx';

export default function LeadForm() {
  const navigate = useNavigate();

  const [formData, setFormData] = useState({
    company_name: '',
    email: '',
    message: '',
  });

  const [errors, setErrors] = useState({});
  const [status, setStatus] = useState('idle'); // idle, submitting, success, error
  const [errorMessage, setErrorMessage] = useState('');

  const validate = () => {
    const newErrors = {};
    if (!formData.company_name.trim()) newErrors.company_name = 'Company name is required';
    if (!formData.email.trim()) {
      newErrors.email = 'Work email is required';
    } else if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(formData.email)) {
      newErrors.email = 'Please enter a valid work email (e.g. jane@acme.com)';
    }
    setErrors(newErrors);
    return Object.keys(newErrors).length === 0;
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!validate()) return;

    setStatus('submitting');
    setErrorMessage('');

    try {
      const response = await fetch(`${import.meta.env.VITE_BACKEND_URL}/submit/lead`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(formData),
      });
      const data = await response.json();

      if (!response.ok || data.status === 'error') {
        setStatus('error');
        setErrorMessage(data.detail || data.message || 'Something went wrong. Please try again.');
        return;
      }

      setStatus('success');
      setFormData({ company_name: '', email: '', message: '' });
    } catch (err) {
      setStatus('error');
      setErrorMessage('Unable to connect to the server. Please check if the backend is running.');
      console.error(err);
    }
  };

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prev) => ({ ...prev, [name]: value }));
    if (errors[name]) setErrors((prev) => ({ ...prev, [name]: '' }));
  };

  const inputClass = (field) =>
    clsx(
      'w-full bg-white border rounded-lg pl-11 pr-4 py-3 text-[15px] text-[var(--color-ink)] placeholder:text-stone-400 focus:outline-none focus:ring-2 transition-all',
      errors[field]
        ? 'border-orange-400 focus:ring-orange-300'
        : 'border-[var(--color-border)] focus:border-orange-500 focus:ring-orange-200'
    );

  return (
    <div className="flex-1 w-full h-full overflow-y-auto custom-scrollbar flex flex-col items-center py-12 px-6">

      {/* Form Container */}
      <div className="w-full max-w-2xl bg-[var(--color-surface)] border border-[var(--color-border)] rounded-2xl shadow-sm overflow-hidden">

        {/* Header Ribbon */}
        <div className="bg-orange-500 px-8 py-10 text-center relative overflow-hidden">
          <div className="relative z-10 flex flex-col items-center">
            <div className="w-12 h-12 bg-white rounded-xl shadow-lg flex items-center justify-center mb-4">
              <Sparkles className="w-7 h-7 text-orange-500" />
            </div>
            <h2 className="text-3xl font-black text-white tracking-tight">Request a Demo</h2>
            <p className="text-orange-50 mt-2 font-medium tracking-wide">
              Tell us who you are — our AI researches your company instantly.
            </p>
          </div>
        </div>

        <div className="p-8">
          {status === 'success' ? (
            <div className="flex flex-col items-center text-center py-8">
              <div className="w-16 h-16 bg-green-100 rounded-full flex items-center justify-center mb-6">
                <CheckCircle2 className="w-10 h-10 text-green-600" />
              </div>
              <h3 className="text-2xl font-bold text-[var(--color-ink)] mb-3">Lead submitted!</h3>
              <p className="text-[var(--color-ink-soft)] mb-8 max-w-md leading-relaxed">
                Our AI agents are enriching the company profile and running ICP analysis now.
                Track progress live on the Kanban board.
              </p>
              <button
                onClick={() => navigate('/kanban')}
                className="flex items-center gap-2 px-8 py-3 bg-orange-500 hover:bg-orange-600 text-white rounded-lg font-bold shadow-md hover:shadow-lg hover:-translate-y-0.5 transition-all"
              >
                View Kanban Board
                <ArrowRight className="w-4 h-4" />
              </button>
            </div>
          ) : (
            <form onSubmit={handleSubmit} className="space-y-6">

              {status === 'error' && (
                <div className="flex items-start gap-3 p-4 bg-orange-50 border border-orange-200 rounded-lg text-orange-700 mb-2">
                  <AlertCircle className="w-5 h-5 shrink-0 mt-0.5" />
                  <p className="font-medium text-sm leading-relaxed">{errorMessage}</p>
                </div>
              )}

              {/* Company Name */}
              <div>
                <label className="block text-sm font-semibold text-[var(--color-ink)] mb-2">
                  Company Name <span className="text-orange-500">*</span>
                </label>
                <div className="relative">
                  <div className="absolute inset-y-0 left-0 pl-3.5 flex items-center pointer-events-none">
                    <Building2 className="w-5 h-5 text-stone-400" />
                  </div>
                  <input
                    type="text"
                    name="company_name"
                    value={formData.company_name}
                    onChange={handleChange}
                    className={inputClass('company_name')}
                    placeholder="e.g. Acme Inc."
                  />
                </div>
                {errors.company_name && <p className="mt-1.5 text-xs font-medium text-orange-600">{errors.company_name}</p>}
              </div>

              {/* Work Email */}
              <div>
                <label className="block text-sm font-semibold text-[var(--color-ink)] mb-2">
                  Work Email <span className="text-orange-500">*</span>
                </label>
                <div className="relative">
                  <div className="absolute inset-y-0 left-0 pl-3.5 flex items-center pointer-events-none">
                    <Mail className="w-5 h-5 text-stone-400" />
                  </div>
                  <input
                    type="email"
                    name="email"
                    value={formData.email}
                    onChange={handleChange}
                    className={inputClass('email')}
                    placeholder="jane@acme.com"
                  />
                </div>
                {errors.email
                  ? <p className="mt-1.5 text-xs font-medium text-orange-600">{errors.email}</p>
                  : <p className="mt-1.5 text-xs text-[var(--color-ink-soft)]">We use the email domain to identify and research your company.</p>}
              </div>

              {/* Message (optional) */}
              <div>
                <label className="block text-sm font-semibold text-[var(--color-ink)] mb-2">
                  What are you looking for? <span className="text-stone-400 font-normal">(optional)</span>
                </label>
                <div className="relative">
                  <div className="absolute top-3 left-0 pl-3.5 flex items-start pointer-events-none">
                    <MessageSquare className="w-5 h-5 text-stone-400" />
                  </div>
                  <textarea
                    name="message"
                    value={formData.message}
                    onChange={handleChange}
                    rows={3}
                    className="w-full bg-white border border-[var(--color-border)] rounded-lg pl-11 pr-4 py-3 text-[15px] text-[var(--color-ink)] placeholder:text-stone-400 focus:outline-none focus:ring-2 focus:border-orange-500 focus:ring-orange-200 transition-all resize-y"
                    placeholder="Tell us about your use case, team size, or current tools…"
                  />
                </div>
              </div>

              {/* Submit Button */}
              <button
                type="submit"
                disabled={status === 'submitting'}
                className="w-full flex items-center justify-center gap-2 py-3.5 rounded-lg text-[15px] font-bold tracking-wide transition-all bg-orange-500 hover:bg-orange-600 text-white shadow-md hover:shadow-lg disabled:opacity-70 disabled:cursor-wait mt-2"
              >
                {status === 'submitting' ? (
                  <><Loader2 className="w-5 h-5 animate-spin" /> Submitting…</>
                ) : (
                  <>Request a demo <ArrowRight className="w-4 h-4" /></>
                )}
              </button>
            </form>
          )}
        </div>
      </div>

      {/* AI Process Timeline */}
      <div className="w-full max-w-3xl mt-12 grid grid-cols-4 gap-4 px-4">
        <Step icon={<CheckCircle2 className="w-5 h-5" />} step="Step 1" label="Lead submitted" />
        <Step icon={<Sparkles className="w-5 h-5" />} step="Step 2" label="AI enriches & analyzes" />
        <Step icon={<BarChart3 className="w-5 h-5" />} step="Step 3" label="Lead scored" />
        <Step icon={<Target className="w-5 h-5" />} step="Step 4" label="Ready for presales" green />
      </div>
    </div>
  );
}

function Step({ icon, step, label, green }) {
  return (
    <div className="flex flex-col items-center text-center group">
      <div className={clsx(
        'w-10 h-10 rounded-full border flex items-center justify-center mb-3 transition-colors',
        green
          ? 'bg-green-50 border-green-200 text-green-600'
          : 'bg-orange-50 border-orange-200 text-orange-500'
      )}>
        {icon}
      </div>
      <span className="text-[11px] font-bold uppercase tracking-wider text-[var(--color-ink-soft)]">{step}</span>
      <p className="text-xs text-[var(--color-ink)] mt-1 font-medium">{label}</p>
    </div>
  );
}
