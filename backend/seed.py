from dependencies import pegar_sessao
from models import (
    AlternativaEnum,
    Base,
    Conteudo,
    DificuldadeEnum,
    EtapaEnum,
    Questao,
    db,
)

# CONTEÚDO 1 (Grandezas, Medidas, Razão e Proporção)
def povoar_conteudo_1(session):
    conteudo1 = Conteudo(
        cont_nome="Grandezas, Medidas, Razão e Proporção",
        cont_etapa=EtapaEnum.ETAPA_1,
        cont_texto="Texto completo do conteúdo de Grandezas, Medidas, Razão e Proporção.",
        cont_texto_resumo="Resumo sobre razão, proporção e unidades de medida.",
        cont_slide_pdf="IFUNÇÃO.pdf",
        cont_relacionados={"topicos": ["Razão", "Proporção", "Regra de Três"]},
    )
    session.add(conteudo1)
    session.flush()

    questoes = [
        Questao(
            ques_cont_id=conteudo1.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.FACIL,
            ques_enunciado="1 - Um concurso para preencher 200 vagas recebeu 1600 inscrições. Quantos candidatos há para cada vaga?",
            ques_alternativas={"A": "a) 4", "B": "b) 6", "C": "c) 8", "D": "d) 12"},
            ques_resposta_correta=AlternativaEnum.C,
        ),
        Questao(
            ques_cont_id=conteudo1.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.MEDIO,
            ques_enunciado="2 - Em uma seleção, a razão entre o número de homens e mulheres candidatos a vaga é 4/7. Sabendo que 32 candidatos são do sexo masculino, o número total de participantes na seleção é:",
            ques_alternativas={"A": "a) 56", "B": "b) 72", "C": "c) 88", "D": "d) 94"},
            ques_resposta_correta=AlternativaEnum.C,
        ),
        Questao(
            ques_cont_id=conteudo1.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.MEDIO,
            ques_enunciado="3 - (UEPB/2014) A razão entre o peso de uma pessoa na Terra e o seu peso em Netuno é 5/7. Dessa forma, o peso de uma pessoa que na terra pesa 60 kg, em Netuno, está no intervalo:",
            ques_alternativas={"A": "a) [40 kg; 45 kg]", "B": "b) [45 kg; 50 kg]", "C": "c) [55 kg; 60 kg]", "D": "d) [75 kg; 80 kg]", "E": "e) [80 kg; 85 kg]"},
            ques_resposta_correta=AlternativaEnum.E,
        ),
        Questao(
            ques_cont_id=conteudo1.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.FACIL,
            ques_enunciado="4 - Sabendo que x e 6 são diretamente proporcionais aos números 6 e 18, então podemos afirmar que x vale:",
            ques_alternativas={"A": "A) 1", "B": "B) 2", "C": "C) 3", "D": "D) 4", "E": "E) 5"},
            ques_resposta_correta=AlternativaEnum.B,
        ),
        Questao(
            ques_cont_id=conteudo1.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.FACIL,
            ques_enunciado="5 - Dados recentes mostram que 1 a cada 4 brasileiros já foi contaminado por covid-19. Se essa proporção for aplicada a um bairro de 13116 habitantes, então a quantidade de pessoas que já teve covid nesse bairro é igual a:",
            ques_alternativas={"A": "A) 3279", "B": "B) 3490", "C": "C) 3521", "D": "D) 3674", "E": "E) 4001"},
            ques_resposta_correta=AlternativaEnum.A,
        ),
        Questao(
            ques_cont_id=conteudo1.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.DIFICIL,
            ques_enunciado="6 - (Vunesp) Dez funcionários de uma repartição trabalham 8 horas por dia, durante 27 dias, para atender certo número de pessoas. Se um funcionário doente foi afastado por tempo indeterminado e outro se aposentou, o total de dias que os funcionários restantes levarão para atender o mesmo número de pessoas, trabalhando uma hora a mais por dia, no mesmo ritmo de trabalho, será:",
            ques_alternativas={"A": "a) 29", "B": "b) 30", "C": "c) 33", "D": "d) 28", "E": "e) 31"},
            ques_resposta_correta=AlternativaEnum.B,
        ),
        Questao(
            ques_cont_id=conteudo1.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.MEDIO,
            ques_enunciado="7 - Bruno gostaria de comprar um vídeo game, que a vista estava com 30% de desconto e, por isso, diminuía R$ 60,00 do valor da compra. A outra forma de pagamento oferecida pela loja era comprar no cartão em uma única parcela com 12% de desconto. Se Bruno escolheu pagar o vídeo game com o cartão, qual o valor em reais do desconto concedido?",
            ques_alternativas={"A": "a) R$ 24,00", "B": "b) R$ 18,00", "C": "c) R$ 22,00", "D": "d) R$ 14,00"},
            ques_resposta_correta=AlternativaEnum.A,
        ),
        Questao(
            ques_cont_id=conteudo1.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.MEDIO,
            ques_enunciado="8 - Os agentes comunitários de saúde são profissionais que... Sabendo que 12 profissionais necessitam de 28 dias para visitar todas as casas de 3 bairros de uma cidade, em quanto tempo um quarto da equipe consegue visitar as mesmas casas?",
            ques_alternativas={"A": "a) 90", "B": "b) 98", "C": "c) 120", "D": "d) 112"},
            ques_resposta_correta=AlternativaEnum.D,
        ),
        Questao(
            ques_cont_id=conteudo1.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.DIFICIL,
            ques_enunciado="9 - Em uma obra, 10 homens concluíram um dos trabalhos em 6 dias, fazendo 8 horas diárias. Se apenas 5 homens estiverem trabalhando, quantos dias levarão para o mesmo trabalho ser concluído com execução de 6 horas por dia?",
            ques_alternativas={"A": "a) 12 dias", "B": "b) 14 dias", "C": "c) 16 dias", "D": "d) 18 dias"},
            ques_resposta_correta=AlternativaEnum.C,
        ),
        Questao(
            ques_cont_id=conteudo1.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.MEDIO,
            ques_enunciado="10 - Maria está interessada em comprar livros para a sua biblioteca pessoal... Se Maria comprasse 4 livros do mesmo autor pelo mesmo valor de R$ 150,00 cada, qual seria o valor total com o desconto aplicado?",
            ques_alternativas={"A": "a) R$ 45,00", "B": "b) R$ 54,00", "C": "c) R$ 58,00", "D": "d) R$ 64,00"},
            ques_resposta_correta=AlternativaEnum.B,
        ),
    ]
    session.add_all(questoes)
    session.commit()

