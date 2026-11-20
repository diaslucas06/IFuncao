from sqlalchemy.orm import Session
from models import Conteudo, Questao, EtapaEnum, DificuldadeEnum, AlternativaEnum
from contextlib import contextmanager

from dependencies import pegar_sessao

sessao_seed = contextmanager(pegar_sessao)

def povoar_conteudo_3(db: Session):
    conteudo3 = Conteudo(
        cont_nome="Trigonometria no Triângulo Retângulo",
        cont_etapa=EtapaEnum.ETAPA_1,
        cont_texto=(
            "1. TRIÂNGULO RETÂNGULO E CLASSIFICAÇÕES\n"
            "A trigonometria no triângulo retângulo estuda as relações entre os ângulos e as medidas dos lados de triângulos que possuem um ângulo interno reto (90°). "
            "Nesse triângulo, o lado oposto ao ângulo de 90° é chamado de hipotenusa (maior lado) e os outros dois lados são chamados de catetos.\n"
            "• Quanto aos lados: equilátero (três lados iguais), isósceles (dois lados iguais) e escaleno (três lados diferentes).\n"
            "• Quanto aos ângulos: retângulo (um ângulo de 90°), acutângulo (ângulos internos menores que 90°) e obtusângulo (um ângulo interno maior que 90°). A soma dos ângulos internos de qualquer triângulo é sempre 180°.\n\n"
            "2. RAZÕES TRIGONOMÉTRICAS NO TRIÂNGULO RETÂNGULO\n"
            "Para um ângulo agudo α em um triângulo retângulo, definem-se as três razões principais:\n"
            "• Seno (sen α) = cateto oposto / hipotenusa\n"
            "• Cosseno (cos α) = cateto adjacente / hipotenusa\n"
            "• Tangente (tg α) = cateto oposto / cateto adjacente = sen α / cos α\n\n"
            "3. ÂNGULOS NOTÁVEIS (30°, 45° e 60°)\n"
            "• 30°: sen = 1/2 | cos = √3/2 | tg = √3/3\n"
            "• 45°: sen = √2/2 | cos = √2/2 | tg = 1\n"
            "• 60°: sen = √3/2 | cos = 1/2 | tg = √3\n\n"
            "4. CÍRCULO TRIGONOMÉTRICO\n"
            "No círculo trigonométrico, o eixo vertical corresponde ao seno e o eixo horizontal corresponde ao cosseno. Além das razões principais, existem as razões inversas: cossecante (1/sen), secante (1/cos) e cotangente (1/tg).\n\n"
            "5. EXEMPLOS RESOLVIDOS\n"
            "• Exemplo 1: Um engenheiro se posiciona a 8 m da base de um poste e mede um ângulo de elevação de 45° até o topo. Qual a altura x do poste?\n"
            "Resolução: tg 45° = x / 8 → 1 = x / 8 → x = 8 m.\n"
            "• Exemplo 2: Um barco atravessa um rio de 50 m de largura formando um ângulo de 30° com a margem. Qual a distância x percorrida?\n"
            "Resolução: sen 30° = 50 / x → 1/2 = 50 / x → x = 100 m."
        ),
        cont_texto_resumo="Estudo das razões trigonométricas no triângulo retângulo (seno, cosseno e tangente), tabela de ângulos notáveis (30°, 45° e 60°), círculo trigonométrico e aplicações práticas.",
        cont_slide_pdf="IFUNÇÃO-GP2.pdf",
        cont_relacionados={
            "topicos": [
                "Teorema de Pitágoras",
                "Relações Métricas no Triângulo Retângulo",
                "Círculo Trigonométrico",
            ]
        },
    )
    db.add(conteudo3)
    db.flush()

    questoes = [
        Questao(
            ques_cont_id=conteudo3.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.FACIL,
            ques_enunciado="1 - Observando pela manhã a sombra de um prédio no chão, uma pessoa verificou que essa media 63 metros quando os raios de Sol faziam um ângulo de 30° com a superfície. Baseado nessas informações, calcule a altura do prédio.",
            ques_alternativas={
                "A": "a) 30,50 m",
                "B": "b) 20,10 m",
                "C": "c) 36,37 m",
                "D": "d) 38,45 m",
                "E": "e) 40,08 m",
            },
            ques_resposta_correta=AlternativaEnum.C,
        ),
        Questao(
            ques_cont_id=conteudo3.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.FACIL,
            ques_enunciado="2 - Uma ciclista participando de um campeonato se aproxima da linha de chegada que se encontra no alto de uma ladeira. O comprimento total dessa última parte da prova é de 60 m e o ângulo formado entre a rampa e a horizontal é de 30°. Sabendo disso, calcule a altura vertical que a ciclista precisa subir.",
            ques_alternativas={
                "A": "a) 25 m",
                "B": "b) 30 m",
                "C": "c) 35 m",
                "D": "d) 45 m",
            },
            ques_resposta_correta=AlternativaEnum.B,
        ),
        Questao(
            ques_cont_id=conteudo3.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.MEDIO,
            ques_enunciado="3 - (EPCAR-MG) Um avião decola de um ponto B sob inclinação constante de 15° com a horizontal. A 2 km de B se encontra a projeção vertical C do ponto mais alto D de uma serra de 600 m de altura. Dados: cos 15° = 0,97; sen 15° = 0,26; tg 15° = 0,27. É correto afirmar que:",
            ques_alternativas={
                "A": "a) Não haverá colisão do avião com a serra antes de alcançar 540 m de altura.",
                "B": "b) Haverá colisão do avião com a serra em 540 m de altura.",
                "C": "c) Haverá colisão do avião com a serra em D.",
                "D": "d) Se o avião decolar 220 m antes de B, mantendo a mesma inclinação, não haverá colisão do avião com a serra.",
            },
            ques_resposta_correta=AlternativaEnum.B,
        ),
        Questao(
            ques_cont_id=conteudo3.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.FACIL,
            ques_enunciado="4 - Um avião decolou sob um ângulo constante de 40º e percorreu em linha reta 8000 m. Nesta situação, qual a altura que se encontrava o avião ao percorrer essa distância? Considere: sen 40º = 0,64; cos 40º = 0,77; tg 40º = 0,84.",
            ques_alternativas={
                "A": "a) 5120 m",
                "B": "b) 6000 m",
                "C": "c) 4570 m",
                "D": "d) 3540 m",
            },
            ques_resposta_correta=AlternativaEnum.A,
        ),
        Questao(
            ques_cont_id=conteudo3.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.MEDIO,
            ques_enunciado="5 - Um menino de 1,30 m de altura avista o ponto mais alto de um morro sob um ângulo visual de 20º em relação à horizontal. Considerando que ele está a uma distância de 500 m da base do morro, calcule a altura (h) deste ponto. Considere: sen 20º = 0,34; cos 20º = 0,93; tg 20º = 0,36.",
            ques_alternativas={
                "A": "a) 192,1 m",
                "B": "b) 131 m",
                "C": "c) 500,3 m",
                "D": "d) 181,3 m",
            },
            ques_resposta_correta=AlternativaEnum.D,
        ),
        Questao(
            ques_cont_id=conteudo3.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.MEDIO,
            ques_enunciado="6 - Um terreno possui o formato de um retângulo cuja base mede 8 cm, sabendo que o ângulo formado entre a base e a diagonal é de 30º, qual o valor que mais se aproxima da diagonal? (Use √3 = 1,7)",
            ques_alternativas={
                "A": "a) 5",
                "B": "b) 6",
                "C": "c) 7",
                "D": "d) 8",
                "E": "e) 9",
            },
            ques_resposta_correta=AlternativaEnum.E,
        ),
        Questao(
            ques_cont_id=conteudo3.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.MEDIO,
            ques_enunciado="7 - Qual deve ser o valor do seno de um ângulo, sabendo que ele se encontra no primeiro quadrante e que o cosseno desse mesmo ângulo é igual a 3/5?",
            ques_alternativas={
                "A": "a) 4/5",
                "B": "b) 2/5",
                "C": "c) 3/4",
                "D": "d) 1/5",
                "E": "e) 2/3",
            },
            ques_resposta_correta=AlternativaEnum.A,
        ),
        Questao(
            ques_cont_id=conteudo3.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.FACIL,
            ques_enunciado="8 - Um teleférico foi instalado ligando uma base ao cume de uma montanha. Para a instalação, foram utilizados 1358 m de cabos, dispostos a uma angulação de 30° em relação ao solo. Qual a altura da montanha?",
            ques_alternativas={
                "A": "a) 450 m",
                "B": "b) 300 m",
                "C": "c) 400 m",
                "D": "d) 579 m",
                "E": "e) 679 m",
            },
            ques_resposta_correta=AlternativaEnum.E,
        ),
        Questao(
            ques_cont_id=conteudo3.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.FACIL,
            ques_enunciado="9 - Sendo o ângulo oposto ao cateto 'a' igual a 30° e a hipotenusa igual a 47 m em um triângulo retângulo, calcule a medida da altura 'a' do triângulo.",
            ques_alternativas={
                "A": "a) 20 m",
                "B": "b) 23,50 m",
                "C": "c) 30,50 m",
                "D": "d) 40 m",
                "E": "e) 50 m",
            },
            ques_resposta_correta=AlternativaEnum.B,
        ),
        Questao(
            ques_cont_id=conteudo3.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.DIFICIL,
            ques_enunciado="10 - A vista superior de um parque mostra dois caminhos para se chegar ao ponto C, a partir do ponto A. Uma das opções é ir para B, onde há bebedouros e lugares de descanso e, depois, ir para C. Caso um visitante do parque queira ir direto para C, quantos metros ele terá caminhado a menos do que a primeira opção? Considerar as aproximações: sen 58° = 0,85; cos 58° = 0,53; tan 58° = 1,60.",
            ques_alternativas={
                "A": "a) 7,54 m",
                "B": "b) 3,50 m",
                "C": "c) 56,75 m",
                "D": "d) 12,40 m",
            },
            ques_resposta_correta=AlternativaEnum.A,
        ),
    ]

    db.add_all(questoes)
    db.commit()

