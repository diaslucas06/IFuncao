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
        'bg_barra': 'bg-(--primary-opacity-70)', 
        'barra': 'bg-(--primary-900)', 
        'texto': 'text-(--primary-900)'
    },
    {
        'bg': 'bg-(--primary-800)', 
        'bg_barra': 'bg-(--neutral-0)', 
        'barra': 'bg(--neutral-0)',
        'texto': 'text-(--neutral-0)'
    },
    {
        'bg': 'bg-(--primary-700)', 
        'bg_barra': 'bg-(--primary-300)', 
        'barra': 'bg-(--neutral-0)',
        'texto': 'text-(--neutral-0)'
    },
    {
        'bg': 'bg-(--primary-300)', 
        'bg_barra': 'bg-(--primary-300)', 
        'barra': 'bg-(--neutral-0)',
        'texto': 'text-(--neutral-0)'
    }
]

export default function CardHistorico(props:CardHistoricoProps) {
    const cor_atual = cores[props.index % 4]
    return (
        <Link href={props.link} className={`flex flex-col justify-between ${cor_atual.bg} w-full ml:w-auto ml:aspect-square p-3 md:p-5 rounded-xl shadow-lg`}>
            <div className="flex-1 flex items-center justify-center w-full ml:w-[115px] md:w-[130px] lg:w-[190px] lp:w-[250px] pc:w-[350px]">
                <p className={`font-poppins-sans text-center font-extrabold text-[14px] lg:text-[20px] lp:text-[24px] pc:text-[40px] ${cor_atual.texto}`}>{props.nome}</p>
            </div>
            <div className="hidden flex-col justify-end ml:flex">
                <p className={`flex absolute justify-start ${cor_atual.texto} pb-0.5 text-[14px] md:pb-2 lg:text-[16px] pc:text-[20px]`}>{props.porcentagem}%</p>
                <div className={`${cor_atual.bg_barra} h-1 md:h-2 rounded-md w-full`}>
                    <div className={`relative rounded-md h-1 md:h-2 ${cor_atual.barra}`} style={{ width: `${props.porcentagem}%` }}></div>
                </div>
            </div>
        </Link>
    )
}