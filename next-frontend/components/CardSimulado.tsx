"use client";
import { useState, useEffect } from "react";

type CardSimuladoProps = {
  idQuestao: number;
  titulo: string;
  enunciado: string;
  imagemUrl?: string | null;
  alternativas: Record<string, string>;
  alternativaSalva?: string;
  proximaQuestao: () => void;
  questaoAnterior: () => void;
  ehUltimaQuestao: boolean;        
  finalizarSimulado: () => void;
  aoResponder: (quesId: number, alternativa: string) => void;
  enviando?: boolean;
};

export default function CardSimulado(props: CardSimuladoProps) {
  const [alternativaSelecionada, setAlternativaSelecionada] = useState(
    props.alternativaSalva || ""
  );

  useEffect(() => {
    setAlternativaSelecionada(props.alternativaSalva || "");
  }, [props.idQuestao, props.alternativaSalva]);
  
  function verificarResposta(id: string) {
    if (props.enviando) return;

    setAlternativaSelecionada(id);
    props.aoResponder(props.idQuestao, id);
  }

  return (
   <div className="border p-3 md:p-4 lp:p-6 rounded-sm w-full bg-(--question-card-bg) border-(--question-card-border) text-(--question-card-text)">
      <h1 className="font-bold md:text-xl lp:text-2xl pc:text-[28px]">{props.titulo}</h1>

      <p className="font-normal md:text-xl lp:text-2xl mt-1.5">{props.enunciado}</p>

      {props.imagemUrl && (
        <div className="my-3">
          <img  src={props.imagemUrl} alt="Ilustração da questão" referrerPolicy="no-referrer"
           className="max-h-64 rounded-md object-contain" 
          />
        </div>
      )}

      <div className="flex flex-col justify-between gap-2 mt-3">
        {Object.entries(props.alternativas).map(([chave, texto]) => {
          return (
            <div key={chave} className="p-2 flex items-center gap-2 cursor-pointer w-full border rounded-md text-(--question-option-text) border-(--question-option-border) shadow-sm shadow-(--neutral-500)">
              <input type="radio" onChange={() => verificarResposta(chave)} checked={alternativaSelecionada === chave} disabled={Boolean(alternativaSelecionada)} className="w-5 h-5 hover:cursor-pointer accent-(--primary-900)" />
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