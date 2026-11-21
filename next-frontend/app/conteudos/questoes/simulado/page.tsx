"use client";

import CardSimulado from "@/components/CardSimulado";
import Header from "@/components/Header";
import { useState, useEffect } from "react";
import { useSearchParams } from "next/navigation";


export default function simulado() {
  const [questoes, setQuestoes] = useState<any[]>([]);
  const [questaoAtual, setQuestaoAtual] = useState<number>(0);
  const [carregando, setCarregando] = useState<boolean>(true);
  const [totalAcertos, setTotalAcertos] = useState<number>(0);
  const [respostasUsuario, setRespostasUsuario] = useState<Record<number, string>>({});
  const [resultadoFinal, setResultadoFinal] = useState<any>(null);

  const searchParams = useSearchParams();
  const etapa = searchParams.get("etapa") || "1";

  function registrarTentativa(quesId: number, alternativa: string, acertou: boolean) {
    setRespostasUsuario((prev) => ({ ...prev, [quesId]: alternativa }));
    if (acertou) {
      setTotalAcertos((prev) => prev + 1);
    }
  }

  useEffect(() => {
    setCarregando(true);
    setQuestoes([]);
    setQuestaoAtual(0);
    setTotalAcertos(0);
    setRespostasUsuario({});
    setResultadoFinal(null);

    fetch(`http://localhost:8000/simulados/iniciar?etapa=${etapa}`)
      .then((resposta) => {
        if (!resposta.ok) {
          throw new Error('Erro ao carregar questões');
        }

        return resposta.json();
      })
      .then((dados) => {
        setQuestoes(dados.questoes || []);
        setCarregando(false);
      })
      .catch((erro) => {
        console.log(erro);
        setCarregando(false);
      });
  }, [etapa]);

  if (carregando) {
    return <div>Carregando questões...</div>;
  }

  if (questoes.length === 0) {
    return (
      <div className="min-h-screen">
        <Header />
        <main className="p-8">
          <h2 className="text-2xl font-bold">Nenhuma questão encontrada para a Etapa {etapa}.</h2>
        </main>
      </div>
    );
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
  
  function finalizarSimulado() {
    const dadosUsuario = localStorage.getItem('usuario');

    if (!dadosUsuario) {
        console.log("Nenhum dado do usuário encontrado");
        return;
    }
    
    const token = JSON.parse(dadosUsuario).access_token;

    fetch('http://localhost:8000/simulados/finalizar', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${token}`
      },
      body: JSON.stringify({
        etapa: etapa,
        respostas: questoes.map((q) => ({
          ques_id: q.ques_id,
          alternativa_escolhida: respostasUsuario[q.ques_id] || null
        }))
      })
    })
    .then(res => res.json())
    .then(dados => {
      console.log("Simulado concluido com sucesso:", dados);
      setResultadoFinal(dados);
    })
    .catch(err => console.log("Erro ao concluir simulado:", err));
  }

  return (
    <div className="min-h-screen">
      <Header />

      <main className="mx-2 sm:mx-4 lg:mx-8 p-4">
        {resultadoFinal ? (
          <div className="border p-6 md:p-8 rounded-sm w-full bg-(--question-card-bg) border-(--question-card-border) text-(--question-card-text) text-center my-4 max-w-2xl mx-auto">
            <h2 className="font-bold text-2xl md:text-3xl mb-4">Simulado Concluído</h2>
            <p className="font-normal md:text-xl mb-2">Você finalizou todas as questões deste simulado</p>
            <p className="font-bold md:text-2xl mb-2">
              Total de acertos: <span className="px-3 py-1 rounded-md">{resultadoFinal.sim_acertos} / {resultadoFinal.sim_total_questoes}</span>
            </p>
            <p className="font-bold md:text-2xl mb-8">
              Nota final: <span className="px-3 py-1 rounded-md">{resultadoFinal.sim_nota}</span>
            </p>

            <div className="flex justify-center">
              <button 
                onClick={() => { window.location.href = "/simulados"; }}
                className="px-6 py-3 rounded-full font-bold uppercase bg-(--btn-next-bg) text-(--btn-next-text) hover:bg-(--primary-500) cursor-pointer"
              >
                Voltar para os Simulados
              </button>
            </div>
          </div>
        ) : (
        <>
          <h1 className="text-[24px] md:text-[40px] lg:text-[48px] lp:text-[56px] pc:text-[64px] font-bold mt-3">
            Simulado
          </h1>
          <div className="flex flex-col lg:flex-row items-start gap-6 lg:gap-8 mt-3">

            <section className="w-full lg:flex-1 min-w-0">

              <div className="rounded-md bg-(--theory-header-bg) text-(--theory-header-text)">
                <h2 className="font-bold  rounded-2xl ml-1.5 p-2 text-[20px] md:text-[28px] lg:text-[32px] pc:text-[36px]">
                  Simulado - Etapa {etapa}
                </h2>
              </div>
              
              <div className="flex flex-col gap-4 mt-3">
                <CardSimulado key={questao.ques_id} idQuestao={questao.ques_id} titulo={`Questão ${questaoAtual + 1}`}
                  enunciado={questao.ques_enunciado} imagemUrl={questao.ques_imagem_url} alternativas={questao.ques_alternativas}
                  respostaCorreta={questao.ques_resposta_correta} resolucao={questao.ques_resolucao} resolucaoImagemUrl={questao.ques_resolucao_imagem_url}
                  alternativaSalva={respostasUsuario[questao.ques_id]} aoResponder={registrarTentativa}
                  proximaQuestao={proximaQuestao} questaoAnterior={questaoAnterior} ehUltimaQuestao={ehUltimaQuestao} finalizarSimulado={finalizarSimulado}
                />
              </div>

            </section>

          </div>
        </>
        )}
      </main>
    </div>
  );
}