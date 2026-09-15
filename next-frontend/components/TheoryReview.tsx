"use client";

import Link from "next/link";
import Image from "next/image";
import { NotebookPen } from "lucide-react";

export default function TheoryReview() {
  return (
    <div className="w-full shadow-xl">

      <div className="p-1 rounded-t-lg flex items-center gap-3 bg-(--theory-header-bg) text-(--theory-header-text)">
        <NotebookPen className="text-(--theory-card-text: var(--neutral-900); w-6 h-6 md:w-7 md:h-7 lg:w-8 lg:h-8 lp:w-10 lp:h-10 pc:w-12 pc:h-12 ml-1.5"/>

        <h1 className="text-xl md:text-[28px] lg:text-[32px] pc:text-[40px] font-bold text-center text-(--profile-text-card-color)">
          Revisar a teoria
        </h1>
      </div>

      <div className="p-6 bg-(--theory-card-bg) rounded-b-lg ">

        <p className="font-normal text-base md:text-lg lp:text-2xl  text-left text-(--theory-card-text) whitespace-normal leading-normal">
          Reveja a teoria de Análise Combinatória antes de continuar resolvendo os exercícios.
        </p>

        <Link
          href="/conteudoRecomendados"
          className="text-center bg-(--theory-button-bg) text-(--theory-button-text) rounded-full flex items-center justify-center py-2 font-semibold md:text-xl lp:text-2xl hover:bg-(--primary-800)] transition-colors mt-4"
        >
          Acessar conteúdo
        </Link>

      </div>

    </div>
  );
}