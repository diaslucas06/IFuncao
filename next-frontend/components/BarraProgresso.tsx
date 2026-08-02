interface BarraProgressoProps {
    porcentagem: number,
    ano: any
}

export default function BarraProgresso(props:BarraProgressoProps) {
    return (
        <div>
            {typeof props.ano === 'string' ? <p className="flex justify-start text-[20px] font-bold">{props.ano}:</p>: <p className="flex justify-start text-[20px] font-bold"> {props.ano}° ano:</p>}
            <div className="bg-(--porcentagem-background-color) h-2 rounded-md w-full">
                <div className="relative rounded-md h-2 bg-(--porcentagem-color)" style={{ width: `${props.porcentagem}%` }}></div>
            </div>
            <p className="flex justify-end text-[20px] font-semibold pt-0.5">{props.porcentagem}%</p>
        </div>
        
    )
}