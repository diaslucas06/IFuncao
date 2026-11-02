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

interface Conteudo {
    id: number,
    nome: string,
    link: string,
    porcentagem: number
}

export default function conteudo2ano() {
    const [cont_nome, setContNome] = useState("");
    const [conteudo, setConteudo] = useState<Conteudo | null>(null);
    const [erro, setErro] = useState("");
    const {pessoa_logada, carregando} = useAuth()

    const conteudos = conteudoEtapa('2', setErro)

    if (carregando) {
        return null;
    }

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
    
    if (pessoa_logada) {
        return (
            <div className="container">
                <Header/>
                <main className="flex flex-col p-10 gap-10">
                    <div className="flex flex-col justify-between gap-5">
                        <div className="flex flex-col lg:flex-row justify-between items-center">
                            <h1 className="h1_inicio">Conteúdos - 2° ano</h1>
                            <BarraPesquisa cont_nome={cont_nome} setContNome={setContNome} setErro={setErro} setConteudo={setConteudo} etapa="2" buscarConteudo={buscarConteudo} />
                        </div>
                        {conteudo ? 
                            <div key={conteudo.id} className="basis-1/3 lg:basis-8/26 lp:basis-2/9 pc:basis-3/13">
                                <CardHistorico nome={conteudo.nome}  link={conteudo.link}  porcentagem={conteudo.porcentagem} index={0}/> 
                            </div>
                            : 
                            <CardBackground className="w-full bg-(--settings-card-color)">
                                {erro ? <p className="font-bold text-2xl">{erro}</p>: ''}
                                <div className="flex flex-wrap gap-3 lg:gap-8 lp:gap-11">
                                    {conteudos?.map((conteudo, index) => (
                                        <div key={conteudo.id} className="basis-1/3 lg:basis-8/26 lp:basis-2/9 pc:basis-3/13">
                                            <CardHistorico nome={conteudo.nome}  link={conteudo.link}  porcentagem={conteudo.porcentagem} index={index}/> 
                                        </div>
                                    ))}
                                </div>
                            </CardBackground>
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