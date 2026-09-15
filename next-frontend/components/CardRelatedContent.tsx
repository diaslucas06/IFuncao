"use client";

import { BookMarked } from "lucide-react";
import Link from "next/link";

type Relacionado = {
  id: number;
  titulo: string;
};

type Conteudo = {
  id: number;
  relacionados: Relacionado[];
};

type ListaRelacionadosProps = {
  conteudo: Conteudo;
};

export default function CardRelatedContent({
  conteudo,
}: ListaRelacionadosProps) {
  return (
    <div className="w-full bg-(--opacity-background-color) rounded-md p-2">

      <div className="flex items-center justify-start gap-1 mt-1.5">
        <BookMarked className="ml-1 w-6 h-6 md:w-7 md:h-7 lg:w-8 lg:h-8 lp:w-10 lp:h-10 pc:w-12 pc:h-12 shrink-0" />

        <h1 className="text-left ml-0.5 text-base md:text-2xl lg:text-[28px] pc:text-4xl pc:text-center font-bold px-2">
          Conteúdos Relacionados
        </h1>
      </div>

      <ul>
        {conteudo.relacionados.map((item) => (
          <li
            key={item.id}
            className="font-normal text-base md:text-lg lp:text-2xl  mx-1.5 my-2.5 hover:text-(--primary-500)"
          >
            <hr className="my-2.5 w-full" />

            <Link href={`/resumos/${item.id}`}>
              {item.titulo}
            </Link>
          </li>
        ))}
      </ul>

    </div>
  );
}