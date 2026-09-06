'use client'

import HeaderNotLogged from "@/components/HeaderNotLogged";
import Image from "next/image";
import { User, Lock, Eye, EyeOff } from "lucide-react";

export default function login() {
  return (
    <main className="min-h-screen flex flex-col justify-between">
      <HeaderNotLogged />

      <div className="flex flex-col lg:flex-row flex-1 items-center justify-center max-w-7xl mx-auto w-full p-4 ml:px-10 my-auto gap-8 lg:gap-12 pc:gap-16">

        <section className="w-full m-6 max-ml:mt-8 flex flex-col items-center lg:items-start lg:w-1/2 text-center lg:text-left">

          <h1 className="text-lg ml:text-2xl lg:text-3xl font-bold leading-tight">
            Construa sua jornada.
          </h1>

          <p className="text-base ml:text-lg mt-2 max-w-[350px] lg:max-w-[480px]">
            Acesse sua conta e retome seus estudos de onde parou.
          </p>

          <div className="w-full flex justify-center lg:justify-start">
            <Image
              src="/images/illustrations/login-illustration.png" alt="Imagem dos estudantes" width={600} height={600}
              className="w-full h-auto mt-5"
            />
          </div>

        </section>

        <section className="w-full lg:w-1/2 flex items-center justify-center">

          <div className="w-full max-w-[340px] lg:max-w-[360px]">

            <h2 className="text-3xl lg:text-4xl font-extrabold text-center">
              Faça seu <span className="text-(--primary-400)">Login</span>
            </h2>

            <form action="">

              <div className="relative mt-6 lg:mt-8">
                <User
                  size={24}
                  className="text-(--neutral-900) absolute left-3 top-1/2 -translate-y-1/2 pointer-events-none"
                />

                <input type="text" name="matricula" id="matricula" placeholder="Matrícula"
                  className="w-full rounded-lg border bg-(--neutral-0) text-sm ml:text-base py-2.5 pl-11 pr-11 text-(--neutral-500) outline-none"
                />
              </div>

              <div className="relative mt-4">

                <Lock
                  size={24}
                  className="text-(--neutral-900) absolute left-3 top-1/2 -translate-y-1/2 pointer-events-none"
                />

                <input type="password" id="senha" placeholder="Senha"
                  className="w-full rounded-lg border bg-(--neutral-0) text-sm ml:text-base py-2.5 pl-11 pr-11 text-(--neutral-500) outline-none"
                />

                <Eye
                  size={24}
                  className="absolute right-3.5 top-1/2 -translate-y-1/2 text-(--neutral-900) cursor-pointer"
                />

              </div>

              <button type="submit"
                className="w-full bg-(--primary-700) rounded-full py-2.5 flex items-center justify-center text-white text-sm font-medium mt-6"
              >
                Entrar
              </button>

              <div className="flex items-center gap-4 mt-6">
                <hr className="flex-1" />
                <span className="text-sm">Ou</span>
                <hr className="flex-1" />
              </div>

              <div className="flex justify-center">
                <Image src="/images/icons/logoSuap.png" alt="Logo do suap" width={50} height={40}
                  className="mt-4 h-auto w-auto"
                />
              </div>

            </form>

          </div>

        </section>

      </div>
    </main>
  );
}