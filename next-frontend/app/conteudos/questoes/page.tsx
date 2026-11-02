'use client'

import Header from "@/components/Header";
import HeaderNotLogged from "@/components/HeaderNotLogged";
import Footer from "@/components/Footer";
import { CardBackground } from "@/components/CardProfile";
import CardConteudo from "@/components/CardConteudo";
import ButtonContent from "@/components/ButtonContent";
import BarraPesquisa from "@/components/BarraPesquisa";
import { useEffect, useState } from "react";

let logado = true

export default function seuprogresso() {
    const [pessoa_logada, setPessoaLogada] = useState(false);
    const [carregando, setCarregando] = useState(true);

    useEffect (() => {
        const usuario = localStorage.getItem('usuario');
        if (!usuario) {
            setPessoaLogada(false)
            return;
        }
        const usuarioObjeto = JSON.parse(usuario);
        const token = usuarioObjeto.access_token
        fetch('http://localhost:8000/auth/perfil', {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${token}` 
            }
        })
        .then((resposta) => {
            if (!resposta.ok) {
                throw new Error('Erro ao carregar perfil');
            }
            return resposta.json(); 
        })
        .then((objetoDados) => {
            setPessoaLogada(true)
            console.log(objetoDados)
        })
        .catch((err) => {
        setPessoaLogada(false)
        });
        setCarregando(false)
    }, [])

    if (carregando) {
        return null; 
    }

    if (pessoa_logada) {
        return (
            <div className="h-screen">
                <Header/>
                <main className="flex flex-col p-5 md:p-10 gap-10 mb-6">
                    <div className="flex flex-col justify-between gap-5">
                        <div className="flex justify-between items-center">
                            <h1 className="h1_inicio">Questões</h1>
                            <BarraPesquisa/>
                        </div>
                        <CardBackground className="w-full bg-(--settings-card-color)">
                            <div className="w-full flex flex-row justify-between gap-2 md:gap-4 grid grid-cols-2 lg:grid-cols-4">
                                <CardConteudo index={0} link="/conteudos/conteudo/primeiro_ano" linha1="1" linha2="ano"/>
                                <CardConteudo index={1} link="/conteudos/conteudo/segundo_ano" linha1="2" linha2="ano"/>
                                <CardConteudo index={2} link="/conteudos/conteudo/terceiro_ano" linha1="3" linha2="ano"/>
                                <CardConteudo index={3} link="/conteudos/conteudo/enem" linha1="MATEMÁTICA" linha2="ENEM"/>
                            </div>
                        </CardBackground>
                    </div>
                    <ButtonContent link="/conteudos" text="Acessar a página de conteúdos"/>
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