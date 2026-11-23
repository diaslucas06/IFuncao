'use client'

import Header from "@/components/Header";
import HeaderNotLogged from "@/components/HeaderNotLogged";
import Footer from "@/components/Footer";
import { CardBackground } from "@/components/CardProfile";
import CardHistorico from "@/components/CardHistorico";
import { BarraPesquisaEtapa } from "@/components/BarraPesquisa";
import { useState } from "react";
import { useAuth } from "@/utils/auth";
import { conteudoEtapa } from "@/utils/conteudoEtapa";

interface Conteudo {
    cont_id: number,
    cont_nome: string,
}

export default function conteudo2ano() {
    const [erro, setErro] = useState("");
    const {pessoa_logada, carregando} = useAuth()
    const [conteudosBuscados, setConteudosBuscados] = useState<Array<Conteudo> | null> (null);

    const conteudos = conteudoEtapa('2', setErro)

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
                            <h1 className="h1_inicio">Conteúdos - 2° ano</h1>
                            <BarraPesquisaEtapa setConteudosBuscados={setConteudosBuscados} setErro={setErro} etapa="1"/>
                        </div>
                        {erro &&
                            <CardBackground className="w-full bg-(--settings-card-color)">
                                <p className="font-bold text-2xl">{erro}</p>
                            </CardBackground>
                        }
                        {conteudosBuscados ? 
                            <CardBackground className="w-full bg-(--settings-card-color)">
                                <div className="flex flex-wrap gap-3 lg:gap-8 lp:gap-11">
                                    {conteudosBuscados?.map((conteudo, index) => (
                                        <div key={index} className="basis-1/3 lg:basis-8/26 lp:basis-2/9 pc:basis-3/13">
                                            <CardHistorico nome={conteudo.cont_nome} index={index}/> 
                                        </div>
                                    ))}
                                </div>
                            </CardBackground>
                            :
                            <>
                                { conteudos ? 
                                    <CardBackground className="w-full bg-(--settings-card-color)">
                                        <div className="flex flex-wrap gap-3 lg:gap-8 lp:gap-11">
                                            {conteudos?.map((conteudo, index) => (
                                                <div key={index} className="basis-1/3 lg:basis-8/26 lp:basis-2/9 pc:basis-3/13">
                                                    <CardHistorico nome={conteudo.cont_nome} index={index}/> 
                                                </div>
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
                    
                {conteudos ?
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
                        <h1 className="h1_inicio">Conteúdos - 2° ano</h1>
                        { conteudos && 
                            <CardBackground className="w-full bg-(--settings-card-color)">
                                <div className="flex flex-wrap gap-3 lg:gap-8 lp:gap-11">
                                    {conteudos?.map((conteudo, index) => (
                                        <div key={index} className="basis-1/3 lg:basis-8/26 lp:basis-2/9 pc:basis-3/13">
                                            <CardHistorico nome={conteudo.cont_nome} index={index}/> 
                                        </div>
                                    ))}
                                </div>
                            </CardBackground>
                        }
                        {erro &&
                            <CardBackground className="w-full bg-(--settings-card-color)">
                                <p className="font-bold text-2xl">{erro}</p>
                            </CardBackground>
                        }
                    </div>
                </main>
                {conteudos ?
                    <Footer/>
                    :
                    <Footer position="fixed"/>
                } 
            </div>
        )
}