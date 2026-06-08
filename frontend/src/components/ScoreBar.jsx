import React from 'react';
import clsx from 'clsx';

export default function ScoreBar({ label, score, colorClass }) {
  const widthPercentage = Math.min(Math.max((score || 0), 0), 100);

  return (
    <div className="flex flex-col gap-1 w-full">
      <div className="flex justify-between items-end text-[10px] font-bold tracking-wider">
        <span className="uppercase text-[var(--color-ink-soft)]">{label}</span>
        <span className={clsx('font-mono', colorClass)}>{score || 0}/100</span>
      </div>
      <div className="h-1.5 w-full bg-black/10 rounded-full overflow-hidden">
        <div
          className={clsx('h-full rounded-full transition-all duration-500', colorClass.replace('text-', 'bg-'))}
          style={{ width: `${widthPercentage}%` }}
        />
      </div>
    </div>
  );
}
