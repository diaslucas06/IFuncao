import { Search } from "lucide-react";

export default function BarraPesquisa() {
    return (
        <div className="flex border-2 border-(--border-search) items-center px-5 rounded-md h-15">
            <input className="w-[250px] focus:outline-none text-(--border-search)" type="text" name="busca" placeholder="Busque conteúdos pelo nome"/>
            <Search size={25}/>
        </div>
    )
}