'use client'
import { ArrowRight } from 'lucide-react';

type ContentSummaryProps = {
  dados: {
    id: number
    titulo: string;
    conteudo: string;
  };
};

export default function ContentSummary({ dados }: ContentSummaryProps) {
  return (
      <div key={dados.id} className="text-left flex flex-col gap-10">
        
        <h1 className="text-3xl md:text-[40px] lg:text-5xl lp:text-[56px] pc:text-[64px] font-bold">{dados.titulo}</h1>
        <div className="flex flex-col gap-1.5 text-sm sm:text-base leading-relaxed">
          {dados.conteudo?.split("\n").map((linha: string, i: number) => {
            const linhaLimpa = linha.trim();
            const comecaComNumero = /^\d+\./.test(linhaLimpa);
            return (
              <p
                key={i}
                className={
                  linhaLimpa === ""
                    ? "h-2 text-xl"
                    : comecaComNumero
                    ? "text-2xl font-bold text-2xl pb-5"
                    : "text-xl"
                }
              >
                {linha}
              </p>
            );
          })}
        </div>

        <div className="flex items-center justify-start gap-2 mt-6">
            <ArrowRight className="w-6 h-6  hidden md:block" /> 
            <h2 className="uppercase text-3xl md:text-2xl lg:text-3xl pc:text-[32px] font-bold pb-5">Slide sobre {dados.titulo}</h2>
        </div>

      </div>
  );
}