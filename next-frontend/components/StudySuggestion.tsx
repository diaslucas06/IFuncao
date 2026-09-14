'use client'
import Link from "next/link";

type StudySuggestionProps = {
  conteudoRecomendado: string;
  etapa: number;
};

export default function StudySuggestion(props: StudySuggestionProps) {
  return (
    <div className="bg-(--sugestion-card-color) flex flex-col lp:flex-row border-l-4 justify-between items-start lp:items-end basis-1/2 gap-2 md:gap-4 p-4 rounded-sm border-(--primary-200) shadow-md shadow-black/20">

      <div className="flex-1">
      
        <h1 className="font-bold text-[24px] text-center md:text-start md:text-[28px] lg:text-[32px] lp:text-[40px] text-(--base-text-color)">
          Sugestão de estudo
        </h1>

        <h2 className="font-medium text-[16px] md:text-[20px] lp:text-[24px] pc:text-[32px] text-(--search-color) mt-1">
          Com base no seu desempenho,você deve focar em:
        </h2>

        <p className="text-[16px] md:text-[20px] lp:text-[24px] pc:text-[32px] text-(--sugestion-tag-color) mt-1">
          {props.conteudoRecomendado} - {props.etapa}
        </p>

      </div>

      <div className="w-full ml:w-auto mt-2 ml:mt-0">

        <Link href="/conteudoRecomendado"
          className="bg-(--sugestion-button-color) text-(--sugestion-button-text-color) md:text-[20px] lp:text-[24px] flex items-center p-2 px-4 md:px-6 rounded-sm font-bold whitespace-nowrap"
        >
          Ir para conteúdo
        </Link>

      </div>

    </div>
  );
}