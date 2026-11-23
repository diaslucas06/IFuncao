'use client'

import Header from "@/components/Header";
import HeaderNotLogged from "@/components/HeaderNotLogged";
import Footer from "@/components/Footer";
import { CardBackground } from "@/components/CardProfile";
import CardConteudo from "@/components/CardConteudo";
import ButtonContent from "@/components/ButtonContent";
import { BarraPesquisa } from "@/components/BarraPesquisa";
import { useAuth } from "@/utils/auth";
import { useState } from "react";
import CardHistorico from "@/components/CardHistorico";
import Link from "next/link";

interface Conteudo {
    cont_id: number,
    cont_nome: string,
}

export default function seuprogresso() {
    const [erro, setErro] = useState('')
    const [questoesBuscadas, setQuestoesBuscadas] = useState<Array<Conteudo> | null> (null);
    const { pessoa_logada, carregando } = useAuth()
      
    if (carregando) {
        return null; 
    }

    if (pessoa_logada) {
        return (
            <div className="h-screen">
                <Header/>
                <main className="flex flex-col p-5 md:p-10 gap-10 mb-6">
                    <div className="flex flex-col justify-between gap-5">
                        <div className="flex justify-between items-center">
                            <h1 className="h1_inicio">Questões</h1>
                            <BarraPesquisa setErro={setErro} setConteudosBuscados={setQuestoesBuscadas}/>
                        </div>
                        <CardBackground className="w-full bg-(--settings-card-color)">
                            <div className="w-full flex flex-row justify-between gap-2 md:gap-4 grid grid-cols-2 lg:grid-cols-4">
                                <CardConteudo index={0} link="/conteudos/questoes/conteudos/primeiro_ano" linha1="1" linha2="ano"/>
                                <CardConteudo index={1} link="/conteudos/questoes/conteudos/segundo_ano" linha1="2" linha2="ano"/>
                                <CardConteudo index={2} link="/conteudos/questoes/conteudos/terceiro_ano" linha1="3" linha2="ano"/>
                                <CardConteudo index={3} link="/conteudos/questoes/conteudos/enem" linha1="MATEMÁTICA" linha2="ENEM"/>
                            </div>
                        </CardBackground>
                    </div>
                    {questoesBuscadas &&
                        <>
                            <h1 className="h1_inicio">Questões buscadas</h1>
                            <CardBackground className="w-full bg-(--settings-card-color)">
                                <div className="flex flex-wrap gap-3 lg:gap-8 lp:gap-11">
                                    {questoesBuscadas?.map((questao, index) => (
                                        <Link href={`/conteudos/questoes/questao?id=${questao.cont_id}&nome=${encodeURIComponent(questao.cont_nome)}`} key={index} className="basis-1/3 lg:basis-8/26 lp:basis-2/9 pc:basis-3/13">
                                            <CardHistorico nome={questao.cont_nome} index={index}/> 
                                        </Link>
                                    ))}
                                </div>
                            </CardBackground>
                        </>
                    }
                    <ButtonContent link="/conteudos/questoes" text="Acessar a página de conteúdos"/>
                </main>
                    
                <Footer/>
            </div>
        )
    } else {
        return (
            <div className="container">
                <HeaderNotLogged/>
                <main className="flex flex-col p-5 md:p-10 gap-10 mb-6">
                    <div className="flex flex-col justify-between gap-5">
                        <div className="flex justify-between items-center">
                            <h1 className="h1_inicio">Questões</h1>
                            <p>Entre para acessar as questões disponíveis</p>
                        </div>
                        <CardBackground className="w-full bg-(--settings-card-color)">
                            <div className="w-full flex flex-row justify-between gap-2 md:gap-4 grid grid-cols-2 lg:grid-cols-4">
                                <CardConteudo index={0} link="/conteudos/conteudo/primeiro_ano" linha1="1" linha2="ano"/>
                                <CardConteudo index={1} link="/conteudos/conteudo/segundo_ano" linha1="2" linha2="ano"/>
                                <CardConteudo index={2} link="/conteudos/conteudo/terceiro_ano" linha1="3" linha2="ano"/>
                                <CardConteudo index={3} link="/conteudos/conteudo/enem" linha1="MATEMÁTICA" linha2="ENEM"/>
                            </div>
                        </CardBackground>
                    </div>
                    <ButtonContent link="/conteudos/questoes" text="Acessar a página de questões"/>
                </main>          
            </div>
        )
    }
    
}