'use client'
import HeaderNotLogged from "@/components/HeaderNotLogged";
import Image from "next/image";
import Link from "next/link";
import { User, Lock, Eye } from "lucide-react";

export default function Login() {
  return (
    <main>
      <HeaderNotLogged />

      <div className="flex">
        <section className="w-1/2 p-12 px-10">
          <h1 className="text-2xl font-bold leading-tight mt-10">
            Construa sua jornada.
          </h1>
          <p className="text-xl mt-3 max-w-117.5">
            Acesse sua conta e retome seus estudos de onde parou.
          </p>
          <div>
            <Image src="/images/illustrations/login-illustration.png" alt="Imagem dos estudantes" width={500} height={400}
              className="w-full h-auto max-w-[700px] mt-6"
            />
          </div>
        </section>

        <section className="w-1/2 flex items-center justify-center">
          <div className="w-full max-w-sm">
            <h2 className="text-4xl font-bold text-center">
              Faça seu <span className="text-(--primary-700)">Login</span>
            </h2>

            <form action="">
              <div className="relative mt-4">
                <User size={24}
                  className="text-(--neutral-900) absolute left-3 top-1/2 -translate-y-1/2 "
                />
                <input type="text" name="matricula" id="matricula" placeholder="Matricula"
                  className="w-full rounded-lg border bg-(--neutral-0) py-3 pl-12 pr-3 text-neutral-500"
                />
                <Eye size={24}
                  className="absolute right-3 top-1/2 -translate-y-1/2 text-(--neutral-900)"
                />
              </div>

              <div className="relative mt-4">
                <Lock size={24}
                  className="text-(--neutral-900) absolute left-3 top-1/2 -translate-y-1/2 "
                />
                <input type="password" id="senha" placeholder="senha"
                  className="w-full rounded-lg border bg-(--neutral-0) py-3 pl-12 pr-3 text-neutral-500"/>
              </div>

              <Link href={"/telaInicial"}
                className="w-full bg-(--primary-700) rounded-full py-3 flex items-center justify-center text-white text-sm font-medium mt-4"
              >
                Entrar
              </Link>

              <div className="flex items-center gap-4 mt-4">
                <hr className="flex-1" />
                <span className="text-sm">Ou</span>
                <hr className="flex-1" />
              </div>

              <div className="flex justify-center">
                <Image src={"/images/icons/logoSuap.png"} alt="Logo do suap" width={50} height={40} className="mt-3"/>
              </div>
            </form>
          </div>
        </section>
      </div>
    </main>
  );
}