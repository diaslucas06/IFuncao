"use client";

import Link from "next/link";
import Image from "next/image";

export default function TheoryReview() {
  return (
    <div className="w-full shadow-xl">

      <div className="p-1 rounded-t-lg flex items-center gap-3 bg-(--theory-header-bg) text-(--theory-header-text)">
        <Image  src="/images/icons/livro.png" alt="Livro" width={50} height={50}
        />

        <h1 className="text-lg ml:text-xl lp:text-2xl font-bold text-center text-(--profile-text-card-color)">
          Revisar a teoria
        </h1>
      </div>

      <div className="p-3 bg-(--theory-card-bg) rounded-b-lg">

        <p className="text-sm ml:text-sm lp:text-base text-left text-(--theory-card-text) whitespace-normal leading-normal">
          Reveja a teoria de Análise Combinatória antes de continuar resolvendo os exercícios.
        </p>

        <Link
          href="/conteudoRecomendados"
          className="w-3/4 text-center bg-(--theory-button-bg) text-(--theory-button-text) rounded-full flex items-center justify-center py-2 font-semibold text-sm hover:bg-[var(--primary-800)] transition-colors mt-3"
        >
          Acessar conteúdo
        </Link>

      </div>

    </div>
  );
}