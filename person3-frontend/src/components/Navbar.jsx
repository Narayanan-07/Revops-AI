import React from 'react';
import { NavLink } from 'react-router-dom';
import { Target, LayoutDashboard, UploadCloud } from 'lucide-react';

export default function Navbar() {
  return (
    <header className="h-14 border-b border-[var(--color-border)] bg-[var(--color-board-bg)]/80 backdrop-blur-md flex items-center justify-between px-6 sticky top-0 z-40">
      
      {/* Brand */}
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

      {/* Navigation Links */}
      <nav className="flex items-center gap-2 bg-black/20 p-1 rounded-lg border border-white/5">
        <NavLink
          to="/"
          className={({ isActive }) => 
            `flex items-center gap-2 px-4 py-1.5 rounded-md text-sm font-medium transition-all ${
              isActive 
                ? 'bg-white/10 text-emerald-400 shadow-sm' 
                : 'text-gray-400 hover:text-emerald-300 hover:bg-white/5'
            }`
          }
        >
          <Target className="w-4 h-4" />
          Submit Lead
        </NavLink>
        
        <NavLink
          to="/kanban"
          className={({ isActive }) => 
            `flex items-center gap-2 px-4 py-1.5 rounded-md text-sm font-medium transition-all ${
              isActive 
                ? 'bg-white/10 text-white shadow-sm' 
                : 'text-gray-400 hover:text-gray-200 hover:bg-white/5'
            }`
          }
        >
          <LayoutDashboard className="w-4 h-4" />
          Kanban Board
        </NavLink>
        
        <NavLink
          to="/transcripts"
          className={({ isActive }) => 
            `flex items-center gap-2 px-4 py-1.5 rounded-md text-sm font-medium transition-all ${
              isActive 
                ? 'bg-white/10 text-white shadow-sm' 
                : 'text-gray-400 hover:text-gray-200 hover:bg-white/5'
            }`
          }
        >
          <UploadCloud className="w-4 h-4" />
          Transcripts
        </NavLink>
      </nav>
      
      {/* Spacer to keep center alignment balanced if needed, or just right side controls */}
      <div className="w-[120px]"></div>
    </header>
  );
}
