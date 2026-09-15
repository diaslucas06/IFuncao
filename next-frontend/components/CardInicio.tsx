import Image from "next/image";

interface CardProps {
    children: React.ReactNode,
    img: string,
    alt: string
}

export default function CardInicio({img, children, alt}:CardProps) {
    return (
        <div className="flex flex-col lg:flex-row items-center gap-5 md:gap-10 lp:gap-15 bg-(--primary-700) py-5 md:py-10 px-5 md:px-10 lg:px-12 lp:px-20 rounded-4xl md:text-justify">
            <Image className="h-auto w-[200px] md:w-[270px] lg:w-[350px] lp:w-[400px] pc:w-[600px]" src={img} alt={alt} width={600} height={520}/>
            <p className="font-poppins-sans lg:text-base lp:text-2xl pc:text-[32px] font-semibold text-white">{children}</p>
        </div>
    )
}