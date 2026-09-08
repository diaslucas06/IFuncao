import Image from "next/image";

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

    return (
        <>
            <div className="flex bg-(--primary-800) text-(--neutral-0) justify-center h-30 py-5 md:h-auto md:justify-start md:px-10 md:py-8 pc:px-15 pc:pt-15 pc:pb-10">
                <Image className='absolute border-(--primary-800) border-3 rounded-[325px] md:w-[200px] lg:w-[245px] lp:w-[270px] pc:w-[325px]' src={verificar_imagem(props.imagem) ? props.imagem: '/images/icons/user.png'} alt="User" width={150} height={150}/>
                <div className='hidden md:pl-60 lg:pl-70 lp:pl-75 pc:pl-95 md:flex md:flex-col'>
                    <h1 className="font-bold font-poppins-sans md:text-[32px] lg:text-[36px] lp:text-[40px] pc:text-[48px]">{props.usuario}</h1>
                    <p className="font-poppins-sans md:text-[20px] lg:text-[24px] lp:text-[28px] pc:text-[32px]">{props.ano}° ano, {props.curso}</p>
                    <p className="font-poppins-sans md:text-[20px] lg:text-[24px] lp:text-[28px] pc:text-[32px]">{props.matricula}, {props.idade} anos</p>
                </div> 
            </div>
            <div className='flex flex-col items-center pt-18 md:pl-60 lg:pl-70 lp:pl-75 pc:pl-95 md:hidden'>
                <h1 className="font-bold font-poppins-sans">{props.usuario}</h1>
                <p className="font-poppins-sans text-[16px]">{props.ano}° ano, {props.curso}</p>
                <p className="font-poppins-sans text-[16px]">{props.matricula}, {props.idade} anos</p>
            </div> 
        </>
    )
}