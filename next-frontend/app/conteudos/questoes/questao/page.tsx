"use client";

import CardQuestion from "@/components/CardQuestion";
import Header from "@/components/Header";
import TheoryReview from "@/components/TheoryReview";
import { useState } from "react";

export default function questoes() {
  const [questaoAtual, setQuestaoAtual] = useState<number>(0);

  const questoes = [
    {
      id: 1,
      enunciado: "Um técnico possui 15 jogadores...",
      alternativas: [
        { id: "a", texto: "Resposta A" },
        { id: "b", texto: "Resposta B" },
        { id: "c", texto: "Resposta C" },
        { id: "d", texto: "Resposta D" },
      ],
      respostaCorreta: "a",
      resolucao: "texto texto",
    },

    {
      id: 2,
      enunciado: "Uma turma possui 30 alunos...",
      alternativas: [
        { id: "a", texto: "Resposta A" },
        { id: "b", texto: "Resposta B" },
        { id: "c", texto: "Resposta C" },
        { id: "d", texto: "Resposta D" },
      ],
      respostaCorreta: "b",
      resolucao: "texto texto",
    },
  ];

  const questao = questoes[questaoAtual];

  function proximaQuestao() {
    if (questaoAtual < questoes.length - 1) {
      setQuestaoAtual(questaoAtual + 1);
    }
  }

  function questaoAnterior() {
    if (questaoAtual > 0) {
      setQuestaoAtual(questaoAtual - 1);
    }
  }

  return (
    <div className="min-h-screen">
      <Header />

      <main className="mx-2 sm:mx-4 lg:mx-8 p-4">

        <h1 className="text-[24px] md:text-[40px] lg:text-[48px] lp:text-[56px] pc:text-[64px] font-bold mt-3">
          Lista de exercícios
        </h1>

        <div className="flex flex-col lg:flex-row items-start gap-6 lg:gap-8 mt-3">

          <section className="w-full lg:flex-1 min-w-0">

            <div className="rounded-md bg-(--theory-header-bg) text-(--theory-header-text)">
              <h2 className="font-bold  rounded-2xl ml-1.5 p-2 text-[20px] md:text-[28px] lg:text-[32px] pc:text-[36px]">
                Questões de Análise Combinatória
              </h2>
            </div>

            <div className="flex flex-col gap-4 mt-3">
              <CardQuestion key={questao.id} titulo={`Questão ${questao.id}`}
                enunciado={questao.enunciado} alternativas={questao.alternativas}
                respostaCorreta={questao.respostaCorreta} resolucao={questao.resolucao}
                proximaQuestao={proximaQuestao} questaoAnterior={questaoAnterior}
              />
            </div>

          </section>

          <div className="w-full md:w-[35%] max-w-full shrink-0 self-start">
            <TheoryReview />
          </div>

        </div>
      </main>
    </div>
  );
}