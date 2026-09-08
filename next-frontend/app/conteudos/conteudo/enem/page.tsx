'use client'

import Header from "@/components/Header";
import HeaderNotLogged from "@/components/HeaderNotLogged";
import Footer from "@/components/Footer";
import { CardBackground } from "@/components/CardProfile";
import CardHistorico from "@/components/CardHistorico";

let logado = true

export default function seuprogresso() {

    let historico = [
        {'id': 1, 'nome': 'MATEMÁTICA BÁSICA', 'link': '/conteudos/matematica_basica', 'porcentagem': 50},
        {'id': 2, 'nome': 'TRIGONOMETRIA', 'link': '/conteudos/matematica_basica', 'porcentagem': 0},
        {'id': 3, 'nome': 'GEOMETRIA', 'link': '/conteudos/matematica_basica', 'porcentagem': 80},
        {'id': 4, 'nome': 'PROGRESSÃO ARITMÉTICA', 'link': '/conteudos/matematica_basica', 'porcentagem': 100},
        {'id': 5, 'nome': 'MATEMÁTICA FINANCEIRA', 'link': '/conteudos/matematica_basica', 'porcentagem': 40},
        {'id': 6, 'nome': 'MATRIZ', 'link': '/conteudos/matematica_basica', 'porcentagem': 100},
        {'id': 7, 'nome': 'PROGRESSÃO GEOMÉTRICA', 'link': '/conteudos/matematica_basica', 'porcentagem': 20},
        {'id': 8, 'nome': 'DIVISÃO', 'link': '/conteudos/matematica_basica', 'porcentagem': 100},
        {'id': 9, 'nome': 'PROGRESSÃO GEOMÉTRICA', 'link': '/conteudos/matematica_basica', 'porcentagem': 20},
        {'id': 10, 'nome': 'DIVISÃO', 'link': '/conteudos/matematica_basica', 'porcentagem': 100},
        {'id': 11, 'nome': 'PROGRESSÃO GEOMÉTRICA', 'link': '/conteudos/matematica_basica', 'porcentagem': 20},
    ]
    
    if (logado) {
        return (
            <div>
                <Header/>
                <main className="flex flex-col p-10 gap-10">
                    <div className="flex flex-col justify-between gap-5">
                        <h1 className="text-[64px] font-bold">Conteúdos - ENEM </h1>
                        <CardBackground className="w-full bg-(--settings-card-color)">
                            <div className="flex flex-col flex-wrap items-center w-full ml:flex-row ml:gap-15">
                                {historico.map((conteudo, index) => (
                                    <CardHistorico key={conteudo.id} nome={conteudo.nome}  link={conteudo.link}  porcentagem={conteudo.porcentagem} index={index}/>
                                ))}
                            </div>
                        </CardBackground>
                    </div>
                </main>
                    
                <Footer/>
            </div>
        )
    }
    return (
        <div>
            <HeaderNotLogged/>
            <Footer/>
        </div>
    )
}