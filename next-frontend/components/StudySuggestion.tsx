'use client'
import Link from "next/link";

type StudySuggestionProps = {
  conteudoRecomendado: string;
  etapa: number;
};

export default function StudySuggestion(props: StudySuggestionProps) {
  return (
    <div className="bg-(--sugestion-card-color) flex flex-col lp:flex-row border-l-4 justify-between items-start lp:items-end gap-4 p-4 rounded-sm border-(--primary-200) shadow-md shadow-black/20">

      <div className="flex-1 max-w-sm">

        <h2 className="font-bold text-base ml:text-lg lp:text-2xl text-(--base-text-color)">
          Sugestão de estudo
        </h2>

        <p className="text-sm ml:text-base lp:text-xl font-normal text-(--search-color) mt-1">
          Com base no seu desempenho, você deve focar em:
        </p>

        <p className="text-sm ml:text-base lp:text-xl font-medium text-(--sugestion-tag-color) mt-1">
          {props.conteudoRecomendado} - {props.etapa}
        </p>

      </div>

      <div className="w-full ml:w-auto mt-2 ml:mt-0">

        <Link href="/conteudoRecomendado"
          className="bg-(--sugestion-button-color) text-(--sugestion-button-text-color) flex items-center p-2 px-6 rounded-sm font-bold whitespace-nowrap"
        >
          Ir para conteúdo
        </Link>

      </div>

    </div>
  );
}