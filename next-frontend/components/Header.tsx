import Link from "next/link";
import Image from "next/image";

export default function Header() {
    return (
        <header className="flex justify-between items-center py-5 px-10 bg-(--primary-700)">
            <Image src={'/logo.png'} alt="Logo" width={225} height={65}/>
            <div className="flex justify-between items-center gap-20">
                <Link href={'/'} className="text-2xl">Início</Link>
                <Link href={'/'} className="text-2xl">Conteúdos</Link>
                <Link href={'/'} className="text-2xl">Login</Link>
                <Link href={'/'} className="text-2xl">Modo Escuro</Link>
            </div>
        </header>
    )
}