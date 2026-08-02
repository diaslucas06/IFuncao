import Link from "next/link";
import { Settings, PencilSparkles } from "lucide-react";

interface ButtonProfileProps {
    icon: any,
    text: string,
    callback: string
}

export default function ButtonProfile(props:ButtonProfileProps) {

    return (
        <Link href={props.callback} className="flex gap-5 bg-(--profile-button-color) p-3 rounded-md justify-center items-center hover:bg-(--profile-button-color-hover) transition-colors duration-300">
            {props.icon}
            <p className="font-bold font-poppins text-[32px] text-(--sugestion-button-text-color)">{props.text}</p>
        </Link>
    )
}