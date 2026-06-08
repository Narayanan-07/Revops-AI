import React from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Navbar from './components/Navbar';
import KanbanPage from './pages/KanbanPage';
import TranscriptUpload from './pages/TranscriptUpload';
import LeadForm from './pages/LeadForm';

function App() {
  return (
    <BrowserRouter>
      <div className="min-h-screen bg-[var(--color-page)] text-[var(--color-ink)] overflow-hidden flex flex-col font-sans selection:bg-orange-500/20">
        <Navbar />
        
        {/* Main Content Area */}
        <main className="flex-1 w-full max-w-[1700px] mx-auto overflow-hidden flex flex-col pt-2 relative">
          <Routes>
            <Route path="/" element={<LeadForm />} />
            <Route path="/kanban" element={<KanbanPage />} />
            <Route path="/transcripts" element={<TranscriptUpload />} />
          </Routes>
        </main>
      </div>
    </BrowserRouter>
  );
}

export default App;
