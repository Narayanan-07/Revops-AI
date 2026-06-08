import React from 'react';
import { NavLink } from 'react-router-dom';
import { Sparkles, LayoutDashboard, UploadCloud, PlusCircle } from 'lucide-react';
import clsx from 'clsx';

const linkClass = ({ isActive }) =>
  clsx(
    'flex items-center gap-2 px-4 py-1.5 rounded-md text-sm font-medium transition-all',
    isActive
      ? 'bg-orange-500 text-white shadow-sm'
      : 'text-[var(--color-ink-soft)] hover:text-[var(--color-ink)] hover:bg-black/5'
  );

export default function Navbar() {
  return (
    <header className="h-14 border-b border-[var(--color-border)] bg-[var(--color-surface)]/90 backdrop-blur-md flex items-center justify-between px-6 sticky top-0 z-40">

      {/* Brand */}
      <div className="flex items-center gap-2.5">
        <div className="w-8 h-8 rounded-lg bg-orange-500 flex items-center justify-center shadow-[0_2px_10px_rgba(249,115,22,0.4)]">
          <Sparkles className="w-5 h-5 text-white" />
        </div>
        <h1 className="font-extrabold text-lg tracking-tight text-[var(--color-ink)]">
          RevOps<span className="text-orange-500"> AI</span>
        </h1>
        <span className="ml-1 px-2 py-0.5 rounded text-[10px] font-black tracking-widest bg-green-100 text-green-700 uppercase">
          Live
        </span>
      </div>

      {/* Navigation Links */}
      <nav className="flex items-center gap-1 bg-[var(--color-surface-2)] p-1 rounded-lg border border-[var(--color-border)]">
        <NavLink to="/" className={linkClass}>
          <PlusCircle className="w-4 h-4" />
          Submit Lead
        </NavLink>
        <NavLink to="/kanban" className={linkClass}>
          <LayoutDashboard className="w-4 h-4" />
          Kanban Board
        </NavLink>
        <NavLink to="/transcripts" className={linkClass}>
          <UploadCloud className="w-4 h-4" />
          Transcripts
        </NavLink>
      </nav>

      <div className="w-[120px]" />
    </header>
  );
}
