import Header from "@/components/Header";
import Profile from "@/components/Profile";

export default function perfil() {
    let lista_dados = [
        'Nome',
        'Nome',
        'Nome',
        'Nome',
        'Nome',
        'Nome'
    ]

    return (
        <div>
            <Header/>
            <Profile usuario={'Nome do usuário'} ano={3} matricula={20241101110000} curso={'Informática para Internet'} imagem={''}/>
            <div className="flex-col p-10 pt-40">
                <div className="flex w-11/12">
                    <div className="card-profile">
                        <h1 className="font-bold text-[40px] ">Dados Pessoais</h1>
                        {lista_dados.map((linhas, indice) => (
                            <p className='' key={indice}>{linhas}</p>
                        ))}
                    </div>
                    <div className="flex">
                        
                    </div> 
                </div>
               
            </div>
            
        </div>
    )
}