# CONTEÚDO 2 (Teoria dos Conjuntos e Conjuntos Numéricos)
def povoar_conteudo_2(session, base_url="https://seu-storage-publico.com"):
    conteudo2 = Conteudo(
        cont_nome="Teoria dos Conjuntos",
        cont_etapa=EtapaEnum.ETAPA_1,
        cont_texto="Texto explicativo sobre Teoria dos Conjuntos e Conjuntos Numéricos.",
        cont_texto_resumo="Resumo sobre união, intersecção e conjuntos numéricos.",
        cont_slide_pdf=f"{base_url}/pdfs/C-1ANO.pdf",
        cont_relacionados={"topicos": ["Conjuntos", "Diagramas", "Números Racionais"]},
    )
    session.add(conteudo2)
    session.flush()

    questoes = [
        Questao(
            ques_cont_id=conteudo2.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.MEDIO,
            ques_enunciado="A região destacada em azul pode ser descrita pela operação:",
            ques_alternativas={"A": "A – B – C", "B": "A U B – C", "C": "A ∩ C – B", "D": "A ∩ B – C", "E": "A ∩ B ∩ C"},
            ques_resposta_correta=AlternativaEnum.C,
        ),
        Questao(
            ques_cont_id=conteudo2.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.MEDIO,
            ques_enunciado="Observe a área hachurada da figura e marque a alternativa que a representa.",
            ques_alternativas={"A": "C ∩ (A U B)", "B": "C – (A U B)", "C": "C U (A – B)", "D": "C ∩ (A – B)"},
            ques_resposta_correta=AlternativaEnum.B,
        ),
        Questao(
            ques_cont_id=conteudo2.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.MEDIO,
            ques_enunciado="(UNB-Adaptada) De 200 pessoas pesquisadas sobre suas preferências em assistir a corridas na TV: 55 não assistem; 101 assistem à Fórmula 1; 27 assistem à Fórmula 1 e Motovelocidade. Quantas assistem exclusivamente à Motovelocidade?",
            ques_alternativas={"A": "32", "B": "44", "C": "56", "D": "28"},
            ques_resposta_correta=AlternativaEnum.B,
        ),
        Questao(
            ques_cont_id=conteudo2.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.FACIL,
            ques_enunciado="Em uma autoescola com 34 alunos, 12 pretendem tirar CNH categoria A e 29 categoria B. A quantidade de candidatos que pretendem tirar somente a CNH categoria A é:",
            ques_alternativas={"A": "22", "B": "7", "C": "5", "D": "19", "E": "10"},
            ques_resposta_correta=AlternativaEnum.C,
        ),
        Questao(
            ques_cont_id=conteudo2.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.MEDIO,
            ques_enunciado="Dados os conjuntos A (números pares), B (números ímpares) e C (múltiplos de 4). Julgue as afirmativas: I – A ⊂ C; II – C ⊂ A; III – A ∩ B = ∅.",
            ques_alternativas={"A": "Somente I e II são verdadeiras.", "B": "Somente II e III são verdadeiras.", "C": "Somente I e III são verdadeiras.", "D": "Somente I é verdadeira.", "E": "Todas são verdadeiras."},
            ques_resposta_correta=AlternativaEnum.B,
        ),
        Questao(
            ques_cont_id=conteudo2.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.FACIL,
            ques_enunciado="Qual a proposição abaixo é verdadeira?",
            ques_alternativas={"A": "Todo número inteiro é racional e todo real é inteiro.", "B": "A intersecção de Q e I tem 1 elemento.", "C": "O número 1,83333... é um número racional.", "D": "A divisão de dois inteiros é sempre um número inteiro."},
            ques_resposta_correta=AlternativaEnum.C,
        ),
        Questao(
            ques_cont_id=conteudo2.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.FACIL,
            ques_enunciado="Nos conjuntos apresentados no quadro abaixo, qual opção representa uma relação de inclusão?",
            ques_alternativas={"A": "Primeira opção", "B": "Segunda opção", "C": "Terceira opção", "D": "Quarta opção"},
            ques_resposta_correta=AlternativaEnum.A,
        ),
        Questao(
            ques_cont_id=conteudo2.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.MEDIO,
            ques_enunciado="Seja A = {2,5}, B = {2,5,6} e C = {6,10}, determine os elementos da operação (A U B) ∩ (B U C).",
            ques_alternativas={"A": "{2,5,6}", "B": "{2,5}", "C": "{6,10}", "D": "{2,5,6,10}", "E": "{2,10}"},
            ques_resposta_correta=AlternativaEnum.A,
        ),
        Questao(
            ques_cont_id=conteudo2.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.MEDIO,
            ques_enunciado="(IFPE 2016) Em uma cooperativa, 125 agricultores cultivam cana-de-açúcar, 85 cultivam algodão e 45 cultivam ambos. Sabendo que todos cultivam pelo menos uma cultura, qual é o total de agricultores?",
            ques_alternativas={"A": "210", "B": "255", "C": "165", "D": "125", "E": "45"},
            ques_resposta_correta=AlternativaEnum.C,
        ),
        Questao(
            ques_cont_id=conteudo2.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.FACIL,
            ques_enunciado="Sobre os conjuntos numéricos, julgue: I – a soma de dois racionais é racional; II – a divisão de dois naturais é natural; III – a diferença entre dois inteiros é inteira; IV – o produto de dois reais é real.",
            ques_alternativas={"A": "Somente a I é falsa.", "B": "Somente a II é falsa.", "C": "Somente a III é falsa.", "D": "Somente a IV é falsa.", "E": "Todas são verdadeiras."},
            ques_resposta_correta=AlternativaEnum.B,
        ),
    ]
    session.add_all(questoes)
    session.commit()

