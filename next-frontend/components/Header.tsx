'use client'

import Link from "next/link";
import { usePathname } from 'next/navigation'
import Image from "next/image";
import { useTheme } from "next-themes";
import { useState, useEffect } from "react";
import { Moon, Sun, Trophy } from 'lucide-react';

export default function Header() {
    const nome_do_caminho = usePathname()
    const {theme, setTheme} = useTheme()
    // montada serve para renderizar a página primeiro e depois definir os icones com base na preferencia de tema
    const [montada, setMontada] = useState(false)
    const [menuAberto, setMenuAberto] = useState(false)

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
                <Link href={'/inicio'} className={verificar_caminho('/inicio') ? 'text-2xl hover:font-medium bg-white rounded-md px-4 py-2 text-(--primary-700)': 'text-2xl hover:font-medium'}>Início</Link>
                <Link href={'/conteudos'} className={verificar_caminho('/conteudos') ? 'text-2xl hover:font-medium bg-white rounded-md px-4 py-2 text-(--primary-700)': 'text-2xl hover:font-medium'}>Conteúdos</Link>
                <div className={verificar_caminho('/seuprogresso') ? 'flex gap-4 bg-white rounded-md px-4 py-2 text-(--primary-700) items-center': 'flex gap-4 items-center'}>
                    {verificar_caminho('/seuprogresso') ? <Trophy size={30} color="var(--primary-700)"/>: <Trophy size={30}/>}
                    <Link href={'/seuprogresso'} className="text-2xl hover:font-medium">Seu Progresso</Link>
                </div>
                <div className='flex gap-4 items-center relative cursor-pointer' onClick={() => setMenuAberto(!menuAberto)}>
                    {/* a tela renderiza primeiro vazia e depois define o texto e o icone que vao aparecer de acordo com o tema que a pessoa escolheu */}
                    {montada ? (
                        <>
                            {theme === 'dark' ? <Moon size={40}/>: <Sun size={40}/>}
                            <p className="text-2xl">
                                {theme === 'dark' ? 'Modo Escuro': 'Modo Claro'}
                            </p>
                        </>
                    ) : (
                        <div></div>
                    )}
                    {menuAberto && (
                        <ul className="absolute rounded-md group-hover:block bg-black left-0 ofset-0 top-full mt-5">
                            <li className="flex justify-between hover:bg-(--primary-900) rounded-md">
                                <button className='flex justify-between text-[20px] p-5 w-55 hover:cursor-pointer' onClick={() => setTheme('light')}>
                                    Modo Claro
                                    <Sun size={25}/>
                                </button>
                            </li>
                            <hr />
                            <li className="flex justify-between hover:bg-(--primary-900) rounded-md">
                                <button className='flex justify-between text-[20px] p-5 w-55 hover:cursor-pointer' onClick={() => setTheme('dark')}>
                                    Modo Escuro
                                    <Moon size={25}/>
                                </button>
                            </li>
                        </ul>
                    )}
                </div>
                <div className={verificar_caminho('/perfil') ? 'flex gap-4 bg-white rounded-md rounded-s-4xl  pr-4 text-(--primary-700) items-center': 'flex gap-4 items-center'}>
                    <Image className={verificar_caminho('/perfil') ? 'w-[50px] h-[50px]': ''} src={'/images/icons/user.png'} alt="Logo" width={40} height={35}/>
                    <Link href={'/perfil'} className="text-2xl hover:font-medium">Seu Perfil</Link>
                </div>
            </div>
        </header>
    )
}