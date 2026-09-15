import Header from "@/components/Header";
import HeaderNotLogged from "@/components/HeaderNotLogged";
import Footer from "@/components/Footer";
import { CardBackground } from "@/components/CardProfile";
import CardConteudo from "@/components/CardConteudo";
import ButtonContent from "@/components/ButtonContent";
import BarraPesquisa from "@/components/BarraPesquisa";

let logado = true

export default function seuprogresso() {
    if (logado) {
        return (
            <div>
                <Header/>
                <main className="flex flex-col p-5 md:p-10 gap-10 mb-6">
                    <div className="flex flex-col justify-between gap-5">
                        <div className="flex justify-between items-center">
                            <h1 className="h1_inicio">Conteúdos</h1>
                            <BarraPesquisa/>
                        </div>
                        <CardBackground className="w-full bg-(--settings-card-color)">
                            <div className="w-full flex flex-row justify-between gap-2 md:gap-4 bg-(--settings-card-color) grid grid-cols-2 lg:grid-cols-4">
                                <CardConteudo index={0} link="/conteudos/conteudo/primeiro_ano" linha1="1" linha2="ano"/>
                                <CardConteudo index={1} link="/conteudos/conteudo/segundo_ano" linha1="2" linha2="ano"/>
                                <CardConteudo index={2} link="/conteudos/conteudo/terceiro_ano" linha1="3" linha2="ano"/>
                                <CardConteudo index={3} link="/conteudos/conteudo/enem" linha1="MATEMÁTICA" linha2="ENEM"/>
                            </div>
                        </CardBackground>
                    </div>
                    <ButtonContent link="/conteudos/questoes" text="Acessar a página de questões"/>
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