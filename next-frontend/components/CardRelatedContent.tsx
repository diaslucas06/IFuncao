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
        <BookMarked className="w-6 h-6 ml-1.5 lg:w-7 lg:h-7 shrink-0" />

        <h1 className="text-lg md:text-xl lg:text-xl font-bold px-2">
          Conteúdos Relacionados
        </h1>
      </div>

      <ul>
        {conteudo.relacionados.map((item) => (
          <li
            key={item.id}
            className="text-base md:text-lg lg:text-lg mx-1.5 my-2.5 hover:text-(--primary-500)"
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