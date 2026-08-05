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
    const [largura_logo, setLarguraLogo] = useState<number>(0)
    const [altura_logo, setAlturaLogo] = useState<number>(0)
    
    useEffect(() => {
        if (window.innerWidth <= 1920) {
            setLarguraLogo(225)
            setAlturaLogo(65)
        }
        if (window.innerWidth <= 1440) {
            setLarguraLogo(215)
            setAlturaLogo(55)
        }
        if (window.innerWidth <= 1024) {
            setLarguraLogo(195)
            setAlturaLogo(45)
        }
        setMontada(true)
    }, [])

    function verificar_caminho(caminho:string) {
        if (nome_do_caminho.includes(caminho)) {
            return true
        } else {
            return false
        }
    }

    return (
        <header className="sticky top-0 z-50 flex justify-between items-center py-5 px-10 bg-(--primary-700) text-(--neutral-0) shadow-xl lg:gap-25 lp:gap-40 pc:gap-100">
            <Image src={'/logo.png'} alt="Logo" width={largura_logo} height={altura_logo}/>
            <div className="flex flex-1 justify-between items-center">
                <Link href={'/inicio'} className={verificar_caminho('/inicio') ? 'hover:font-medium bg-white rounded-md px-4 py-2 text-(--primary-700) lg:text-xl lp:text-2xl': 'hover:font-medium lg:text-xl lp:text-2xl'}>Início</Link>
                <Link href={'/conteudos'} className={verificar_caminho('/conteudos') ? 'hover:font-medium bg-white rounded-md px-4 py-2 text-(--primary-700) lg:text-xl lp:text-2xl': 'hover:font-medium lg:text-xl lp:text-2xl'}>Conteúdos</Link>
                <div className={verificar_caminho('/seuprogresso') ? 'bg-white rounded-md px-4 py-2 text-(--primary-700) items-center': ''}>
                    <Link href={'/seuprogresso'} className="flex gap-4 text-2xl hover:font-medium">
                        {verificar_caminho('/seuprogresso') ? <Trophy size={30} color="var(--primary-700)"/>: <Trophy size={30}/>}
                        <p className={verificar_caminho('/seuprogresso') ? 'lg:text-xl lp:text-2xl':'lg:hidden lp:flex'}>Seu Progresso</p>
                    </Link>
                </div>
                <div className='flex gap-4 items-center relative cursor-pointer' onClick={() => setMenuAberto(!menuAberto)}>
                    {/* a tela renderiza primeiro vazia e depois define o texto e o icone que vao aparecer de acordo com o tema que a pessoa escolheu */}
                    {montada ? (
                        <>
                            {theme === 'dark' ? <Moon size={40}/>: <Sun size={40}/>}
                            <p className="lg:hidden lp:flex text-2xl">
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
                <div className={verificar_caminho('/perfil') ? 'flex bg-white rounded-md rounded-s-4xl pr-4 text-(--primary-700) items-center': ''}>
                    <Link href={'/perfil'} className="flex gap-4 items-center text-2xl hover:font-medium">
                        <Image className={verificar_caminho('/perfil') ? 'w-[50px] h-[50px]': ''} src={'/images/icons/user.png'} alt="Logo" width={40} height={35}/>
                        <p className={verificar_caminho('/perfil') ? 'lg:text-xl lp:text-2xl':'lg:hidden lp:flex'}>Seu Perfil</p>
                    </Link>
                </div>
            </div>
        </header>
    )
}