# CONTEÚDO 4 (Funções e Função Afim - Função do 1º Grau)
def povoar_conteudo_4(db: Session):
    conteudo4 = Conteudo(
        cont_nome="Funções e Função Afim (Função do 1º Grau)",
        cont_etapa=EtapaEnum.ETAPA_1,
        cont_texto=(
            "1. CONCEITO DE FUNÇÃO\n"
            "Uma função f: A → B é uma relação que associa cada elemento x do conjunto A (Domínio - D) a um único elemento y do conjunto B (Contradomínio - CD). "
            "Os elementos de B que estão efetivamente relacionados a algum elemento de A formam o Conjunto Imagem (Im).\n\n"
            "2. TIPOS DE FUNÇÕES\n"
            "• Função Sobrejetora: o conjunto imagem é igual ao contradomínio (Im(f) = B), ou seja, todo elemento de B é imagem de pelo menos um elemento de A.\n"
            "• Função Injetora: elementos distintos do domínio possuem imagens distintas no contradomínio (se x₁ ≠ x₂, então f(x₁) ≠ f(x₂)).\n"
            "• Função Bijetora: é simultaneamente injetora e sobrejetora, permitindo a existência de função inversa.\n"
            "• Função Composta: combina duas funções f e g, representada por (f ∘ g)(x) = f(g(x)) ou (g ∘ f)(x) = g(f(x)).\n\n"
            "3. FUNÇÃO AFIM (FUNÇÃO DO 1º GRAU)\n"
            "É toda função f: R → R definida pela lei de formação f(x) = ax + b, com a e b números reais (a ≠ 0).\n"
            "• Coeficiente angular (a): representa a taxa de variação e determina a inclinação da reta em relação ao eixo x.\n"
            "  - Se a > 0: a função é crescente.\n"
            "  - Se a < 0: a função é decrescente.\n"
            "  - Se a = 0: a função é constante.\n"
            "• Coeficiente linear (b): termo constante que indica o ponto (0, b) onde a reta corta o eixo vertical y.\n\n"
            "4. GRÁFICO E ZERO DA FUNÇÃO AFIM\n"
            "O gráfico de uma função afim é uma reta, podendo ser traçado a partir de dois pontos distintos.\n"
            "O zero (ou raiz) da função é o valor de x para o qual f(x) = 0, indicando o ponto onde a reta intercepta o eixo x:\n"
            "ax + b = 0  →  x = -b / a\n\n"
            "5. INEQUAÇÕES DO 1º GRAU\n"
            "São sentenças matemáticas que envolvem uma incógnita e um sinal de desigualdade (<, >, ≤ ou ≥). "
            "Para resolvê-las, isola-se a variável da mesma forma que nas equações; caso a incógnita fique negativa, multiplica-se toda a inequação por (-1) e inverte-se o sentido da desigualdade.\n\n"
            "6. EXEMPLOS RESOLVIDOS\n"
            "• Exemplo 1 (Lucro e Zero da Função): Um comerciante teve despesa de R$ 950,00 na compra de biquínis e vende cada peça por R$ 50,00. A função lucro é f(x) = 50x - 950. "
            "Fazendo f(x) = 0: 50x - 950 = 0 → 50x = 950 → x = 19. Logo, terá lucro a partir de 20 peças vendidas.\n"
            "• Exemplo 2 (Zero da Função): Para f(x) = 2x - 4, fazemos 2x - 4 = 0 → 2x = 4 → x = 2.\n"
            "• Exemplo 3 (Inequação): Resolva 3x + 19 < 40 → 3x < 40 - 19 → 3x < 21 → x < 7."
        ),
        cont_texto_resumo="Definição e classificação de funções (injetora, sobrejetora, bijetora, inversa e composta), estudo da função afim f(x) = ax + b, coeficientes angular e linear, gráfico, zero da função e inequações do 1º grau.",
        cont_slide_pdf="IFUNÇÃO F.A.pdf",
        cont_relacionados={
            "topicos": [
                "Função Quadrática",
                "Equação do 1º Grau",
                "Inequações do 1º Grau",
            ]
        },
    )
    db.add(conteudo4)
    db.flush()

    questoes = [
        Questao(
            ques_cont_id=conteudo4.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.MEDIO,
            ques_enunciado=(
                "1 - (UFMA) Considere as seguintes afirmações:\n"
                "I. Uma função é uma relação que associa a cada elemento do seu domínio um único elemento no seu contradomínio.\n"
                "II. Toda relação é uma função.\n"
                "III. Dada uma função sobrejetora, então seu contradomínio é diferente de sua imagem.\n"
                "IV. Uma função será injetora se, e somente se, elementos distintos do domínio possuírem imagens distintas.\n"
                "Assinale a alternativa correta:"
            ),
            ques_alternativas={
                "A": "a) I, II e III estão corretas.",
                "B": "b) I e II estão corretas.",
                "C": "c) III e I estão corretas.",
                "D": "d) II, III e IV estão corretas.",
                "E": "e) I e IV estão corretas.",
            },
            ques_resposta_correta=AlternativaEnum.E,
        ),
        Questao(
            ques_cont_id=conteudo4.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.FACIL,
            ques_enunciado="2 - Dada a função f: Z → Z definida por f(x) = 2x, podemos afirmar que f é:",
            ques_alternativas={
                "A": "a) Apenas sobrejetora",
                "B": "b) Apenas injetora",
                "C": "c) Bijetora",
                "D": "d) Nem injetora e nem sobrejetora",
                "E": "e) Injetora e sobrejetora apenas para os números ímpares",
            },
            ques_resposta_correta=AlternativaEnum.B,
        ),
        Questao(
            ques_cont_id=conteudo4.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.MEDIO,
            ques_enunciado="3 - Seja f(x) = √(x - 2) inversível em todo o seu domínio. Se g(x) é função inversa de f(x), o valor de g(f(5)) é igual a:",
            ques_alternativas={
                "A": "a) 5",
                "B": "b) 4",
                "C": "c) 3",
                "D": "d) 2",
            },
            ques_resposta_correta=AlternativaEnum.A,
        ),
        Questao(
            ques_cont_id=conteudo4.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.FACIL,
            ques_enunciado="4 - Qual deve ser o valor de m para que a função definida por f(x) = (2m - 6)x + 4 seja decrescente?",
            ques_alternativas={
                "A": "a) m < 3",
                "B": "b) m > 3",
                "C": "c) m = 3",
                "D": "d) m ≥ 3",
            },
            ques_resposta_correta=AlternativaEnum.A,
        ),
        Questao(
            ques_cont_id=conteudo4.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.MEDIO,
            ques_enunciado="5 - (Cefet - MG - 2015) Um motorista de táxi cobra, para cada corrida, uma taxa fixa de R$ 5,00 e mais R$ 2,00 por quilômetro rodado. O valor total arrecadado (R) num dia é função da quantidade total (x) de quilômetros percorridos e calculado por meio da função R(x) = ax + b, em que a é o preço cobrado por quilômetro e b, a soma de todas as taxas fixas recebidas no dia. Se, em um dia, o taxista realizou 10 corridas e arrecadou R$ 410,00, então a média de quilômetros rodados por corrida foi de:",
            ques_alternativas={
                "A": "a) 14",
                "B": "b) 16",
                "C": "c) 18",
                "D": "d) 20",
            },
            ques_resposta_correta=AlternativaEnum.C,
        ),
        Questao(
            ques_cont_id=conteudo4.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.DIFICIL,
            ques_enunciado="6 - (Unicamp - 2016) Considere a função afim f(x) = ax + b definida para todo número real x, onde a e b são números reais. Sabendo que f(4) = 2, podemos afirmar que f(f(3) + f(5)) é igual a:",
            ques_alternativas={
                "A": "a) 5",
                "B": "b) 4",
                "C": "c) 3",
                "D": "d) 2",
            },
            ques_resposta_correta=AlternativaEnum.D,
        ),
        Questao(
            ques_cont_id=conteudo4.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.FACIL,
            ques_enunciado="7 - (Encceja 2018) Uma prestadora de serviços cobra pela visita à residência do cliente e pelo tempo necessário para realizar o serviço na residência. O valor da visita é R$ 40 e o valor da hora para realização do serviço é R$ 20. Uma expressão que indica o valor a ser pago (P) em função das horas (h) necessárias à execução do serviço é:",
            ques_alternativas={
                "A": "A) P = 40h",
                "B": "B) P = 60h",
                "C": "C) P = 20 + 40h",
                "D": "D) P = 40 + 20h",
            },
            ques_resposta_correta=AlternativaEnum.D,
        ),
        Questao(
            ques_cont_id=conteudo4.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.FACIL,
            ques_enunciado="8 - (UFSM) Sabe-se que o preço a ser pago por uma corrida de táxi inclui uma parcela fixa, que é denominada bandeirada, e uma parcela variável, que é função da distância percorrida. Se o preço da bandeirada é de R$ 4,60 e o quilômetro rodado é R$ 0,96, a distância percorrida pelo passageiro que pagou R$ 19 para ir de sua casa ao shopping é de:",
            ques_alternativas={
                "A": "A) 5 km",
                "B": "B) 10 km",
                "C": "C) 15 km",
                "D": "D) 20 km",
                "E": "E) 25 km",
            },
            ques_resposta_correta=AlternativaEnum.C,
        ),
        Questao(
            ques_cont_id=conteudo4.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.FACIL,
            ques_enunciado="9 - Podemos afirmar que o zero da função f(x) = -2x + 5 é igual a:",
            ques_alternativas={
                "A": "A) 2",
                "B": "B) 2,5",
                "C": "C) -2,5",
                "D": "D) -3",
                "E": "E) 3",
            },
            ques_resposta_correta=AlternativaEnum.B,
        ),
        Questao(
            ques_cont_id=conteudo4.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.MEDIO,
            ques_enunciado="10 - Um fazendeiro resolveu investir em uma colheitadeira para facilitar o serviço na plantação. Sabendo que o valor pago foi de R$ 300.000 no ano da compra, é bastante comum que máquinas desse porte percam o seu valor V ao decorrer dos anos t. Supondo que a taxa de depreciação de uma máquina desse porte é de R$ 22.000 por ano, devido ao seu constante uso, podemos afirmar que o valor da colheitadeira, ao final de 7 anos, será de:",
            ques_alternativas={
                "A": "A) R$ 154.000",
                "B": "B) R$ 246.000",
                "C": "C) R$ 146.000",
                "D": "D) R$ 174.000",
                "E": "E) R$ 210.000",
            },
            ques_resposta_correta=AlternativaEnum.C,
        ),
    ]

    db.add_all(questoes)
    db.commit()

