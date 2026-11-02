import { Search } from "lucide-react";

interface PesquisaProps {
    buscarConteudo: Function,
    cont_nome: string,
    etapa: string,
    setConteudo: any,
    setErro: any,
    setContNome: any
}

export default function BarraPesquisa(props:PesquisaProps) {
    return (
        <form onSubmit={(e) => { e.preventDefault(); props.buscarConteudo('1', props.cont_nome, props.setConteudo, props.setErro); }}>
            <div className="flex border-2 border-(--border-search) items-center px-5 rounded-md h-15">
                <input type="text" name="conteudo" id="conteudo" placeholder="Buscar conteúdo pelo nome" value={props.cont_nome} 
                    onChange={(e) => props.setContNome(e.target.value)}
                    className="w-[250px] focus:outline-none text-(--border-search)"
                />
                <Search size={25}/>
            </div>
        </form>
    )
}