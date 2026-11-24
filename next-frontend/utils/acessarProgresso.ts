import { useState, useEffect } from "react";

interface Progresso {
    etapa: string,
    total_conteudos: number;
    concluidos: any;
    porcentagem: number;
}

export function acessarProgresso(setErro:any) {
    const [progressos, setProgressos] = useState<Array<Progresso> | null>(null)

    useEffect(() => {
       
        
        const usuario = localStorage.getItem('usuario');
        if (!usuario) {
            return;
        }
        const usuarioObjeto = JSON.parse(usuario);
        const token = usuarioObjeto.access_token

        fetch(`http://localhost:8000/conteudos/progresso`, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${token}`
            }
        })
        .then((resposta) => {
            if (!resposta.ok) {
                throw new Error('Erro ao carregar progresso.');
            }
            return resposta.json(); 
        })
        .then((objetoDados) => {
            if (objetoDados.length == 0) {
                setErro("Nenhum progresso encontrado.")
                return;
            }
            console.log('progressos', progressos)
            setProgressos(objetoDados)
        })
        .catch((err) => {
            setErro("Progresso não encontrado!")
            return;
        });
    }, [setErro]);

    return progressos;
}