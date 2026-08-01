import Image from "next/image"

interface ProfileProps {
    usuario: string,
    ano: number,
    curso: string,
    matricula: number,
    imagem?: any
}

export default function Profile(props:ProfileProps) {

    function verificar_imagem(imagem:any) {
        if (imagem) {
            return true
        } else {
            return false
        }
    }

    return (
        <div className="flex bg-(--primary-800) px-15 pt-15 pb-10">
            <div className="flex gap-15 text-(--neutral-0)">
               <Image className='absolute border-(--primary-800) border-3 rounded-[325px]' src={verificar_imagem(props.imagem) ? props.imagem: '/images/icons/user.png'} alt="User" width={325} height={325}/>
                <div className='pl-95'>
                    <h1 className="text-[48px] font-bold font-(--font-poppins)">{props.usuario}</h1>
                    <p className="text-[32px] font-(--font-poppins)">{props.ano}° ano, {props.curso}</p>
                    <p className="text-[32px] font-(--font-poppins)">{props.matricula}</p>
                </div> 
            </div>
        </div>
    )
}