# CONTEÚDO 3 (Grandezas, Unidades de Medida e Notação Científica) 
def povoar_conteudo_3(session, base_url="https://seu-storage-publico.com"):
    conteudo3 = Conteudo(
        cont_nome="Grandezas e Unidades",
        cont_etapa=EtapaEnum.ETAPA_1,
        cont_texto="Texto completo sobre unidades de medida e notação científica.",
        cont_texto_resumo="Resumo de conversões e notação científica.",
        cont_slide_pdf=f"{base_url}/pdfs/GM-1ANO.pdf",
        cont_relacionados={"topicos": ["Unidades", "Notação Científica", "Proporções"]},
    )
    session.add(conteudo3)
    session.flush()

    questoes = [
        Questao(
            ques_cont_id=conteudo3.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.FACIL,
            ques_enunciado="Em um teste de aptidão da Polícia Militar, o candidato deve percorrer uma distância de 2400 metros em um tempo de 12 minutos. Qual alternativa indica os valores de distância e tempo em km e hora, respectivamente?",
            ques_alternativas={"A": "2,4 km e 2 h", "B": "4,2 km e 0,2 h", "C": "0,24 km e 0,2 h", "D": "4,2 km e 2 h", "E": "2,4 km e 0,2 h"},
            ques_resposta_correta=AlternativaEnum.E,
        ),
        Questao(
            ques_cont_id=conteudo3.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.FACIL,
            ques_enunciado="Um aluno de Ensino Médio vai até o açougue comprar 5 kg de carne e 8 litros de refrigerante. Qual das alternativas possui os valores nas unidades tonelada (t) e mililitro (mL), respectivamente?",
            ques_alternativas={"A": "0,005 t e 0,008 mL", "B": "5000 t e 0,008 mL", "C": "0,005 t e 8000 mL", "D": "5000 t e 8000 mL", "E": "0,005 t e 0,8 mL"},
            ques_resposta_correta=AlternativaEnum.C,
        ),
        Questao(
            ques_cont_id=conteudo3.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.FACIL,
            ques_enunciado="A distância em linha reta entre as cidades de São Paulo e Rio de Janeiro é de, aproximadamente, 357,37 km. Esta mesma distância em metros é igual a:",
            ques_alternativas={"A": "35 737 m", "B": "357 370 m", "C": "3 573 700 m", "D": "35,737 m"},
            ques_resposta_correta=AlternativaEnum.B,
        ),
        Questao(
            ques_cont_id=conteudo3.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.MEDIO,
            ques_enunciado="A carga elétrica fundamental de um elétron é estimada em 0,00000000000000000016 C. Seu valor expresso em notação científica fica:",
            ques_alternativas={"A": "16 x 10^-18 C", "B": "1,6 x 10^-19 C", "C": "160 x 10^-17 C", "D": "0,16 x 10^-20 C"},
            ques_resposta_correta=AlternativaEnum.B,
        ),
        Questao(
            ques_cont_id=conteudo3.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.FACIL,
            ques_enunciado="Se um estudante assiste 6 aulas de 50 minutos por dia e estuda 5 dias em uma semana, o número de horas que ele estará em sala de aula será de:",
            ques_alternativas={"A": "20 h", "B": "25 h", "C": "30 h", "D": "1500 h"},
            ques_resposta_correta=AlternativaEnum.B,
        ),
        Questao(
            ques_cont_id=conteudo3.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.MEDIO,
            ques_enunciado="Uma herança de R$ 3.000.000 será dividida de forma diretamente proporcional às idades de três herdeiros (24, 28 e 44 anos). O herdeiro de maior idade receberá um total de:",
            ques_alternativas={"A": "R$ 950.000", "B": "R$ 975.000", "C": "R$ 1.225.000", "D": "R$ 1.375.000", "E": "R$ 1.625.000"},
            ques_resposta_correta=AlternativaEnum.D,
        ),
        Questao(
            ques_cont_id=conteudo3.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.FACIL,
            ques_enunciado="Ao analisar grandezas proporcionais, marque a alternativa que descreve uma relação CORRETA:",
            ques_alternativas={"A": "Distância e tempo são grandezas inversamente proporcionais.", "B": "Velocidade e quantidade de alimento comprado são diretamente proporcionais.", "C": "Em um churrasco, a quantidade de carne e a quantidade de pessoas são grandezas diretamente proporcionais.", "D": "Velocidade e tempo são grandezas diretamente proporcionais."},
            ques_resposta_correta=AlternativaEnum.C,
        ),
        Questao(
            ques_cont_id=conteudo3.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.FACIL,
            ques_enunciado="Das situações abaixo, marque aquela que descreve duas grandezas inversamente proporcionais:",
            ques_alternativas={"A": "Quantidade de pessoas em um churrasco e a quantidade de carne necessária.", "B": "Número de habitantes em uma cidade e a taxa de mortalidade.", "C": "Velocidade de um automóvel e a distância percorrida em um mesmo intervalo de tempo.", "D": "Comprimento da altura e a área de um polígono.", "E": "Vazão de um ralo e o tempo necessário para esvaziar um reservatório."},
            ques_resposta_correta=AlternativaEnum.E,
        ),
        Questao(
            ques_cont_id=conteudo3.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.MEDIO,
            ques_enunciado="Um triângulo possui ângulos internos proporcionais aos números 1, 3 e 6. O valor do seu maior ângulo é:",
            ques_alternativas={"A": "30°", "B": "60°", "C": "90°", "D": "120°", "E": "150°"},
            ques_resposta_correta=AlternativaEnum.D,
        ),
        Questao(
            ques_cont_id=conteudo3.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.MEDIO,
            ques_enunciado="Para fazer uma viagem da cidade A para a cidade B, um automóvel gasta cerca de 4 horas a uma velocidade média de 75 km/h. Caso fosse necessário fazer a viagem em 3 horas, a velocidade deveria ser de:",
            ques_alternativas={"A": "86 km/h", "B": "90 km/h", "C": "95 km/h", "D": "100 km/h", "E": "110 km/h"},
            ques_resposta_correta=AlternativaEnum.D,
        ),
    ]
    session.add_all(questoes)
    session.commit()

