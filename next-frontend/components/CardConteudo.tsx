import Link from "next/link"

interface CardProps {
    link: string,
    linha1: string,
    linha2: string,
    index: number
}

const cores = [
    {
        'bg': 'bg-(--neutral-0)', 
        'texto': 'text-(--primary-900)',
        'hover': 'bg-(--neutral-100)'
    },
    {
        'bg': 'bg-(--primary-800)', 
        'texto': 'text-(--neutral-0)',
        'hover': 'bg-(--primary-900)'
    },
    {
        'bg': 'bg-(--primary-200)', 
        'texto': 'text-(--primary-800)',
        'hover': 'bg-(--primary-300)'
    },
    {
        'bg': 'bg-(--primary-300)', 
        'texto': 'text-(--neutral-0)',
        'hover': 'bg-(--primary-500)'
    }
]

export default function CardConteudo({link, linha1, linha2, index}:CardProps) {
    const cor_atual = cores[index % 4]
    if (linha1 == 'MATEMÁTICA') {
        return (
            <Link href={link} className={`flex items-center justify-center flex-col ${cor_atual.bg} basis-1/4 aspect-square p-3 md:p-5 rounded-xl shadow-lg`}>
                <p className={`font-poppins-sans text-center font-extrabold text-xs md:text-2xl lg:text-xl lp:text-3xl pc:text-4xl ${cor_atual.texto}`}>{linha1}</p>
                <p className={`font-poppins-sans text-center font-extrabold text-3xl md:text-6xl lg:text-5xl lp:text-7xl pc:text-8xl ${cor_atual.texto}`}>{linha2}</p>
            </Link>
        )
    } else {
        return (
            <Link href={link} className={`flex items-center justify-center flex-col ${cor_atual.bg} basis-1/4 aspect-square p-3 md:p-5 rounded-xl shadow-lg`}>
                <p className={`font-poppins-sans text-center font-extrabold text-2xl md:text-6xl lp:text-7xl pc:text-9xl ${cor_atual.texto}`}>{linha1}</p>
                <p className={`font-poppins-sans text-center font-extrabold text-xl md:text-4xl lp:text-5xl pc:text-[64px] ${cor_atual.texto}`}>{linha2}</p>
            </Link>
        )
    }
}