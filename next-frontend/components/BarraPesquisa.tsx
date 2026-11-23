import { Search } from "lucide-react";
import { useState } from "react";
import { buscarConteudoNome } from "@/utils/buscarConteudoNome";
import { buscarConteudoNomeEtapa } from "@/utils/buscarConteudoNomeEtapa";

interface PesquisaProps {
    etapa?: string,
    setErro: any,
    setConteudosBuscados: any
}

export function BarraPesquisa(props:PesquisaProps) {
    const [cont_nome, setContNome] = useState("");
    return (
        <form onSubmit={(e) => { e.preventDefault(); buscarConteudoNome(cont_nome, props.setErro, props.setConteudosBuscados); }}>
            <div className="flex border-2 border-(--border-search) items-center px-5 rounded-md h-15">
                <input type="text" name="conteudo" id="conteudo" placeholder="Buscar conteúdo pelo nome"
                    onChange={(e) => setContNome(e.target.value)}
                    className="w-[250px] focus:outline-none text-(--border-search)"
                />
                <Search size={25}/>
            </div>
        </form>
    )
}

export function BarraPesquisaEtapa(props:PesquisaProps) {
    const [cont_nome, setContNome] = useState("");
    return (
        <form onSubmit={(e) => { e.preventDefault(); buscarConteudoNomeEtapa(cont_nome, props.setErro, props.setConteudosBuscados, props.etapa); }}>
            <div className="flex border-2 border-(--border-search) items-center px-5 rounded-md h-15">
                <input type="text" name="conteudo" id="conteudo" placeholder="Buscar conteúdo pelo nome"
                    onChange={(e) => setContNome(e.target.value)}
                    className="w-[250px] focus:outline-none text-(--border-search)"
                />
                <Search size={25}/>
            </div>
        </form>
    )
}