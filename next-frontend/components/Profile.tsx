import Image from "next/image";
import { useState, useEffect } from "react";

interface ProfileProps {
    usuario: string,
    ano: number,
    curso: string,
    matricula: number,
    idade: number,
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

    const [largura_user, setLarguraUser] = useState<number>(0)
    
    useEffect(() => {
        if (window.innerWidth <= 1920) {
            setLarguraUser(325)
        }
        if (window.innerWidth <= 1440) {
            setLarguraUser(270)
        }
        if (window.innerWidth <= 1024) {
            setLarguraUser(240)
        }
    }, [])

    return (
        <div className="flex bg-(--primary-800) lg:px-10 lg:py-8 pc:px-15 pc:pt-15 pc:pb-10">
            <div className="flex text-(--neutral-0)">
               <Image className='absolute border-(--primary-800) border-3 rounded-[325px]' src={verificar_imagem(props.imagem) ? props.imagem: '/images/icons/user.png'} alt="User" width={largura_user} height={largura_user}/>
                <div className='lg:pl-70 lp:pl-75 pc:pl-95'>
                    <h1 className="font-bold font-poppins-sans lg:text-[36px] lp:text-[40px] pc:text-[48px]">{props.usuario}</h1>
                    <p className="font-poppins-sans lg:text-[24px] lp:text-[28px] pc:text-[32px]">{props.ano}° ano, {props.curso}</p>
                    <p className="font-poppins-sans lg:text-[24px] lp:text-[28px] pc:text-[32px]">{props.matricula}, {props.idade} anos</p>
                </div> 
            </div>
        </div>
    )
}