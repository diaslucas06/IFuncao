import Header from "@/components/Header";
import HeaderNotLogged from "@/components/HeaderNotLogged";
import Footer from "@/components/Footer";
import { CardBackground } from "@/components/CardProfile";
import Link from "next/link";

let logado = true

export default function seuprogresso() {
    if (logado) {
        return (
            <div>
                <Header/>
                <main className="flex flex-col p-10 gap-10">
                    <div className="flex flex-col justify-between gap-5">
                        <h1 className="text-[64px] font-bold">Conteúdos</h1>
                        <CardBackground className="w-full bg-(--settings-card-color)">
                            <div className="flex flex-col flex-wrap items-center w-full ml:flex-row ml:gap-15">
                                <Link href={'/conteudos/conteudo/primeiro_ano'} className="bg-white w-full ml:w-auto ml:aspect-square p-3 md:p-5 rounded-xl shadow-lg">
                                    <div className="flex-1 flex flex-col items-center justify-center aspect-square w-full ml:w-[115px] md:w-[130px] lg:w-[190px] lp:w-[250px] pc:w-[350px]">
                                        <p className={`font-poppins-sans text-(--primary-800) text-center font-extrabold text-[14px] lg:text-[20px] lp:text-[24px] pc:text-[128px] mb-[-70px]`}>1</p>
                                        <p className={`font-poppins-sans text-(--primary-800) text-center font-extrabold text-[14px] lg:text-[20px] lp:text-[24px] pc:text-[64px]`}>ano</p>
                                    </div>
                                </Link>
                                <Link href={'/conteudos/conteudo/segundo_ano'} className="bg-(--primary-800) w-full ml:w-auto ml:aspect-square p-3 md:p-5 rounded-xl shadow-lg">
                                    <div className="flex-1 flex flex-col items-center justify-center aspect-square w-full ml:w-[115px] md:w-[130px] lg:w-[190px] lp:w-[250px] pc:w-[350px]">
                                        <p className={`font-poppins-sans text-white text-center font-extrabold text-[14px] lg:text-[20px] lp:text-[24px] pc:text-[128px] mb-[-70px]`}>2</p>
                                        <p className={`font-poppins-sans text-white text-center font-extrabold text-[14px] lg:text-[20px] lp:text-[24px] pc:text-[64px]`}>ano</p>
                                    </div>
                                </Link>
                                <Link href={'/conteudos/conteudo/terceiro_ano'} className="bg-(--primary-200) w-full ml:w-auto ml:aspect-square p-3 md:p-5 rounded-xl shadow-lg">
                                    <div className="flex-1 flex flex-col items-center justify-center aspect-square w-full ml:w-[115px] md:w-[130px] lg:w-[190px] lp:w-[250px] pc:w-[350px]">
                                        <p className={`font-poppins-sans text-(--primary-800) text-center font-extrabold text-[14px] lg:text-[20px] lp:text-[24px] pc:text-[128px] mb-[-70px]`}>3</p>
                                        <p className={`font-poppins-sans text-(--primary-800) text-center font-extrabold text-[14px] lg:text-[20px] lp:text-[24px] pc:text-[64px]`}>ano</p>
                                    </div>
                                </Link>
                                <Link href={'/conteudos/conteudo/enem'} className="bg-(--primary-300) w-full ml:w-auto ml:aspect-square p-3 md:p-5 rounded-xl shadow-lg">
                                    <div className="flex-1 flex flex-col items-center justify-center aspect-square w-full ml:w-[115px] md:w-[130px] lg:w-[190px] lp:w-[250px] pc:w-[350px]">
                                        <p className={`font-poppins-sans text-white text-center font-extrabold text-[14px] lg:text-[20px] lp:text-[24px] pc:text-[32px] mb-[-30px]`}>MATEMÁTICA</p>
                                        <p className={`font-poppins-sans text-white text-center font-extrabold text-[14px] lg:text-[20px] lp:text-[24px] pc:text-[80px]`}>ENEM</p>
                                    </div>
                                </Link>
                            </div>
                        </CardBackground>
                    </div>
                </main>
                    
                <Footer/>
            </div>
        )
    } else {
        return (
            <HeaderNotLogged/>
        )
    }
    
}