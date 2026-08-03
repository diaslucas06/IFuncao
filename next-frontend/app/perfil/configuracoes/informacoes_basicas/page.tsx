'use client'

import Header from "@/components/Header";
import Sidebar from "@/components/Sidebar";
import { useState } from "react";
import { ConfDiv, ConfH1, ConfH2, ConfP, ConfCard, ConfLi } from "@/components/ConfComponents";
import { ChevronDown, ChevronUp } from "lucide-react";

export default function informacoes_basicas() {
    const [menuAberto, setMenuAberto] = useState(false)

    let perguntas = [
        {'enunciado': 'Pergunta 1?', 'resposta': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Adipisci vel ipsum, impedit similique tempore veniam perspiciatis consequatur vero? Nemo ratione iusto repellendus nihil minima reiciendis ipsam nostrum animi cumque aspernatur?'},
        {'enunciado': 'Pergunta 2?', 'resposta': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Adipisci vel ipsum, impedit similique tempore veniam perspiciatis consequatur vero? Nemo ratione iusto repellendus nihil minima reiciendis ipsam nostrum animi cumque aspernatur?'},
        {'enunciado': 'Pergunta 3?', 'resposta': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Adipisci vel ipsum, impedit similique tempore veniam perspiciatis consequatur vero? Nemo ratione iusto repellendus nihil minima reiciendis ipsam nostrum animi cumque aspernatur?'}
    ]

    return (
        <div>
            <Header/>
            <div className="flex">
                <Sidebar/>
                <ConfDiv>
                    <ConfH1>
                        Informações Básicas
                    </ConfH1>
                    <div className="flex flex-col gap-3">
                        <ConfCard>
                            <ConfH2>IFunção</ConfH2>
                            <ConfP>A plataforma atua como uma ferramenta de apoio pedagógico eficaz, facilitando o acesso aos materiais didáticos e promovendo a autonomia dos estudantes na preparação estratégica para o ENEM e acesso a conteúdos de matemática do ensino médio.</ConfP>
                        </ConfCard>
                        <ConfCard>
                            <ConfH2>Como usar</ConfH2>
                            <ConfP>Para utilizar a plataforma <b>IFunção</b>, é necessário se conectar por meio do SUAP, dessa forma, você poderá acessar todos os conteúdos e questões disponíveis no site, podendo acompanhar seu progresso e personalizar seu perfil com uma foto e nome de usuário próprio.</ConfP>
                        </ConfCard>
                        <ConfCard>
                            <ConfH2>Ajuda</ConfH2>
                            <div className="flex flex-col gap-5" onClick={() => setMenuAberto(!menuAberto)}>
                                <div className="flex gap-3 items-center hover:cursor-pointer">
                                    <ConfP><b>Perguntas comuns</b></ConfP>
                                    {menuAberto ? <ChevronUp size={30}/>: <ChevronDown size={30}/>}
                                </div>
                                {menuAberto && (
                                    <ul className="flex flex-col gap-5 w-[100%]">
                                        {perguntas.map((pergunta, index) => (
                                            <ConfLi key={index}>
                                                <ConfP><b>{pergunta.enunciado}</b></ConfP>
                                                <ConfP>{pergunta.resposta}</ConfP>
                                            </ConfLi>
                                        ))}
                                    </ul>
                                )}
                            </div>
                        </ConfCard>
                    </div>
                </ConfDiv>
            </div>
            
        </div>
    )
}