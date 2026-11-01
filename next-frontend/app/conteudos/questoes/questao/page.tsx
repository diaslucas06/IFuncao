"use client";

import CardQuestion from "@/components/CardQuestion";
import Header from "@/components/Header";
import TheoryReview from "@/components/TheoryReview";
import { useState, useEffect } from "react";

export default function questoes() {
  const [questoes, setQuestoes] = useState<any[]>([]);
  const [questaoAtual, setQuestaoAtual] = useState<number>(0);
  const [carregando, setCarregando] = useState<boolean>(true);

  useEffect(() => {
    fetch(`http://localhost:8000/questoes/conteudo/1`)

    .then((resposta) =>{
      if (!resposta.ok){
         throw new Error('Erro ao carregar questões');
      }

      return resposta.json()
    })

    .then((dados) => {
      setQuestoes(dados)
      setCarregando(false)
    })

    .catch((erro) => {
          console.log(erro)
      });

  }, [])

  if (carregando) {
    return <div>Carregando questões...</div>;
  }

  const questao = questoes[questaoAtual];
  const ehUltimaQuestao = questaoAtual === questoes.length - 1;

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
  
  function concluirConteudo() {
    const dadosUsuario = localStorage.getItem('usuario');
    if (!dadosUsuario) {
        console.log("Nenhum dado do usuário encontrado");
        return;
    }

    const token = JSON.parse(dadosUsuario).access_token;

    fetch('http://localhost:8000/conteudos/concluir', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${token}`
      },
      body: JSON.stringify({
        cont_id: 1 
      })
    })
    .then(res => res.json())
    .then(dados => {
      console.log("Conteúdo concluido com sucesso:", dados);
      window.location.href = "/conteudos"; 
    })
    .catch(err => console.log("Erro ao concluir conteudo:", err));
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
              <CardQuestion key={questao.ques_id} idQuestao={questao.ques_id} titulo={`Questão ${questao.ques_id}`}
                enunciado={questao.ques_enunciado} alternativas={questao.ques_alternativas}
                respostaCorreta={questao.ques_resposta_correta} resolucao={questao.ques_resolucao}
                proximaQuestao={proximaQuestao} questaoAnterior={questaoAnterior} ehUltimaQuestao={ehUltimaQuestao} concluirConteudo={concluirConteudo}
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