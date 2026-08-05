import Link from "next/link"

interface CardConteudoProps {
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

export default function CardConteudo(props:CardConteudoProps) {
    const cor_atual = cores[props.index % 4]
    return (
        <Link href={props.link} className={`flex flex-col justify-between aspect-square ${cor_atual.bg} p-5 rounded-xl shadow-lg`}>
            <div className="flex-1 flex items-center justify-center lg:w-[190px] lp:w-[250px] pc:w-[350px]">
                <p className={`font-poppins-sans text-center font-extrabold lg:text-[20px] lp:text-[24px] pc:text-[40px] ${cor_atual.texto}`}>{props.nome}</p>
            </div>
            
            <div className="flex flex-col justify-end">
                <p className={`flex justify-start  pt-0.5 ${cor_atual.texto} lg:text-[16px] pc:text-[20px]`}>{props.porcentagem}%</p>
                <div className={`${cor_atual.bg_barra} h-2 rounded-md w-full`}>
                    <div className={`relative rounded-md h-2 ${cor_atual.barra}`} style={{ width: `${props.porcentagem}%` }}></div>
                </div>
            </div>
        </Link>
    )
}