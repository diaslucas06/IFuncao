export function buscarConteudo(etapa:string, conteudo:string, setConteudo:any, setErro:any) {
    if (!buscarConteudo) {
        return;
    }
    const usuario = localStorage.getItem('usuario');
    if (!usuario) {
        return;
    }
    const usuarioObjeto = JSON.parse(usuario);
    const token = usuarioObjeto.access_token
    fetch(`http://localhost:8000/conteudos/${etapa}/${conteudo}`, {
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
        setErro("Conteúdo não encontrado!")
        return;
    });
}