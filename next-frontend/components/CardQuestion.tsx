"use client";
import { useState } from "react";


type Alternativa = {
  id: string;
  texto: string;
};

type CardQuestionProps = {
  titulo: string;
  enunciado: string;
  alternativas: Alternativa[];
  respostaCorreta: string;
  resolucao: string;
  proximaQuestao: () => void;
  questaoAnterior: () => void;
};

export default function CardQuestion(props: CardQuestionProps) {
 const [alternativaSelecionada, setAlternativaSelecionada] = useState("");
 const [respondida, setRespondida] = useState(false);
 const [respostaCorreta, setrespostaCorreta] = useState<boolean | null>(null);

 function verificarResposta(id: string) {
    console.log(id);

    setAlternativaSelecionada(id);
    setRespondida(true);

    if (id === props.respostaCorreta) {
        setrespostaCorreta(true);
    } else {
        setrespostaCorreta(false);
    }
 }

  return (
   <div className="border p-3 md:p-4 lp:p-6 rounded-sm w-full bg-(--question-card-bg) border-(--question-card-border) text-(--question-card-text)">
      <h1 className="font-bold md:text-[20px] lp:text-[24px] pc:text-[28px]">{props.titulo}</h1>

      <p className="font-normal md:text-[20px] lp:text-[24px] mt-1.5">{props.enunciado}</p>

      <div className="flex flex-col justify-between gap-2 mt-3">
        {respondida && (
            <h2 className="font-bold md:text-[18px] lp:text-[24px]">Resolução</h2>
         ) }
        {props.alternativas.map((alternativa) => (
            <div key={alternativa.id} className={`p-2 flex items-center gap-2 cursor-pointer w-full border rounded-md ${respondida ? (alternativa.id === props.respostaCorreta ? "bg-(--light-green) border-(--primary-100) text-(--question-resolution-text)" : alternativa.id === alternativaSelecionada ? "border-(--alert) bg-(--neutral-50) text-(--question-resolution-text)" : "hidden") : "text-(--question-option-text) border-(--question-option-border) shadow-sm shadow-(--neutral-500)"}`}>
                <input type="radio" onChange={() => verificarResposta(alternativa.id)} checked={alternativaSelecionada === alternativa.id} className={`w-5 h-5 ${respondida ? (alternativa.id === props.respostaCorreta ? "accent-(--primary-900)" : alternativa.id === alternativaSelecionada ? "accent-(--dark)" : "") : ""}`} />
                <label className="pl-1.5 font-normal md:text-[20px] lp:text-[24px]">
                  {alternativa.texto}
                </label>
            </div>
      ))}
      </div>

      {respondida && (
        <div className="p-1 font-normal md:text-[20px] lp:text-[24px] text-(--question-card-text)">
            {props.resolucao}
        </div>
      )}

      <div className="flex justify-end gap-3 mt-6">
        <button onClick={props.questaoAnterior } className="px-2 sm:px-5 py-2 rounded-full font-bold md:text-[12px] lp:text-[16px] uppercase bg-(--btn-prev-bg) text-(--btn-prev-text) hover:bg-(--neutral-0)">
          Anterior
        </button>
        <button onClick={props.proximaQuestao} className="px-2 sm:px-5 py-2 rounded-full font-bold md:text-[12px] lp:text-[16px] uppercase bg-(--btn-next-bg) text-(--btn-next-text) hover:bg-(--primary-500)">
          Próxima
        </button>
      </div>
      
    </div>
  );
}