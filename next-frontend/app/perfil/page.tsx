'use client'

import Header from "@/components/Header";
import Footer from "@/components/Footer";
import Profile from "@/components/Profile";
import ButtonProfile from "@/components/ButtonProfile";
import BarraProgresso from "@/components/BarraProgresso";
import { CardBackground, CardH1, CardLi, CardP } from "@/components/CardProfile";
import CardConteudo from "@/components/CardConteudo";
import { Settings, PencilSparkles, ChevronLeft, ChevronRight } from "lucide-react";
import { useState } from "react";
import { useEffect } from "react";

export default function perfil() {
    const [inicioIndex, setInicioIndex] = useState(0)
    const [conteudos_por_pagina, setConteudosPorPagina] = useState(4)

    useEffect(() => {
        if (window.innerWidth === 1920) {
            setConteudosPorPagina(4)
        } 
        if (window.innerWidth === 1440) {
            setConteudosPorPagina(4)
        }
        if (window.innerWidth === 1024) {
            setConteudosPorPagina(3)
        }
    }, [])

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
            <main className="flex flex-col p-10 gap-7 lg:pt-28 lp:pt-30 pc:pt-40">
                <div className="flex flex-1 flex-wrap justify-between gap-5">
                    <CardBackground className="flex gap-[20px] lg:flex-1 pc:flex-1 pc:w-[47%]">
                        <CardH1>Dados Pessoais</CardH1>
                        <ul className="flex flex-col gap-2">
                            <CardLi><b className="font-semibold">Nome completo:</b> {dados.nome}</CardLi>
                            <CardLi><b className="font-semibold">Matrícula:</b> {dados.matricula}</CardLi>
                            <CardLi><b className="font-semibold">E-mail:</b> {dados.email}</CardLi>
                            <CardLi><b className="font-semibold">Ano letivo:</b> {dados.ano_letivo}° ano</CardLi>
                            <CardLi><b className="font-semibold">Curso:</b> {dados.curso}</CardLi>
                            <CardLi><b className="font-semibold">Idade:</b> {dados.idade} anos</CardLi>
                        </ul>
                    </CardBackground>
                    <CardBackground className="flex gap-[20px] lg:flex-1 pc:flex-none pc:w-[25%]">
                        <CardH1>Seu progresso por ano</CardH1>
                        <div>
                            <BarraProgresso ano={1} porcentagem={progresso.primeiro}/>
                            <BarraProgresso ano={2} porcentagem={progresso.segundo}/>
                            <BarraProgresso ano={3} porcentagem={progresso.terceiro}/>
                            <BarraProgresso ano={'Matemática Enem'} porcentagem={progresso["Matemática Enem"]}/>
                        </div>
                    </CardBackground>
                    <div className="flex justify-between gap-4 lg:w-[100%] lg:flex-row pc:w-[25%] pc:flex-col">
                        <CardBackground className="flex lg:gap-[20px] lg:flex-3 lp:flex-1 pc:gap-[5px]">
                            <CardH1>Sua média</CardH1>
                            <CardP>Média das notas em matemática do ano letivo: </CardP>
                            <div>
                                <p className="text-4xl text-(--profile-text-card-color) font-extrabold">{dados.media}</p>
                            </div>
                        </CardBackground>
                        <CardBackground className="flex flex-1 justify-between">
                            <ButtonProfile icon={<PencilSparkles size={35} color="var(--profile-button-icon-color)"/>} text={'Editar'} callback={'/editarperfil'}/>
                            <ButtonProfile icon={<Settings size={35} color="var(--profile-button-icon-color)"/>} text={'Configurações'} callback={'/perfil/configuracoes/informacoes_basicas'}/>
                        </CardBackground>
                    </div>
                </div>
                <div className="flex justify-between gap-5">
                    <CardBackground className="w-[100%] gap-[20px]">
                        <CardH1>Histórico de conteúdos acessados</CardH1>
                        <div className="flex items-center w-[100%]">
                            <button onClick={() => paginaAnterior()} disabled={inicioIndex === 0} className="disabled:opacity-30 transition-opacity">
                                <ChevronLeft className='hover:cursor-pointer' size={40} color="var(--arrow-color)"/>
                            </button>
                            <div className="flex flex-wrap items-center justify-around w-[100%]">
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
            <Footer/>
        </div>
    )
}