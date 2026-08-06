interface BarraProgressoProps {
    porcentagem: number,
    ano: any
}

export default function BarraProgresso(props:BarraProgressoProps) {
    return (
        <div>
            <p className="flex justify-start font-bold text-[16px] lp:text-[20px]">{typeof props.ano === 'string' ? `${props.ano}:`: `${props.ano}° ano:`}</p>
            <div className="bg-(--porcentagem-background-color) h-2 rounded-md w-full">
                <div className="relative rounded-md h-2 bg-(--porcentagem-color)" style={{ width: `${props.porcentagem}%` }}></div>
            </div>
            <p className="flex justify-end font-semibold pt-0.5 text-[16px] lp:text-[20px]">{props.porcentagem}%</p>
        </div>
        
    )
}