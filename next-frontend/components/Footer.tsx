import Image from "next/image";

interface FooterProps {
    position?: string
}

export default function Footer(props:FooterProps) {
    return (
        <footer className={`flex flex-col gap-5 items-center py-5 px-10 bg-(--primary-700) text-(--neutral-0) md:flex-row md:gap-12 bottom-0 w-full ${props.position}`}>
            <Image className="h-auto w-[130px] md:w-[150px] lg:w-[200px] lp:w-[225px]" src={'/logo.png'} alt="Logo" width={225} height={65}/>
            <div className="flex flex-col text-center md:text-start">
                <p className="text-[12px] md:text-[20px] pc:text-[24px]">&copy; 2026 IFunção. Todos os direitos reservados.</p>
                <p className="text-[12px] md:text-[20px] pc:text-[24px]">Privacidade & Segurança | Termos e Condições</p>
            </div>
        </footer>
    )
}