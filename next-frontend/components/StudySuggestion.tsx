"use client";

import { useState, useEffect } from "react";
import Link from "next/link";

export default function StudySuggestion() {
  const [conteudoRecomendado, setConteudoRecomendado] = useState("Nenhuma sugestão");
  const [etapa, setEtapa] = useState<string | number>(0);
  const [temSugestao, setTemSugestao] = useState(false);

  useEffect(() => {
    const dadosUsuario = localStorage.getItem("usuario");
    if (!dadosUsuario) return;

    const token = JSON.parse(dadosUsuario).access_token;
    if (!token) return;

    const headers = {
      "Content-Type": "application/json",
      Authorization: `Bearer ${token}`,
    };

    fetch("http://localhost:8000/simulados/historico", { headers })
      .then((resposta) => {
        if (!resposta.ok) {
          throw new Error(`Erro ao buscar simulados: ${resposta.status}`);
        }
        return resposta.json();
      })
      .then((simulados) => {
        if (!Array.isArray(simulados) || simulados.length === 0) return null;

        let piorSimulado = simulados[0];
        for (const sim of simulados) {
          if (sim.sim_acertos < piorSimulado.sim_acertos) {
            piorSimulado = sim;
          }
        }

        const etapaRaw = String(piorSimulado.sim_etapa);
        const etapaFormatada =
          etapaRaw === "ENEM" ? "ENEM" : Number(etapaRaw.slice(-1)) || 1;
        setEtapa(etapaFormatada);

        return fetch(`http://localhost:8000/conteudos/${etapaFormatada}`, { headers })
          .then((respostaConteudos) => {
            if (!respostaConteudos.ok) {
              throw new Error(`Erro ao buscar conteúdos: ${respostaConteudos.status}`);
            }
            return respostaConteudos.json();
          });
      })
      .then((listaConteudos) => {
        if (Array.isArray(listaConteudos) && listaConteudos.length > 0) {
          setConteudoRecomendado(listaConteudos[0].cont_nome);
          setTemSugestao(true);
        }
      })
      .catch((erro) => {
        console.log("Erro ao buscar sugestão:", erro);
      });
  }, []);

  const hrefDestino = temSugestao
    ? `/conteudos/resumo?etapa=${etapa}&nome=${encodeURIComponent(conteudoRecomendado)}`
    : "/conteudos";

  return (
    <div className="bg-(--sugestion-card-color) flex flex-col lp:flex-row border-l-4 justify-between items-start lp:items-end basis-1/2 gap-2 md:gap-4 p-4 rounded-sm border-(--primary-200) shadow-md shadow-black/20">
      <div className="flex-1">
        <h1 className="font-bold text-2xl md:text-start md:text-[28px] lg:text-[32px] lp:text-[40px] text-(--base-text-color)">
          Sugestão de estudo
        </h1>

        <h2 className="font-medium text-base md:text-xl lp:text-2xl pc:text-[32px] text-(--search-color) mt-1">
          Com base no seu desempenho, você deve focar em:
        </h2>

        <p className="text-base md:text-xl lp:text-2xl pc:text-[32px] text-(--sugestion-tag-color) mt-1">
          {temSugestao
            ? `${conteudoRecomendado} - ${etapa === "ENEM" ? "ENEM" : `${etapa}º Ano`}`
            : "Realize um simulado para receber sugestões"}
        </p>
      </div>

      <div className="w-full ml:w-auto mt-2 ml:mt-0">
        <Link
          href={hrefDestino}
          className="bg-(--sugestion-button-color) text-(--sugestion-button-text-color) md:text-xl lp:text-2xl flex items-center p-2 px-4 md:px-6 rounded-sm font-bold whitespace-nowrap hover:bg-(--profile-button-color-hover)"
        >
          {temSugestao ? "Ir para conteúdo" : "Ver conteúdos"}
        </Link>
      </div>
    </div>
  );
}