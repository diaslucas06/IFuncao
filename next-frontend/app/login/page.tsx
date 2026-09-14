'use client'

import HeaderNotLogged from "@/components/HeaderNotLogged";
import Image from "next/image";
import { User, Lock, Eye, EyeOff } from "lucide-react";

export default function login() {
  return (
    <main className="min-h-screen flex flex-col justify-between">
      <HeaderNotLogged />

      <div className="flex flex-col lg:flex-row flex-1 items-center justify-center mx-auto w-full p-4 ml:px-10 my-auto gap-8 lg:gap-12 pc:gap-16">

        <section className="w-full m-6 max-ml:mt-8 flex flex-col items-center lg:items-start lg:w-1/2 text-center lg:text-left">

          <h1 className="text-[24px] md:text-[32px] lg:text-[36px] font-bold leading-tight">
            Construa sua jornada.
          </h1>

          <p className="font-normal texlg:text-[18px] lp:text-[24px] pc:text-[32px] mt-2">
            Acesse sua conta e retome seus estudos de onde parou.
          </p>

          <div className="w-full flex justify-center lg:justify-start">
            <Image
              src="/images/illustrations/login-illustration.png" alt="Imagem dos estudantes" width={600} height={600}
              className="w-full h-auto mt-5"
            />
          </div>

        </section>

        <section className="w-full g:w-1/2 flex items-center justify-center">

          <div className="w-full lg:max-w-1/2">

            <h2 className="text-[28px] md:text-[40px] lg:text-[48px] lp:text-[56px] pc:text-[64px] font-extrabold text-center">
              Faça seu <span className="text-(--primary-400)">Login</span>
            </h2>

            <form action="">

              <div className="relative mt-6 lg:mt-8">
                <User
                  size={24}
                  className="text-(--neutral-900) absolute left-3 top-1/2 -translate-y-1/2 pointer-events-none"
                />

                <input type="text" name="matricula" id="matricula" placeholder="Matrícula"
                  className="w-full rounded-lg border bg-(--neutral-0) md:text-[16px] lp:text-[20px]  py-2.5 pl-11 pr-11 text-(--neutral-500) outline-none"
                />
              </div>

              <div className="relative mt-4">

                <Lock
                  size={24}
                  className="text-(--neutral-900) absolute left-3 top-1/2 -translate-y-1/2 pointer-events-none"
                />

                <input type="password" id="senha" placeholder="Senha"
                  className="w-full rounded-lg border bg-(--neutral-0) md:text-[16px] lp:text-[20px] py-2.5 pl-11 pr-11 text-(--neutral-500) outline-none"
                />

                <Eye
                  size={24}
                  className="absolute right-3.5 top-1/2 -translate-y-1/2 text-(--neutral-900) cursor-pointer"
                />

              </div>

              <button type="submit" 
                className="w-full bg-(--primary-700) rounded-full md:text-[20px] lp:text-[24px] py-2.5 flex items-center justify-center text-white text-sm font-medium mt-6"
              >
                Entrar
              </button>

              <div className="flex items-center gap-4 mt-6">
                <hr className="flex-1" />
                <span className="md:text-[20px] lp:text-[24px]">Ou</span>
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