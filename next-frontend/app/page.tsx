'use client'
import HeaderNotLogged from "@/components/HeaderNotLogged";
import Header from "@/components/Header";
import Footer from "@/components/Footer";
import Link from "next/link";
import Image from "next/image";
import CardHistorico from "@/components/CardHistorico";
import { CardBackground } from "@/components/CardProfile";
import { BookOpen, CircleCheckBig, Target, Flame } from "lucide-react";
import CardStatus from "@/components/CardStatus";
import { useState } from "react";
import StudySuggestion from "@/components/StudySuggestion";
import { Carousel, CarouselContent, CarouselItem, CarouselNext, CarouselPrevious } from "@/components/ui/carousel";

let pessoa_logada = true;

export default function Inicio() {
  const dadosProgresso = {
    assuntosConcluidos: 3,
    totalAssuntos: 30,
    questoesRespondidas: 120,
    totalAcertos: 89,
    ofensiva: 10,
    conteudoRecomendado: "Análise Combinatória",
    etapa: 1,
  };

  if (pessoa_logada) {

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

    return (
      <div>
        <Header/>
        <main className="flex flex-col p-10 pt-20 gap-10">
          <div className="flex items-center gap-15 bg-(--primary-700) py-10 px-20 rounded-4xl">
            <Image src={'/logo.png'} alt="Logo" width={600} height={520}/>
            <p className="font-poppins-sans text-[32px] font-semibold text-white">Sua plataforma de estudos para Matemática do Ensino Médio Técnico Integrado do Instituto Federal do Rio Grande do Norte e para o ENEM. Acesse conteúdos, slides, questões e acompanhe sua evolução na disciplina.</p>
          </div>
          <div className="flex flex-col justify-between gap-5">
            <h1 className="text-[64px] font-bold">Sua Evolução</h1>
            <CardBackground className="w-full flex flex-row justify-between gap-4 bg-(--settings-card-color) grid grid-cols-2 lp:grid-cols-4">
              <CardStatus
                titulo="Assuntos concluídos" valor={`${dadosProgresso.assuntosConcluidos}/${dadosProgresso.totalAssuntos}`} icone={BookOpen} bgColor="bg-(--neutral-0)"
                textColor="text-(--neutral-900)" iconeColor="text-(--primary-300)"
              />

              <CardStatus
                titulo="Questões respondidas" valor={String(dadosProgresso.questoesRespondidas)} icone={CircleCheckBig} bgColor="bg-(--primary-800)"
                textColor="text-(--neutral-0)" iconeColor="text-(--neutral-0)"
              />
              
              <CardStatus
                titulo="Total de acertos" valor={`${dadosProgresso.totalAcertos}%`} icone={Target} bgColor="bg-(--primary-300)"
                textColor="text-(--neutral-0)" iconeColor="text-(--neutral-0)"
              />

              <CardStatus titulo="Ofensiva" valor={String(dadosProgresso.ofensiva)} icone={Flame} bgColor="bg-(--primary-200)" textColor="text-(--neutral-0)"
                iconeColor="text-(--neutral-0)" descricao="dias"
              />
            </CardBackground>
          </div>
          <div className="flex flex-col justify-between gap-5">
            <h1 className="text-[64px] font-bold">Sugestões com base no seu desempenho</h1>
            <div className="flex justify-between gap-5">
              <StudySuggestion
                conteudoRecomendado={dadosProgresso.conteudoRecomendado}
                etapa={dadosProgresso.etapa}
              />
              <StudySuggestion
                conteudoRecomendado={dadosProgresso.conteudoRecomendado}
                etapa={dadosProgresso.etapa}
              />
            </div>
          </div>
          <div className="flex flex-col justify-between gap-5">
            <h1 className="text-[64px] font-bold">Histórico de conteúdos acessados</h1>
            <CardBackground className="w-full gap-[20px] bg-(--settings-card-color)">
                <div className="flex items-center w-full">
                  <div className="flex items-center w-full px-10">
                      <Carousel opts={{
                              align: "start",
                              slidesToScroll: 1,
                          }} 
                          className="flex flex-col flex-wrap items-center justify-between w-full ml:flex-row">
                          <CarouselContent className="flex-col ml:flex-row">
                              {historico.map((conteudo, index) => (
                                  <CarouselItem className="basis-1/2 lg:basis-1/3 lp:basis-1/4" key={conteudo.id}>
                                      <CardHistorico nome={conteudo.nome}  link={conteudo.link}  porcentagem={conteudo.porcentagem} index={index}/>
                                  </CarouselItem>
                              ))}
                          </CarouselContent>
                          <CarouselPrevious />
                          <CarouselNext />
                      </Carousel>
                    </div>
                  </div>
            </CardBackground>
          </div>
          <div className="flex items-center gap-15 bg-(--primary-700) py-10 px-20 rounded-4xl">
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
      <div>
        <HeaderNotLogged />
        <main className="w-full max-w-[1920px] mx-auto flex min-h-[calc(100vh-72px)] flex-col lg:flex-row">

        <section className="w-full lp:w-1/2 bg-(--primary-800) text-(--neutral-0) flex flex-col justify-start items-start px-6 ml:px-12 pt-16 lp:pt-[140px]">

          <div className="w-full ml:max-w-lg lp:max-w-[650px] mb-5">

            <h1 className="text-2xl ml:text-3xl lp:text-4xl font-bold leading-[1.2]">
              Domine a Matemática do Ensino Médio ao ENEM.
            </h1>

            <p className="mt-4 lp:mt-6 text-sm leading-relaxed ml:text-base lp:text-7 lp:leading-[1.5] pc:text-[28px]">
              No IFunção, você simplifica o que parece complexo. Acesse conteúdos
              completos do 1º ao 3º ano e conquiste a base necessária para
              gabaritar as provas mais difíceis.
            </p>

            <Link
              href="/login"
              className="flex items-center justify-center w-3/4 ml:w-1/2 lp:w-64 h-9 ml:h-10 mt-6 bg-(--primary-700) hover:bg-(--primary-500) text-sm lp:text-base font-medium rounded-3xl"
            >
              Acessar Conteúdos
            </Link>

          </div>

        </section>

        <div className="w-full lp:w-1/2 flex items-center justify-center p-6 pc:p-12">
          <Image
            src="/images/illustrations/home-illustration.png" alt="Imagem dos estudantes" width={900} height={750}
            className="h-auto w-full max-w-xl object-contain"
          />
        </div>

      </main>
      </div>
    );
  }
}
