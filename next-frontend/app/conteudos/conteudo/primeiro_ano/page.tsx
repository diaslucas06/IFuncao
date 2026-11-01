'use client'

import Header from "@/components/Header";
import HeaderNotLogged from "@/components/HeaderNotLogged";
import Footer from "@/components/Footer";
import { CardBackground } from "@/components/CardProfile";
import CardHistorico from "@/components/CardHistorico";
import BarraPesquisa from "@/components/BarraPesquisa";
import { Search } from "lucide-react";
import { useState, useEffect, use } from "react";
import { useAuth } from "@/components/ui/auth";

let logado = true

interface Conteudo {
    id: number,
    nome: string,
    link: string,
    porcentagem: number
}

export default function conteudo() {
    const [cont_nome, setContNome] = useState("");
    const [conteudo, setConteudo] = useState<Conteudo | null>(null);
    const [erro, setErro] = useState("");
    const {pessoa_logada, carregando} = useAuth()

    function buscar_conteudo(conteudo:string) {
        if (!buscar_conteudo) {
            return;
        }
        const usuario = localStorage.getItem('usuario');
        if (!usuario) {
            return;
        }
        const usuarioObjeto = JSON.parse(usuario);
        const token = usuarioObjeto.access_token
        fetch(`http://localhost:8000/conteudos/${conteudo}`, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${token}`
            }
        })
        .then((resposta) => {
            if (!resposta.ok) {
                throw new Error('Erro ao carregar conteúdo');
            }
            return resposta.json(); 
        })
        .then((objetoDados) => {
            setConteudo(objetoDados)
        })
        .catch((err) => {
            setErro("Conteúdo não encontrado")
            return;
        });
    }

    if (carregando) {
        return null;
    }

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
    
    if (pessoa_logada) {
        return (
            <div>
                <Header/>
                <main className="flex flex-col p-10 gap-10">
                    <div className="flex flex-col justify-between gap-5">
                        <div className="flex flex-col lg:flex-row justify-between items-center">
                            <h1 className="h1_inicio">Conteúdos - 1° ano</h1>
                            <form onSubmit={(e) => { e.preventDefault(); buscar_conteudo(cont_nome); }}>
                                <div className="flex border-2 border-(--border-search) items-center px-5 rounded-md h-15">
                                    <input type="text" name="conteudo" id="conteudo" placeholder="Buscar conteúdo pelo nome" value={cont_nome} 
                                        onChange={(e) => setContNome(e.target.value)}
                                        className="w-[250px] focus:outline-none text-(--border-search)"
                                    />
                                    <Search size={25}/>
                                </div>
                            </form>
                        </div>
                        {erro ? <h1>{erro}</h1>: ''}
                        {conteudo ? 
                            <div key={conteudo.id} className="basis-1/3 lg:basis-8/26 lp:basis-2/9 pc:basis-3/13">
                                <CardHistorico nome={conteudo.nome}  link={conteudo.link}  porcentagem={conteudo.porcentagem} index={0}/> 
                            </div>
                            : ''
                        }
                        <CardBackground className="w-full bg-(--settings-card-color)">
                            <div className="flex flex-wrap gap-3 lg:gap-8 lp:gap-11">
                                {historico.map((conteudo, index) => (
                                    <div key={conteudo.id} className="basis-1/3 lg:basis-8/26 lp:basis-2/9 pc:basis-3/13">
                                       <CardHistorico nome={conteudo.nome}  link={conteudo.link}  porcentagem={conteudo.porcentagem} index={index}/> 
                                    </div>
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