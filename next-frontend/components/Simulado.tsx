'use client'
import Link from "next/link";

export default function Simulado() {
  return (
    <div className="bg-(--sugestion-card-color) flex flex-col justify-between items-start border-l-4 gap-4 p-4 rounded-sm border-(--primary-500) shadow-md shadow-black/20 h-full">
      <div>
        <h1 className="font-bold text-2xl md:text-[28px] lg:text-[32px] lp:text-[40px] text-(--base-text-color)">
          Simulado do ENEM
        </h1>

        <h2 className="font-medium text-base md:text-xl lp:text-2xl pc:text-[32px] text-(--search-color) mt-1">
          Pratique com questões reais de provas anteriores no formato oficial e avalie seu desempenho.
        </h2>
      </div>

      <div className="mt-2">
        <Link href="/simulados"
          className="bg-(--sugestion-button-color) text-(--sugestion-button-text-color) md:text-xl lp:text-2xl inline-flex items-center p-2 px-4 md:px-6 rounded-sm font-bold whitespace-nowrap hover:bg-(--profile-button-color-hover)"
        >
          Fazer simulado
        </Link>
      </div>
    </div>
  );
}