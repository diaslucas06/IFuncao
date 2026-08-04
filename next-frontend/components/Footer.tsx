import Image from "next/image";

export default function Footer() {
    return (
        <footer className="flex gap-12 items-center py-5 px-10 bg-(--primary-700) text-(--neutral-0)">
            <Image src={'/logo.png'} alt="Logo" width={225} height={65}/>
            <div>
                <p className="text-[24px]">&copy; 2026 IFunção. Todos os direitos reservados.</p>
                <p className="text-[24px]">Privacidade & Segurança | Termos e Condições</p>
            </div>
        </footer>
    )
}