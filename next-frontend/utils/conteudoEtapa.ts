import { useState, useEffect } from "react";

interface Conteudo {
    id: number,
    nome: string,
    link: string,
    porcentagem: number
}

export function conteudoEtapa(etapa:string, setErro:any) {
    const [conteudos, setConteudos] = useState<Array<Conteudo> | null>(null);
    
    if (!conteudoEtapa) {
        return;
    }

    useEffect(() => {
        const usuario = localStorage.getItem('usuario');
        if (!usuario) {
            return;
        }
        const usuarioObjeto = JSON.parse(usuario);
        const token = usuarioObjeto.access_token
        fetch(`http://localhost:8000/conteudos/${etapa}`, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${token}`
            }
        })
        .then((resposta) => {
            if (!resposta.ok) {
                throw new Error('Erro ao carregar conteúdos');
            }
            return resposta.json(); 
        })
        .then((objetoDados) => {
            setConteudos(objetoDados)
        })
        .catch((err) => {
            setErro("Nenhum conteúdo encontrado para essa etapa.")
            return;
        });
    }, [])
    
    return conteudos;
}