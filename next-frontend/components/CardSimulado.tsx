"use client";
import { useState, useEffect } from "react";

type CardSimuladoProps = {
  idQuestao: number;
  titulo: string;
  enunciado: string;
  imagemUrl?: string | null;
  alternativas: Record<string, string>;
  respostaCorreta: string;
  resolucao?: string | null;
  resolucaoImagemUrl?: string | null;
  alternativaSalva?: string;
  proximaQuestao: () => void;
  questaoAnterior: () => void;
  ehUltimaQuestao: boolean;        
  finalizarSimulado: () => void;
  aoResponder: (quesId: number, alternativa: string, acertou: boolean) => void;
  enviando?: boolean;
};

export default function CardSimulado(props: CardSimuladoProps) {
  const [alternativaSelecionada, setAlternativaSelecionada] = useState(props.alternativaSalva || "");
  const [respondida, setRespondida] = useState(Boolean(props.alternativaSalva));
  const [acertouQuestao, setAcertouQuestao] = useState<boolean | null>(
    props.alternativaSalva ? props.alternativaSalva === props.respostaCorreta : null
  );

  useEffect(() => {
    if (props.alternativaSalva) {
      setAlternativaSelecionada(props.alternativaSalva);
      setRespondida(true);
      setAcertouQuestao(props.alternativaSalva === props.respostaCorreta);
    } else {
      setAlternativaSelecionada("");
      setRespondida(false);
      setAcertouQuestao(null);
    }
  }, [props.idQuestao, props.alternativaSalva, props.respostaCorreta]);

  
function verificarResposta(id: string) {
  if (respondida || props.enviando) {
    return;
  }

  const acertou = id === props.respostaCorreta;

  setAlternativaSelecionada(id);
  setAcertouQuestao(acertou);
  setRespondida(true);
  props.aoResponder(props.idQuestao, id, acertou);
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
        {respondida && acertouQuestao !== null && (
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
            <div key={chave} className={`p-2 flex items-center gap-2 cursor-pointer w-full border rounded-md ${respondida && acertouQuestao !== null ? (chave === props.respostaCorreta ? "bg-(--light-green) border-(--primary-100) text-(--question-resolution-text)" : chave === alternativaSelecionada ? "border-(--alert) bg-(--neutral-50) text-(--question-resolution-text)" : "hidden") : "text-(--question-option-text) border-(--question-option-border) shadow-sm shadow-(--neutral-500)"}`}>
              <input type="radio" onChange={() => verificarResposta(chave)} checked={alternativaSelecionada === chave} disabled={respondida || props.enviando} className={`w-5 h-5 ${respondida ? (chave === props.respostaCorreta ? "accent-(--primary-900)" : chave === alternativaSelecionada ? "accent-(--dark)" : "") : ""}`} />
              <label className="pl-1.5 font-normal md:text-xl lp:text-2xl cursor-pointer w-full">{texto}</label>
            </div>
          );
        })} 
      </div>

      <div className="flex justify-end gap-3 mt-6">
        <button onClick={props.questaoAnterior } disabled={props.enviando} className="px-2 sm:px-5 py-2 rounded-full font-bold md:text-xs lp:text-base uppercase bg-(--btn-prev-bg) text-(--btn-prev-text) hover:bg-(--neutral-0)">
          Anterior
        </button>
        <button onClick={props.ehUltimaQuestao ? props.finalizarSimulado : props.proximaQuestao} disabled={props.enviando} className="px-2 sm:px-5 py-2 rounded-full font-bold md:text-xs lp:text-base uppercase bg-(--btn-next-bg) text-(--btn-next-text) hover:bg-(--primary-500)">
          {props.enviando ? "Finalizando..." : props.ehUltimaQuestao ? "Finalizar" : "Próxima"}
        </button>
      </div>
    </div>
  );
}