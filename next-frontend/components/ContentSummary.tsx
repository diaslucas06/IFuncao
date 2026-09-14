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
    <section>
        <div key={dados.id} className="text-left">
          <h1 className="text-[24px] md:text-[40px] lg:text-[48px] lp:text-[56px] pc:text-[64px] font-bold">{dados.titulo}</h1>
          <p className="font-normal texlg:text-[18px] lp:text-[24px] pc:text-[32px] ">{dados.conteudo}</p>

        <div className="flex items-center justify-start gap-2 mt-6">
            <ArrowRight className="w-6 h-6  hidden md:block" /> 
            <h2 className="uppercase text-[18px] md:text-[24px] lg:text-[30px] pc:text-[32px] font-bold">Slide sobre {dados.titulo}</h2>
        </div>

        </div>
    </section>
  );
}