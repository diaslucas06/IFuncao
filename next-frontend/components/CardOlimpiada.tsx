import Image from "next/image"

interface CardProps {
    img: string,
    title: string,
    text: string,
    link: string,
}

export default function CardOlimpiada({img, title, text, link}:CardProps) {
    return(
        <div className="flex flex-col text-center md:w-1/4 justify-center items-center gap-3 md:gap-5 lg:gap-8 lp:gap-10">
            <a href={link} className="flex bg-(--primary-800) rounded-full p-2 md:p-3 lp:p-5 w-fit aspect-square items-center">
                <Image className="h-auto w-[150px] md:w-[200px] lg:w-[270px] lp:w-[300px] pc:w-[320px]" src={img} alt={title} width={320} height={320}/>
            </a>
            <div>
                <h4 className="text-xl md:text-[28px] lg:text-[32px] lp:text-4xl pc:text-[40px] font-bold">{title}</h4>
                <p className="md:text-xl lg:text-2xl lp:text-[28px] pc:text-[32px] font-medium">{text}</p>
            </div>
        </div>
    )
}