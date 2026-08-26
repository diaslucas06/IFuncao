'use client'
import HeaderNotLogged from "@/components/HeaderNotLogged";
import Header from "@/components/Header";
import Footer from "@/components/Footer";
import Link from "next/link";
import Image from "next/image";
import CardHistorico from "@/components/CardHistorico";
import { CardBackground } from "@/components/CardProfile";
import { ChevronLeft, ChevronRight } from "lucide-react";
import { useState } from "react";

let pessoa_logada = true;

export default function Inicio() {

  if (pessoa_logada) {

    const [inicioIndex, setInicioIndex] = useState(0)
    const [conteudos_por_pagina, setConteudosPorPagina] = useState(4)

    let historico = [
        {'id': 1, 'nome': 'MATEMÁTICA BÁSICA', 'link': '/conteudos/matematica_basica', 'porcentagem': 50},
        {'id': 2, 'nome': 'TRIGONOMETRIA', 'link': '/conteudos/matematica_basica', 'porcentagem': 0},
        {'id': 3, 'nome': 'GEOMETRIA', 'link': '/conteudos/matematica_basica', 'porcentagem': 80},
        {'id': 4, 'nome': 'PROGRESSÃO ARITMÉTICA', 'link': '/conteudos/matematica_basica', 'porcentagem': 100},
        {'id': 5, 'nome': 'MATEMÁTICA FINANCEIRA', 'link': '/conteudos/matematica_basica', 'porcentagem': 40},
        {'id': 6, 'nome': 'MATRIZ', 'link': '/conteudos/matematica_basica', 'porcentagem': 100},
        {'id': 7, 'nome': 'PROGRESSÃO GEOMÉTRICA', 'link': '/conteudos/matematica_basica', 'porcentagem': 20},
        {'id': 8, 'nome': 'DIVISÃO', 'link': '/conteudos/matematica_basica', 'porcentagem': 100},
        {'id': 9, 'nome': 'PROGRESSÃO GEOMÉTRICA', 'link': '/conteudos/matematica_basica', 'porcentagem': 20},
        {'id': 10, 'nome': 'DIVISÃO', 'link': '/conteudos/matematica_basica', 'porcentagem': 100},
        {'id': 11, 'nome': 'PROGRESSÃO GEOMÉTRICA', 'link': '/conteudos/matematica_basica', 'porcentagem': 20},
    ]

    function proximaPagina() {
        if (inicioIndex + conteudos_por_pagina <= historico.length) {
            setInicioIndex(inicioIndex + conteudos_por_pagina)
        }
    }

    function paginaAnterior() {
        if (inicioIndex - conteudos_por_pagina >= 0) {
            setInicioIndex(inicioIndex - conteudos_por_pagina)
        }
    }

    // pega os 4 conteudos que devem ser dessa pagina
    const conteudosExibidos = historico.slice(inicioIndex, inicioIndex + conteudos_por_pagina)

    return (
      <div>
        <Header/>
        <main className="flex flex-col p-10 pt-20 gap-20">
          <div className="flex gap-15 bg-(--primary-700) py-10 px-20 rounded-4xl">
            <Image src={'/logo.png'} alt="Logo" width={520} height={145}/>
            <p className="font-poppins-sans text-[32px] font-semibold text-white">Sua plataforma de estudos para Matemática do Ensino Médio Técnico Integrado do Instituto Federal do Rio Grande do Norte e para o ENEM. Acesse conteúdos, slides, questões e acompanhe sua evolução na disciplina.</p>
          </div>
          <div className="flex flex-col justify-between gap-5">
            <h1 className="text-[64px] font-bold">Sua Evolução</h1>
            <CardBackground className="w-full gap-[20px] bg-(--settings-card-color)">
              <div className="flex flex-col gap-2 flex-wrap items-center justify-around w-full ml:flex-row ml:gap-0">
                  {conteudosExibidos.map((conteudo, index) => (
                      <CardHistorico key={conteudo.id} nome={conteudo.nome}  link={conteudo.link}  porcentagem={conteudo.porcentagem} index={index}/>
                  ))}
              </div>
            </CardBackground>
          </div>
          <div className="flex flex-col justify-between gap-5">
            <h1 className="text-[64px] font-bold">Sugestões com base no seu desempenho</h1>
            <div className="flex flex-col gap-2 flex-wrap items-center justify-around w-full ml:flex-row ml:gap-0">
                {conteudosExibidos.map((conteudo, index) => (
                    <CardHistorico key={conteudo.id} nome={conteudo.nome}  link={conteudo.link}  porcentagem={conteudo.porcentagem} index={index}/>
                ))}
            </div>
          </div>
          <div className="flex flex-col justify-between gap-5">
            <h1 className="text-[64px] font-bold">Histórico de conteúdos acessados</h1>
            <CardBackground className="w-full gap-[20px] bg-(--settings-card-color)">
                <div className="flex items-center w-full">
                    <button onClick={() => paginaAnterior()} disabled={inicioIndex === 0} className="disabled:opacity-30 transition-opacity">
                        <ChevronLeft className='hidden hover:cursor-pointer w-[20px] ml:flex ml:w-[25px] lg:w-[40px]' size={40} color="var(--arrow-color)"/>
                    </button>
                    <div className="flex flex-col gap-2 flex-wrap items-center justify-around w-full ml:flex-row ml:gap-0">
                        {conteudosExibidos.map((conteudo, index) => (
                            <CardHistorico key={conteudo.id} nome={conteudo.nome}  link={conteudo.link}  porcentagem={conteudo.porcentagem} index={index}/>
                        ))}
                    </div>
                    <button onClick={() => proximaPagina()} disabled={inicioIndex + conteudos_por_pagina > historico.length} className="disabled:opacity-30 transition-opacity">
                        <ChevronRight className='hidden hover:cursor-pointer w-[20px] ml:flex ml:w-[25px] lg:w-[40px]' size={40} color="var(--arrow-color)"/>
                    </button>
                  </div>
            </CardBackground>
          </div>
          <div className="flex gap-15 bg-(--primary-700) py-10 px-20 rounded-4xl">
            <Image src={'/images/illustrations/olimpiadas.png'} alt="Logo" width={520} height={145}/>
            <p className="font-poppins-sans text-[32px] font-semibold text-white">As olimpíadas de Matemática nacionais são ótimas formas de se incentivar a estudar e praticar a matéria, oferecendo inúmeros benefícios que vão muito além da competição, impactando a vida acadêmica e pessoal dos estudante. As olimpíadas nacionais de matemática são:</p>
          </div>
          <div className="flex justify-around items-start">
            <div className="flex flex-col text-center w-1/4 justify-center items-center gap-10">
              <a href="https://www.obmep.org.br/" className="bg-(--primary-800) rounded-full p-5 w-fit aspect-square">
                <Image src={'/images/illustrations/olimpiadas/obmep.png'} alt="Logo" width={320} height={320}/>
              </a>
              <div>
                <h4 className="text-[40px] font-bold">OBMEP</h4>
                <p className="text-[32px] font-medium">Olimpíada Brasileira de Matemática das Escolas Públicas</p>
              </div>
            </div>
            <div className="flex flex-col text-center w-1/4 justify-center items-center gap-10">
              <a href="https://www.cangurudematematicabrasil.com.br/" className="flex bg-(--primary-800) rounded-full p-5 w-fit aspect-square items-center">
                <Image src={'/images/illustrations/olimpiadas/canguru.png'} alt="Logo" width={320} height={320}/>
              </a>
              <div>
                <h4 className="text-[40px] font-bold">CANGURU</h4>
                <p className="text-[32px] font-medium">Canguru de matemática Brasil.</p>
              </div>
            </div>
            <div className="flex flex-col text-center w-1/4 justify-center items-center gap-10">
              <a href="https://www.obm.org.br/" className="bg-(--primary-800) rounded-full p-5 w-fit">
                <Image src={'/images/illustrations/olimpiadas/obm.png'} alt="Logo" width={320} height={320}/>
              </a>
              <div>
                <h4 className="text-[40px] font-bold">OBM</h4>
                <p className="text-[32px] font-medium">Olimpíada Brasileira de Matemática</p>
              </div>
            </div>
          </div>
        </main>
        <Footer/>
      </div>
    )
  } else {
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
}
