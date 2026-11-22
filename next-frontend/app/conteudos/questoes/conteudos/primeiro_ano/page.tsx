'use client'

import Header from "@/components/Header";
import HeaderNotLogged from "@/components/HeaderNotLogged";
import Footer from "@/components/Footer";
import { CardBackground } from "@/components/CardProfile";
import CardHistorico from "@/components/CardHistorico";
import BarraPesquisa from "@/components/BarraPesquisa";
import { useState } from "react";
import { useAuth } from "@/utils/auth";
import { conteudoEtapa } from "@/utils/conteudoEtapa";
import Link from "next/link";

interface Conteudo {
    cont_id: number,
    cont_nome: string,
}

export default function conteudo1ano() {
    const [erro, setErro] = useState("");
    const {pessoa_logada, carregando} = useAuth()
    const [questoesBuscadas, setQuestoesBuscadas] = useState<Array<Conteudo> | null> (null);

    const questoes = conteudoEtapa('1', setErro)

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
                            <BarraPesquisa setConteudosBuscados={setQuestoesBuscadas} setErro={setErro} etapa="1"/>
                        </div>
                        {erro &&
                            <CardBackground className="w-full bg-(--settings-card-color)">
                                <p className="font-bold text-2xl">{erro}</p>
                            </CardBackground>
                        }
                        {questoesBuscadas ? 
                            <CardBackground className="w-full bg-(--settings-card-color)">
                                <div className="flex flex-wrap gap-3 lg:gap-8 lp:gap-11">
                                    {questoesBuscadas?.map((conteudo, index) => (
                                        <div key={index} className="basis-1/3 lg:basis-8/26 lp:basis-2/9 pc:basis-3/13">
                                            <CardHistorico nome={conteudo.cont_nome} index={index}/> 
                                        </div>
                                    ))}
                                </div>
                            </CardBackground>
                            :
                            <>
                                { questoes ? 
                                    <CardBackground className="w-full bg-(--settings-card-color)">
                                        <div className="flex flex-wrap gap-3 lg:gap-8 lp:gap-11">
                                            {questoes?.map((questao, index) => (
                                                <Link href={`/conteudos/questoes/questao?id=${questao.cont_id}&nome=${encodeURIComponent(questao.cont_nome)}`} key={index} className="basis-1/3 lg:basis-8/26 lp:basis-2/9 pc:basis-3/13">
                                                    <CardHistorico nome={questao.cont_nome} index={index}/> 
                                                </Link>
                                            ))}
                                        </div>
                                    </CardBackground>
                                    :
                                    ''
                                }
                                
                            </>
                        }
                        
                    </div>
                </main>
                    
                {questoes ?
                    <Footer/>
                    :
                    <Footer position="fixed"/>
                }
                                
            </div>
        )
    }
    return (
        <div className="container">
            <HeaderNotLogged/>
            <main className="flex flex-col p-10 gap-10">
                <div className="flex flex-col justify-between gap-5">
                    <h1 className="h1_inicio">Questões - 1° ano</h1>
                    <CardBackground className="w-full bg-(--settings-card-color)">
                        <div className="flex flex-wrap gap-3 lg:gap-8 lp:gap-11">
                            {questoes?.map((questao, index) => (
                                <div className="basis-1/3 lg:basis-8/26 lp:basis-2/9 pc:basis-3/13">
                                    <CardHistorico nome={questao.cont_nome} index={index}/> 
                                </div>
                            ))}
                        </div>
                    </CardBackground>
                </div>
            </main>
            {questoes ?
                <Footer/>
                :
                <Footer position="fixed"/>
            }
                            
        </div>
    )
}