# CONTEÚDO 4 (Geometria Plana) 
def povoar_conteudo_4(session, base_url="https://seu-storage-publico.com"):
    conteudo4 = Conteudo(
        cont_nome="Geometria Plana",
        cont_etapa=EtapaEnum.ETAPA_1,
        cont_texto="Texto explicativo sobre Teorema de Tales, Semelhança de Triângulos e Relações Métricas.",
        cont_texto_resumo="Resumo dos principais tópicos de Geometria Plana.",
        cont_slide_pdf=f"{base_url}/pdfs/GP-1ANO.pdf",
        cont_relacionados={"topicos": ["Tales", "Semelhança", "Triângulo Retângulo"]},
    )
    session.add(conteudo4)
    session.flush()

    questoes = [
        Questao(
            ques_cont_id=conteudo4.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.MEDIO,
            ques_enunciado="Considere o triângulo seguinte e determine o valor de x, sabendo que o segmento AD é a bissetriz relativa ao lado BC.",
            ques_alternativas={"A": "9", "B": "10", "C": "11", "D": "12", "E": "13"},
            ques_resposta_correta=AlternativaEnum.C,
        ),
        Questao(
            ques_cont_id=conteudo4.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.FACIL,
            ques_enunciado="As retas t, u e v são paralelas. Determine o valor da medida do segmento x.",
            ques_alternativas={"A": "18", "B": "20", "C": "21", "D": "22", "E": "24"},
            ques_resposta_correta=AlternativaEnum.C,
        ),
        Questao(
            ques_cont_id=conteudo4.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.MEDIO,
            ques_enunciado="Existem 5 bolas dispostas em uma mesa de bilhar. A reta formada entre as bolas 1 e 2 é paralela à reta formada entre as bolas 4 e 5. Conforme as medidas dispostas na imagem responda: qual a distância entre as bolas 1 e 3?",
            ques_alternativas={"A": "20 cm", "B": "30 cm", "C": "40 cm", "D": "50 cm", "E": "60 cm"},
            ques_resposta_correta=AlternativaEnum.C,
        ),
        Questao(
            ques_cont_id=conteudo4.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.DIFICIL,
            ques_enunciado="(Colégio Pedro II - 2012) Para melhorar a qualidade do solo, aumentando a produtividade do milho e da soja, em uma fazenda é feito o rodízio entre essas culturas e a área destinada ao pasto...",
            ques_alternativas={"A": "665", "B": "660", "C": "655", "D": "650", "E": "645"},
            ques_resposta_correta=AlternativaEnum.B,
        ),
        Questao(
            ques_cont_id=conteudo4.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.MEDIO,
            ques_enunciado="(Enem - 2009) A rampa de um hospital tem na sua parte mais elevada uma altura de 2,2 metros. Um paciente ao caminhar sobre a rampa percebe que se deslocou 3,2 metros e alcançou uma altura de 0,8 metros. A distância em metros que o paciente ainda deve caminhar para atingir o ponto mais alto da rampa é:",
            ques_alternativas={"A": "1,16 metros", "B": "3,0 metros", "C": "5,4 metros", "D": "5,6 metros", "E": "7,04 metros"},
            ques_resposta_correta=AlternativaEnum.D,
        ),
        Questao(
            ques_cont_id=conteudo4.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.FACIL,
            ques_enunciado="Existem alguns procedimentos que podem ser usados para descobrir se dois triângulos são semelhantes...",
            ques_alternativas={"A": "Para que dois triângulos sejam semelhantes, basta que eles tenham três ângulos correspondentes congruentes.", "B": "Para que dois triângulos sejam semelhantes, basta que eles tenham dois lados proporcionais...", "C": "Para que dois triângulos sejam congruentes, basta que eles tenham os três lados correspondentes com medidas proporcionais.", "D": "Dois triângulos que possuem dois lados correspondentes proporcionais não serão semelhantes em qualquer hipótese.", "E": "Dois triângulos que possuem apenas dois ângulos correspondentes congruentes não podem ser considerados semelhantes."},
            ques_resposta_correta=AlternativaEnum.C,
        ),
        Questao(
            ques_cont_id=conteudo4.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.MEDIO,
            ques_enunciado="Na imagem a seguir, é possível perceber dois triângulos que compartilham parte de dois lados. Sabendo que os segmentos BA e DE são paralelos, qual a medida de x?",
            ques_alternativas={"A": "210 m", "B": "220 m", "C": "230 m", "D": "240 m", "E": "250 m"},
            ques_resposta_correta=AlternativaEnum.E,
        ),
        Questao(
            ques_cont_id=conteudo4.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.FACIL,
            ques_enunciado="Carla ao procurar seu gatinho o avistou em cima de uma árvore. Ela então pediu ajuda a sua mãe e colocaram uma escada junto à árvore para ajudar o gato a descer. Sabendo que o gato estava a 8 metros do chão e a base da escada estava posicionada a 6 metros da árvore, qual o comprimento da escada utilizada para salvar o gatinho?",
            ques_alternativas={"A": "8 metros", "B": "10 metros", "C": "12 metros", "D": "14 metros"},
            ques_resposta_correta=AlternativaEnum.B,
        ),
        Questao(
            ques_cont_id=conteudo4.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.MEDIO,
            ques_enunciado="(IFRJ - 2013) O pátio de esportes do Campus Arrozal de um Instituto Federal é retangular, com 100 m de comprimento e 50 m de largura...",
            ques_alternativas={"A": "38 m", "B": "64 m", "C": "76 m", "D": "82 m"},
            ques_resposta_correta=AlternativaEnum.C,
        ),
        Questao(
            ques_cont_id=conteudo4.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.DIFICIL,
            ques_enunciado="Em um triângulo retângulo, com ângulo reto em A, a altura relativa à hipotenusa encontra-a no ponto H...",
            ques_alternativas={"A": "I, II e III", "B": "I, II e IV", "C": "I, III e IV", "D": "II, III e IV"},
            ques_resposta_correta=AlternativaEnum.A,
        ),
    ]
    session.add_all(questoes)
    session.commit()

if __name__ == "__main__":
    session = next(pegar_sessao())
    print("Iniciando...")

    Base.metadata.create_all(bind=db)

    povoar_conteudo_1(session)
    povoar_conteudo_2(session)
    povoar_conteudo_3(session)
    povoar_conteudo_4(session)

    print("Conteúdos 1, 2, 3 e 4 cadastrados com sucesso!")