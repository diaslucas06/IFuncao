'use client'

import Link from "next/link";
import { usePathname } from 'next/navigation'
import Image from "next/image";

export default function HeaderNotLogged() {
    const nome_do_caminho = usePathname()

    function verificar_caminho(caminho:string) {
        if (caminho === nome_do_caminho) {
            return true
        } else {
            return false
        }
    }

    return (
        <header className="flex justify-between items-center py-5 px-10 bg-(--primary-700)">
            <Image src={'/logo.png'} alt="Logo" width={225} height={65}/>
            <div className="flex justify-between items-center gap-20">
                <Link href={'/'} className={verificar_caminho('/') ? 'text-2xl hover:font-medium bg-white rounded-md px-4 py-2 text-(--primary-700)': 'text-2xl hover:font-medium'}>Início</Link>
                <Link href={'/conteudos'} className={verificar_caminho('/conteudos') ? 'text-2xl hover:font-medium bg-white rounded-md px-4 py-2 text-(--primary-700)': 'text-2xl hover:font-medium'}>Conteúdos</Link>
                <Link href={'/login'} className={verificar_caminho('/login') ? 'text-2xl hover:font-medium bg-white rounded-md px-4 py-2 text-(--primary-700)': 'text-2xl hover:font-medium'}>Login</Link>
                <div className="flex gap-3">
                    <Image src={'/images/icons/icon_darkmode.png'} alt="DarkMode" width={30} height={20}/>
                    <Link href={'/'} className="text-2xl hover:font-medium">Modo Escuro</Link>
                </div>
            </div>
        </header>
    )
}