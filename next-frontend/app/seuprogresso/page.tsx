"use client";

import Header from "@/components/Header";
import EvolucaoSection from "@/components/EvolucaoSection";
import Simulado from "@/components/Simulado";
import StudySuggestion from "@/components/StudySuggestion";
import { CardBackground } from "@/components/CardProfile";

export default function Progresso() {
  return (
    <div className="min-h-screen flex flex-col bg-(--background-color)">
      <Header />

      <main className="flex-1 w-full mx-auto p-4 sm:p-6 lg:p-10">
        <section className="bg-(--settings-card-color) p-5 sm:p-8 rounded-xl shadow-sm border border-(--background-color)">
          
          <h1 className="text-[24px] md:text-[40px] lg:text-[48px] lp:text-[56px] pc:text-[64px] font-bold">
            Sua Evolução
          </h1>

          <EvolucaoSection/>

           <div className="flex flex-col justify-between gap-3 md:gap-5">
              <h1 className="h1_inicio mt-2">Sugestões com base no seu desempenho</h1>
              <div className="grid grid-cols-1 md:grid-cols-2 gap-5 items-stretch">
                <StudySuggestion/>
                <Simulado />
              </div>
            </div>
        </section>
      </main>
    </div>
  );
}