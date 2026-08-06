'use client'

import Link from "next/link";
import { usePathname } from 'next/navigation'
import Image from "next/image";
import { useTheme } from "next-themes";
import { useEffect, useState } from "react";
import { Moon, Sun, Book, Home, LogIn, CircleX, Menu } from "lucide-react";

export default function HeaderNotLogged() {
    const nome_do_caminho = usePathname()
    const {theme, setTheme} = useTheme()
    const [montada, setMontada] = useState(false)
    const [menuAberto, setMenuAberto] = useState(false)
    const [menuTemaAberto, setMenuTemaAberto] = useState(false)
    
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
        <header className="sticky top-0 z-50 flex justify-between items-center bg-(--primary-700) text-(--neutral-0) shadow-xl py-2.5 px-5 md:py-5 md:px-10 md:gap-40 lg:gap-55 lp:gap-90 pc:gap-150">
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
            <Link href={'/login'} className={verificar_caminho('/login') ? 'flex gap-3 items-center hover:font-medium bg-white rounded-md px-4 py-2 text-(--primary-700) md:hidden md:text-lg lg:text-xl lp:text-2xl': 'flex gap-3 items-center hover:font-medium md:hidden md:text-lg lg:text-xl lp:text-2xl'}>
                {verificar_caminho('/login') ? <LogIn className="md:w-[25px] lg:w-[40px]" color="var(--primary-700)" size={25} />: <LogIn className="md:w-[25px] lg:w-[40px]" size={25}/>}
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
                <Link href={'/login'} className={verificar_caminho('/login') ? 'flex gap-3 items-center hover:font-medium bg-white rounded-md px-4 py-2 text-(--primary-700) md:text-lg lg:text-xl lp:text-2xl': 'flex gap-3 items-center hover:font-medium md:text-lg lg:text-xl lp:text-2xl'}>
                    {verificar_caminho('/login') ? <LogIn className="md:w-[25px] lg:w-[40px]" color="var(--primary-700)" size={30} />: <LogIn className="md:w-[25px] lg:w-[40px]" size={30}/>}
                    <p className="hover:font-medium">Login</p>
                </Link>
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
                        <ul className="absolute rounded-md group-hover:block bg-black right-0 ofset-0 top-full mt-5">
                            <li className="flex justify-between hover:bg-(--primary-900) rounded-md">
                                <button className='flex justify-between p-5 hover:cursor-pointer w-45 lg:w-55' onClick={() => setTheme('light')}>
                                    <p className="lg:text-[20px]">Modo Claro</p>
                                    <Sun size={25}/>
                                </button>
                            </li>
                            <hr />
                            <li className="flex justify-between hover:bg-(--primary-900) rounded-md">
                                <button className='flex justify-between p-5 hover:cursor-pointer w-45 lg:w-55' onClick={() => setTheme('dark')}>
                                    <p className="lg:text-[20px]">Modo Escuro</p>
                                    <Moon size={25}/>
                                </button>
                            </li>
                        </ul>
                    )}
                </div>
            </div>
        </header>
    )
}