import Link from "next/link";
import Image from "next/image";

interface ButtonProfileProps {
    image: string,
    text: string,
    callback: string
}

export default function ButtonProfile(props:ButtonProfileProps) {

    return (
        <Link href={props.callback} className="flex gap-5 bg-(--profile-button-color) p-3 rounded-md justify-center">
            <Image src={props.image} alt={props.text} width={40} height={20}/>
            <p className="font-bold font-poppins text-[32px] text-(--sugestion-button-text-color)">{props.text}</p>
        </Link>
    )
}