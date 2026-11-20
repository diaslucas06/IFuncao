'use client'

import Header from "@/components/Header";
import HeaderNotLogged from "@/components/HeaderNotLogged";
import Footer from "@/components/Footer";
import { CardBackground } from "@/components/CardProfile";
import CardHistorico from "@/components/CardHistorico";
import BarraPesquisa from "@/components/BarraPesquisa";
import { useState, useEffect, use } from "react";
import { useAuth } from "@/utils/auth";
import { buscarConteudo } from "@/utils/buscarConteudo";
import { conteudoEtapa } from "@/utils/conteudoEtapa";
import Link from "next/link";

interface Conteudo {
    cont_id: number,
    cont_nome: string,
    cont_porcentagem: number
}

export default function conteudo1ano() {
    const [conteudo, setConteudo] = useState<Conteudo | null>(null);
    const [erro, setErro] = useState("");
    const {pessoa_logada, carregando} = useAuth()

    const conteudos = conteudoEtapa('1', setErro)

    if (carregando) {
        return null;
    }
    
    if (pessoa_logada) {
        return (
            <div className="container">
                <Header/>
                <main className="flex flex-col p-10 gap-10">
                    <div className="flex flex-col justify-between gap-5">
                        <div className="flex flex-col lg:flex-row justify-between items-center">
                            <h1 className="h1_inicio">Questões - 1° ano</h1>
                            <BarraPesquisa setErro={setErro} setConteudo={setConteudo} etapa="1" buscarConteudo={buscarConteudo} />
                        </div>
                        {conteudo ? 
                            <CardBackground className="w-full bg-(--settings-card-color)">
                                <div className="flex flex-wrap gap-3 lg:gap-8 lp:gap-11">
                                    <Link href={`/conteudos/questoes/questao?id=${conteudo.cont_id}&nome=${encodeURIComponent(conteudo.cont_nome)}`}>
                                        <CardHistorico nome={conteudo.cont_nome}  porcentagem={conteudo.cont_porcentagem} index={index}/> 
                                    </Link>
                                </div>
                            </CardBackground>
                            : 
                            <>
                                {erro ? 
                                    <CardBackground className="w-full bg-(--settings-card-color)">
                                        <p className="font-bold text-2xl">{erro}</p>
                                    </CardBackground>
                                    : 
                                    ''
                                }
                                <CardBackground className="w-full bg-(--settings-card-color)">
                                    <div className="flex flex-wrap gap-3 lg:gap-8 lp:gap-11">
                                        {conteudos?.map((conteudo, index) => (
                                            <div key={index} className="basis-1/3 lg:basis-8/26 lp:basis-2/9 pc:basis-3/13">
                                                <Link href={`/conteudos/questoes/questao?id=${conteudo.cont_id}&nome=${encodeURIComponent(conteudo.cont_nome)}`}>
                                                    <CardHistorico nome={conteudo.cont_nome}  porcentagem={conteudo.cont_porcentagem} index={index}/> 
                                                </Link>
                                            </div>
                                        ))}
                                    </div>
                                </CardBackground>
                            </>
                        }
                    </div>
                </main>
                    
                <Footer position="fixed"/>
            </div>
        )
    }
    return (
        <div className="container">
            <HeaderNotLogged/>
            <Footer/>
        </div>
    )
}