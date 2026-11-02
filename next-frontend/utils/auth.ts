import { useState, useEffect } from "react";

export function useAuth() {
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

    return { pessoa_logada, carregando };
}

