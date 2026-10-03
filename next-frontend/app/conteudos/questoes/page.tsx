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
      enunciado: " Um concurso para preencher 200 vagas recebeu 1600 inscrições. Quantos candidatos há para cada vaga?",
      alternativas: [
        { id: "a", texto: "4" },
        { id: "b", texto: "6" },
        { id: "c", texto: "8" },
        { id: "d", texto: "12" },
      ],
      respostaCorreta: "c",
      resolucao: "Comparando o número de candidatos com o número de vagas em uma divisão, temos: 1600:200 = 8/1, Sendo assim, a razão entre os números é 8 para 1, ou seja, há 8 candidatos para 1 vaga no concurso. Como um número dividido por 1 tem como resultado ele mesmo, então a alternativa correta é a letra c) 8.",
    },

    {
      id: 2,
      enunciado: " Em uma seleção, a razão entre o número de homens e mulheres candidatos a vaga é 4/7. Sabendo que 32 candidatos são do sexo masculino, o número total de participantes na seleção é:",
      alternativas: [
        { id: "a", texto: "56" },
        { id: "b", texto: "72" },
        { id: "c", texto: "88" },
        { id: "d", texto: "94" },
      ],
      respostaCorreta: "b",
      resolucao: "Primeiramente, calculamos, através da regra fundamental da proporção, o número de mulheres na seleção. Agora, somamos o número de homens e mulheres para encontrarmos o total de participantes. 56 + 32 = 88",
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
                Questões de Razão e Proporção
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