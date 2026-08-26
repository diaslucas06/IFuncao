'use client'

import Header from "@/components/Header";
import Footer from "@/components/Footer";
import Sidebar from "@/components/Sidebar";
import { ConfDiv, ConfH1, ConfH2, ConfP, ConfCard, ConfLi, ConfNotificacoesText } from "@/components/ConfComponents";
import { ToggleLeft, ToggleRight } from "lucide-react";

import { useState } from "react";

export default function informacoes_basicas() {

    const [ToogleNot, setToogleNot] = useState(false)
    const [ToogleNotProg, setToogleNotProg] = useState(false)
    const [ToogleNotLemb, setToogleNotLemb] = useState(false)

    return (
        <div>
            <Header/>
            <div className="flex h-dvh">
                <Sidebar/>
                <ConfDiv>
                    <ConfH1>
                        Notificações
                    </ConfH1>
                    <div className="flex flex-col gap-3">
                        <ConfCard>
                            <div className="flex gap-2 md:gap-5 items-center">
                                <button className="hover:cursor-pointer" onClick={() => setToogleNot(!ToogleNot)}>
                                    {ToogleNot ? <ToggleRight className="h-auto w-[40px] lg:w-[50px]" size={50} color={'var(--base-text-color)'}/>: <ToggleLeft className="h-auto w-[40px] lg:w-[50px]" size={50} color={'var(--base-text-color)'}/>}
                                </button>
                                <ConfNotificacoesText>Notificações ativas</ConfNotificacoesText>
                            </div>
                            <div className="flex gap-2 md:gap-5 items-center">
                                <button className="hover:cursor-pointer" onClick={() => setToogleNotProg(!ToogleNotProg)}>
                                    {ToogleNotProg ? <ToggleRight className="h-auto w-[40px] lg:w-[50px]" size={50} color={'var(--base-text-color)'}/>: <ToggleLeft className="h-auto w-[40px] lg:w-[50px]" size={50} color={'var(--base-text-color)'}/>}
                                </button>
                                <ConfNotificacoesText>Notificar progresso</ConfNotificacoesText>
                            </div>
                            <div className="flex gap-2 md:gap-5 items-center">
                                <button className="hover:cursor-pointer" onClick={() => setToogleNotLemb(!ToogleNotLemb)}>
                                    {ToogleNotLemb ? <ToggleRight className="h-auto w-[40px] lg:w-[50px]" size={50} color={'var(--base-text-color)'}/>: <ToggleLeft className="h-auto w-[40px] lg:w-[50px]" size={50} color={'var(--base-text-color)'}/>}
                                </button>
                                <ConfNotificacoesText>Notificar lembretes para ofensiva</ConfNotificacoesText>
                            </div>
                        </ConfCard>
                    </div>
                    <ConfH1>
                        Suas notificações
                    </ConfH1>
                    <div className="flex flex-col gap-3">
                        <ConfCard>
                            <ConfH2>Continue sua ofensiva!</ConfH2>
                            <ConfP>Você já tem 23 dias de ofensiva! Acesse o site e estude por alguns minutos para continuar não perder seus dias.</ConfP>
                        </ConfCard>
                    </div>
                </ConfDiv>
            </div>
            <Footer/>
        </div>
    )
}