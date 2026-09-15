import Link from "next/link"

interface CardHistoricoProps {
    nome: string,
    link: string,
    porcentagem: number,
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
        'bg': 'bg-(--primary-700)', 
        'texto': 'text-(--neutral-0)',
        'hover': 'bg-(--primary-900)'
    },
    {
        'bg': 'bg-(--primary-300)', 
        'texto': 'text-(--neutral-0)',
        'hover': 'bg-(--primary-500)'
    }
]

export default function CardHistorico(props:CardHistoricoProps) {
    const cor_atual = cores[props.index % 4]
    return (
        <Link href={props.link} className={`flex flex-col justify-between ${cor_atual.bg} hover:${cor_atual.hover} w-full ml:w-auto ml:aspect-square p-3 md:p-5 rounded-xl shadow-lg`}>
            <div className="flex-1 flex items-center justify-center text-center w-full">
                <p className={`font-poppins-sans text-center font-extrabold text-sm md:text-xl lp:text-2xl pc:text-[40px] ${cor_atual.texto}`}>{props.nome}</p>
            </div>
        </Link>
    )
}