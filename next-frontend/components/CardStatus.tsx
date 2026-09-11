import { LucideIcon } from "lucide-react";

type CardStatusProps = {
  titulo: string;
  valor: string;
  descricao?: string;
  icone: LucideIcon;
  bgColor: string;
  textColor: string;
  iconeColor: string;
};

export default function CardStatus(props:CardStatusProps){
    return(
        <div className={`${props.bgColor} flex flex-col aspect-square lg:aspect-auto lp:aspect-square justify-between p-2 md:p-4 gap-1 md:gap-4 shadow-md rounded-sm shadow-black/20 lg:basis-1/2 lg:basis-1/4`}>
            
            <div></div>
            <div className="flex flex-col ml:gap-2 md:gap-5">
                <div className="flex justify-center md:mt-2">
                    <props.icone className={`${props.iconeColor} w-8 ml:w-10 h-10 sm:w-12 sm:h-12 md:w-15 md:h-15 lg:w-20 lg:h-20 lp:h-30`} />
                </div>
                <p className={`${props.textColor} text-center text-xs ml:text-[16px] font-medium md:text-xl lp:text-2xl`}>
                    {props.titulo}
                </p>
            </div>

            <div className="flex items-baseline flex-wrap md:mt-2">
                <h2 className={`${props.textColor} text-[10px] ml:text-[12px] md:text-[16px] lg:text-lg font-bold`}>
                    {props.valor}
                </h2>

                {props.descricao && (
                <p className={`${props.textColor} text-center text-[10px] ml:text-[12px] md:text-[16px] lg:text-xl ml-1.5`}>
                    {props.descricao}
                </p>
                )}
            </div>

        </div>
    )
}