'use client'

import Link from "next/link";
import { usePathname } from 'next/navigation'
import Image from "next/image";
import { useTheme } from "next-themes";
import { useState, useEffect } from "react";
import { Moon, Sun, Trophy, Home, Book, Menu, CircleX } from 'lucide-react';

export default function Header() {
    const nome_do_caminho = usePathname()
    const {theme, setTheme} = useTheme()
    // montada serve para renderizar a página primeiro e depois definir os icones com base na preferencia de tema
    const [montada, setMontada] = useState(false)
    const [menuAberto, setMenuAberto] = useState(false)
    const [menuTemaAberto, setMenuTemaAberto] = useState(false)
    
    useEffect(() => {
        setMontada(true)
    }, [])

    function verificar_caminho(caminho:string) {
        if (nome_do_caminho === caminho) {
            return true
        } else {
            return false
        }
    }

    return (
        <header className="sticky top-0 z-50 flex justify-between items-center bg-(--primary-700) text-(--neutral-0) shadow-xl py-2.5 px-5 md:py-5 md:px-10 md:gap-20 lg:gap-25 lp:gap-40 pc:gap-100">
            <div className="flex md:hidden" onClick={() => setMenuAberto(!menuAberto)}>
                {menuAberto ? <CircleX/>:<Menu/> }
            </div>
            {menuAberto && (
                <ul className="absolute group-hover:block bg-(--menu-color) ofset-0 top-full mt-5 left-5 right-5 rounded-lg">
                    <li className="flex justify-between hover:bg-(--primary-900) rounded-md">
                        <Link href={'/'} className='flex gap-5 p-5 hover:cursor-pointer'>
                            <Home size={25}/>
                            <p>Início</p>
                        </Link>
                    </li>
                    <hr />
                    <li className="flex justify-between hover:bg-(--primary-900) rounded-md">
                        <Link href={'/'} className='flex gap-5 p-5 hover:cursor-pointer'>
                            <Book size={25}/>
                            <p>Conteúdos</p>
                        </Link>
                    </li>
                    <hr />
                    <li className="flex justify-between hover:bg-(--primary-900) rounded-md">
                        <button className='flex gap-5 p-5 hover:cursor-pointer' onClick={() => {theme === 'dark' ? setTheme('light'): setTheme('dark')}}>
                            {theme === 'dark' ? <Moon size={25}/>: <Sun size={25}/>}
                            <p>Altere o tema do site</p>
                        </button>
                    </li>
                </ul>
            )}
            <Image className="h-auto w-[130px] md:w-[150px] lg:w-[200px] lp:w-[225px]" src={'/logo.png'} alt="Logo" width={225} height={65}/>
            <Link href={'/perfil'} className="flex md:hidden">
                <Image src={'/images/icons/user.png'} alt="Logo" width={30} height={35}/>
            </Link>
            <div className="hidden flex-1 justify-between items-center md:flex">
                <Link href={'/'} className={verificar_caminho('/') ? 'hover:font-medium bg-white rounded-md px-4 py-2 text-(--primary-700) md:text-lg lg:text-xl lp:text-2xl': 'hover:font-medium md:text-lg lg:text-xl lp:text-2xl'}>
                    <Home className={verificar_caminho('/') ? 'md:flex lg:hidden': 'md:flex lg:hidden'}/>
                    <p className={verificar_caminho('/') ? 'md:hidden lg:flex hover:font-medium': 'md:hidden lg:flex'}>Início</p>
                </Link>
                <Link href={'/conteudos'} className={verificar_caminho('/conteudos') ? 'hover:font-medium bg-white rounded-md px-4 py-2 text-(--primary-700) md:text-lg lg:text-xl lp:text-2xl': 'hover:font-medium md:text-lg lg:text-xl lp:text-2xl'}>
                    <Book className={verificar_caminho('/conteudos') ? 'md:flex lg:hidden': 'md:flex lg:hidden'}/>
                    <p className={verificar_caminho('/conteudos') ? 'md:hidden lg:flex hover:font-medium': 'md:hidden lg:flex'}>Conteúdos</p>
                </Link>
                <div className={verificar_caminho('/seuprogresso') ? 'bg-white rounded-md px-4 py-2 text-(--primary-700) items-center': ''}>
                    <Link href={'/seuprogresso'} className="flex gap-4 hover:font-medium md:text-lg lg:text-xl lp:text-2xl">
                        {verificar_caminho('/seuprogresso') ? <Trophy className="md:w-[25px] lg:w-[40px]" color="var(--primary-700)" size={30} />: <Trophy className="md:w-[25px] lg:w-[40px]" size={30}/>}
                        <p className={verificar_caminho('/seuprogresso') ? 'md:hidden lg:flex':'md:hidden lp:flex'}>Seu Progresso</p>
                    </Link>
                </div>
                <div className='flex gap-4 items-center relative cursor-pointer' onClick={() => setMenuTemaAberto(!menuTemaAberto)}>
                    {/* a tela renderiza primeiro vazia e depois define o texto e o icone que vao aparecer de acordo com o tema que a pessoa escolheu */}
                    {montada ? (
                        <>
                            {theme === 'dark' ? <Moon className="md:w-[30px] lg:w-[35px]" size={40}/>: <Sun className="md:w-[30px] lg:w-[35px]" size={40}/>}
                            <p className="md:hidden lp:flex text-2xl">
                                {theme === 'dark' ? 'Modo Escuro': 'Modo Claro'}
                            </p>
                        </>
                    ) : (
                        <div></div>
                    )}
                    {menuTemaAberto && (
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
                    <Link href={'/perfil'} className="flex gap-4 items-center md:text-lg lg:text-xl lp:text-2xl hover:font-medium">
                        <Image className="h-auto md:w-[40px] lg:w-[50px]" src={'/images/icons/user.png'} alt="Logo" width={40} height={35}/>
                        <p className={verificar_caminho('/perfil') ? '':'md:hidden lp:flex'}>Seu Perfil</p>
                    </Link>
                </div>
            </div>
        </header>
    )
}