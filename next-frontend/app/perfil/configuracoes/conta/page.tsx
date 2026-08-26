'use client'

import Link from "next/link";
import Header from "@/components/Header";
import Footer from "@/components/Footer";
import Sidebar from "@/components/Sidebar";
import { useState } from "react";
import { ConfDiv, ConfH1, ConfH2, ConfCard, ConfInfoLi } from "@/components/ConfComponents";
import MenuConf from "@/components/MenuConf";
import { EllipsisVertical, ChevronUp } from "lucide-react";

export default function informacoes_basicas() {
    const [menuAberto, setMenuAberto] = useState(false)

    let dados = {
        'nome': 'Maria José dos Santos',
        'matricula': 20241101110000,
        'email': 'maria.jose@escolar.ifrn.edu.br',
        'ano_letivo': 3,
        'curso': 'Informática para Internet',
        'idade': 18,
        'media': 80
    }

    return (
        <div>
            <Header/>
            <div className="flex h-full">
                <Sidebar/>
                <ConfDiv>
                    <div className="flex items-center gap-3">
                        <div className="flex md:hidden" onClick={() => setMenuAberto(!menuAberto)}>
                            {menuAberto ? <ChevronUp/>: <EllipsisVertical/>}
                        </div>
                        <ConfH1>
                            Conta
                        </ConfH1>
                    </div>
                    {menuAberto && (
                        <MenuConf/>
                    )}
                    <div className="flex flex-col gap-3">
                        <ConfCard>
                            <ConfH2>Informações Pessoais</ConfH2>
                            <ul className="flex flex-col gap-2">
                                <ConfInfoLi><b className="font-semibold">Nome completo:</b> {dados.nome}</ConfInfoLi>
                                <ConfInfoLi><b className="font-semibold">Matrícula:</b> {dados.matricula}</ConfInfoLi>
                                <ConfInfoLi><b className="font-semibold">E-mail:</b> {dados.email}</ConfInfoLi>
                                <ConfInfoLi><b className="font-semibold">Ano letivo:</b> {dados.ano_letivo}° ano</ConfInfoLi>
                                <ConfInfoLi><b className="font-semibold">Curso:</b> {dados.curso}</ConfInfoLi>
                            </ul>
                        </ConfCard>
                        <ConfCard>
                            <ConfH2>Opções</ConfH2>
                            <div className="flex flex-col gap-2">
                                <Link className="font-poppins-sans font-semibold md:text-[20px] lp:text-[24px] underline text-(--link-color)" href={''}>Desconectar do SUAP</Link>
                                <Link className="font-poppins-sans font-semibold md:text-[20px] lp:text-[24px] underline text-(--link-color)" href={''}>Sair do IFunção</Link>
                                <Link className="font-poppins-sans font-semibold md:text-[20px] lp:text-[24px] underline text-(--link-color)" href={''}>Apagar histórico de conteúdos vistos</Link>
                            </div>
                        </ConfCard>
                    </div>
                </ConfDiv>
            </div>
            <Footer/>
        </div>
    )
}