# CONTEÚDO 5 (Função Quadrática, Exponencial e Logarítmica)
def povoar_conteudo_5(db: Session):
    conteudo5 = Conteudo(
        cont_nome="Função Quadrática, Exponencial e Logarítmica",
        cont_etapa=EtapaEnum.ETAPA_1,
        cont_texto=(
            "1. FUNÇÃO QUADRÁTICA (FUNÇÃO DO 2º GRAU)\n"
            "Definição: É toda função f: R → R definida pela lei de formação f(x) = ax² + bx + c, com a, b e c reais e a ≠ 0.\n\n"
            "Gráfico (Parábola):\n"
            "• Concavidade: Se a > 0, a concavidade é voltada para cima (ponto de mínimo). Se a < 0, a concavidade é voltada para baixo (ponto de máximo).\n"
            "• Interseção com o eixo y: Ocorre no ponto (0, c). Se b > 0, cruza o eixo y na subida; se b < 0, cruza na descida.\n"
            "• Discriminante (Δ = b² - 4ac) e raízes (eixo x): Se Δ > 0, corta o eixo x em dois pontos distintos; se Δ = 0, toca o eixo x em apenas um ponto; se Δ < 0, não corta o eixo x.\n\n"
            "Raízes e Vértice da Parábola:\n"
            "• Fórmula de Bhaskara: x = (-b ± √Δ) / 2a.\n"
            "• Vértice da parábola: V = (xv, yv), em que xv = -b / 2a e yv = -Δ / 4a.\n\n"
            "Inequação do 2º Grau:\n"
            "• Expressão algébrica com desigualdade (ax² + bx + c > 0, < 0, ≥ 0 ou ≤ 0). Para resolver, determinam-se as raízes da equação correspondente e analisa-se o estudo de sinais da parábola nos intervalos reais.\n\n"
            "2. FUNÇÃO EXPONENCIAL\n"
            "Definição: É toda função f: R → R*+ definida por f(x) = a^x, em que a variável está no expoente e a base satisfaz a > 0 e a ≠ 1.\n\n"
            "Gráfico e Classificação:\n"
            "• O gráfico passa sempre pelo ponto (0, 1), pois a⁰ = 1, e nunca toca o eixo x (imagem sempre positiva, localizada nos quadrantes I e II).\n"
            "• Função Crescente: quando a > 1 (ex.: y = 2^x).\n"
            "• Função Decrescente: quando 0 < a < 1 (ex.: y = 0,5^x).\n\n"
            "Inequação Exponencial:\n"
            "• Igualam-se as bases nos dois membros da desigualdade:\n"
            "  - Se a > 1, mantém-se o sinal da desigualdade: a^x > a^y → x > y.\n"
            "  - Se 0 < a < 1, inverte-se o sinal da desigualdade: a^x > a^y → x < y.\n\n"
            "3. FUNÇÃO LOGARÍTMICA\n"
            "Definição: É a função inversa da exponencial, definida de R*+ → R por f(x) = log_a(x), com base a > 0 e a ≠ 1, em que log_a(x) = y ⇔ a^y = x.\n\n"
            "Domínio e Gráfico:\n"
            "• Condição de existência: o logaritmando deve ser estritamente positivo (x > 0).\n"
            "• O gráfico situa-se nos quadrantes I e IV, não toca o eixo y e intercepta o eixo x no ponto (1, 0), pois log_a(1) = 0.\n"
            "• Crescente quando a > 1 (ex.: f(x) = log₂(x)) e decrescente quando 0 < a < 1 (ex.: f(x) = log₀,₅(x)).\n\n"
            "4. EXEMPLOS RESOLVIDOS\n"
            "• Raízes e Vértice: Para f(x) = x² - 5x + 6 (a = 1, b = -5, c = 6), temos Δ = 1, raízes x₁ = 2 e x₂ = 3, e vértice V = (2,5; -0,25).\n"
            "• Inequação Exponencial: 2^x < 8 → 2^x < 2³ → x < 3.\n"
            "• Domínio Logarítmico: Em f(x) = log₂(x + 3), impõe-se x + 3 > 0 → x > -3.\n"
            "• Cálculo com Logaritmos: Dadas f(x) = log₂(x) e g(x) = log₁/₂(x), tem-se f(2) = 1 e g(2) = -1, logo f(2) - g(2) = 1 - (-1) = 2."
        ),
        cont_texto_resumo="Estudo da função quadrática (parábola, raízes por Bhaskara, vértice e inequações do 2º grau), função exponencial (crescimento, decrescimento e inequações exponenciais) e função logarítmica (definição, domínio, gráfico e propriedades).",
        cont_slide_pdf="IFUNÇÃO 1° FQ_2.pdf",
        cont_relacionados={
            "topicos": [
                "Função Afim",
                "Equação do 2º Grau",
                "Logaritmos",
            ]
        },
    )
    db.add(conteudo5)
    db.flush()

    questoes = [
        Questao(
            ques_cont_id=conteudo5.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.MEDIO,
            ques_enunciado="1 - (UERJ - 2016) Observe a função f, definida por f(x) = x² - 2kx + 29. Se f(x) ≥ 4, para todo número real x, o valor mínimo da função f é 4. Assim, o valor positivo do parâmetro k é:",
            ques_alternativas={
                "A": "a) 5",
                "B": "b) 6",
                "C": "c) 10",
                "D": "d) 15",
            },
            ques_resposta_correta=AlternativaEnum.A,
        ),
        Questao(
            ques_cont_id=conteudo5.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.FACIL,
            ques_enunciado="2 - Dada a função f(x) = x² - 4x + 5, o valor de f(2) é:",
            ques_alternativas={
                "A": "A) 0.",
                "B": "B) 1.",
                "C": "C) 3.",
                "D": "D) 4.",
                "E": "E) 7.",
            },
            ques_resposta_correta=AlternativaEnum.B,
        ),
        Questao(
            ques_cont_id=conteudo5.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.FACIL,
            ques_enunciado="3 - A concavidade da parábola da função f(x) = -3x² + 2x + 1 é:",
            ques_alternativas={
                "A": "A) voltada para cima.",
                "B": "B) inexistente.",
                "C": "C) voltada para baixo.",
                "D": "D) vertical.",
                "E": "E) horizontal.",
            },
            ques_resposta_correta=AlternativaEnum.C,
        ),
        Questao(
            ques_cont_id=conteudo5.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.MEDIO,
            ques_enunciado="4 - A trajetória de uma bola chutada é descrita pela função h(t) = -5t² + 20t, em que h(t) é a altura em metros e t é o tempo em segundos. A altura máxima atingida pela bola é:",
            ques_alternativas={
                "A": "A) 10 m.",
                "B": "B) 15 m.",
                "C": "C) 20 m.",
                "D": "D) 25 m.",
                "E": "E) 30 m.",
            },
            ques_resposta_correta=AlternativaEnum.C,
        ),
        Questao(
            ques_cont_id=conteudo5.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.FACIL,
            ques_enunciado="5 - Dada a função f(x) = 2^(x+3) + 10, o valor de x para que f(x) = 42 é de:",
            ques_alternativas={
                "A": "A) 2",
                "B": "B) 3",
                "C": "C) 4",
                "D": "D) 5",
                "E": "E) 6",
            },
            ques_resposta_correta=AlternativaEnum.A,
        ),
        Questao(
            ques_cont_id=conteudo5.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.MEDIO,
            ques_enunciado="6 - O gráfico, a seguir, é a representação de uma função exponencial decrescente que passa pelos pontos (-1, 2) e (0, 1). Analisando o gráfico, a lei de formação dessa função exponencial é:",
            ques_alternativas={
                "A": "A) f(x) = 5^x",
                "B": "B) f(x) = 0,2^x",
                "C": "C) f(x) = 2^x",
                "D": "D) f(x) = 0,5^x",
                "E": "E) f(x) = 0,5^(-x)",
            },
            ques_resposta_correta=AlternativaEnum.D,
        ),
        Questao(
            ques_cont_id=conteudo5.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.FACIL,
            ques_enunciado=(
                "7 - Dada uma função de R → R com a lei de formação f(x) = a^x, em que a é um número positivo diferente de 1, julgue as afirmativas a seguir:\n"
                "I → Essa função será crescente se a for positivo.\n"
                "II → Se x = 0, então, f(x) = 1.\n"
                "III → Essa é uma função exponencial.\n"
                "Marque a alternativa correta:"
            ),
            ques_alternativas={
                "A": "A) Somente a afirmativa I é falsa.",
                "B": "B) Somente a afirmativa II é falsa.",
                "C": "C) Somente a afirmativa III é falsa.",
                "D": "D) Todas as afirmativas são verdadeiras.",
                "E": "E) Todas as afirmativas são falsas.",
            },
            ques_resposta_correta=AlternativaEnum.A,
        ),
        Questao(
            ques_cont_id=conteudo5.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.DIFICIL,
            ques_enunciado="8 - Observe o gráfico da função logarítmica que possui assíntota vertical em x = 3 e corta o eixo x no ponto (4, 0) (translação horizontal de 3 unidades para a direita em relação a y = log₂(x)). A função representada no gráfico pode ser definida como:",
            ques_alternativas={
                "A": "a) f(x) = log₂(x - 3)",
                "B": "b) f(x) = log₂(x + 3)",
                "C": "c) f(x) = log₃(x - 2)",
                "D": "d) f(x) = log₃(x + 2)",
            },
            ques_resposta_correta=AlternativaEnum.A,
        ),
        Questao(
            ques_cont_id=conteudo5.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.FACIL,
            ques_enunciado="9 - Seja f(x) = log₂(x) e g(x) = log₃(x) a lei de formação de duas funções f(x) e g(x), então o valor de f(8) – g(9) é igual a:",
            ques_alternativas={
                "A": "A) 0.",
                "B": "B) 1.",
                "C": "C) 2.",
                "D": "D) –1.",
                "E": "E) –2.",
            },
            ques_resposta_correta=AlternativaEnum.B,
        ),
        Questao(
            ques_cont_id=conteudo5.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.MEDIO,
            ques_enunciado="10 - Durante os estudos sobre o crescimento de uma determinada árvore, foi possível modelar o crescimento dela no decorrer do tempo por meio da função A(t) = 1 + log₃(5 + t), em que t é o tempo em anos e A(t) é a altura em metros. Sendo assim, podemos afirmar que a altura dessa árvore, após 4 anos, será de:",
            ques_alternativas={
                "A": "A) 1 metro.",
                "B": "B) 2 metros.",
                "C": "C) 2 metros e meio.",
                "D": "D) 3 metros.",
                "E": "E) 3 metros e meio.",
            },
            ques_resposta_correta=AlternativaEnum.D,
        ),
    ]

    db.add_all(questoes)
    db.commit()

