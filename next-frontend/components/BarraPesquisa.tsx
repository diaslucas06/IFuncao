import { Search } from "lucide-react";
import { useState } from "react";

interface PesquisaProps {
    buscarConteudo: Function,
    etapa: string,
    setErro: any,
    setConteudo: any
}

export default function BarraPesquisa(props:PesquisaProps) {
    const [cont_nome, setContNome] = useState("");
    return (
        <form onSubmit={(e) => { e.preventDefault(); props.buscarConteudo('1', cont_nome, props.setConteudo, props.setErro); }}>
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