import Link from "next/link";
import { ArrowRight } from "lucide-react";

interface ButtonProps {
    link: string,
    text: string
}

export default function ButtonContent({link, text}:ButtonProps) {
    return (
        <Link className="bg-(--button-content-bg) flex justify-center gap-3 items-center p-7 rounded-2xl" href={link}>
            <h3 className="text-4xl font-bold">{text}</h3>
            <ArrowRight size={40}/>
        </Link>
    )
}