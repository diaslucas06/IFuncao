import Link from "next/link";
import { Settings, PencilSparkles } from "lucide-react";

interface ButtonProfileProps {
    icon: any,
    text: string,
    callback: string
}

export default function ButtonProfile(props:ButtonProfileProps) {

    return (
        <Link href={props.callback} className="flex bg-(--profile-button-color) rounded-md justify-center items-center hover:bg-(--profile-button-color-hover) transition-colors duration-300 p-2 gap-2 lg:gap-3 lp:p-3 lp:gap-5">
            {props.icon}
            <p className="font-semibold font-poppins text-(--sugestion-button-text-color) text-[18px] md:text-[24px] lg:text-[28px] lp:text-[32px] ">{props.text}</p>
        </Link>
    )
}