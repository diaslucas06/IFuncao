'use client'

import Header from "@/components/Header";
import Profile from "@/components/Profile";
import ButtonProfile from "@/components/ButtonProfile";
import BarraProgresso from "@/components/BarraProgresso";
import { CardBackground, CardH1, CardLi, CardP } from "@/components/CardProfile";
import CardConteudo from "@/components/CardConteudo";
import { Settings, PencilSparkles, ChevronLeft, ChevronRight } from "lucide-react";
import { useState } from "react";

export default function perfil() {
    const [inicioIndex, setInicioIndex] = useState(0)
    const conteudos_por_pagina = 4

    let dados = {
        'nome': 'Maria José dos Santos',
        'matricula': 20241101110000,
        'email': 'maria.jose@escolar.ifrn.edu.br',
        'ano_letivo': 3,
        'curso': 'Informática para Internet',
        'idade': 18,
        'media': 80
    }

    let progresso = {
        'primeiro': 100,
        'segundo': 100,
        'terceiro': 50,
        'Matemática Enem': 0
    }

    let historico = [
        {'id': 1, 'nome': 'MATEMÁTICA BÁSICA', 'link': '/conteudos/matematica_basica', 'porcentagem': 50},
        {'id': 2, 'nome': 'TRIGONOMETRIA', 'link': '/conteudos/matematica_basica', 'porcentagem': 0},
        {'id': 3, 'nome': 'GEOMETRIA', 'link': '/conteudos/matematica_basica', 'porcentagem': 80},
        {'id': 4, 'nome': 'PROGRESSÃO ARITMÉTICA', 'link': '/conteudos/matematica_basica', 'porcentagem': 100},
        {'id': 5, 'nome': 'MATEMÁTICA FINANCEIRA', 'link': '/conteudos/matematica_basica', 'porcentagem': 40},
        {'id': 6, 'nome': 'MATRIZ', 'link': '/conteudos/matematica_basica', 'porcentagem': 100},
        {'id': 7, 'nome': 'PROGRESSÃO GEOMÉTRICA', 'link': '/conteudos/matematica_basica', 'porcentagem': 20},
        {'id': 8, 'nome': 'DIVISÃO', 'link': '/conteudos/matematica_basica', 'porcentagem': 100},
        {'id': 9, 'nome': 'PROGRESSÃO GEOMÉTRICA', 'link': '/conteudos/matematica_basica', 'porcentagem': 20},
        {'id': 10, 'nome': 'DIVISÃO', 'link': '/conteudos/matematica_basica', 'porcentagem': 100},
        {'id': 11, 'nome': 'PROGRESSÃO GEOMÉTRICA', 'link': '/conteudos/matematica_basica', 'porcentagem': 20},
    ]

    function proximaPagina() {
        if (inicioIndex + conteudos_por_pagina <= historico.length) {
            setInicioIndex(inicioIndex + conteudos_por_pagina)
        }
    }

    function paginaAnterior() {
        if (inicioIndex - conteudos_por_pagina >= 0) {
            setInicioIndex(inicioIndex - conteudos_por_pagina)
        }
    }

    // pega os 4 conteudos que devem ser dessa pagina
    const conteudosExibidos = historico.slice(inicioIndex, inicioIndex + conteudos_por_pagina)

    return (
        <div>
            <Header/>
            <Profile usuario={'Nome do usuário'} ano={3} matricula={20241101110000} curso={'Informática para Internet'} idade={18} imagem={''}/>
            <main className="flex flex-col p-10 pt-40 gap-7">
                <div className="flex justify-between gap-5">
                    <CardBackground className="w-[50%] gap-[20px]">
                        <CardH1>Dados Pessoais</CardH1>
                        <ul className="flex flex-col gap-2">
                            <CardLi><b>Nome completo:</b> {dados.nome}</CardLi>
                            <CardLi><b>Matrícula:</b> {dados.matricula}</CardLi>
                            <CardLi><b>E-mail:</b> {dados.email}</CardLi>
                            <CardLi><b>Ano letivo:</b> {dados.ano_letivo}° ano</CardLi>
                            <CardLi><b>Curso:</b> {dados.curso}</CardLi>
                            <CardLi><b>Idade:</b> {dados.idade} anos</CardLi>
                        </ul>
                    </CardBackground>
                    <CardBackground>
                        <CardH1>Seu progresso por ano</CardH1>
                        <div>
                            <BarraProgresso ano={1} porcentagem={progresso.primeiro}/>
                            <BarraProgresso ano={2} porcentagem={progresso.segundo}/>
                            <BarraProgresso ano={3} porcentagem={progresso.terceiro}/>
                            <BarraProgresso ano={'Matemática Enem'} porcentagem={progresso["Matemática Enem"]}/>
                        </div>
                    </CardBackground>
                    <div className="flex flex-col justify-between gap-4">
                        <CardBackground className="gap-[5px]">
                            <CardH1>Sua média</CardH1>
                            <CardP>Média das notas em matemática do ano letivo: </CardP>
                            <div>
                                <p className="text-4xl text-(--profile-text-card-color) font-extrabold">{dados.media}</p>
                            </div>
                        </CardBackground>
                        <CardBackground className="gap-4">
                            <ButtonProfile icon={<PencilSparkles size={35} color="var(--profile-button-icon-color)"/>} text={'Editar'} callback={'/editarperfil'}/>
                            <ButtonProfile icon={<Settings size={35} color="var(--profile-button-icon-color)"/>} text={'Configurações'} callback={'/configuracoes'}/>
                        </CardBackground>
                    </div>
                </div>
                <div className="flex justify-between gap-5">
                    <CardBackground className="w-[100%] gap-[20px]">
                        <CardH1>Histórico de conteúdos acessados</CardH1>
                        <div className="flex justify-between items-center w-[100%]">
                            <button onClick={() => paginaAnterior()} disabled={inicioIndex === 0} className="disabled:opacity-30 transition-opacity">
                                <ChevronLeft className='hover:cursor-pointer' size={40} color="var(--arrow-color)"/>
                            </button>
                            <div className="flex items-center gap-3">
                                {conteudosExibidos.map((conteudo, index) => (
                                    <CardConteudo key={conteudo.id} nome={conteudo.nome}  link={conteudo.link}  porcentagem={conteudo.porcentagem} index={index}/>
                                ))}
                            </div>
                            <button onClick={() => proximaPagina()} disabled={inicioIndex + conteudos_por_pagina > historico.length} className="disabled:opacity-30 transition-opacity">
                                <ChevronRight className='hover:cursor-pointer' size={40} color="var(--arrow-color)"/>
                            </button>
                         </div>
                    </CardBackground>
                </div>
            </main>
        </div>
    )
}