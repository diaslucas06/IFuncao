import Link from "next/link";

export default function MenuConf() {
    return (
        <ul className="flex flex-col md:hidden">
            <li className="flex justify-between hover:bg-(--primary-900) rounded-md">
                <Link href={'/'} className='flex gap-5 p-5 hover:cursor-pointer'>
                    <p>Início</p>
                </Link>
            </li>
            <hr />
            <li className="flex justify-between hover:bg-(--primary-900) rounded-md">
                <Link href={'/'} className='flex gap-5 p-5 hover:cursor-pointer'>
                    <p>Conteúdos</p>
                </Link>
            </li>
            <hr />
            <li className="flex justify-between hover:bg-(--primary-900) rounded-md">
                <Link href={'/'} className='flex gap-5 p-5 hover:cursor-pointer'>
                    <p>Conteúdos</p>
                </Link>
            </li>
            <hr />
            <li className="flex justify-between hover:bg-(--primary-900) rounded-md">
                <Link href={'/'} className='flex gap-5 p-5 hover:cursor-pointer'>
                    <p>Conteúdos</p>
                </Link>
            </li>
            <hr />
            <li className="flex justify-between hover:bg-(--primary-900) rounded-md">
                <Link href={'/'} className='flex gap-5 p-5 hover:cursor-pointer'>
                    <p>Conteúdos</p>
                </Link>
            </li>
        </ul>
    )
}