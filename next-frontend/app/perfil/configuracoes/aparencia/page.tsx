'use client'

import Header from "@/components/Header";
import Footer from "@/components/Footer";
import Sidebar from "@/components/Sidebar";
import { useTheme } from "next-themes";
import { ConfDiv, ConfH1, ConfH2, ConfP, ConfCard } from "@/components/ConfComponents";
import { Moon, Sun } from "lucide-react";

export default function informacoes_basicas() {

    const {theme, setTheme} = useTheme()

    return (
        <div>
            <Header/>
            <div className="flex">
                <Sidebar/>
                <ConfDiv>
                    <ConfH1>
                        Aparência
                    </ConfH1>
                    <div className="flex flex-col gap-5">
                        <ConfCard>
                            <ConfH2>Temas</ConfH2>
                            <ConfP>A plataforma possui dois temas diferentes: o <b>Modo Claro</b> e o <b>Modo Escuro</b>, você pode escolher o que achar mais agradável.</ConfP>
                        </ConfCard>
                    </div>
                    <ConfH2>
                        Clique no ícone para mudar de tema
                    </ConfH2>
                    <div className="flex flex-col gap-5">
                        <div className="flex justify-between gap-5">
                            <ConfCard tamanho={50}>
                                <div className="flex flex-wrap text-center justify-center gap-4">
                                    <ConfH2>Modo Claro</ConfH2>
                                    <Sun onClick={() => setTheme('light')} className="h-auto w-[35px] md:w-[40px] lg:w-[45px] lp:w-[50px] hover:cursor-pointer" size={50}/>
                                </div>
                            </ConfCard>
                            <ConfCard tamanho={50}>
                                <div className="flex flex-wrap text-center justify-center gap-4">
                                    <ConfH2>Modo Escuro</ConfH2>
                                    <Moon onClick={() => setTheme('dark')} className="h-auto w-[35px] md:w-[40px] lg:w-[45px] lp:w-[50px] hover:cursor-pointer" size={50}/>
                                </div>
                            </ConfCard>
                        </div>
                    </div>
                </ConfDiv>
            </div>
            <Footer/>
        </div>
    )
}