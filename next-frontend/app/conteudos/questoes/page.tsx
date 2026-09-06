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

      <main className="max-w-7xl mx-2 sm:mx-4 lg:mx-8 p-4">

        <h1 className="font-bold text-2xl ml:text-3xl mt-3">
          Lista de exercícios
        </h1>

        <div className="flex flex-col lg:flex-row items-start gap-6 lg:gap-8 mt-3">

          <section className="w-full lg:flex-1 min-w-0">

            <div className="rounded-md p-3 w-full bg-(--theory-header-bg) text-(--theory-header-text)">
              <h2 className="font-bold text-base ml:text-lg">
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

          <div className="ml:w-[420px] lp:w-[480px] max-w-full shrink-0 self-start">
            <TheoryReview />
          </div>

        </div>
      </main>
    </div>
  );
}