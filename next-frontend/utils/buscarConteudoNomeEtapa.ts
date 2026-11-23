export async function buscarConteudoNomeEtapa(nome: string, setErro: any, setConteudosBuscados:any, etapa:string) {
    if (!nome || nome.trim() === "") {
        setErro("");
        setConteudosBuscados(null);
        return;
    }

    const usuario = localStorage.getItem('usuario');
    if (!usuario) {
        return;
    }

    const usuarioObjeto = JSON.parse(usuario);
    const token = usuarioObjeto.access_token;

    return fetch(`http://localhost:8000/conteudos/buscar/${etapa}?q=${nome}`, {
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
    .then((resp) => {
        if (!resp || resp.length === 0) {
            setErro("Nenhum conteúdo encontrado para essa busca.");
            setConteudosBuscados(null);
            return;
        }
        setErro("")
        setConteudosBuscados(resp)
    })
    .catch((err) => {
        setErro("Nenhum conteúdo encontrado para essa etapa.");
        setConteudosBuscados(null);
        return;
    });
}
