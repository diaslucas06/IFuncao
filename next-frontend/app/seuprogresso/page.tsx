"use client";

import { useState, useEffect } from "react";
import CardStatus from "@/components/CardStatus";
import Header from "@/components/Header";
import { BookOpen, CircleCheckBig, Target, Flame } from "lucide-react";
import StudySuggestion from "@/components/StudySuggestion";
import Simulado from "@/components/Simulado";

export default function Progresso() {
  const [dadosProgresso, setDadosProgresso] = useState({
    assuntosConcluidos: 0,
    totalAssuntos: 0,
    questoesRespondidas: 0,
    totalAcertos: 0,
    ofensiva: 0,
    conteudoRecomendado: "Nenhuma sugestão",
    etapa: 0,
  });

  useEffect(() => {
    const usuario = localStorage.getItem("usuario");
    const token = usuario ? JSON.parse(usuario).access_token : "";
    if (!token) return;

    const headers = { Authorization: `Bearer ${token}` };

    fetch("http://localhost:8000/conteudos/historico", { headers })
      .then((res) => res.json())
      .then((lista) => {
        if (Array.isArray(lista)) {
          setDadosProgresso((prev) => ({
            ...prev,
            assuntosConcluidos: lista.length,
          }));
        }
      });

    fetch("http://localhost:8000/simulados/historico", { headers })
      .then((res) => res.json())
      .then((simulados) => {
        if (!Array.isArray(simulados) || simulados.length === 0) return;

        let questoes = 0;
        let acertos = 0;
        let pior = simulados[0];

        simulados.forEach((s) => {
          questoes += s.sim_total_questoes || 0;
          acertos += s.sim_acertos || 0;
          if (s.sim_acertos < pior.sim_acertos) pior = s;
        });

        const etapaPior = Number(String(pior.sim_etapa).replace(/\D/g, "")) || 1;

        setDadosProgresso((prev) => ({
          ...prev,
          questoesRespondidas: questoes,
          totalAcertos: questoes > 0 ? Math.round((acertos / questoes) * 100) : 0,
          ofensiva: simulados.length,
          etapa: etapaPior,
        }));

        fetch(`http://localhost:8000/conteudos/${etapaPior}`)
          .then((res) => res.json())
          .then((conteudos) => {
            if (conteudos?.[0]?.cont_nome) {
              setDadosProgresso((prev) => ({
                ...prev,
                conteudoRecomendado: conteudos[0].cont_nome,
              }));
            }
          });
      });
  }, []);

  return (
    <div className="min-h-screen flex flex-col bg-(--background-color)">
      <Header />

      <main className="flex-1 w-full mx-auto p-4 sm:p-6 lg:p-10">
        <section className="bg-(--settings-card-color) p-5 sm:p-8 rounded-xl shadow-sm border border-(--background-color)">
          
          <h1 className="text-[24px] md:text-[40px] lg:text-[48px] lp:text-[56px] pc:text-[64px] font-bold">
            Sua Evolução
          </h1>

          <div className="grid grid-cols-2 lp:grid-cols-4 gap-4 lg:gap-6 mt-6">
            
            <CardStatus
              titulo="Assuntos concluídos" valor={`${dadosProgresso.assuntosConcluidos}/${dadosProgresso.totalAssuntos}`} icone={BookOpen} bgColor="bg-(--neutral-0)"
              textColor="text-(--neutral-900)" iconeColor="text-(--primary-300)"
            />

            <CardStatus
              titulo="Questões respondidas" valor={String(dadosProgresso.questoesRespondidas)} icone={CircleCheckBig} bgColor="bg-(--primary-800)"
              textColor="text-(--neutral-0)" iconeColor="text-(--neutral-0)"
            />

            <CardStatus
              titulo="Total de acertos" valor={`${dadosProgresso.totalAcertos}%`} icone={Target} bgColor="bg-(--primary-300)"
              textColor="text-(--neutral-0)" iconeColor="text-(--neutral-0)"
            />

            <CardStatus titulo="Ofensiva" valor={String(dadosProgresso.ofensiva)} icone={Flame} bgColor="bg-(--primary-200)" textColor="text-(--neutral-0)"
              iconeColor="text-(--neutral-0)" descricao="dias"
            />
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 gap-4 lg:gap-6 mt-6">
            <StudySuggestion
              conteudoRecomendado={dadosProgresso.conteudoRecomendado}
              etapa={dadosProgresso.etapa}
            />
            <Simulado />
          </div>

        </section>
      </main>
    </div>
  );
}