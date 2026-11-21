"use client";
import { useState, useEffect } from "react";

type CardQuestionProps = {
  idQuestao: number;
  titulo: string;
  enunciado: string;
  imagemUrl?: string | null;
  alternativas: Record<string, string>;
  respostaCorreta: string;
  resolucao: string;
  resolucaoImagemUrl?: string | null;
  respostaSalva?: {
    alternativa: string;
    acertou: boolean;
    respostaCorreta: string;
  };
  proximaQuestao: () => void;
  questaoAnterior: () => void;
  ehUltimaQuestao: boolean;        
  concluirConteudo: () => void;
  aoResponder: (quesId: number, alternativa: string, acertou: boolean, respostaCorreta: string) => void;
};

export default function CardQuestion(props: CardQuestionProps) {
  const [alternativaSelecionada, setAlternativaSelecionada] = useState(props.respostaSalva?.alternativa || "");
  const [respondida, setRespondida] = useState(Boolean(props.respostaSalva));
  const [respostaCorreta, setRespostaCorreta] = useState<boolean | null>(
    props.respostaSalva ? props.respostaSalva.acertou : null
  );
  const [verificando, setVerificando] = useState(false);
  const [erroResposta, setErroResposta] = useState("");
  const [alternativaCorretaAPI, setAlternativaCorretaAPI] = useState<string | null>(
    props.respostaSalva?.respostaCorreta || null
  );

  useEffect(() => {
    if (props.respostaSalva) {
      setAlternativaSelecionada(props.respostaSalva.alternativa);
      setRespondida(true);
      setRespostaCorreta(props.respostaSalva.acertou);
      setAlternativaCorretaAPI(props.respostaSalva.respostaCorreta);
      setVerificando(false);
      setErroResposta("");
    } else {
      setAlternativaSelecionada("");
      setRespondida(false);
      setRespostaCorreta(null);
      setVerificando(false);
      setErroResposta("");
      setAlternativaCorretaAPI(null);
    }
  }, [props.idQuestao, props.respostaSalva]);

  
function verificarResposta(id: string) {
  if (respondida || verificando) {
    return;
  }

  const dadosUsuario = localStorage.getItem('usuario');

  if (!dadosUsuario) {
    setErroResposta("Nenhum dado de usuário encontrado.");
    return;
  }

  const token = JSON.parse(dadosUsuario).access_token;

  if (!token) {
    setErroResposta("Token de autenticação não encontrado.");
    return;
  }

  setVerificando(true);
  setErroResposta("");
  setAlternativaSelecionada(id);

  fetch('http://localhost:8000/questoes/responder', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${token}`
    },
    body: JSON.stringify({
      respques_ques_id: props.idQuestao,
      respques_alternativa_escolhida: id
    })
    
  })
  .then((resposta) => {
      if (!resposta.ok) {
        throw new Error("Erro ao verificar resposta");
      }

      return resposta.json();
    })
    .then(dados => {
      console.log("Resposta guardada no banco:", dados);

      setRespostaCorreta(dados.acertou);
      setAlternativaCorretaAPI(dados.resposta_correta);
      setRespondida(true);
      props.aoResponder(props.idQuestao, id, dados.acertou, dados.resposta_correta);
    })
    .catch(err => {
      console.log("Erro ao enviar resposta:", err);

      setErroResposta("Não foi possível verificar sua resposta.");
      setAlternativaSelecionada("");
    })
    .finally(() => {
      setVerificando(false);
    });
  }

  return (
   <div className="border p-3 md:p-4 lp:p-6 rounded-sm w-full bg-(--question-card-bg) border-(--question-card-border) text-(--question-card-text)">
      <h1 className="font-bold md:text-xl lp:text-2xl pc:text-[28px]">{props.titulo}</h1>

      <p className="font-normal md:text-xl lp:text-2xl mt-1.5">{props.enunciado}</p>

      {props.imagemUrl && (
        <div className="my-3">
          <img  src={props.imagemUrl} alt="Ilustração da questão" 
           className="max-h-64 rounded-md object-contain" 
          />
        </div>
      )}

      <div className="flex flex-col justify-between gap-2 mt-3">
        {respondida && respostaCorreta !== null && (
          <><h2 className="font-bold md:text-[18px] lp:text-2xl">Resolução</h2>
          <p className="p-1 font-normal md:text-xl lp:text-2xl text-(--question-card-text)">{props.resolucao}</p>

          {props.resolucaoImagemUrl && (
           <div className="my-2">
            <img  src={props.resolucaoImagemUrl} alt="Imagem da resolução" 
              className="max-h-64 rounded-md object-contain" 
            />
            </div>
          )}
          </>
        )}
        {Object.entries(props.alternativas).map(([chave, texto]) => {
          return (
            <div key={chave} className={`p-2 flex items-center gap-2 cursor-pointer w-full border rounded-md ${respondida && respostaCorreta !== null ? (chave === alternativaCorretaAPI ? "bg-(--light-green) border-(--primary-100) text-(--question-resolution-text)" : chave === alternativaSelecionada ? "border-(--alert) bg-(--neutral-50) text-(--question-resolution-text)" : "hidden") : "text-(--question-option-text) border-(--question-option-border) shadow-sm shadow-(--neutral-500)"}`}>
              <input type="radio" onChange={() => verificarResposta(chave)} checked={alternativaSelecionada === chave} disabled={respondida || verificando} className={`w-5 h-5 ${respondida ? (chave === alternativaCorretaAPI ? "accent-(--primary-900)" : chave === alternativaSelecionada ? "accent-(--dark)" : "") : ""}`} />
              <label className="pl-1.5 font-normal md:text-xl lp:text-2xl cursor-pointer w-full">{texto}</label>
            </div>
          );
        })} 
      </div>

      <div className="flex justify-end gap-3 mt-6">
        <button onClick={props.questaoAnterior } disabled={verificando} className="px-2 sm:px-5 py-2 rounded-full font-bold md:text-xs lp:text-base uppercase bg-(--btn-prev-bg) text-(--btn-prev-text) hover:bg-(--neutral-0)">
          Anterior
        </button>
        <button onClick={props.ehUltimaQuestao ? props.concluirConteudo : props.proximaQuestao} disabled={verificando} className="px-2 sm:px-5 py-2 rounded-full font-bold md:text-xs lp:text-base uppercase bg-(--btn-next-bg) text-(--btn-next-text) hover:bg-(--primary-500)">
          {props.ehUltimaQuestao ? "Finalizar" : "Próxima"}
        </button>
      </div>
    </div>
  );
}