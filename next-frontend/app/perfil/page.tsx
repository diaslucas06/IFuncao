import Header from "@/components/Header";
import Profile from "@/components/Profile";
import ButtonProfile from "@/components/ButtonProfile";

export default function perfil() {
    let dados = {
        nome: 'Maria José dos Santos',
        matricula: 20241101110000,
        email: 'maria.jose@escolar.ifrn.edu.br',
        ano_letivo: 3,
        curso: 'Informática para Internet',
        idade: 18,
        media: 80
    }

    return (
        <div>
            <Header/>
            <Profile usuario={'Nome do usuário'} ano={3} matricula={20241101110000} curso={'Informática para Internet'} idade={18} imagem={''}/>
            <div className="flex-col p-10 pt-40">
                <div className="flex justify-between gap-10">
                    <div className="card-profile" id="card-profile-data">
                        <h1>Dados Pessoais</h1>
                        <ul>
                            <li><b>Nome completo:</b> {dados.nome}</li>
                            <li><b>Matrícula:</b> {dados.matricula}</li>
                            <li><b>E-mail:</b> {dados.email}</li>
                            <li><b>Ano letivo:</b> {dados.ano_letivo}° ano</li>
                            <li><b>Curso:</b> {dados.curso}</li>
                            <li><b>Idade:</b> {dados.idade} anos</li>
                        </ul>
                    </div>
                    <div className="card-profile">
                        <h1>Seu progresso por ano</h1>
                    
                    </div>
                    <div className="flex flex-col justify-between gap-4">
                        <div className="card-profile" id="card-profile-media">
                            <h1>Sua média</h1>
                            <p>Média das notas em matemática do ano letivo: </p>
                            <div>
                                <p className="text-4xl text-(--profile-text-card-color) font-extrabold">{dados.media}</p>
                            </div>
                        </div>
                        <div className="card-profile" id="card-profile-media">
                            <ButtonProfile image={'/images/icons/pincel_dark.png'} text={'Editar'} callback={'/editarperfil'}/>
                            <ButtonProfile image={'/images/icons/pincel_dark.png'} text={'Configurações'} callback={'/configuracoes'}/>
                        </div>
                    </div>
                    
                </div>
               
            </div>
            
        </div>
    )
}