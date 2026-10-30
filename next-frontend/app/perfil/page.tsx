'use client'
import Header from "@/components/Header";
import Footer from "@/components/Footer";
import Profile from "@/components/Profile";
import ButtonProfile from "@/components/ButtonProfile";
import BarraProgresso from "@/components/BarraProgresso";
import { CardBackground, CardH1, CardLi, CardP } from "@/components/CardProfile";
import CardHistorico from "@/components/CardHistorico";
import { Settings, LogOut } from "lucide-react";
import { useEffect, useState } from "react";
import { CarouselItem, Carousel, CarouselContent, CarouselPrevious, CarouselNext } from "@/components/ui/carousel";

interface Usuario {
    user_nome: string;
    user_matricula: number;
    user_email: string;
    user_ano_letivo: number;
    user_curso: string;
    user_data_nascimento: string;
    user_foto_url: string;
}

export default function perfil() {
    const [perfil, setPerfil] = useState<Usuario | null>(null);
    const [erro, setErro] = useState<string | null>(null);

    useEffect (() => {
        const usuario = localStorage.getItem('usuario');
        if (!usuario) {
            setErro("Usuário não está logado.");
            window.location.href = '/login';
            return;
        }
        const usuarioObjeto = JSON.parse(usuario);
        const token = usuarioObjeto.access_token
        fetch('http://localhost:8000/auth/perfil', {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${token}` 
            }
        })
        .then((resposta) => {
            if (!resposta.ok) {
                throw new Error('Erro ao carregar perfil');
            }
            return resposta.json(); 
        })
        .then((objetoDados) => {
            setPerfil(objetoDados); 
            console.log(objetoDados)
        })
        .catch((err) => {
            setErro(err.message);
            window.location.href = '/login';
        });
    }, [])

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

    return (
        <div>
            <Header/>
            <Profile usuario={perfil?.user_nome} ano={perfil?.user_ano_letivo} matricula={perfil?.user_matricula} curso={perfil?.user_curso} imagem={perfil?.user_foto_url}/>
            <main className="flex flex-col p-5 pt-10 gap-5 md:p-10 md:pt-20 lg:gap-7 lg:pt-33 lp:pt-35 pc:pt-45">
                <div className="flex flex-1 flex-wrap justify-between gap-5">
                    <CardBackground className="flex gap-[20px] flex-1/1 lg:flex-1 pc:flex-1 pc:w-[47%]">
                        <CardH1>Dados Pessoais</CardH1>
                        <ul className="flex flex-col gap-2">
                            <CardLi><b className="font-semibold">Nome completo:</b> {perfil?.user_nome}</CardLi>
                            <CardLi><b className="font-semibold">Matrícula:</b> {perfil?.user_matricula}</CardLi>
                            <CardLi><b className="font-semibold">E-mail:</b> {perfil?.user_email}</CardLi>
                            <CardLi><b className="font-semibold">Ano letivo:</b> {perfil?.user_ano_letivo}° ano</CardLi>
                            <CardLi><b className="font-semibold">Curso:</b> {perfil?.user_curso}</CardLi>
                            <CardLi><b className="font-semibold">Data de nascimento:</b> {perfil?.user_data_nascimento}</CardLi>
                        </ul>
                    </CardBackground>
                    <CardBackground className="flex gap-[20px] flex-1/1 lg:flex-1 pc:flex-none pc:w-[25%]">
                        <CardH1>Seu progresso por ano</CardH1>
                        <div>
                            <BarraProgresso ano={1} porcentagem={progresso.primeiro}/>
                            <BarraProgresso ano={2} porcentagem={progresso.segundo}/>
                            <BarraProgresso ano={3} porcentagem={progresso.terceiro}/>
                            <BarraProgresso ano={'Matemática Enem'} porcentagem={progresso["Matemática Enem"]}/>
                        </div>
                    </CardBackground>
                    <div className="flex flex-col justify-between gap-4 w-full md:flex-row lg:flex-row pc:w-[25%] pc:flex-col">
                        <CardBackground className="flex flex-1 md:gap-[20px] lg:flex-3 lp:flex-1 pc:gap-[5px]">
                            <CardH1>Sua média</CardH1>
                            <CardP>Média das notas em matemática do ano letivo: </CardP>
                            <div>
                                <p className="text-base md:text-3xl lp:text-4xl text-(--profile-text-card-color) font-extrabold"></p>
                            </div>
                        </CardBackground>
                        <CardBackground className="flex flex-1 gap-2 justify-around md:gap-0 lp:justify-around">
                            <ButtonProfile icon={<Settings size={35} color="var(--profile-button-icon-color)" className="w-[25px] md:w-[35px]"/>} text={'Configurações'} callback={'/perfil/configuracoes/informacoes_basicas'}/>
                            <ButtonProfile icon={<LogOut size={35} color="var(--profile-button-icon-color)" className="w-[25px] md:w-[35px]"/>} text={'Sair'} callback={'/sair'}/>
                        </CardBackground>
                    </div>
                </div>
                <div className="flex justify-between gap-5">
                    <CardBackground className="w-full gap-[20px]">
                        <CardH1>Histórico de conteúdos acessados</CardH1>
                        <div className="flex items-center w-full px-10">
                            <Carousel opts={{
                                    align: "start",
                                    slidesToScroll: 1,
                                }} 
                                className="flex flex-col flex-wrap items-center justify-between w-full ml:flex-row">
                                <CarouselContent className="flex-col ml:flex-row">
                                    {historico.map((conteudo, index) => (
                                        <CarouselItem className="basis-1/2 lg:basis-1/3 lp:basis-1/4" key={conteudo.id}>
                                            <CardHistorico nome={conteudo.nome}  link={conteudo.link}  porcentagem={conteudo.porcentagem} index={index}/>
                                        </CarouselItem>
                                    ))}
                                </CarouselContent>
                                <CarouselPrevious />
                                <CarouselNext />
                            </Carousel>
                         </div>
                    </CardBackground>
                </div>
            </main>
            <Footer/>
        </div>
    )
}