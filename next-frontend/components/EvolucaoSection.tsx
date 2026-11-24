
"use client";

import { useState, useEffect } from "react";
import { BookOpen, CircleCheckBig, Target, Flame } from "lucide-react";
import CardStatus from "@/components/CardStatus";

export default function EvolucaoSection() {
  const [concluidos, setConcluidos] = useState(0);
  const [totalConteudos, setTotalConteudos] = useState(0);
  const [questoes, setQuestoes] = useState(0);
  const [acertos, setAcertos] = useState(0);
  const [ofensiva, setOfensiva] = useState(0);

   useEffect(() => {
  async function buscarEvolucao() {
    try {
      const dadosUsuario = localStorage.getItem("usuario");
      if (!dadosUsuario) return;

      const token = JSON.parse(dadosUsuario).access_token;

      const resposta = await fetch("http://localhost:8000/conteudos/evolucao", {
        headers: {
          "Authorization": `Bearer ${token}`
        }
      });

      console.log("Status da evolução:", resposta.status);

      const dados = await resposta.json();

      console.log("Dados recebidos:", dados);

      if (!resposta.ok) {
        throw new Error("Não foi possível buscar a evolução");
      }

      setConcluidos(dados.conteudos_concluidos);
      setTotalConteudos(dados.total_conteudos);
      setQuestoes(dados.questoes_respondidas);
      setAcertos(dados.total_acertos);
      setOfensiva(dados.ofensiva);

    } catch (erro) {
      console.log("Erro ao buscar evolução:", erro);
    }
  }

  buscarEvolucao();
}, []);
  return (
    <div className="w-full justify-between gap-2 md:gap-4 grid grid-cols-2 lg:grid-cols-4">
      <CardStatus
        titulo="Assuntos concluídos" valor={`${concluidos}/${totalConteudos}`} icone={BookOpen} bgColor="bg-(--neutral-0)"
        textColor="text-(--neutral-900)" iconeColor="text-(--primary-300)"
      />

      <CardStatus
        titulo="Questões respondidas" valor={String(questoes)} icone={CircleCheckBig} bgColor="bg-(--primary-800)"
        textColor="text-(--neutral-0)" iconeColor="text-(--neutral-0)"
      />

      <CardStatus
        titulo="Total de acertos" valor={`${acertos}%`} icone={Target} bgColor="bg-(--primary-300)"
        textColor="text-(--neutral-0)" iconeColor="text-(--neutral-0)"
      />

      <CardStatus
        titulo="Ofensiva" valor={String(ofensiva)} icone={Flame} bgColor="bg-(--primary-200)" textColor="text-(--neutral-0)"
        iconeColor="text-(--neutral-0)" descricao="dias"
      />
    </div>
  );
}
