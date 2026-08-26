'use client'

import Header from "@/components/Header";
import Footer from "@/components/Footer";
import Sidebar from "@/components/Sidebar";
import { ConfDiv, ConfH1, ConfH2, ConfCard, ConfInfoLi } from "@/components/ConfComponents";
import BarraProgresso from "@/components/BarraProgresso";

export default function informacoes_basicas() {

    function media(nota1:number, nota2:number, nota3:number) {
        return ((nota1 + nota2 + nota3) / 3).toFixed(0)
    }

    let notas = {
        "primeiro": 80,
        "segundo": 70,
        "terceiro": 70
    }

    let progresso = {
        'primeiro': 100,
        'segundo': 100,
        'terceiro': 50,
        'Matemática Enem': 0
    }

    return (
        <div>
            <Header/>
            <div className="flex">
                <Sidebar/>
                <ConfDiv>
                    <ConfH1>
                        Seu Progresso
                    </ConfH1>
                    <div className="flex flex-col gap-3">
                        <ConfCard>
                            <ConfH2>Suas notas em matemática por ano letivo</ConfH2>
                            <ul className="flex flex-col gap-2">
                                <ConfInfoLi><b className="font-semibold">1° ano:</b> {notas.primeiro}</ConfInfoLi>
                                <ConfInfoLi><b className="font-semibold">2° ano:</b> {notas.segundo}</ConfInfoLi>
                                <ConfInfoLi><b className="font-semibold">3° ano:</b> {notas.terceiro}</ConfInfoLi>
                                <p className="text-[20px] md:text-[24px] lg:text-[28px] lp:text-[32px] font-poppins-sans"><b>Média total:</b> {media(notas.primeiro, notas.segundo, notas.terceiro)}</p>
                            </ul>
                        </ConfCard>
                        <ConfCard>
                            <ConfH2>Seu progresso por ano</ConfH2>
                            <div>
                                <BarraProgresso ano={1} porcentagem={progresso.primeiro}/>
                                <BarraProgresso ano={2} porcentagem={progresso.segundo}/>
                                <BarraProgresso ano={3} porcentagem={progresso.terceiro}/>
                                <BarraProgresso ano={'Matemática Enem'} porcentagem={progresso["Matemática Enem"]}/>
                            </div>
                        </ConfCard>
                    </div>
                </ConfDiv>
            </div>
            <Footer/>
        </div>
    )
}