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
          <h1 className="text-3xl md:text-4xl font-bold">{dados.titulo}</h1>
          <p className="mt-5 text-xl pc:text-2xl">{dados.conteudo}</p>

        <div className="flex items-center justify-start gap-2 mt-6">
            <ArrowRight className="w-6 h-6 " /> 
            <h2 className="uppercase text-xl font-bold">Slide sobre {dados.titulo}</h2>
        </div>

        </div>
    </section>
  );
}