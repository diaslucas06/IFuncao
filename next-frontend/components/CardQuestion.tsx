"use client";
import { useState, useEffect } from "react";

type CardQuestionProps = {
  idQuestao: number;
  titulo: string;
  enunciado: string;
  alternativas: Record<string, string>;
  respostaCorreta: string;
  resolucao: string;
  proximaQuestao: () => void;
  questaoAnterior: () => void;
  ehUltimaQuestao: boolean;        
  concluirConteudo: () => void;
};

export default function CardQuestion(props: CardQuestionProps) {
  const [alternativaSelecionada, setAlternativaSelecionada] = useState("");
  const [respondida, setRespondida] = useState(false);
  const [respostaCorreta, setrespostaCorreta] = useState<boolean | null>(null);

  useEffect(() => {
    setAlternativaSelecionada("");
    setRespondida(false);
    setrespostaCorreta(null);
  }, [props.idQuestao]);

  function verificarResposta(id: string) {
    console.log(id);

    setAlternativaSelecionada(id);
    setRespondida(true);

    const dadosUsuario = localStorage.getItem('usuario');
    if (!dadosUsuario) {
        console.log("Nenhum dado de usuário encontrado no localStorage!");
        return;
    }

    if (id === props.respostaCorreta) {
        setrespostaCorreta(true);
    } else {
        setrespostaCorreta(false);
    }

    const token = JSON.parse(dadosUsuario).access_token;

    fetch('http://localhost:8000/questoes/responder', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${token}`
      },
      body: JSON.stringify({
        respquest_ques_id: props.idQuestao,    
        respquest_alternativa_escolhida: id    
      })
    })
    .then(res => res.json())
    .then(dados => {
      console.log("Resposta guardada no banco:", dados);
    })
    .catch(err => console.log("Erro ao enviar resposta:", err));
  }

  return (
   <div className="border p-3 md:p-4 lp:p-6 rounded-sm w-full bg-(--question-card-bg) border-(--question-card-border) text-(--question-card-text)">
      <h1 className="font-bold md:text-xl lp:text-2xl pc:text-[28px]">{props.titulo}</h1>

      <p className="font-normal md:text-xl lp:text-2xl mt-1.5">{props.enunciado}</p>

      <div className="flex flex-col justify-between gap-2 mt-3">
        {respondida && (
            <h2 className="font-bold md:text-[18px] lp:text-2xl">Resolução</h2>
         ) }
        {Object.entries(props.alternativas).map(([chave, texto]) => {
          return (
            <div key={chave} className={`p-2 flex items-center gap-2 cursor-pointer w-full border rounded-md ${respondida ? (chave === props.respostaCorreta ? "bg-(--light-green) border-(--primary-100) text-(--question-resolution-text)" : chave === alternativaSelecionada ? "border-(--alert) bg-(--neutral-50) text-(--question-resolution-text)" : "hidden") : "text-(--question-option-text) border-(--question-option-border) shadow-sm shadow-(--neutral-500)"}`}>
              <input type="radio" onChange={() => verificarResposta(chave)} checked={alternativaSelecionada === chave} className={`w-5 h-5 ${respondida ? (chave === props.respostaCorreta ? "accent-(--primary-900)" : chave === alternativaSelecionada ? "accent-(--dark)" : "") : ""}`} />
              <label className="pl-1.5 font-normal md:text-xl lp:text-2xl cursor-pointer w-full">{texto}</label>
            </div>
          );
        })} 
      </div>

      {respondida && (
        <div className="p-1 font-normal md:text-xl lp:text-2xl text-(--question-card-text)">
            {props.resolucao}
        </div>
      )}

      <div className="flex justify-end gap-3 mt-6">
        <button onClick={props.questaoAnterior } className="px-2 sm:px-5 py-2 rounded-full font-bold md:text-xs lp:text-base uppercase bg-(--btn-prev-bg) text-(--btn-prev-text) hover:bg-(--neutral-0)">
          Anterior
        </button>
        <button onClick={props.ehUltimaQuestao ? props.concluirConteudo : props.proximaQuestao} className="px-2 sm:px-5 py-2 rounded-full font-bold md:text-xs lp:text-base uppercase bg-(--btn-next-bg) text-(--btn-next-text) hover:bg-(--primary-500)">
          {props.ehUltimaQuestao ? "Finalizar" : "Próxima"}
        </button>
      </div>
    </div>
  );
}