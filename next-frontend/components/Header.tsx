'use client'

import Link from "next/link";
import { usePathname } from 'next/navigation'
import Image from "next/image";

export default function Header() {
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
                <Link href={'/inicio'} className={verificar_caminho('/inicio') ? 'text-2xl hover:font-medium bg-white rounded-md px-4 py-2 text-(--primary-700)': 'text-2xl hover:font-medium'}>Início</Link>
                <Link href={'/conteudos'} className={verificar_caminho('/conteudos') ? 'text-2xl hover:font-medium bg-white rounded-md px-4 py-2 text-(--primary-700)': 'text-2xl hover:font-medium'}>Conteúdos</Link>
                <div className={verificar_caminho('/seuprogresso') ? 'flex gap-4 bg-white rounded-md px-4 py-2 text-(--primary-700) items-center': 'flex gap-4 items-center'}>
                    <Image src={verificar_caminho('/seuprogresso') ? '/images/icons/trophy_green.png': '/images/icons/trophy_white.png'} alt="Logo" width={30} height={15}/>
                    <Link href={'/seuprogresso'} className="text-2xl hover:font-medium">Seu Progresso</Link>
                </div>
                <div className='flex gap-4 items-center'>
                    <Image src={'/images/icons/icon_darkmode.png'} alt="Logo" width={35} height={15}/>
                    <Link href={'/'} className="text-2xl hover:font-medium">Modo Escuro</Link>
                </div>
                <div className={verificar_caminho('/perfil') ? 'flex gap-4 bg-white rounded-md rounded-s-4xl  pr-4 text-(--primary-700) items-center': 'flex gap-4 items-center'}>
                    <Image className={verificar_caminho('/perfil') ? 'w-[50px] h-[50px]': ''} src={'/images/icons/user.png'} alt="Logo" width={40} height={35}/>
                    <Link href={'/perfil'} className="text-2xl hover:font-medium">Seu Perfil</Link>
                </div>
            </div>
        </header>
    )
}