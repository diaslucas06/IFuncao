'use client'
import HeaderNotLogged from "@/components/HeaderNotLogged";
import Link from "next/link";
import Image from "next/image";

export default function Inicio() {
  return (
    <section>
      <HeaderNotLogged />
      <div className="flex w-full min-h-screen">
        <div className="w-1/2 p-12 bg-(--primary-900) text-(--neutral-0)">
          <h1 className="text-3xl font-bold leading-tight mt-10">
            Domine a Matemática do Ensino Médio ao ENEM.
          </h1>
          <p className="mt-3">
            No IFunção, você simplifica o que parece complexo. Acesse conteúdos
            completos do 1º ao 3º ano e conquiste a base necessária para
            gabaritar as provas mais difíceis.
          </p>
          <Link
            href={"/login"}
            className=" text-md w-[235px] h-[50px] bg-(--primary-700) rounded-2xl flex items-center justify-center mt-3"
          >
            Acessar Conteúdos
          </Link>
        </div>
        <div className=" flex items-center justify-center p-10">
          <Image src="/images/illustrations/home-illustration.png" alt="Imagem dos estudantes" width={600} height={500}
          />
        </div>
      </div>
    </section>
  );
}
