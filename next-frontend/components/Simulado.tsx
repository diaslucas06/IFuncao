'use client'
import Link from "next/link";

export default function Simulado() {
  return (
    <div className="bg-(--sugestion-card-color) flex flex-col lp:flex-row border-l-4 justify-between items-start lp:items-end basis-1/2 gap-2 md:gap-4 p-4 rounded-sm border-(--primary-500) shadow-md shadow-black/20">

      <div className="flex-1">
      
        <h1 className="font-bold text-2xl md:text-start md:text-[28px] lg:text-[32px] lp:text-[40px] text-(--base-text-color)">
          Hora de resolver questões do ENEM
        </h1>

        <h2 className="font-medium text-base md:text-xl lp:text-2xl pc:text-[32px] text-(--search-color) mt-1">
          Treine com exames focados no padrão oficial
        </h2>

      </div>

      <div className="w-full ml:w-auto mt-2 ml:mt-0">

        <Link href={`/simulados`}
          className="bg-(--sugestion-button-color) text-(--sugestion-button-text-color) md:text-xl lp:text-2xl flex items-center p-2 px-4 md:px-6 rounded-sm font-bold whitespace-nowrap"
        >
          Fazer simulado
        </Link>

      </div>

    </div>
  );
}