# CONTEÚDO 6 (Geometria Plana - Teorema de Tales, Semelhança e Relações Métricas)
def povoar_conteudo_6(db: Session):
    conteudo6 = Conteudo(
        cont_nome="Geometria Plana (Teorema de Tales, Semelhança e Relações Métricas)",
        cont_etapa=EtapaEnum.ETAPA_1,
        cont_texto=(
            "1. TEOREMA DE TALES\n"
            "Definição: Um feixe de retas paralelas determina sobre duas retas transversais segmentos proporcionais.\n"
            "• Se as retas paralelas r, s e t cortam duas transversais nos pontos A, B, C e D, E, F, respetivamente, temos:\n"
            "  AB / BC = DE / EF   e   AB / AC = DE / DF\n"
            "• Teorema de Tales em Triângulos: Ao traçar uma reta paralela à base de um triângulo que interceta os outros dois lados, "
            "formam-se segmentos laterais proporcionais e um triângulo menor semelhante ao triângulo maior.\n\n"
            "2. SEMELHANÇA DE TRIÂNGULOS\n"
            "Dois triângulos são semelhantes (~) quando possuem os três ângulos ordenadamente congruentes (mesma medida) e os lados correspondentes proporcionais.\n"
            "• Casos de Semelhança:\n"
            "  - 1º Caso (AA - Ângulo, Ângulo): dois ângulos de um triângulo são congruentes a dois do outro.\n"
            "  - 2º Caso (LLL - Lado, Lado, Lado): os três lados de um triângulo são proporcionais aos três lados do outro.\n"
            "  - 3º Caso (LAL - Lado, Ângulo, Lado): possuem um ângulo congruente compreendido entre dois lados proporcionais.\n"
            "• Teorema Fundamental da Semelhança: Toda reta paralela a um dos lados de um triângulo que interceta os outros dois lados determina um segundo triângulo semelhante ao primeiro.\n\n"
            "3. RELAÇÕES MÉTRICAS NO TRIÂNGULO RETÂNGULO\n"
            "Num triângulo retângulo (ângulo interno de 90°), o lado oposto ao ângulo reto é a hipotenusa (a) e os outros dois lados são os catetos (b e c). "
            "Ao traçar a altura (h) relativa à hipotenusa, definem-se as projeções m (do cateto c) e n (do cateto b) sobre a hipotenusa:\n"
            "• a = m + n\n"
            "• a · h = b · c\n"
            "• b² = a · n\n"
            "• c² = a · m\n"
            "• h² = m · n\n\n"
            "4. TEOREMA DE PITÁGORAS\n"
            "Enunciado: A hipotenusa ao quadrado é igual à soma dos quadrados dos catetos:\n"
            "• Fórmula: a² = b² + c²\n\n"
            "5. EXEMPLOS RESOLVIDOS\n"
            "• Exemplo 1 (Teorema de Tales): Numa proporção entre transversais, 10 / x = 12 / 7 → 12x = 70 → x ≈ 5,83.\n"
            "• Exemplo 2 (Tales em Triângulos - IFG): No triângulo ABC, com DE paralelo a BC, AC = 50 cm, AE = 20 cm e AD = 10 cm: "
            "50 / 20 = AB / 10 → 20 · AB = 500 → AB = 25 cm.\n"
            "• Exemplo 3 (Relações Métricas e Área): Num triângulo retângulo de lados 10 cm, 8 cm e 6 cm, a hipotenusa é 10 cm. "
            "Usando a · h = b · c → 10 · h = 8 · 6 → h = 4,8 cm. A área será A = (10 · 4,8) / 2 = 24 cm².\n"
            "• Exemplo 4 (Teorema de Pitágoras): Com hipotenusa 10 cm e um cateto de 8 cm: 10² = b² + 8² → 100 = b² + 64 → b² = 36 → b = 6 cm."
        ),
        cont_texto_resumo="Estudo do Teorema de Tales em feixes de paralelas e triângulos, casos de semelhança de triângulos (AA, LLL, LAL), relações métricas no triângulo retângulo e Teorema de Pitágoras.",
        cont_slide_pdf="GP 1° ANO_2.pdf",
        cont_relacionados={
            "topicos": [
                "Teorema de Tales",
                "Semelhança de Triângulos",
                "Teorema de Pitágoras",
                "Trigonometria no Triângulo Retângulo",
            ]
        },
    )
    db.add(conteudo6)
    db.flush()

    questoes = [
        Questao(
            ques_cont_id=conteudo6.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.MEDIO,
            ques_enunciado="1 - Considere o triângulo ABC e determine o valor de x, sabendo que o segmento AD é a bissetriz relativa ao lado BC e determina os segmentos proporcionais na razão (3x + 3) / 12 = (6x - 3) / 21.",
            ques_alternativas={
                "A": "a) 9",
                "B": "b) 10",
                "C": "c) 11",
                "D": "d) 12",
                "E": "e) 13",
            },
            ques_resposta_correta=AlternativaEnum.C,
        ),
        Questao(
            ques_cont_id=conteudo6.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.FACIL,
            ques_enunciado="2 - As retas t, u e v são paralelas. Aplicando o Teorema de Tales às retas transversais da figura, determine o valor da medida do segmento x.",
            ques_alternativas={
                "A": "a) 18",
                "B": "b) 20",
                "C": "c) 21",
                "D": "d) 22",
                "E": "e) 24",
            },
            ques_resposta_correta=AlternativaEnum.C,
        ),
        Questao(
            ques_cont_id=conteudo6.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.FACIL,
            ques_enunciado="3 - Existem 5 bolas dispostas em uma mesa de bilhar. A reta formada entre as bolas 1 e 2 é paralela à reta formada entre as bolas 4 e 5. Conforme as medidas dispostas na imagem responda: qual a distância entre as bolas 1 e 3?",
            ques_alternativas={
                "A": "a) 20 cm",
                "B": "b) 30 cm",
                "C": "c) 40 cm",
                "D": "d) 50 cm",
                "E": "e) 60 cm",
            },
            ques_resposta_correta=AlternativaEnum.C,
        ),
        Questao(
            ques_cont_id=conteudo6.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.MEDIO,
            ques_enunciado=(
                "4 - (Colégio Pedro II - 2012) Para melhorar a qualidade do solo, aumentando a produtividade do milho e da soja, em uma fazenda é feito o rodízio entre essas culturas e a área destinada ao pasto. Com essa finalidade, a área produtiva da fazenda foi dividida em três partes conforme a figura.\n"
                "Considere que:\n"
                "• os pontos A, B, C e D estão alinhados;\n"
                "• os pontos H, G, F e E estão alinhados;\n"
                "• os segmentos AH, BG, CF e DE são, dois a dois, paralelos entre si;\n"
                "• AB = 500 m, BC = 600 m, CD = 700 m e HE = 1980 m.\n"
                "Nessas condições, a medida do segmento GF é, em metros:"
            ),
            ques_alternativas={
                "A": "a) 665.",
                "B": "b) 660.",
                "C": "c) 655.",
                "D": "d) 650.",
                "E": "e) 645.",
            },
            ques_resposta_correta=AlternativaEnum.B,
        ),
        Questao(
            ques_cont_id=conteudo6.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.MEDIO,
            ques_enunciado="5 - (Enem - 2009) A rampa de um hospital tem na sua parte mais elevada uma altura de 2,2 metros. Um paciente ao caminhar sobre a rampa percebe que se deslocou 3,2 metros e alcançou uma altura de 0,8 metros. A distância em metros que o paciente ainda deve caminhar para atingir o ponto mais alto da rampa é:",
            ques_alternativas={
                "A": "a) 1,16 metros.",
                "B": "b) 3,0 metros.",
                "C": "c) 5,4 metros.",
                "D": "d) 5,6 metros.",
                "E": "e) 7,04 metros.",
            },
            ques_resposta_correta=AlternativaEnum.D,
        ),
        Questao(
            ques_cont_id=conteudo6.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.MEDIO,
            ques_enunciado="6 - Existem alguns procedimentos que podem ser usados para descobrir se dois triângulos são semelhantes sem ter de analisar a proporcionalidade de todos os lados e, ao mesmo tempo, as medidas de todos os ângulos desses triângulos. A respeito desses casos, assinale a alternativa correta:",
            ques_alternativas={
                "A": "a) Para que dois triângulos sejam semelhantes, basta que eles tenham três ângulos correspondentes congruentes.",
                "B": "b) Para que dois triângulos sejam semelhantes, basta que eles tenham dois lados proporcionais e um ângulo congruente, em qualquer ordem.",
                "C": "c) Para que dois triângulos sejam congruentes, basta que eles tenham os três lados correspondentes com medidas proporcionais.",
                "D": "d) Dois triângulos que possuem dois lados correspondentes proporcionais não serão semelhantes em qualquer hipótese.",
                "E": "e) Dois triângulos que possuem apenas dois ângulos correspondentes congruentes não podem ser considerados semelhantes.",
            },
            ques_resposta_correta=AlternativaEnum.A,
        ),
        Questao(
            ques_cont_id=conteudo6.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.FACIL,
            ques_enunciado="7 - Na imagem a seguir, é possível perceber dois triângulos que compartilham parte de dois lados. Sabendo que os segmentos BA e DE são paralelos, qual a medida de x?",
            ques_alternativas={
                "A": "a) 210 m",
                "B": "b) 220 m",
                "C": "c) 230 m",
                "D": "d) 240 m",
                "E": "e) 250 m",
            },
            ques_resposta_correta=AlternativaEnum.E,
        ),
        Questao(
            ques_cont_id=conteudo6.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.FACIL,
            ques_enunciado="8 - Carla ao procurar seu gatinho o avistou em cima de uma árvore. Ela então pediu ajuda a sua mãe e colocaram uma escada junto à árvore para ajudar o gato a descer. Sabendo que o gato estava a 8 metros do chão e a base da escada estava posicionada a 6 metros da árvore, qual o comprimento da escada utilizada para salvar o gatinho?",
            ques_alternativas={
                "A": "a) 8 metros.",
                "B": "b) 10 metros.",
                "C": "c) 12 metros.",
                "D": "d) 14 metros.",
            },
            ques_resposta_correta=AlternativaEnum.B,
        ),
        Questao(
            ques_cont_id=conteudo6.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.DIFICIL,
            ques_enunciado="9 - (IFRJ - 2013) O pátio de esportes do Campus Arrozal de um Instituto Federal é retangular, com 100 m de comprimento e 50 m de largura, representado pelo retângulo ABCD desta figura. Alberto e Bruno são dois alunos, que estão praticando esportes no pátio. Alberto caminha do ponto A ao ponto C pela diagonal do retângulo e volta ao ponto de partida pelo mesmo caminho. Bruno parte do ponto B, dá uma volta completa no pátio, andando pelas linhas laterais, e volta ao ponto de partida. Assim, considerando √5 = 2,24, afirma-se que Bruno andou mais que Alberto:",
            ques_alternativas={
                "A": "a) 38 m.",
                "B": "b) 64 m.",
                "C": "c) 76 m.",
                "D": "d) 82 m.",
            },
            ques_resposta_correta=AlternativaEnum.C,
        ),
        Questao(
            ques_cont_id=conteudo6.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.MEDIO,
            ques_enunciado=(
                "10 - Em um triângulo retângulo ABC, com ângulo reto em A, a altura relativa à hipotenusa encontra-a no ponto H. Denotam-se por m e n as projeções dos catetos e por h a altura. Considere as afirmações:\n"
                "I. h² = m · n\n"
                "II. b² = a · n\n"
                "III. c² = a · m\n"
                "IV. a · h = b + c\n"
                "É correto afirmar que são verdadeiras apenas:"
            ),
            ques_alternativas={
                "A": "a) I, II e III",
                "B": "b) I, II e IV",
                "C": "c) I, III e IV",
                "D": "d) II, III e IV",
            },
            ques_resposta_correta=AlternativaEnum.A,
        ),
    ]

    db.add_all(questoes)
    db.commit()

