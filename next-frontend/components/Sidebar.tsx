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
       <div className="sticky top-[112px] h-[calc(100vh-112px)] flex flex-col bg-(--side-bar-color) w-[506px] p-12"> {/* altura da header (112px) */}
            <h1 className="text-[56px] font-bold">Configurações</h1>
            <div className="flex flex-col gap-[20px] font-poppins-sans py-10">
                <Link href={'/perfil/configuracoes/informacoes_basicas'} className={verificar_caminho('/informacoes_basicas') ? 'text-[32px] text-(--side-bar-text-color) font-bold': 'text-[32px] hover:font-semibold'}>Informações Básicas</Link>
                <Link href={'/perfil/configuracoes/notificacoes'} className={verificar_caminho('/notificacoes') ? 'text-[32px] text-(--side-bar-text-color) font-bold': 'text-[32px] hover:font-semibold'}>Notificações</Link>
                <Link href={'/perfil/configuracoes/seguranca'} className={verificar_caminho('/seguranca') ? 'text-[32px] text-(--side-bar-text-color) font-bold': 'text-[32px] hover:font-semibold'}>Segurança</Link>
                <Link href={'/perfil/configuracoes/aparencia'} className={verificar_caminho('/aparencia') ? 'text-[32px] text-(--side-bar-text-color) font-bold': 'text-[32px] hover:font-semibold'}>Aparência</Link>
            </div>
            <hr />
            <div className="flex flex-col gap-[20px] font-poppins-sans py-10">
                <Link href={'/perfil/configuracoes/conta'} className={verificar_caminho('/conta') ? 'text-[32px] text-(--side-bar-text-color) font-bold': 'text-[32px] hover:font-semibold'}>Conta</Link>
                <Link href={'/perfil/configuracoes/seu_progresso'} className={verificar_caminho('/seu_progresso') ? 'text-[32px] text-(--side-bar-text-color) font-bold': 'text-[32px] hover:font-semibold'}>Seu Progresso</Link>
                <Link href={'/perfil/configuracoes/seu_progresso'} className="flex items-center gap-3 text-[32px] font-bold text-(--side-bar-text-color)">
                    Sair
                    <LogOut size={35} strokeWidth={3}/>
                </Link>
            </div>
        </div>
    )
}