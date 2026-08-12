'use client'

import { usePathname } from "next/navigation";
import Link from "next/link";
import { LogOut } from "lucide-react";

export default function Sidebar() {

    const nome_do_caminho = usePathname()

    function verificar_caminho(caminho:string) {
        if (nome_do_caminho.includes(caminho)) {
            return true
        } else {
            return false
        }
    }

    return (
       <div className="hidden md:flex flex-col sticky bg-(--side-bar-color) p-5 md:p-7 lg:p-10 lp:p-12"> {/* altura da header (112px) */}
            <h1 className="font-bold md:text-[28px] lg:text-[32px] lp:text-[44px] pc:text-[56px]">Configurações</h1>
            <div className="flex flex-col font-poppins-sans gap-[8px] py-3 md:py-6 md:gap-[12px] lg:py-8 lg:gap-[15px] lp:gap-[20px] lp:py-10">
                <Link href={'/perfil/configuracoes/informacoes_basicas'} className={verificar_caminho('/informacoes_basicas') ? 'md:text-[20px] lg:text-[24px] pc:text-[32px] text-(--side-bar-text-color) font-bold': 'md:text-[20px] lg:text-[24px] pc:text-[32px] hover:font-semibold'}>Informações Básicas</Link>
                <Link href={'/perfil/configuracoes/notificacoes'} className={verificar_caminho('/notificacoes') ? 'md:text-[20px] lg:text-[24px] pc:text-[32px] text-(--side-bar-text-color) font-bold': 'md:text-[20px] lg:text-[24px] pc:text-[32px] hover:font-semibold'}>Notificações</Link>
                <Link href={'/perfil/configuracoes/seguranca'} className={verificar_caminho('/seguranca') ? 'md:text-[20px] lg:text-[24px] pc:text-[32px] text-(--side-bar-text-color) font-bold': 'md:text-[20px] lg:text-[24px] pc:text-[32px] hover:font-semibold'}>Segurança</Link>
                <Link href={'/perfil/configuracoes/aparencia'} className={verificar_caminho('/aparencia') ? 'md:text-[20px] lg:text-[24px] pc:text-[32px] text-(--side-bar-text-color) font-bold': 'md:text-[20px] lg:text-[24px] pc:text-[32px] hover:font-semibold'}>Aparência</Link>
            </div>
            <hr />
            <div className="flex flex-col font-poppins-sans gap-[8px] py-3 md:py-6 md:gap-[12px] lg:py-8 lg:gap-[15px] lp:gap-[20px] lp:py-10">
                <Link href={'/perfil/configuracoes/conta'} className={verificar_caminho('/conta') ? 'md:text-[20px] lg:text-[24px] pc:text-[32px] text-(--side-bar-text-color) font-bold': 'md:text-[20px] lg:text-[24px] pc:text-[32px] hover:font-semibold'}>Conta</Link>
                <Link href={'/perfil/configuracoes/seu_progresso'} className={verificar_caminho('/seu_progresso') ? 'md:text-[20px] lg:text-[24px] pc:text-[32px] text-(--side-bar-text-color) font-bold': 'md:text-[20px] lg:text-[24px] pc:text-[32px] hover:font-semibold'}>Seu Progresso</Link>
                <Link href={'/perfil/configuracoes/seu_progresso'} className="flex items-center gap-3 md:text-[20px] lg:text-[24px] pc:text-[32px] text-(--side-bar-text-color) font-bold hover:font-semibold">
                    Sair
                    <LogOut className="h-auto w-[20px] md:w-[30px] lg:w-[35px]" size={35} strokeWidth={3}/>
                </Link>
            </div>
        </div>
    )
}