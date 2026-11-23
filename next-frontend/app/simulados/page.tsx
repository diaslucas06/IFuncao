'use client'

import Header from "@/components/Header";
import HeaderNotLogged from "@/components/HeaderNotLogged";
import Footer from "@/components/Footer";
import { CardBackground } from "@/components/CardProfile";
import CardConteudo from "@/components/CardConteudo";
import { useAuth } from "@/utils/auth";
import { useState, useEffect } from "react";

export default function SimuladosPage() {
    const { pessoa_logada, carregando } = useAuth();
    const [historico, setHistorico] = useState<any[]>([]);

    useEffect(() => {
        if (!pessoa_logada) return;

        const dadosUsuario = localStorage.getItem('usuario');
        if (!dadosUsuario) return;
        
        const token = JSON.parse(dadosUsuario).access_token;

        fetch('http://localhost:8000/simulados/historico', {
            headers: {
                'Authorization': `Bearer ${token}`
            }
        })
            .then((res) => res.ok ? res.json() : [])
            .then((dados) => setHistorico(dados))
            .catch((err) => console.error("Erro ao buscar histórico:", err));
    }, [pessoa_logada]);
      
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
                            <h1 className="h1_inicio">Simulados</h1>
                        </div>
                        <CardBackground className="w-full bg-(--settings-card-color)">
                            <div className="w-full flex flex-row justify-between gap-2 md:gap-4 grid grid-cols-2 lg:grid-cols-4">
                                <CardConteudo index={0} link="/conteudos/questoes/simulado?etapa=1" linha1="1" linha2="ETAPA"/>
                                <CardConteudo index={1} link="/conteudos/questoes/simulado?etapa=2" linha1="2" linha2="ETAPA"/>
                                <CardConteudo index={2} link="/conteudos/questoes/simulado?etapa=3" linha1="3" linha2="ETAPA"/>
                                <CardConteudo index={3} link="/conteudos/questoes/simulado?etapa=4" linha1="4" linha2="ETAPA"/>
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