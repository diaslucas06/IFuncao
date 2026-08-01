'use client'

import Link from "next/link";
import { usePathname } from 'next/navigation'
import Image from "next/image";
import { useTheme } from "next-themes";
import { useEffect, useState } from "react";

export default function HeaderNotLogged() {
    const nome_do_caminho = usePathname()
    const {theme, setTheme} = useTheme()
    const [montada, setMontada] = useState(false)
    
    useEffect(() => {
        setMontada(true)
    }, [])

    function verificar_caminho(caminho:string) {
        if (caminho === nome_do_caminho) {
            return true
        } else {
            return false
        }
    }

    return (
        <header className="flex justify-between items-center py-5 px-10 bg-(--primary-700) text-(--neutral-0)">
            <Image src={'/logo.png'} alt="Logo" width={225} height={65}/>
            <div className="flex justify-between items-center gap-20">
                <Link href={'/'} className={verificar_caminho('/') ? 'text-2xl hover:font-medium bg-white rounded-md px-4 py-2 text-(--primary-700)': 'text-2xl hover:font-medium'}>Início</Link>
                <Link href={'/conteudos'} className={verificar_caminho('/conteudos') ? 'text-2xl hover:font-medium bg-white rounded-md px-4 py-2 text-(--primary-700)': 'text-2xl hover:font-medium'}>Conteúdos</Link>
                <Link href={'/login'} className={verificar_caminho('/login') ? 'text-2xl hover:font-medium bg-white rounded-md px-4 py-2 text-(--primary-700)': 'text-2xl hover:font-medium'}>Login</Link>
                <button className='flex gap-4 items-center' onClick={() => setTheme(theme === 'dark' ? 'light': 'dark')}>
                    {montada ? (
                        <>
                            <Image src={theme === 'dark' ? '/images/icons/icon_darkmode_pressed.png': '/images/icons/icon_darkmode.png'} alt="Tema" width={35} height={35}/>
                            <p className="text-2xl hover:font-medium">
                                {theme === 'dark' ? 'Modo Escuro': 'Modo Claro'}
                            </p>
                        </>
                    ) : (
                        <div></div>
                    )}
                </button>
            </div>
        </header>
    )
}