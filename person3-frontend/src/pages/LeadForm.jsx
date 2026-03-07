import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { Building2, Globe, MessageSquare, ArrowRight, Loader2, CheckCircle2, AlertCircle, Bot, BarChart3, Target } from 'lucide-react';
import clsx from 'clsx';

export default function LeadForm() {
  const navigate = useNavigate();

  const [formData, setFormData] = useState({
    company_name: '',
    domain: '',
    message: ''
  });

  const [errors, setErrors] = useState({});
  const [status, setStatus] = useState('idle'); // idle, submitting, success, error
  const [errorMessage, setErrorMessage] = useState('');

  const validate = () => {
    const newErrors = {};
    if (!formData.company_name.trim()) newErrors.company_name = 'Company name is required';
    if (!formData.domain.trim()) {
      newErrors.domain = 'Domain is required';
    } else if (!formData.domain.includes('.')) {
      newErrors.domain = 'Please enter a valid domain (e.g., example.com)';
    }
    if (!formData.message.trim()) newErrors.message = 'Message is required';

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
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(formData)
      });

      const data = await response.json();

      if (!response.ok || data.status === 'error') {
        setStatus('error');
        setErrorMessage(data.detail || data.message || "This company is not in our database. Please contact the sales team.");
        return;
      }

      setStatus('success');
      setFormData({ company_name: '', domain: '', message: '' }); // clear form

    } catch (err) {
      setStatus('error');
      setErrorMessage("Unable to connect to the server. Please check if the backend is running.");
      console.error(err);
    }
  };

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({ ...prev, [name]: value }));
    // clear error for this field
    if (errors[name]) {
      setErrors(prev => ({ ...prev, [name]: '' }));
    }
  };

  return (
    <div className="flex-1 w-full h-full overflow-y-auto custom-scrollbar flex flex-col items-center py-12 px-6">

      {/* Form Container */}
      <div className="w-full max-w-2xl bg-[var(--color-card-bg)] border border-[var(--color-border)] rounded-2xl shadow-xl overflow-hidden">

        {/* Header Ribbon */}
        <div className="bg-gradient-to-r from-emerald-600 to-teal-800 px-8 py-10 text-center relative overflow-hidden">
          <div className="absolute inset-0 bg-black/20" />
          <div className="relative z-10 flex flex-col items-center">
            <div className="w-12 h-12 bg-white rounded-xl shadow-lg flex items-center justify-center mb-4">
              <Target className="w-7 h-7 text-emerald-600" />
            </div>
            <h2 className="text-3xl font-black text-white tracking-tight">RevOps AI Ingestion</h2>
            <p className="text-emerald-100 mt-2 font-medium tracking-wide">Enter lead details to initialize AI analysis</p>
          </div>
        </div>

        <div className="p-8">
          {status === 'success' ? (
            <div className="flex flex-col items-center text-center py-8">
              <div className="w-16 h-16 bg-emerald-500/10 rounded-full flex items-center justify-center mb-6">
                <CheckCircle2 className="w-10 h-10 text-emerald-500" />
              </div>
              <h3 className="text-2xl font-bold text-white mb-3">Lead submitted successfully!</h3>
              <p className="text-gray-400 mb-8 max-w-md leading-relaxed">
                Our AI agents are now analyzing <span className="text-white font-bold">{formData.company_name}</span>. Check the Kanban board to see progress in real time.
              </p>
              <button
                onClick={() => navigate('/kanban')}
                className="flex items-center gap-2 px-8 py-3 bg-white text-black rounded-lg font-bold shadow-lg hover:shadow-xl hover:-translate-y-0.5 transition-all"
              >
                View Kanban Board
                <ArrowRight className="w-4 h-4" />
              </button>
            </div>
          ) : (
            <form onSubmit={handleSubmit} className="space-y-6">

              {status === 'error' && (
                <div className="flex items-start gap-3 p-4 bg-red-500/10 border border-red-500/20 rounded-lg text-red-400 mb-6">
                  <AlertCircle className="w-5 h-5 shrink-0 mt-0.5" />
                  <p className="font-medium text-sm leading-relaxed">{errorMessage}</p>
                </div>
              )}

              {/* Company Name */}
              <div>
                <label className="block text-sm font-semibold text-gray-300 mb-2">
                  Company Name <span className="text-red-500">*</span>
                </label>
                <div className="relative">
                  <div className="absolute inset-y-0 left-0 pl-3.5 flex items-center pointer-events-none">
                    <Building2 className="w-5 h-5 text-gray-500" />
                  </div>
                  <input
                    type="text"
                    name="company_name"
                    value={formData.company_name}
                    onChange={handleChange}
                    className={clsx(
                      "w-full bg-black/40 border rounded-lg pl-11 pr-4 py-3 text-[15px] text-white placeholder:text-gray-600 focus:outline-none focus:ring-2 transition-all",
                      errors.company_name ? "border-red-500/50 focus:ring-red-500/30" : "border-white/10 focus:border-emerald-500 focus:ring-emerald-500/20"
                    )}
                    placeholder="e.g. SurveySparrow"
                  />
                </div>
                {errors.company_name && <p className="mt-1.5 text-xs font-medium text-red-400">{errors.company_name}</p>}
              </div>

              {/* Domain */}
              <div>
                <label className="block text-sm font-semibold text-gray-300 mb-2">
                  Domain <span className="text-red-500">*</span>
                </label>
                <div className="relative">
                  <div className="absolute inset-y-0 left-0 pl-3.5 flex items-center pointer-events-none">
                    <Globe className="w-5 h-5 text-gray-500" />
                  </div>
                  <input
                    type="text"
                    name="domain"
                    value={formData.domain}
                    onChange={handleChange}
                    className={clsx(
                      "w-full bg-black/40 border rounded-lg pl-11 pr-4 py-3 text-[15px] text-white placeholder:text-gray-600 focus:outline-none focus:ring-2 transition-all",
                      errors.domain ? "border-red-500/50 focus:ring-red-500/30" : "border-white/10 focus:border-emerald-500 focus:ring-emerald-500/20"
                    )}
                    placeholder="www.example.com"
                  />
                </div>
                {errors.domain && <p className="mt-1.5 text-xs font-medium text-red-400">{errors.domain}</p>}
              </div>



              {/* Submit Button */}
              <button
                type="submit"
                disabled={status === 'submitting'}
                className="w-full flex items-center justify-center gap-2 py-3.5 rounded-lg text-[15px] font-bold tracking-wide transition-all bg-emerald-600 hover:bg-emerald-500 text-white shadow-[0_0_20px_rgba(5,150,105,0.3)] hover:shadow-[0_0_25px_rgba(5,150,105,0.4)] disabled:opacity-70 disabled:cursor-wait mt-8"
              >
                {status === 'submitting' ? (
                  <>
                    <Loader2 className="w-5 h-5 animate-spin" />
                    Submitting...
                  </>
                ) : (
                  'Request a demo'
                )}
              </button>

            </form>
          )}
        </div>
      </div>

      {/* AI Process Timeline */}
      <div className="w-full max-w-3xl mt-12 grid grid-cols-4 gap-4 px-4 opacity-70">

        <div className="flex flex-col items-center text-center group">
          <div className="w-10 h-10 rounded-full bg-white/5 border border-white/10 flex items-center justify-center mb-3 group-hover:bg-emerald-500/20 group-hover:border-emerald-500/30 transition-colors">
            <CheckCircle2 className="w-5 h-5 text-gray-400 group-hover:text-emerald-400" />
          </div>
          <span className="text-[11px] font-bold uppercase tracking-wider text-gray-500 group-hover:text-emerald-400/80 transition-colors">Step 1</span>
          <p className="text-xs text-gray-400 mt-1 font-medium">Lead submitted</p>
        </div>

        <div className="flex flex-col items-center text-center group relative">
          <div className="absolute top-5 left-[-50%] w-full h-px bg-white/10 -z-10" />
          <div className="w-10 h-10 rounded-full bg-white/5 border border-white/10 flex items-center justify-center mb-3 group-hover:bg-purple-500/20 group-hover:border-purple-500/30 transition-colors">
            <Bot className="w-5 h-5 text-gray-400 group-hover:text-purple-400" />
          </div>
          <span className="text-[11px] font-bold uppercase tracking-wider text-gray-500 group-hover:text-purple-400/80 transition-colors">Step 2</span>
          <p className="text-xs text-gray-400 mt-1 font-medium">AI analyzes company</p>
        </div>

        <div className="flex flex-col items-center text-center group relative">
          <div className="absolute top-5 left-[-50%] w-full h-px bg-white/10 -z-10" />
          <div className="w-10 h-10 rounded-full bg-white/5 border border-white/10 flex items-center justify-center mb-3 group-hover:bg-blue-500/20 group-hover:border-blue-500/30 transition-colors">
            <BarChart3 className="w-5 h-5 text-gray-400 group-hover:text-blue-400" />
          </div>
          <span className="text-[11px] font-bold uppercase tracking-wider text-gray-500 group-hover:text-blue-400/80 transition-colors">Step 3</span>
          <p className="text-xs text-gray-400 mt-1 font-medium">Lead scored</p>
        </div>

        <div className="flex flex-col items-center text-center group relative">
          <div className="absolute top-5 left-[-50%] w-full h-px bg-white/10 -z-10" />
          <div className="w-10 h-10 rounded-full bg-white/5 border border-white/10 flex items-center justify-center mb-3 group-hover:bg-amber-500/20 group-hover:border-amber-500/30 transition-colors">
            <Target className="w-5 h-5 text-gray-400 group-hover:text-amber-400" />
          </div>
          <span className="text-[11px] font-bold uppercase tracking-wider text-gray-500 group-hover:text-amber-400/80 transition-colors">Step 4</span>
          <p className="text-xs text-gray-400 mt-1 font-medium">Ready for presales</p>
        </div>

      </div>

    </div>
  );
}
