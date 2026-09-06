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
        <div className={`${props.bgColor} flex flex-col p-4 gap-4 shadow-md rounded-sm shadow-black/20`}>
            <div className="flex justify-center mt-2">
                <props.icone className={`${props.iconeColor} w-10 h-10 sm:w-12 sm:h-12 lg:w-18 lg:h-18`} />
            </div>

            <p className={`${props.textColor} text-center text-xs font-medium md:text-xl`}>
                {props.titulo}
            </p>

            <div className="flex items-baseline flex-wrap mt-2">
                <h2 className={`${props.textColor} text-sm lg:text-lg font-bold`}>
                    {props.valor}
                </h2>

                {props.descricao && (
                <p className={`${props.textColor} text-center text-xs lg:text-xl ml-1.5`}>
                    {props.descricao}
                </p>
                )}
            </div>

        </div>
    )
}