# CONTEÚDO 7 (Frações Decimais, Dízimas Periódicas e Intervalos Reais)
def povoar_conteudo_7(db: Session):
    conteudo7 = Conteudo(
        cont_nome="Frações Decimais, Dízimas Periódicas e Intervalos Reais",
        cont_etapa=EtapaEnum.ETAPA_1,
        cont_texto=(
            "1. REPRESENTAÇÃO DECIMAL DE FRAÇÕES\n"
            "Uma fração decimal é toda fração cujo denominador é uma potência de 10 (10⁰ = 1, 10¹ = 10, 10² = 100, 10³ = 1000, ...). "
            "Para transformá-la em número decimal, o número de zeros do denominador indica a quantidade de casas decimais após a vírgula:\n"
            "• Exemplos: 23 / 10 = 2,3 (um zero → uma casa decimal); 23 / 100 = 0,23 (dois zeros → duas casas decimais).\n\n"
            "2. DÍZIMAS PERIÓDICAS\n"
            "As dízimas periódicas são números decimais infinitos que apresentam um ou mais algarismos que se repetem na mesma ordem infinitamente (chamado de período). "
            "Pertencem ao conjunto dos números racionais (Q), pois podem ser escritas na forma de fração.\n"
            "• Período vs. Padrão: Números decimais infinitos sem repetição periódica (como 1,1212314... ou 1,232324...) não são dízimas periódicas, mas sim números irracionais (I).\n"
            "• Dízima Periódica Simples: Não possui antiperíodo; o período surge imediatamente após a vírgula (ex.: 0,323232..., período = 32).\n"
            "• Dízima Periódica Composta: Possui um antiperíodo (parte decimal que não se repete) entre a vírgula e o período (ex.: 2,324444..., antiperíodo = 32, período = 4).\n\n"
            "3. FRAÇÃO GERATRIZ\n"
            "É a fração que dá origem à dízima periódica ao dividir o numerador pelo denominador:\n"
            "• Dízima Simples (Método Algébrico): Nomeia-se a dízima como x, multiplica-se por 10^n (sendo n o número de algarismos do período) e subtrai-se a equação original.\n"
            "  - Exemplo: x = 0,323232... → 100x = 32,323232... → 100x - x = 32 → 99x = 32 → x = 32/99.\n"
            "  - Regra prática: Na dízima 3,1717..., o período tem 2 algarismos (denominador 99), logo x = (317 - 3) / 99 = 314/99.\n"
            "• Dízima Composta: Multiplica-se primeiro por uma potência de 10 para deslocar o antiperíodo para antes da vírgula e depois aplica-se o processo da dízima simples.\n"
            "  - Exemplo: x = 2,34555... → 100x = 234,555... e 1000x = 2345,555... → 900x = 2345 - 234 → x = 2111/900.\n\n"
            "4. INTERVALOS REAIS\n"
            "São subconjuntos do conjunto dos números reais (R). Dados dois números reais a e b, com a < b, temos:\n"
            "• Intervalo aberto: ]a, b[ = {x ∈ R | a < x < b} (os extremos a e b não pertencem ao intervalo; bolinha aberta).\n"
            "• Intervalo fechado: [a, b] = {x ∈ R | a ≤ x ≤ b} (os extremos a e b pertencem ao intervalo; bolinha fechada).\n"
            "• Intervalo fechado à esquerda e aberto à direita: [a, b[ = {x ∈ R | a ≤ x < b}.\n"
            "• Intervalo aberto à esquerda e fechado à direita: ]a, b] = {x ∈ R | a < x ≤ b}.\n"
            "• Intervalos infinitos: Sempre abertos no infinito (ex.: ]-3, +∞[ = {x ∈ R | x > -3})."
        ),
        cont_texto_resumo="Estudo das frações decimais, dízimas periódicas simples e compostas, cálculo da fração geratriz e representação algébrica e geométrica de intervalos reais.",
        cont_slide_pdf="IFUNÇÃO 1° ano.pdf",
        cont_relacionados={
            "topicos": [
                "Conjuntos Numéricos",
                "Números Racionais e Irracionais",
                "Fração Geratriz",
                "Intervalos Reais",
            ]
        },
    )
    db.add(conteudo7)
    db.flush()

    questoes = [
        Questao(
            ques_cont_id=conteudo7.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.MEDIO,
            ques_enunciado="1 - Qual é a fração irredutível geratriz da dízima periódica 1,2431313131...?",
            ques_alternativas={
                "A": "a) 12431/1000",
                "B": "b) 12431/9900",
                "C": "c) 12307/1000",
                "D": "d) 12307/9900",
            },
            ques_resposta_correta=AlternativaEnum.D,
        ),
        Questao(
            ques_cont_id=conteudo7.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.MEDIO,
            ques_enunciado=(
                "2 - Analise as afirmativas abaixo:\n"
                "I. Os números decimais exatos são assim chamados por possuírem uma representação decimal finita.\n"
                "II. O número 0,1010010001... é uma dízima periódica.\n"
                "III. Uma fração irredutível só terá representação decimal exata se o denominador tiver apenas os fatores primos 2 ou 5.\n"
                "IV. A fração geratriz da dízima 0,777... é 7/9.\n"
                "São verdadeiras:"
            ),
            ques_alternativas={
                "A": "a) I, II e III",
                "B": "b) I, II e IV",
                "C": "c) II, III e IV",
                "D": "d) I, III e IV",
            },
            ques_resposta_correta=AlternativaEnum.D,
        ),
        Questao(
            ques_cont_id=conteudo7.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.FACIL,
            ques_enunciado="3 - O valor da soma 0,232323... + 0,878787... vale:",
            ques_alternativas={
                "A": "a) 1",
                "B": "b) 1,0101...",
                "C": "c) 1,1111…",
                "D": "d) 1,1010...",
            },
            ques_resposta_correta=AlternativaEnum.C,
        ),
        Questao(
            ques_cont_id=conteudo7.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.MEDIO,
            ques_enunciado="4 - (PUC/RJ - 2003) A soma 1,3333... + 0,16666... é igual a:",
            ques_alternativas={
                "A": "a) 1/2",
                "B": "b) 1",
                "C": "c) 4/3",
                "D": "d) 5/3",
                "E": "e) 3/2",
            },
            ques_resposta_correta=AlternativaEnum.E,
        ),
        Questao(
            ques_cont_id=conteudo7.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.FACIL,
            ques_enunciado="5 - Seja x = 1,123123… A diferença entre o numerador e o denominador da sua representação fracionária é:",
            ques_alternativas={
                "A": "A) 123.",
                "B": "B) 999.",
                "C": "C) 321.",
                "D": "D) 112.",
                "E": "E) 1122.",
            },
            ques_resposta_correta=AlternativaEnum.A,
        ),
        Questao(
            ques_cont_id=conteudo7.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.FACIL,
            ques_enunciado=(
                "6 - Analise os números reais a seguir:\n"
                "I. 4/6\n"
                "II. 0,4555...\n"
                "III. π\n"
                "IV. 1/2\n"
                "Podemos escrever como uma dízima periódica:"
            ),
            ques_alternativas={
                "A": "A) somente II e III.",
                "B": "B) somente I e II.",
                "C": "C) somente III e IV.",
                "D": "D) somente I, II e III.",
                "E": "E) somente II, III e IV.",
            },
            ques_resposta_correta=AlternativaEnum.B,
        ),
        Questao(
            ques_cont_id=conteudo7.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.MEDIO,
            ques_enunciado="7 - (Pref. de Niterói) Simplificando a expressão (1,333... + 3/2) / (1,5 + 4/3), obtém-se:",
            ques_alternativas={
                "A": "A) 0",
                "B": "B) 1",
                "C": "C) 4/3",
                "D": "D) 3/2",
                "E": "E) 17/6",
            },
            ques_resposta_correta=AlternativaEnum.B,
        ),
        Questao(
            ques_cont_id=conteudo7.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.FACIL,
            ques_enunciado="8 - A fração geratriz da dízima 15,2222… é:",
            ques_alternativas={
                "A": "A) 152/9",
                "B": "B) 152/90",
                "C": "C) 137/9",
                "D": "D) 137/99",
                "E": "E) 15/2",
            },
            ques_resposta_correta=AlternativaEnum.C,
        ),
        Questao(
            ques_cont_id=conteudo7.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.FACIL,
            ques_enunciado="9 - A fração geratriz da dízima periódica 1,44444... é:",
            ques_alternativas={
                "A": "a) 17/9.",
                "B": "b) 11/9.",
                "C": "c) 5/9.",
                "D": "d) 13/9.",
                "E": "e) 12/9.",
            },
            ques_resposta_correta=AlternativaEnum.D,
        ),
        Questao(
            ques_cont_id=conteudo7.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.MEDIO,
            ques_enunciado=(
                "10 - (Objetiva Concursos) Considerando-se os intervalos numéricos A = [-5, 21], B = [0, 12], C = [-1, 17], analisar os itens abaixo:\n"
                "I. O intervalo A contém os valores do intervalo B, assim como o intervalo B contém os valores do intervalo C.\n"
                "II. Os valores do intervalo C estão contidos no intervalo A, mas não estão contidos no intervalo B.\n"
                "III. Os valores do intervalo B estão contidos no intervalo C, e os valores do intervalo B estão contidos no intervalo A.\n"
                "Está(ão) CORRETO(S):"
            ),
            ques_alternativas={
                "A": "A) Somente o item I.",
                "B": "B) Somente o item III.",
                "C": "C) Somente os itens I e II.",
                "D": "D) Somente os itens I e III.",
                "E": "E) Somente os itens II e III.",
            },
            ques_resposta_correta=AlternativaEnum.E,
        ),
    ]

    db.add_all(questoes)
    db.commit()

