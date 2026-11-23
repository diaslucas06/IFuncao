import { useState, useEffect } from "react";

interface Conteudo {
    cont_id: number,
    cont_nome: string,
}

export function acessarHistorico(setErro:any) {
    const [conteudos, setConteudos] = useState<Array<Conteudo> | null>(null);

    useEffect(() => {
        const usuario = localStorage.getItem('usuario');
        if (!usuario) {
            return;
        }
        const usuarioObjeto = JSON.parse(usuario);
        const token = usuarioObjeto.access_token
        fetch(`http://localhost:8000/conteudos/historico`, {
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
            if (objetoDados.length == 0) {
                setErro("Nenhum conteúdo encontrado no histórico.")
                return;
            }
            setConteudos(objetoDados)
        })
        .catch((err) => {
            setErro("Nenhum conteúdo encontrado no histórico.")
            return;
        });
    }, [])
    
    return conteudos;
}