def povoar_simulado_1(db: Session, base_url: str = "https://seu-storage-publico.com"):
    questoes = [
        Questao(
            ques_cont_id=None,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.FACIL,
            ques_enunciado=(
                "1 - (Enem 2020) Uma empresa de ônibus utiliza um sistema de vendas de passagens que fornece a imagem de todos os assentos do ônibus, "
                "diferenciando os assentos já vendidos, por uma cor mais escura, dos assentos ainda disponíveis. A empresa monitora, permanentemente, "
                "o número de assentos já vendidos e compara-o com o número total de assentos do ônibus para avaliar a necessidade de alocação de veículos extras. "
                "Na imagem tem-se a informação dos assentos já vendidos e dos ainda disponíveis em um determinado instante.\n"
                "A razão entre o número de assentos já vendidos e o total de assentos desse ônibus, no instante considerado na imagem, é:"
            ),
            ques_imagem_url=f"{base_url}/imagens/questoes/sim1_q01_assentos_onibus.png",
            ques_alternativas={"A": "a) 16/42", "B": "b) 16/26", "C": "c) 26/42", "D": "d) 42/26", "E": "e) 42/16"},
            ques_resposta_correta=AlternativaEnum.A,
            ques_resolucao="Contando os assentos na imagem, há 16 assentos escuros (já vendidos) em um total de 42 lugares. Assim, a razão procurada é 16/42.",
            ques_resolucao_imagem_url=f"{base_url}/imagens/respostas/sim1_r01_razao_assentos.png",
        ),
        Questao(
            ques_cont_id=None,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.MEDIO,
            ques_enunciado=(
                "2 - (Enem 2020) O consumo de espumantes no Brasil tem aumentado nos últimos anos. Uma das etapas do seu processo de produção consiste no "
                "envasamento da bebida em garrafas semelhantes às da imagem. Nesse processo, a vazão do líquido no interior da garrafa é constante e cessa "
                "quando atinge o nível de envasamento.\n"
                "Qual esboço de gráfico melhor representa a variação da altura do líquido em função do tempo, na garrafa indicada na imagem?"
            ),
            ques_imagem_url=f"{base_url}/imagens/questoes/sim1_q02_garrafa_graficos.png",
            ques_alternativas={
                "A": "a) Gráfico A",
                "B": "b) Gráfico B",
                "C": "c) Gráfico C",
                "D": "d) Gráfico D",
                "E": "e) Gráfico E",
            },
            ques_resposta_correta=AlternativaEnum.B,
            ques_resolucao=(
                "Como a vazão é constante: na 1ª seção (cilíndrica, de diâmetro constante), a altura cresce linearmente (reta inclinada). "
                "Na 2ª seção (afunilamento da garrafa), o diâmetro diminui com a altura, fazendo o nível subir cada vez mais rápido (curva crescente côncava para cima)."
            ),
            ques_resolucao_imagem_url=f"{base_url}/imagens/respostas/sim1_r02_secoes_garrafa.png",
        ),
        Questao(
            ques_cont_id=None,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.FACIL,
            ques_enunciado=(
                "3 - O estádio do Maracanã passou por algumas modificações estruturais para a realização da Copa do Mundo de 2014, como, por exemplo, "
                "as dimensões do campo retangular. Para se adaptar aos padrões da Fifa, as dimensões do campo foram reduzidas de 110 m × 75 m para 105 m × 68 m.\n"
                "Em quantos metros quadrados a área do campo do Maracanã foi reduzida?"
            ),
            ques_imagem_url=None,
            ques_alternativas={"A": "a) 24", "B": "b) 35", "C": "c) 555", "D": "d) 1110", "E": "e) 1145"},
            ques_resposta_correta=AlternativaEnum.D,
            ques_resolucao="Área original: 110 · 75 = 8.250 m². Área nova: 105 · 68 = 7.140 m². Redução: 8.250 - 7.140 = 1.110 m².",
            ques_resolucao_imagem_url=None,
        ),
        Questao(
            ques_cont_id=None,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.FACIL,
            ques_enunciado=(
                "4 - O uso de aplicativos de transporte tem sido uma alternativa à população que busca preços mais competitivos para se locomover, "
                "principalmente nas grandes cidades. Em geral, o valor V a ser pago, em real, varia em função de: tarifa base F (valor fixo), tempo T (em minuto) "
                "e distância D (em quilômetro). Um desses aplicativos cobra R$ 2,00 de valor fixo, acrescido de R$ 0,26 por minuto de viagem e de R$ 1,40 por quilômetro rodado.\n"
                "Nessas condições, a expressão que fornece o valor V a ser pago por uma viagem desse aplicativo é:"
            ),
            ques_imagem_url=None,
            ques_alternativas={
                "A": "a) 2,00F + 0,26T + 1,40D",
                "B": "b) 2,00 + 0,26T + 1,40D",
                "C": "c) 2,00 + 0,26T + D",
                "D": "d) 0,26T + 1,40D",
                "E": "e) F + T + D",
            },
            ques_resposta_correta=AlternativaEnum.B,
            ques_resolucao="Somando o valor fixo de R$ 2,00 ao custo por minuto (0,26T) e ao custo por quilômetro (1,40D), temos V = 2,00 + 0,26T + 1,40D.",
            ques_resolucao_imagem_url=None,
        ),
        Questao(
            ques_cont_id=None,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.FACIL,
            ques_enunciado=(
                "5 - Os 100 funcionários de uma empresa estão distribuídos em dois setores: Produção e Administração. Os funcionários de um mesmo setor "
                "recebem salários com valores iguais. O quadro apresenta a quantidade de funcionários por setor e seus respectivos salários.\n"
                "A média dos salários dos 100 funcionários dessa empresa, em real, é:"
            ),
            ques_imagem_url=f"{base_url}/imagens/questoes/sim1_q05_quadro_salarios.png",
            ques_alternativas={
                "A": "a) 2 000,00.",
                "B": "b) 2 500,00.",
                "C": "c) 3 250,00.",
                "D": "d) 4 500,00.",
                "E": "e) 9 000,00.",
            },
            ques_resposta_correta=AlternativaEnum.C,
            ques_resolucao="Média ponderada: (75 · 2.000 + 25 · 7.000) / 100 = (150.000 + 175.000) / 100 = 325.000 / 100 = R$ 3.250,00.",
            ques_resolucao_imagem_url=None,
        ),
        Questao(
            ques_cont_id=None,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.MEDIO,
            ques_enunciado=(
                "6 - O ideal é consumir 1 grama de carboidrato para cada minuto de caminhada. Um casal realizará diariamente 30 minutos de caminhada, "
                "ingerindo, antes dessa atividade, a quantidade ideal de carboidratos recomendada. Para ter o consumo ideal apenas por meio do consumo de "
                "pão de fôrma integral, o casal planeja garantir o suprimento de pães para um período de 30 dias ininterruptos. Sabe-se que cada pacote desse "
                "pão vem com 18 fatias, e que cada uma delas tem 15 gramas de carboidratos.\n"
                "A quantidade mínima de pacotes de pão de fôrma necessários para prover o suprimento a esse casal é:"
            ),
            ques_imagem_url=None,
            ques_alternativas={"A": "a) 6", "B": "b) 7", "C": "c) 8", "D": "d) 9", "E": "e) 10"},
            ques_resposta_correta=AlternativaEnum.B,
            ques_resolucao=(
                "Consumo diário do casal: 30 g · 2 pessoas = 60 g/dia. Em 30 dias: 60 · 30 = 1.800 g. "
                "Cada pacote fornece 18 · 15 = 270 g. Dividindo: 1.800 / 270 ≈ 6,67 pacotes, sendo necessários no mínimo 7 pacotes."
            ),
            ques_resolucao_imagem_url=None,
        ),
        Questao(
            ques_cont_id=None,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.FACIL,
            ques_enunciado=(
                "7 - Um investidor iniciante observou o gráfico que apresenta a evolução dos valores de duas criptomoedas A e B em relação ao tempo.\n"
                "Durante horas consecutivas, esses valores foram observados em nove instantes, representados por horas exatas.\n"
                "Em quantos desses instantes a criptomoeda A estava mais valorizada do que a criptomoeda B?"
            ),
            ques_imagem_url=f"{base_url}/imagens/questoes/sim1_q07_grafico_criptomoedas.png",
            ques_alternativas={"A": "a) 3", "B": "b) 4", "C": "c) 6", "D": "d) 7", "E": "e) 9"},
            ques_resposta_correta=AlternativaEnum.B,
            ques_resolucao="Comparando as coordenadas de A (eixo horizontal) e B (eixo vertical) em cada um dos 9 pontos, verifica-se que x_A > y_B em 4 instantes.",
            ques_resolucao_imagem_url=f"{base_url}/imagens/respostas/sim1_r07_diagonal_criptomoedas.png",
        ),
        Questao(
            ques_cont_id=None,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.MEDIO,
            ques_enunciado=(
                "8 - Um agricultor é informado sobre um método de proteção para sua lavoura que consiste em inserir larvas específicas, de rápida reprodução. "
                "A reprodução dessas larvas faz com que sua população multiplique-se por 10 a cada 3 dias e, para evitar eventuais desequilíbrios, é possível cessar "
                "essa reprodução aplicando-se um produto X. O agricultor decide iniciar esse método com 100 larvas e dispõe de 5 litros do produto X, cuja aplicação "
                "recomendada é de exatamente 1 litro para cada população de 200 000 larvas. A quantidade total do produto X de que ele dispõe deverá ser aplicada de uma única vez.\n"
                "Quantos dias após iniciado esse método o agricultor deverá aplicar o produto X?"
            ),
            ques_imagem_url=None,
            ques_alternativas={"A": "a) 2", "B": "b) 4", "C": "c) 6", "D": "d) 12", "E": "e) 18"},
            ques_resposta_correta=AlternativaEnum.D,
            ques_resolucao=(
                "Com 5 L, pode-se controlar 5 · 200.000 = 1.000.000 = 10⁶ larvas. "
                "Pela função exponencial P(t) = 100 · 10^(t/3) = 10⁶ → 10^(t/3) = 10⁴ → t/3 = 4 → t = 12 dias."
            ),
            ques_resolucao_imagem_url=None,
        ),
        Questao(
            ques_cont_id=None,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.FACIL,
            ques_enunciado=(
                "9 - Para concretar a laje de sua residência, uma pessoa contratou uma construtora. Tal empresa informa que o preço y do concreto bombeado é "
                "composto de duas partes: uma fixa, chamada de taxa de bombeamento, e uma variável, que depende do volume x de concreto utilizado. "
                "Sabe-se que a taxa de bombeamento custa R$ 500,00 e que o metro cúbico do concreto bombeado é de R$ 250,00.\n"
                "A expressão que representa o preço y em função do volume x, em metro cúbico, é:"
            ),
            ques_imagem_url=None,
            ques_alternativas={
                "A": "a) y = 250x",
                "B": "b) y = 500x",
                "C": "c) y = 750x",
                "D": "d) y = 250x + 500",
                "E": "e) y = 500x + 250",
            },
            ques_resposta_correta=AlternativaEnum.D,
            ques_resolucao="A função afim é formada pela parcela variável (250x) somada à taxa fixa de bombeamento (500), resultando em y = 250x + 500.",
            ques_resolucao_imagem_url=None,
        ),
        Questao(
            ques_cont_id=None,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.FACIL,
            ques_enunciado=(
                "10 - Entre maratonistas, um parâmetro utilizado é o de economia de corrida (EC). O valor desse parâmetro é calculado pela razão entre o consumo "
                "de oxigênio, em mililitro (mL) por minuto (min), e a massa, em quilograma (kg), do atleta correndo a uma velocidade constante.\n"
                "A unidade de medida da grandeza descrita pelo parâmetro EC é:"
            ),
            ques_imagem_url=None,
            ques_alternativas={
                "A": "a) min/mL.kg",
                "B": "b) mL/min . kg",
                "C": "c) min . mL/kg",
                "D": "d) min . kg/mL",
                "E": "e) mL . kg/min",
            },
            ques_resposta_correta=AlternativaEnum.B,
            ques_resolucao="Dividindo a unidade de consumo de oxigênio (mL/min) pela unidade de massa (kg), obtém-se (mL/min) / kg = mL / (min · kg).",
            ques_resolucao_imagem_url=None,
        ),
        Questao(
            ques_cont_id=None,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.MEDIO,
            ques_enunciado=(
                "11 - A figura ilustra uma roda-gigante no exato instante em que a cadeira onde se encontra a pessoa P está no ponto mais alto dessa roda-gigante.\n"
                "Com o passar do tempo, à medida que a roda-gigante gira, com velocidade angular constante e no sentido horário, a altura da cadeira onde se "
                "encontra a pessoa P, em relação ao solo, vai se alterando.\n"
                "O gráfico que melhor representa a variação dessa altura, em função do tempo, contado a partir do instante em que a cadeira da pessoa P se "
                "encontra na posição mais alta da roda-gigante, é:"
            ),
            ques_imagem_url=f"{base_url}/imagens/questoes/sim1_q11_roda_gigante.png",
            ques_alternativas={
                "A": "a) Gráfico A",
                "B": "b) Gráfico B",
                "C": "c) Gráfico C",
                "D": "d) Gráfico D",
                "E": "e) Gráfico E",
            },
            ques_resposta_correta=AlternativaEnum.A,
            ques_resolucao="O movimento circular uniforme descreve uma função cossenoidal suave que inicia no ponto máximo, desce até o mínimo e retorna ao máximo sem quinas.",
            ques_resolucao_imagem_url=None,
        ),
        Questao(
            ques_cont_id=None,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.MEDIO,
            ques_enunciado=(
                "12 - (Enem 2017) Em um teleférico turístico, bondinhos saem de estações ao nível do mar e do topo de uma montanha. A travessia dura 1,5 minuto "
                "e ambos os bondinhos se deslocam à mesma velocidade. Quarenta segundos após o bondinho A partir da estação ao nível do mar, ele cruza com o "
                "bondinho B, que havia saído do topo da montanha.\n"
                "Quantos segundos após a partida do bondinho B partiu o bondinho A?"
            ),
            ques_imagem_url=None,
            ques_alternativas={"A": "a) 5", "B": "b) 10", "C": "c) 15", "D": "d) 20", "E": "e) 25"},
            ques_resposta_correta=AlternativaEnum.B,
            ques_resolucao=(
                "A travessia total leva 1,5 min = 90 s. Como as velocidades são iguais, o ponto de encontro divide o percurso em trechos percorridos em 40 s e 50 s. "
                "Logo, B já viajava há 50 s quando cruzou com A (que viajava há 40 s), tendo partido 50 - 40 = 10 segundos antes."
            ),
            ques_resolucao_imagem_url=None,
        ),
        Questao(
            ques_cont_id=None,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.DIFICIL,
            ques_enunciado=(
                "13 - (Enem 2013) O dono de um sítio pretende colocar uma haste de sustentação para melhor firmar dois postes de comprimentos iguais a 6 m e 4 m. "
                "A figura representa a situação real na qual os postes são descritos pelos segmentos AC e BD e a haste é representada pelo segmento EF, "
                "todos perpendiculares ao solo, que é indicado pelo segmento de reta AB. Os segmentos AD e BC representam cabos de aço que serão instalados.\n"
                "Qual deve ser o valor do comprimento da haste EF?"
            ),
            ques_imagem_url=f"{base_url}/imagens/questoes/sim1_q13_postes_haste.png",
            ques_alternativas={"A": "a) 1 m", "B": "b) 2 m", "C": "c) 2,4 m", "D": "d) 3 m", "E": "e) 2√6 m"},
            ques_resposta_correta=AlternativaEnum.C,
            ques_resolucao=(
                "Por semelhança de triângulos, a altura EF é dada pelo produto das alturas dos postes dividido pela soma delas: "
                "h = (6 · 4) / (6 + 4) = 24 / 10 = 2,4 m."
            ),
            ques_resolucao_imagem_url=f"{base_url}/imagens/respostas/sim1_r13_semelhanca_postes.png",
        ),
        Questao(
            ques_cont_id=None,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.FACIL,
            ques_enunciado=(
                "14 - Um adolescente, tendo em vista uma alimentação saudável, consome diariamente 7,5 dL de leite durante 1 mês (30 dias). "
                "Sabe-se que o preço de um litro de leite é R$ 1,98.\n"
                "Nessas condições, o custo mensal com o consumo de leite desse adolescente é de:"
            ),
            ques_imagem_url=None,
            ques_alternativas={
                "A": "a) R$ 14,85",
                "B": "b) R$ 22,50",
                "C": "c) R$ 44,55",
                "D": "d) R$ 148,50",
                "E": "e) R$ 445,50",
            },
            ques_resposta_correta=AlternativaEnum.C,
            ques_resolucao="Convertendo: 7,5 dL = 0,75 L/dia. Em 30 dias: 0,75 · 30 = 22,5 L. Custo total: 22,5 · 1,98 = R$ 44,55.",
            ques_resolucao_imagem_url=None,
        ),
        Questao(
            ques_cont_id=None,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.FACIL,
            ques_enunciado=(
                "15 - (Enem 2020) Pesquisadores da Universidade de Tecnologia de Viena, na Áustria, produziram miniaturas de objetos em impressoras 3D de alta precisão. "
                "A escultura apresentada é uma miniatura de um carro de Fórmula 1, com 100 micrômetros de comprimento. Um micrômetro é a milionésima parte de um metro.\n"
                "Usando notação científica, qual é a representação do comprimento dessa miniatura, em metro?"
            ),
            ques_imagem_url=f"{base_url}/imagens/questoes/sim1_q15_carro_micrometro.png",
            ques_alternativas={
                "A": "a) 1,0 × 10⁻²",
                "B": "b) 1,0 × 10⁻³",
                "C": "c) 1,0 × 10⁻⁴",
                "D": "d) 1,0 × 10⁻⁵",
                "E": "e) 1,0 × 10⁻⁶",
            },
            ques_resposta_correta=AlternativaEnum.C,
            ques_resolucao="Como 1 micrômetro = 10⁻⁶ m, temos 100 micrômetros = 100 · 10⁻⁶ m = 10² · 10⁻⁶ m = 1,0 · 10⁻⁴ m.",
            ques_resolucao_imagem_url=None,
        ),
        Questao(
            ques_cont_id=None,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.MEDIO,
            ques_enunciado=(
                "16 - De forma geral, são necessários 50 kg de bauxita para produzir 10 kg de alumínio. O Brasil fechou 2020 como um dos principais líderes "
                "mundiais em reciclagem de latas de alumínio, obtendo um índice de reciclagem de 97,4% de um total de 4,0 × 10⁵ toneladas de latas vendidas. "
                "Considere que a lata é constituída de alumínio puro.\n"
                "Levando em conta apenas a reciclagem de latas, qual é o valor mais próximo da massa de bauxita, em tonelada, que deixou de ser extraída da natureza em 2020 no Brasil?"
            ),
            ques_imagem_url=None,
            ques_alternativas={
                "A": "a) 1,0 × 10⁴ ton",
                "B": "b) 3,9 × 10⁵ ton",
                "C": "c) 5,0 × 10⁵ ton",
                "D": "d) 1,9 × 10⁶ ton",
                "E": "e) 2,0 × 10⁷ ton",
            },
            ques_resposta_correta=AlternativaEnum.D,
            ques_resolucao=(
                "Alumínio reciclado: 0,974 · 4,0 · 10⁵ = 3,896 · 10⁵ t. Como são necessários 5 kg de bauxita para cada 1 kg de alumínio, "
                "a massa de bauxita poupada é 5 · 3,896 · 10⁵ = 19,48 · 10⁵ ≈ 1,9 · 10⁶ toneladas."
            ),
            ques_resolucao_imagem_url=None,
        ),
        Questao(
            ques_cont_id=None,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.MEDIO,
            ques_enunciado=(
                "17 - Ao calcular a média de suas notas em 4 provas, um estudante dividiu, por engano, a soma das notas por 5. Com isso, a média obtida foi "
                "1 unidade menor do que deveria ser, caso fosse calculada corretamente.\n"
                "O valor correto da média das notas desse estudante é:"
            ),
            ques_imagem_url=None,
            ques_alternativas={"A": "a) 4", "B": "b) 5", "C": "c) 6", "D": "d) 19", "E": "e) 21"},
            ques_resposta_correta=AlternativaEnum.B,
            ques_resolucao="Seja S a soma das notas e M a média correta: S / 4 = M → S = 4M. Pelo erro: S / 5 = M - 1 → 4M = 5M - 5 → M = 5.",
            ques_resolucao_imagem_url=None,
        ),
        Questao(
            ques_cont_id=None,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.FACIL,
            ques_enunciado=(
                "18 - O gráfico apresenta o valor total de exportações e o valor total de importações, ao longo de um período, em bilhão de dólares. "
                "O saldo da balança comercial brasileira é dado pelo valor total de exportações menos o valor total de importações num mesmo período.\n"
                "Considere que os saldos nos três meses destacados sejam: S1 (junho de 2009), S2 (janeiro de 2010) e S3 (junho de 2010).\n"
                "A ordenação dos saldos S1, S2 e S3, do maior para o menor, é:"
            ),
            ques_imagem_url=f"{base_url}/imagens/questoes/sim1_q18_balanca_comercial.png",
            ques_alternativas={
                "A": "a) S1, S3 e S2.",
                "B": "b) S2, S1 e S3.",
                "C": "c) S2, S3 e S1.",
                "D": "d) S3, S1 e S2.",
                "E": "e) S3, S2 e S1.",
            },
            ques_resposta_correta=AlternativaEnum.A,
            ques_resolucao="Pelo gráfico: S1 ≈ 14,5 - 10 = 4,5 bi; S2 < 0 (importações superaram exportações); S3 ≈ 17,1 - 14,8 = 2,3 bi. Logo, S1 > S3 > S2.",
            ques_resolucao_imagem_url=None,
        ),
        Questao(
            ques_cont_id=None,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.FACIL,
            ques_enunciado=(
                "19 - Pesquisas indicam que o número de bactérias X é duplicado a cada quarto de hora. Um aluno resolveu fazer uma observação para verificar "
                "a veracidade dessa afirmação. Ele usou uma população inicial de 10⁵ bactérias X e encerrou a observação ao final de uma hora.\n"
                "Após uma hora do início do período de observação desse aluno, o número de bactérias X foi de:"
            ),
            ques_imagem_url=None,
            ques_alternativas={
                "A": "a) 2⁻² . 10⁵",
                "B": "b) 2⁻¹ . 10⁵",
                "C": "c) 2² . 10⁵",
                "D": "d) 2³ . 10⁵",
                "E": "e) 2⁴ . 10⁵",
            },
            ques_resposta_correta=AlternativaEnum.E,
            ques_resolucao="Em 1 hora há 4 quartos de hora (4 períodos de 15 minutos). Como a população dobra 4 vezes, o total final será 2⁴ · 10⁵.",
            ques_resolucao_imagem_url=None,
        ),
        Questao(
            ques_cont_id=None,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.FACIL,
            ques_enunciado=(
                "20 - Uma pessoa ampliou uma foto no computador e, ao imprimi-la, verificou que a qualidade não estava boa. Ao pesquisar, descobriu que "
                "um parâmetro que define a qualidade da imagem, ou resolução, pode ser considerado pela quantidade de pontos, chamados pixels, que há em "
                "cada quadradinho de 1 cm de lado contido na imagem.\n"
                "Considerando a pesquisa realizada, a unidade de medida do parâmetro de qualidade de uma imagem é expressa por:"
            ),
            ques_imagem_url=None,
            ques_alternativas={
                "A": "a) cm² ⋅ pixel",
                "B": "b) cm ⋅ pixel",
                "C": "c) cm / (pixel)²",
                "D": "d) pixel / cm",
                "E": "e) pixel / cm²",
            },
            ques_resposta_correta=AlternativaEnum.E,
            ques_resolucao="Um quadrado de 1 cm de lado possui área igual a 1 cm². A razão entre a quantidade de pixels e a área é expressa em pixel / cm².",
            ques_resolucao_imagem_url=None,
        ),
    ]
    db.add_all(questoes)
    db.commit()


SEEDS = {
    "Trigonometria no Triângulo Retângulo": povoar_conteudo_3,
    "Funções e Função Afim (Função do 1º Grau)": povoar_conteudo_4,
    "Função Quadrática, Exponencial e Logarítmica": povoar_conteudo_5,
    "Geometria Plana (Teorema de Tales, Semelhança e Relações Métricas)": povoar_conteudo_6,
    "Frações Decimais, Dízimas Periódicas e Intervalos Reais": povoar_conteudo_7,
}


def povoar_tudo(db: Session):
    inseridos, ignorados = [], []
    for nome, funcao in SEEDS.items():
        ja_existe = db.query(Conteudo).filter(Conteudo.cont_nome == nome).first()
        if ja_existe:
            ignorados.append(nome)
            continue
        try:
            funcao(db)
            inseridos.append(nome)
        except Exception:
            db.rollback()
            raise

    simulado_existe = db.query(Questao).filter(
        Questao.ques_cont_id.is_(None),
        Questao.ques_etapa == EtapaEnum.ETAPA_1
    ).first()

    if simulado_existe:
        ignorados.append("Simulado 1 - Etapa 1")
    else:
        try:
            povoar_simulado_1(db)
            inseridos.append("Simulado 1 - Etapa 1")
        except Exception:
            db.rollback()
            raise

    return {"inseridos": inseridos, "ignorados": ignorados}


def main():
    with sessao_seed() as session:
        resultado = povoar_tudo(session)

    print("Inseridos:", resultado["inseridos"])
    print("Ignorados (já existiam):", resultado["ignorados"])


if __name__ == "__main__":
    main()