from sqlalchemy.orm import Session
from models import Conteudo, Questao, EtapaEnum, DificuldadeEnum, AlternativaEnum
from contextlib import contextmanager

from dependencies import pegar_sessao

sessao_seed = contextmanager(pegar_sessao)

def povoar_conteudo_1(session, base_url=""):
    conteudo1 = Conteudo(
        cont_nome="Grandezas e Unidades de Medida",
        cont_etapa=EtapaEnum.ETAPA_1,
        cont_texto=(
            "1. UNIDADES DE MEDIDA DECIMAIS E NÃO DECIMAIS\n"
            "As unidades de medida são modelos estabelecidos pelo Sistema Internacional de Unidades (SI) para medir diferentes grandezas:\n"
            "• Medidas de Comprimento: A unidade padrão é o metro (m). Múltiplos e submúltiplos: quilômetro (km), hectômetro (hm), decâmetro (dam), decímetro (dm), centímetro (cm) e milímetro (mm).\n"
            "• Medidas de Capacidade: A unidade padrão é o litro (L). Múltiplos e submúltiplos: quilolitro (kL), hectolitro (hL), decalitro (daL), decilitro (dL), centilitro (cL) e mililitro (mL).\n"
            "• Medidas de Massa: No SI, a unidade padrão é o quilograma (kg). Demais unidades: hectograma (hg), decagrama (dag), grama (g), decigrama (dg), centigrama (cg) e miligrama (mg). Outras unidades usuais: tonelada (1 t = 1000 kg) e libra.\n"
            "• Medidas de Volume: No SI, a unidade é o metro cúbico (m³), com múltiplos e submúltiplos km³, hm³, dam³, dm³, cm³ e mm³. Relação com capacidade: 1 L = 1 dm³.\n"
            "• Medidas de Tempo (Não Decimais): A unidade base é o segundo (s). Relações: 1 minuto (min) = 60 s; 1 hora (h) = 60 min = 3600 s; 1 dia (d) = 24 h.\n\n"
            "2. GRANDEZAS DIRETAMENTE E INVERSAMENTE PROPORCIONAIS\n"
            "• Grandeza: Tudo aquilo que pode ser medido ou calculado e expresso por um número e uma unidade de medida (ex.: velocidade, comprimento, massa, tempo).\n"
            "• Proporcionalidade Direta: A variação de uma grandeza faz com que a outra varie na mesma proporção (se uma dobra, a outra dobra). Ex.: se 20 dias de trabalho rendem R$ 3.200,00, 9 dias renderão R$ 1.440,00.\n"
            "• Proporcionalidade Inversa: O aumento de uma grandeza implica a redução da outra na mesma proporção. Ex.: uma quantidade de suco que enche 60 garrafas de 2 L encherá 40 garrafas de 3 L.\n\n"
            "3. NOTAÇÃO CIENTÍFICA\n"
            "Permite escrever números muito grandes ou muito pequenos na forma a · 10ⁿ, em que 1 ≤ |a| < 10 e n é um número inteiro:\n"
            "• Exemplos: 6 590 000 000 000 000 = 6,59 · 10¹⁵; 0,000000000016 = 1,6 · 10⁻¹¹.\n"
            "• Operações:\n"
            "  - Soma e Subtração: Igualam-se os expoentes de base 10 e somam-se ou subtraem-se os coeficientes.\n"
            "  - Multiplicação: Multiplicam-se os coeficientes e somam-se os expoentes da base 10.\n"
            "  - Divisão: Dividem-se os coeficientes e subtraem-se os expoentes da base 10."
        ),
        cont_texto_resumo="Estudo das unidades de medida decimais e não decimais (comprimento, capacidade, massa, volume e tempo), grandezas diretamente e inversamente proporcionais e notação científica.",
        cont_slide_pdf=f"{base_url}/pdfs/GM-1ANO_2.pdf",
        cont_imagem_url="",
        cont_relacionados={"topicos": ["Unidades de Medida", "Conversão de Medidas", "Grandezas Proporcionais", "Notação Científica"]},
    )
    session.add(conteudo1)
    session.flush()

    questoes = [
        Questao(
            ques_cont_id=conteudo1.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.FACIL,
            ques_enunciado="Em um teste de aptidão em um concurso da Polícia Militar de um determinado estado, o candidato deve percorrer uma distância de 2400 metros em um tempo de 12 minutos. Qual alternativa indica os valores de distância e tempo em km e hora, respectivamente?",
            ques_imagem_url="",
            ques_alternativas={"A": "a) 2,4 km e 2 h", "B": "b) 4,2 km e 0,2 h", "C": "c) 0,24 km e 0,2 h", "D": "d) 4,2 km e 2 h", "E": "e) 2,4 km e 0,2 h"},
            ques_resposta_correta=AlternativaEnum.E,
            ques_resolucao="Dividindo 2400 m por 1000, obtemos 2,4 km. Dividindo 12 min por 60, obtemos 0,2 h.",
            ques_resolucao_imagem_url="",
        ),
        Questao(
            ques_cont_id=conteudo1.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.FACIL,
            ques_enunciado="Um aluno de Ensino Médio vai até o açougue, a pedido de seus pais, comprar 5 kg de carne para um churrasco em sua casa. Além da carne, ele compra 8 litros de refrigerante para oferecer aos convidados. Qual das alternativas a seguir possui os valores da quantidade de carne e de refrigerante, respectivamente, nas unidades tonelada (t) e mililitro (mL)?",
            ques_imagem_url="",
            ques_alternativas={
                "A": "a) 0,005 t e 0,008 mL",
                "B": "b) 5000 t e 0,008 mL",
                "C": "c) 0,005 t e 8000 mL",
                "D": "d) 5000 t e 8000 mL",
                "E": "e) 0,005 t e 0,8 mL",
            },
            ques_resposta_correta=AlternativaEnum.C,
            ques_resolucao="Como 1 t = 1000 kg, 5 kg = 5 / 1000 = 0,005 t. Como 1 L = 1000 mL, 8 L = 8 · 1000 = 8000 mL.",
            ques_resolucao_imagem_url="",
        ),
        Questao(
            ques_cont_id=conteudo1.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.FACIL,
            ques_enunciado="A distância em linha reta entre as cidades de São Paulo e Rio de Janeiro é de, aproximadamente, 357,37 km (quilômetros). Esta mesma distância em metros é igual a:",
            ques_imagem_url="",
            ques_alternativas={"A": "a) 35,737 m", "B": "b) 3.573,7 m", "C": "c) 35.737 m", "D": "d) 357.370 m", "E": "e) 3.573.700 m"},
            ques_resposta_correta=AlternativaEnum.D,
            ques_resolucao="Como 1 km = 1000 m, multiplicamos 357,37 por 1000, obtendo 357.370 m.",
            ques_resolucao_imagem_url="",
        ),
        Questao(
            ques_cont_id=conteudo1.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.FACIL,
            ques_enunciado="A carga elétrica fundamental de um elétron, após diversos experimentos, foi determinada para um valor fundamental estimado em 0,00000000000000000016 C. Seu valor, corretamente expresso em notação científica, fica:",
            ques_imagem_url="",
            ques_alternativas={"A": "a) 16 x 10⁻¹⁸ C", "B": "b) 1,6 x 10⁻¹⁹ C", "C": "c) 160 x 10⁻¹⁷ C", "D": "d) 0,16 x 10⁻²⁰ C"},
            ques_resposta_correta=AlternativaEnum.B,
            ques_resolucao="Deslocando a vírgula 19 casas para a direita até obter um algarismo significativo antes da vírgula, temos 1,6 · 10⁻¹⁹ C.",
            ques_resolucao_imagem_url="",
        ),
        Questao(
            ques_cont_id=conteudo1.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.FACIL,
            ques_enunciado="Nas escolas, é comum dividir o tempo de estudo em aulas de 50 min (minutos). Se um estudante assiste 6 aulas por dia e estuda 5 dias em uma semana, o número de horas que ele estará em sala de aula será de:",
            ques_imagem_url="",
            ques_alternativas={"A": "a) 15 h", "B": "b) 20 h", "C": "c) 25 h", "D": "d) 30 h", "E": "e) 35 h"},
            ques_resposta_correta=AlternativaEnum.C,
            ques_resolucao="Total de aulas: 6 · 5 = 30 aulas. Tempo em minutos: 30 · 50 = 1500 min. Convertendo em horas: 1500 / 60 = 25 h.",
            ques_resolucao_imagem_url="",
        ),
        Questao(
            ques_cont_id=conteudo1.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.MEDIO,
            ques_enunciado="Uma herança de R$ 3.000.000 será dividida de forma diretamente proporcional entre as idades dos três herdeiros. Sabendo que eles possuem 24, 28 e 44 anos, o herdeiro de maior idade receberá um total de:",
            ques_imagem_url="",
            ques_alternativas={"A": "A) R$ 950.000", "B": "B) R$ 975.000", "C": "C) R$ 1.225.000", "D": "D) R$ 1.375.000", "E": "E) R$ 1.625.000"},
            ques_resposta_correta=AlternativaEnum.D,
            ques_resolucao="A soma das idades é 24 + 28 + 44 = 96. Pela proporção 96 / 3.000.000 = 44 / x, temos x = (44 · 3.000.000) / 96 = R$ 1.375.000.",
            ques_resolucao_imagem_url="",
        ),
        Questao(
            ques_cont_id=conteudo1.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.FACIL,
            ques_enunciado="(OMNI) Grandeza é tudo aquilo que pode ser medido ou calculado, porém quando analisamos duas grandezas proporcionais, elas podem ser diretamente proporcionais ou inversamente proporcionais. Sabendo disso, analise as alternativas abaixo e marque a opção CORRETA.",
            ques_imagem_url="",
            ques_alternativas={
                "A": "A) Distância e tempo são grandezas inversamente proporcionais, pois quanto maior a distância que precisa ser percorrida, menos tempo será gasto no percurso.",
                "B": "B) Velocidade e quantidade de alimento comprado por uma família são grandezas diretamente proporcionais.",
                "C": "C) Em um churrasco, a quantidade de carne e a quantidade de pessoas são grandezas diretamente proporcionais.",
                "D": "D) Velocidade e tempo são grandezas diretamente proporcionais, pois quanto maior a velocidade, menor o tempo gasto em um percurso.",
            },
            ques_resposta_correta=AlternativaEnum.C,
            ques_resolucao="Quanto maior a quantidade de pessoas em um churrasco, maior deve ser a quantidade de carne na mesma proporção, caracterizando grandezas diretamente proporcionais.",
            ques_resolucao_imagem_url="",
        ),
        Questao(
            ques_cont_id=conteudo1.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.FACIL,
            ques_enunciado="Das situações abaixo, marque aquela que descreve duas grandezas inversamente proporcionais:",
            ques_imagem_url="",
            ques_alternativas={
                "A": "A) Quantidade de pessoas em um churrasco e a quantidade de carne necessária.",
                "B": "B) Número de habitantes em uma cidade e a taxa de mortalidade.",
                "C": "C) Velocidade de um automóvel e a distância percorrida em um mesmo intervalo de tempo.",
                "D": "D) Comprimento da altura e a área de um polígono.",
                "E": "E) Vazão de um ralo e o tempo necessário para esvaziar um reservatório.",
            },
            ques_resposta_correta=AlternativaEnum.E,
            ques_resolucao="Quanto maior a vazão de água pelo ralo, menor será o tempo necessário para esvaziar o reservatório, tratando-se de grandezas inversamente proporcionais.",
            ques_resolucao_imagem_url="",
        ),
        Questao(
            ques_cont_id=conteudo1.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.DIFICIL,
            ques_enunciado="Um triângulo possui ângulos internos inversamente proporcionais aos números 1, 3 e 6, então, o valor do seu maior ângulo é:",
            ques_imagem_url="",
            ques_alternativas={"A": "A) 30°", "B": "B) 60°", "C": "C) 90°", "D": "D) 120°", "E": "E) 150°"},
            ques_resposta_correta=AlternativaEnum.D,
            ques_resolucao="Sendo a = k/1, b = k/3 e c = k/6, e sabendo que a + b + c = 180°, temos k + k/3 + k/6 = 180° → 9k/6 = 180° → k = 120°. Logo, o maior ângulo mede 120°.",
            ques_resolucao_imagem_url="",
        ),
        Questao(
            ques_cont_id=conteudo1.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.FACIL,
            ques_enunciado="Para fazer uma viagem da cidade A para a cidade B, um automóvel gasta cerca de 4 horas, a uma velocidade média de 75 km/h. Caso fosse necessário que essa viagem fosse feita em 3 horas, a velocidade média seria de:",
            ques_imagem_url="",
            ques_alternativas={"A": "A) 86 km/h", "B": "B) 90 km/h", "C": "C) 95 km/h", "D": "D) 100 km/h", "E": "E) 110 km/h"},
            ques_resposta_correta=AlternativaEnum.D,
            ques_resolucao="Velocidade e tempo são inversamente proporcionais: 3x = 4 · 75 → 3x = 300 → x = 100 km/h.",
            ques_resolucao_imagem_url="",
        ),
    ]
    session.add_all(questoes)
    session.commit()

# CONTEÚDO 2 (Razão, Proporção e Regra de Três)
def povoar_conteudo_2(session, base_url=""):
    conteudo2 = Conteudo(
        cont_nome="Razão, Proporção e Regra de Três",
        cont_etapa=EtapaEnum.ETAPA_1,
        cont_texto=(
            "1. RAZÃO E PROPORÇÃO\n"
            "• Razão: Comparação entre duas grandezas de mesma unidade por meio do quociente A / B (com B ≠ 0). Quando o denominador é 100, chama-se razão centesimal (porcentagem). Ex.: 2/4 = 0,5 = 50%.\n"
            "• Proporção: Igualdade entre duas razões: A / B = C / D (todos os termos diferentes de zero).\n"
            "• Propriedades das Proporções:\n"
            "  1ª (Fundamental): O produto dos meios é igual ao produto dos extremos (A / B = C / D ⇔ A · D = B · C).\n"
            "  2ª: A / B = C / D = (A + C) / (B + D).\n"
            "  3ª: A / B = C / D = (A - C) / (B - D).\n"
            "  4ª: (A + B) / A = (C + D) / C.\n\n"
            "2. REGRA DE TRÊS SIMPLES\n"
            "Método utilizado para encontrar um quarto valor desconhecido em problemas envolvendo duas grandezas:\n"
            "• Grandezas Diretamente Proporcionais: Mantém-se a proporção e multiplica-se cruzado.\n"
            "  - Exemplo: Se 1 bolo usa 300 g de chocolate, 5 bolos usarão x → 1x = 300 · 5 → x = 1500 g (1,5 kg).\n"
            "• Grandezas Inversamente Proporcionais: Inverte-se uma das razões antes de multiplicar cruzado.\n"
            "  - Exemplo: A 80 km/h gasta-se 3 h; a 120 km/h gasta-se x → 120x = 80 · 3 → x = 2 horas.\n\n"
            "3. REGRA DE TRÊS COMPOSTA\n"
            "Utilizada quando há três ou mais grandezas. Fixa-se a coluna da incógnita, analisa-se cada grandeza separadamente em relação a ela e invertem-se apenas as razões inversamente proporcionais:\n"
            "• Exemplo: 3 máquinas produzem 900 perfumes em 12 dias. Para 8 máquinas produzirem 1200 perfumes:\n"
            "  12 / x = (8 / 3) · (900 / 1200) → x = 6 dias."
        ),
        cont_texto_resumo="Estudo de razão, porcentagem como razão centesimal, proporção e suas quatro propriedades, regra de três simples (direta e inversa) e regra de três composta.",
        cont_slide_pdf=f"{base_url}/pdfs/GM-1ANO_2.pdf",
        cont_imagem_url="",
        cont_relacionados={"topicos": ["Razão e Proporção", "Propriedades das Proporções", "Regra de Três Simples e Composta", "Porcentagem"]},
    )
    session.add(conteudo2)
    session.flush()

    questoes = [
        Questao(
            ques_cont_id=conteudo2.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.FACIL,
            ques_enunciado="Um concurso para preencher 200 vagas recebeu 1600 inscrições. Quantos candidatos há para cada vaga?",
            ques_imagem_url="",
            ques_alternativas={"A": "a) 4", "B": "b) 6", "C": "c) 8", "D": "d) 12"},
            ques_resposta_correta=AlternativaEnum.C,
            ques_resolucao="Comparando o número de candidatos com o número de vagas em uma divisão: 1600 : 200 = 1600/200 = 8/1. Sendo assim, a razão é 8 para 1, ou seja, há 8 candidatos para cada vaga no concurso.",
            ques_resolucao_imagem_url="",
        ),
        Questao(
            ques_cont_id=conteudo2.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.MEDIO,
            ques_enunciado="Em uma seleção, a razão entre o número de homens e mulheres candidatos a vaga é 4/7. Sabendo que 32 candidatos são do sexo masculino, o número total de participantes na seleção é:",
            ques_imagem_url="",
            ques_alternativas={"A": "a) 56", "B": "b) 72", "C": "c) 88", "D": "d) 94"},
            ques_resposta_correta=AlternativaEnum.C,
            ques_resolucao="Pela regra fundamental da proporção: 4/7 = 32/x → 4x = 32 · 7 → x = 224/4 → x = 56 mulheres. Somando homens e mulheres: 56 + 32 = 88 participantes.",
            ques_resolucao_imagem_url="",
        ),
        Questao(
            ques_cont_id=conteudo2.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.MEDIO,
            ques_enunciado="(UEPB/2014) A razão entre o peso de uma pessoa na Terra e o seu peso em Netuno é 5/7. Dessa forma, o peso de uma pessoa que na terra pesa 60 kg, em Netuno, está no intervalo:",
            ques_imagem_url="",
            ques_alternativas={"A": "a) [40 kg; 45 kg]", "B": "b) [45 kg; 50 kg]", "C": "c) [55 kg; 60 kg]", "D": "d) [75 kg; 80 kg]", "E": "e) [80 kg; 85 kg]"},
            ques_resposta_correta=AlternativaEnum.E,
            ques_resolucao="Montando a proporção: 5/7 = 60/x → 5x = 60 · 7 → 5x = 420 → x = 420/5 = 84 kg, valor que pertence ao intervalo [80 kg; 85 kg].",
            ques_resolucao_imagem_url="",
        ),
        Questao(
            ques_cont_id=conteudo2.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.FACIL,
            ques_enunciado="Sabendo que x e 6 são diretamente proporcionais aos números 6 e 18, então podemos afirmar que x vale:",
            ques_imagem_url="",
            ques_alternativas={"A": "A) 1", "B": "B) 2", "C": "C) 3", "D": "D) 4", "E": "E) 5"},
            ques_resposta_correta=AlternativaEnum.B,
            ques_resolucao="Sabemos que x/6 = 6/18. Multiplicando cruzado: 18x = 36 → x = 36/18 → x = 2.",
            ques_resolucao_imagem_url="",
        ),
        Questao(
            ques_cont_id=conteudo2.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.FACIL,
            ques_enunciado="Dados recentes mostram que 1 a cada 4 brasileiros já foi contaminado por covid-19. Se essa proporção for aplicada a um bairro de 13116 habitantes, então a quantidade de pessoas que já teve covid nesse bairro é igual a:",
            ques_imagem_url="",
            ques_alternativas={"A": "A) 3279", "B": "B) 3490", "C": "C) 3521", "D": "D) 3674", "E": "E) 4001"},
            ques_resposta_correta=AlternativaEnum.A,
            ques_resolucao="Calculando 1/4 de 13116: (1/4) · 13116 = 13116 / 4 = 3279 pessoas.",
            ques_resolucao_imagem_url="",
        ),
        Questao(
            ques_cont_id=conteudo2.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.DIFICIL,
            ques_enunciado="(Vunesp) Dez funcionários de uma repartição trabalham 8 horas por dia, durante 27 dias, para atender certo número de pessoas. Se um funcionário doente foi afastado por tempo indeterminado e outro se aposentou, o total de dias que os funcionários restantes levarão para atender o mesmo número de pessoas, trabalhando uma hora a mais por dia, no mesmo ritmo de trabalho, será:",
            ques_imagem_url="",
            ques_alternativas={"A": "a) 29", "B": "b) 30", "C": "c) 33", "D": "d) 28", "E": "e) 31"},
            ques_resposta_correta=AlternativaEnum.B,
            ques_resolucao="Restam 10 - 2 = 8 funcionários trabalhando 8 + 1 = 9 h/dia. Como funcionários e horas por dia são inversamente proporcionais aos dias, invertemos suas razões: 27/x = (8/10) · (9/8) → 27/x = 72/80 → 72x = 27 · 80 → x = 2160/72 = 30 dias.",
            ques_resolucao_imagem_url="",
        ),
        Questao(
            ques_cont_id=conteudo2.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.MEDIO,
            ques_enunciado="Bruno gostaria de comprar um vídeo game, que a vista estava com 30% de desconto e, por isso, diminuía R$ 60,00 do valor da compra. A outra forma de pagamento oferecida pela loja era comprar no cartão em uma única parcela com 12% de desconto. Se Bruno escolheu pagar o vídeo game com o cartão, qual o valor em reais do desconto concedido?",
            ques_imagem_url="",
            ques_alternativas={"A": "a) R$ 24,00", "B": "b) R$ 18,00", "C": "c) R$ 22,00", "D": "d) R$ 14,00"},
            ques_resposta_correta=AlternativaEnum.A,
            ques_resolucao="Porcentagem e desconto são diretamente proporcionais (30% está para R$ 60,00 assim como 12% está para x): 30x = 60 · 12 → x = 720/30 → x = R$ 24,00.",
            ques_resolucao_imagem_url="",
        ),
        Questao(
            ques_cont_id=conteudo2.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.MEDIO,
            ques_enunciado="Os agentes comunitários de saúde são profissionais que, entre as suas funções, estão empenhados no combate a uma das doenças mais frequentes no Brasil: a dengue. Para isso, os agentes vão de casa em casa para identificar focos de desenvolvimento do mosquito Aedes aegypti e orientar os moradores. Sabendo que 12 profissionais necessitam de 28 dias para visitar todas as casas de 3 bairros de uma cidade, em quanto tempo um quarto da equipe consegue visitar as mesmas casas?",
            ques_imagem_url="",
            ques_alternativas={"A": "a) 90", "B": "b) 98", "C": "c) 120", "D": "d) 112"},
            ques_resposta_correta=AlternativaEnum.D,
            ques_resolucao="Um quarto da equipe equivale a (1/4) · 12 = 3 profissionais. Como agentes e dias são inversamente proporcionais: 3x = 12 · 28 → x = 336/3 → x = 112 dias.",
            ques_resolucao_imagem_url="",
        ),
        Questao(
            ques_cont_id=conteudo2.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.DIFICIL,
            ques_enunciado="Em uma obra, 10 homens concluíram um dos trabalhos em 6 dias, fazendo 8 horas diárias. Se apenas 5 homens estiverem trabalhando, quantos dias levarão para o mesmo trabalho ser concluído com execução de 6 horas por dia?",
            ques_imagem_url="",
            ques_alternativas={"A": "a) 12 dias", "B": "b) 14 dias", "C": "c) 16 dias", "D": "d) 18 dias"},
            ques_resposta_correta=AlternativaEnum.C,
            ques_resolucao="Homens trabalhando e horas por dia são inversamente proporcionais aos dias: 6/x = (5/10) · (6/8) → 6/x = 30/80 → 30x = 480 → x = 16 dias.",
            ques_resolucao_imagem_url="",
        ),
        Questao(
            ques_cont_id=conteudo2.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.MEDIO,
            ques_enunciado=(
                "Maria está interessada em comprar livros para a sua biblioteca pessoal. Ela percebeu que em uma livraria, os livros do mesmo autor têm um desconto progressivo, conforme a quantidade comprada.\n"
                "Tabela de descontos:\n"
                "• 1 livro: 0% de desconto\n"
                "• 2 livros: 6% de desconto\n"
                "• 3 ou mais livros: ?\n"
                "Na tabela está faltando o percentual de desconto para 3 ou mais livros. Sabe-se que a variação do desconto é proporcional ao número de livros. Se Maria comprasse 4 livros do mesmo autor pelo mesmo valor de R$ 150,00 cada, qual seria o valor total com o desconto aplicado?"
            ),
            ques_imagem_url="",
            ques_alternativas={"A": "a) R$ 45,00", "B": "b) R$ 54,00", "C": "c) R$ 58,00", "D": "d) R$ 64,00"},
            ques_resposta_correta=AlternativaEnum.B,
            ques_resolucao="Como a variação do desconto é proporcional, pela regra de três simples: 2/3 = 6/x → 2x = 18 → x = 9% de desconto. Comprando 4 livros de R$ 150,00 (total de R$ 600,00), o desconto de 9% é 600 · 0,09 = R$ 54,00.",
            ques_resolucao_imagem_url="",
        ),
    ]
    session.add_all(questoes)
    session.commit()

# CONTEÚDO 3 (Teoria dos Conjuntos e Conjuntos Numéricos)
def povoar_conteudo_3(session, base_url=""):
    conteudo3 = Conteudo(
        cont_nome="Teoria dos Conjuntos e Conjuntos Numéricos",
        cont_etapa=EtapaEnum.ETAPA_1,
        cont_texto=(
            "1. NOÇÕES E OPERAÇÕES ENTRE CONJUNTOS\n"
            "Um conjunto representa uma coleção bem definida de elementos. As principais relações e operações são:\n"
            "• Pertinência (∈, ∉): relaciona um elemento a um conjunto.\n"
            "• Inclusão (⊂, ⊄, ⊃): relaciona dois conjuntos; A ⊂ B indica que todo elemento de A pertence a B.\n"
            "• União (A ∪ B): reúne todos os elementos que pertencem a A ou a B.\n"
            "• Intersecção (A ∩ B): reúne apenas os elementos comuns a A e B simultaneamente.\n"
            "• Diferença (A - B): reúne os elementos que pertencem a A e não pertencem a B.\n\n"
            "2. CONJUNTOS NUMÉRICOS\n"
            "• Naturais (N): {0, 1, 2, 3, ...}\n"
            "• Inteiros (Z): {..., -2, -1, 0, 1, 2, ...}\n"
            "• Racionais (Q): números que podem ser expressos como fração a/b (com a ∈ Z e b ∈ Z*), abrangendo decimais exatos e dízimas periódicas.\n"
            "• Irracionais (I): números com representação decimal infinita e não periódica (ex.: π, √2).\n"
            "• Reais (R): união dos conjuntos racionais e irracionais (R = Q ∪ I)."
        ),
        cont_texto_resumo="Estudo das relações de pertinência e inclusão, operações entre conjuntos (união, intersecção e diferença), diagramas de Venn e conjuntos numéricos (N, Z, Q, I e R).",
        cont_slide_pdf=f"{base_url}/pdfs/C-1ANO.pdf",
        cont_imagem_url="",
        cont_relacionados={"topicos": ["Conjuntos", "Diagramas de Venn", "Conjuntos Numéricos"]},
    )
    session.add(conteudo3)
    session.flush()

    questoes = [
        Questao(
            ques_cont_id=conteudo3.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.MEDIO,
            ques_enunciado="A região destacada em azul pode ser descrita pela operação:",
            ques_imagem_url="https://s4.static.brasilescola.uol.com.br/exercicios/2021/03/3-questao-12.jpg",
            ques_alternativas={"A": "A) A – B – C", "B": "B) A ∪ B – C", "C": "C) A ∩ C – B", "D": "D) A ∩ B – C", "E": "E) A ∩ B ∩ C"},
            ques_resposta_correta=AlternativaEnum.C,
            ques_resolucao="Analisando o diagrama, a região em destaque corresponde à intersecção entre os conjuntos A e C (A ∩ C) menos os elementos que pertencem ao conjunto B, resultando em A ∩ C – B.",
            ques_resolucao_imagem_url="",
        ),
        Questao(
            ques_cont_id=conteudo3.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.MEDIO,
            ques_enunciado="Observe a área hachurada da figura e marque a alternativa que a representa.",
            ques_imagem_url="https://static.todamateria.com.br/upload/di/ag/diagramadevennexerciciosconjuntos-cke.jpg",
            ques_alternativas={"A": "a) C ∪ (A ∩ B)", "B": "b) C – (A ∪ B)", "C": "c) C ∩ (A – B)", "D": "d) C ∪ (A ∪ B)"},
            ques_resposta_correta=AlternativaEnum.B,
            ques_resolucao="A área hachurada representa os elementos de C que não pertencem aos conjuntos A nem B. Como A e B estão unidos (A ∪ B), a região destacada é a diferença C – (A ∪ B).",
            ques_resolucao_imagem_url="",
        ),
        Questao(
            ques_cont_id=conteudo3.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.MEDIO,
            ques_enunciado=(
                "(UNB-Adaptada) De 200 pessoas que foram pesquisadas sobre suas preferências em assistir aos campeonatos de corrida pela televisão, foram colhidos os seguintes dados:\n"
                "- 55 dos entrevistados não assistem;\n"
                "- 101 assistem às corridas de Fórmula 1;\n"
                "- 27 assistem às corridas de Fórmula 1 e de Motovelocidade;\n"
                "Quantas das pessoas entrevistadas assistem, exclusivamente, às corridas de Motovelocidade?"
            ),
            ques_imagem_url="",
            ques_alternativas={"A": "a) 32", "B": "b) 44", "C": "c) 56", "D": "d) 28"},
            ques_resposta_correta=AlternativaEnum.B,
            ques_resolucao="1º passo: determinar o total de pessoas que assistem às corridas: 200 - 55 = 145 pessoas. 2º passo: como 101 assistem Fórmula 1 (sendo 74 apenas Fórmula 1 e 27 ambos), temos 74 + 27 + (x - 27) = 145 → x + 74 = 145 → x = 71 pessoas que assistem Motovelocidade. Subtraindo a intersecção: 71 - 27 = 44 assistem exclusivamente Motovelocidade.",
            ques_resolucao_imagem_url="",
        ),
        Questao(
            ques_cont_id=conteudo3.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.FACIL,
            ques_enunciado="Em uma escola de formação de condutores, constatou-se que todos os 34 alunos estavam tirando a primeira carteira nacional de habilitação (CNH). O professor perguntou quantos estavam ali para tirar a CNH da categoria A, e 12 estudantes levantaram a mão, posteriormente, ele perguntou quantos estavam ali para obter CNH da categoria B, e 29 levantaram a mão, sendo assim, a quantidade de candidatos que pretendem tirar somente a CNH da categoria A é:",
            ques_imagem_url="",
            ques_alternativas={"A": "A) 22", "B": "B) 7", "C": "C) 5", "D": "D) 19", "E": "E) 10"},
            ques_resposta_correta=AlternativaEnum.C,
            ques_resolucao="Somando os dois grupos: 29 + 12 = 41. Como o total é 34 alunos, há 41 - 34 = 7 alunos na intersecção (tirando ambas as categorias). Subtraindo esses 7 do total da categoria A: 12 - 7 = 5 alunos tiram somente a CNH A.",
            ques_resolucao_imagem_url="",
        ),
        Questao(
            ques_cont_id=conteudo3.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.MEDIO,
            ques_enunciado=(
                "Dados os conjuntos A, B e C, cujos termos possuem as seguintes características:\n"
                "A → conjunto dos números pares\n"
                "B → conjunto dos números ímpares\n"
                "C → conjunto dos múltiplos de 4\n"
                "Julgue as afirmativas a seguir:\n"
                "I – A está contido em C.\n"
                "II – C está contido em A.\n"
                "III – A intersecção entre A e B é igual ao conjunto vazio."
            ),
            ques_imagem_url="",
            ques_alternativas={
                "A": "A) Somente I e II são verdadeiras.",
                "B": "B) Somente II e III são verdadeiras.",
                "C": "C) Somente I e III são verdadeiras.",
                "D": "D) Somente I é verdadeira.",
                "E": "E) Todas as afirmativas são verdadeiras.",
            },
            ques_resposta_correta=AlternativaEnum.B,
            ques_resolucao="I → Falsa, pois nem todo número par (múltiplo de 2) é múltiplo de 4 (ex.: 2 e 6). II → Verdadeira, pois todos os múltiplos de 4 são pares (C ⊂ A). III → Verdadeira, pois nenhum número é par e ímpar simultaneamente (A ∩ B = ∅).",
            ques_resolucao_imagem_url="",
        ),
        Questao(
            ques_cont_id=conteudo3.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.FACIL,
            ques_enunciado="Qual proposição abaixo é verdadeira?",
            ques_imagem_url="",
            ques_alternativas={
                "A": "a) Todo número inteiro é racional e todo número real é um número inteiro.",
                "B": "b) A intersecção do conjunto dos números racionais com o conjunto dos números irracionais tem 1 elemento.",
                "C": "c) O número 1,83333... é um número racional.",
                "D": "d) A divisão de dois números inteiros é sempre um número inteiro.",
            },
            ques_resposta_correta=AlternativaEnum.C,
            ques_resolucao="a) Falsa: nem todo real é inteiro (ex.: 1/2). b) Falsa: Q ∩ I = ∅. c) Verdadeira: 1,83333... é uma dízima periódica que equivale à fração 11/6, pertencendo a Q. d) Falsa: 7 / 3 = 2,333..., que não é inteiro.",
            ques_resolucao_imagem_url="",
        ),
        Questao(
            ques_cont_id=conteudo3.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.FACIL,
            ques_enunciado="Nos conjuntos (A e B) no quadro abaixo, qual alternativa representa uma relação de inclusão?",
            ques_imagem_url="https://static.todamateria.com.br/upload/co/nj/conjuntosab.jpg",
            ques_alternativas={"A": "a) Primeira opção", "B": "b) Segunda opção", "C": "c) Terceira opção", "D": "d) Quarta opção"},
            ques_resposta_correta=AlternativaEnum.A,
            ques_resolucao="A primeira opção (alternativa A) é a única em que um conjunto está totalmente incluído no outro (B ⊂ A ou A ⊃ B).",
            ques_resolucao_imagem_url="",
        ),
        Questao(
            ques_cont_id=conteudo3.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.MEDIO,
            ques_enunciado="Seja A = {2, 5}, B = {2, 5, 6} e C = {6, 10}, determine os elementos da operação (A ∪ B) ∩ (B ∪ C).",
            ques_imagem_url="",
            ques_alternativas={"A": "A) {2, 5, 6}", "B": "B) {2, 5}", "C": "C) {6, 10}", "D": "D) {2, 5, 6, 10}", "E": "E) {2, 10}"},
            ques_resposta_correta=AlternativaEnum.A,
            ques_resolucao="Calculando as uniões: A ∪ B = {2, 5, 6} e B ∪ C = {2, 5, 6, 10}. A intersecção entre esses dois resultados é {2, 5, 6}.",
            ques_resolucao_imagem_url="",
        ),
        Questao(
            ques_cont_id=conteudo3.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.MEDIO,
            ques_enunciado="(IFPE 2016) Em uma cooperativa de agricultores do município de Vitória de Santo Antão, foi realizada uma consulta em relação ao cultivo de cana-de-açúcar e do algodão. Constatou-se que 125 associados cultivavam a cana-de-açúcar, 85 cultivavam o algodão e 45 cultivavam ambos. Sabendo que todos os cooperativados cultivavam pelo menos uma dessas duas culturas, qual é o número de agricultores da cooperativa?",
            ques_imagem_url="",
            ques_alternativas={"A": "A) 210", "B": "B) 255", "C": "C) 165", "D": "D) 125", "E": "E) 45"},
            ques_resposta_correta=AlternativaEnum.C,
            ques_resolucao="Pelo princípio da inclusão-exclusão: n(A ∪ B) = n(A) + n(B) - n(A ∩ B) = 125 + 85 - 45 = 165 agricultores.",
            ques_resolucao_imagem_url="",
        ),
        Questao(
            ques_cont_id=conteudo3.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.FACIL,
            ques_enunciado=(
                "Sobre os conjuntos numéricos, podemos afirmar que:\n"
                "I – a soma de dois números racionais é sempre um número racional.\n"
                "II – a divisão de dois números naturais é sempre um número natural.\n"
                "III – a diferença entre dois números inteiros é sempre um número inteiro.\n"
                "IV – o produto entre dois números reais é sempre igual a um número real.\n"
                "Julgando as afirmativas, temos que:"
            ),
            ques_imagem_url="",
            ques_alternativas={
                "A": "A) somente a afirmativa I é falsa.",
                "B": "B) somente a afirmativa II é falsa.",
                "C": "C) somente a afirmativa III é falsa.",
                "D": "D) somente a afirmativa IV é falsa.",
                "E": "E) todas as afirmativas são verdadeiras.",
            },
            ques_resposta_correta=AlternativaEnum.B,
            ques_resolucao="I) Verdadeira: a soma de dois racionais sempre resulta em um racional. II) Falsa: a divisão de dois naturais pode gerar um número não natural (ex.: 7 ÷ 2 = 3,5). III) Verdadeira: a diferença de dois inteiros é sempre inteira. IV) Verdadeira: o produto de dois reais é sempre real.",
            ques_resolucao_imagem_url="",
        ),
    ]
    session.add_all(questoes)
    session.commit()

# CONTEÚDO 4 (Frações Decimais, Dízimas Periódicas e Intervalos Reais)
def povoar_conteudo_4(session, base_url=""):
    conteudo4 = Conteudo(
        cont_nome="Frações Decimais, Dízimas Periódicas e Intervalos Reais",
        cont_etapa=EtapaEnum.ETAPA_1,
        cont_texto=(
            "1. FRAÇÕES DECIMAIS\n"
            "Uma fração decimal possui no denominador uma potência de base 10 (10, 100, 1000, ...). "
            "Na conversão para número decimal, a quantidade de zeros do denominador define o número de casas após a vírgula:\n"
            "• Exemplos: 23/10 = 2,3 (1 casa decimal); 23/100 = 0,23 (2 casas decimais).\n\n"
            "2. DÍZIMAS PERIÓDICAS\n"
            "São números decimais infinitos que possuem um grupo de algarismos (período) que se repete ciclicamente. Por admitirem representação fracionária, pertencem ao conjunto dos números racionais (Q).\n"
            "• Dízima Simples: o período começa logo após a vírgula (ex.: 0,323232..., período = 32).\n"
            "• Dízima Composta: apresenta um antiperíodo (algarismos decimais que não se repetem) entre a vírgula e o período (ex.: 2,32444..., antiperíodo = 32, período = 4).\n"
            "• Números Irracionais: decimais infinitos sem repetição periódica (ex.: 1,1212314...) não são dízimas periódicas.\n\n"
            "3. FRAÇÃO GERATRIZ\n"
            "É a fração que origina a dízima periódica:\n"
            "• Dízima Simples: iguala-se a dízima a x, multiplica-se por 10^n (n = quantidade de algarismos do período) e subtrai-se a equação inicial.\n"
            "  - Exemplo: x = 0,323232... → 100x = 32,323232... → 99x = 32 → x = 32/99.\n"
            "• Dízima Composta: desloca-se primeiramente o antiperíodo para antes da vírgula por meio de potência de 10 e aplica-se a subtração.\n"
            "  - Exemplo: x = 2,34555... → 100x = 234,555... e 1000x = 2345,555... → 900x = 2345 - 234 → x = 2111/900.\n\n"
            "4. INTERVALOS REAIS\n"
            "Subconjuntos da reta real delimitados por extremos a e b (com a < b):\n"
            "• Aberto: ]a, b[ = {x ∈ R | a < x < b} (extremos excluídos).\n"
            "• Fechado: [a, b] = {x ∈ R | a ≤ x ≤ b} (extremos incluídos).\n"
            "• Semiabertos: [a, b[ = {x ∈ R | a ≤ x < b} e ]a, b] = {x ∈ R | a < x ≤ b}.\n"
            "• Infinitos: sempre abertos no símbolo de infinito, como ]-3, +∞[ = {x ∈ R | x > -3}."
        ),
        cont_texto_resumo="Estudo das frações decimais, dízimas periódicas simples e compostas, obtenção da fração geratriz e representação de intervalos na reta real.",
        cont_slide_pdf=f"{base_url}/pdfs/IFUNÇÃO-1-ANO.pdf",
        cont_imagem_url="",
        cont_relacionados={"topicos": ["Conjuntos Numéricos", "Números Racionais e Irracionais", "Fração Geratriz", "Intervalos Reais"]},
    )
    session.add(conteudo4)
    session.flush()

    questoes = [
        Questao(
            ques_cont_id=conteudo4.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.MEDIO,
            ques_enunciado="Qual é a fração irredutível geratriz da dízima periódica 1,2431313131...?",
            ques_imagem_url="",
            ques_alternativas={"A": "a) 12431/1000", "B": "b) 12431/9900", "C": "c) 12307/1000", "D": "d) 12307/9900"},
            ques_resposta_correta=AlternativaEnum.D,
            ques_resolucao="Em 1,24313131..., temos parte inteira i = 1, antiperíodo a = 24 (2 algarismos → dois 0s) e período p = 31 (2 algarismos → dois 9s). Aplicando a regra prática: x = (12431 - 124) / 9900 = 12307 / 9900.",
            ques_resolucao_imagem_url="",
        ),
        Questao(
            ques_cont_id=conteudo4.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.MEDIO,
            ques_enunciado=(
                "Analise as afirmativas abaixo:\n"
                "I. Os números decimais exatos são assim chamados por possuírem uma representação decimal finita.\n"
                "II. O número 0,12345... é uma dízima periódica.\n"
                "III. Uma fração irredutível só terá representação decimal exata se o denominador tiver apenas os fatores primos 2 ou 5.\n"
                "IV. A fração geratriz da dízima 1,2333... é 37/30.\n"
                "São verdadeiras:"
            ),
            ques_imagem_url="",
            ques_alternativas={"A": "a) I, II e III", "B": "b) I, II e IV", "C": "c) II, III e IV", "D": "d) I, III e IV"},
            ques_resposta_correta=AlternativaEnum.D,
            ques_resolucao="I. Verdadeira: decimal exato tem representação decimal finita. II. Falsa: 0,12345... não possui período repetitivo. III. Verdadeira: no sistema decimal (base 10 = 2 · 5), a divisão é exata apenas quando o denominador irredutível possui fatores primos 2 ou 5. IV. Verdadeira: x = (123 - 12) / 90 = 111/90 = 37/30.",
            ques_resolucao_imagem_url="",
        ),
        Questao(
            ques_cont_id=conteudo4.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.FACIL,
            ques_enunciado="O valor da soma 0,232323... + 0,878787... vale:",
            ques_imagem_url="",
            ques_alternativas={"A": "a) 1", "B": "b) 1,0101...", "C": "c) 1,1111...", "D": "d) 1,1010..."},
            ques_resposta_correta=AlternativaEnum.C,
            ques_resolucao="Obtendo as frações geratrizes: 0,232323... = 23/99 e 0,878787... = 87/99. Somando as frações: 23/99 + 87/99 = 110/99 = 10/9 = 1,1111...",
            ques_resolucao_imagem_url="",
        ),
        Questao(
            ques_cont_id=conteudo4.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.MEDIO,
            ques_enunciado="(PUC/RJ - 2003) A soma 1,3333... + 0,16666... é igual a:",
            ques_imagem_url="",
            ques_alternativas={"A": "a) 1/2", "B": "b) 5/2", "C": "c) 4/3", "D": "d) 5/3", "E": "e) 3/2"},
            ques_resposta_correta=AlternativaEnum.E,
            ques_resolucao="Transformando em frações geratrizes: 1,3333... = (13 - 1)/9 = 12/9 = 4/3 e 0,16666... = (16 - 1)/90 = 15/90 = 1/6. Somando: 4/3 + 1/6 = (8 + 1)/6 = 9/6 = 3/2.",
            ques_resolucao_imagem_url="",
        ),
        Questao(
            ques_cont_id=conteudo4.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.FACIL,
            ques_enunciado="Seja x = 1,123123... A diferença entre o numerador e o denominador da sua representação fracionária é:",
            ques_imagem_url="",
            ques_alternativas={"A": "A) 123.", "B": "B) 999.", "C": "C) 321.", "D": "D) 112.", "E": "E) 1122."},
            ques_resposta_correta=AlternativaEnum.A,
            ques_resolucao="Encontrando a fração geratriz: x = 1 + 0,123123... = 1 + 123/999 = (999 + 123)/999 = 1122/999. A diferença entre numerador e denominador é 1122 - 999 = 123.",
            ques_resolucao_imagem_url="",
        ),
        Questao(
            ques_cont_id=conteudo4.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.FACIL,
            ques_enunciado=(
                "Analise os números reais a seguir:\n"
                "I) 2/3\n"
                "II) 0,2555...\n"
                "III) 3,141592...\n"
                "IV) 1/2\n"
                "Podemos escrever como uma dízima periódica:"
            ),
            ques_imagem_url="",
            ques_alternativas={
                "A": "A) somente II e III.",
                "B": "B) somente I e II.",
                "C": "C) somente III e IV.",
                "D": "D) somente I, II e III.",
                "E": "E) somente II, III e IV.",
            },
            ques_resposta_correta=AlternativaEnum.B,
            ques_resolucao="I → 2/3 = 0,6666... é dízima periódica simples. II → 0,2555... é dízima periódica composta. III → 3,141592... (π) é irracional (não periódico). IV → 1/2 = 0,5 é decimal exato.",
            ques_resolucao_imagem_url="",
        ),
        Questao(
            ques_cont_id=conteudo4.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.MEDIO,
            ques_enunciado="(Pref. de Niterói) Simplificando a expressão (1,3333... + 3/2) / (1,5 + 4/3), obtém-se:",
            ques_imagem_url="",
            ques_alternativas={"A": "A) 1/2", "B": "B) 1", "C": "C) 3/2", "D": "D) 2", "E": "E) 3"},
            ques_resposta_correta=AlternativaEnum.B,
            ques_resolucao="Substituindo 1,3333... = 1 + 3/9 = 4/3 e 1,5 = 15/10 = 3/2: no numerador temos 4/3 + 3/2 = (8 + 9)/6 = 17/6; no denominador temos 3/2 + 4/3 = 17/6. Dividindo (17/6) / (17/6), obtém-se 1.",
            ques_resolucao_imagem_url="",
        ),
        Questao(
            ques_cont_id=conteudo4.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.FACIL,
            ques_enunciado="A fração geratriz da dízima 15,2222... é:",
            ques_imagem_url="",
            ques_alternativas={"A": "A) 133/99", "B": "B) 90/134", "C": "C) 137/9", "D": "D) 135/90", "E": "E) 2/9"},
            ques_resposta_correta=AlternativaEnum.C,
            ques_resolucao="Separando a parte inteira da periódica: x = 15 + 0,2222... = 15 + 2/9 = (135 + 2)/9 = 137/9.",
            ques_resolucao_imagem_url="",
        ),
        Questao(
            ques_cont_id=conteudo4.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.FACIL,
            ques_enunciado="A fração geratriz da dízima periódica 1,44444... é:",
            ques_imagem_url="",
            ques_alternativas={"A": "a) 17/9.", "B": "b) 11/9.", "C": "c) 5/9.", "D": "d) 13/9.", "E": "e) 12/9."},
            ques_resposta_correta=AlternativaEnum.D,
            ques_resolucao="Pelo método prático: 1 + 4/9 = 9/9 + 4/9 = 13/9. Pelo método algébrico: 10x - x = 14,444... - 1,444... → 9x = 13 → x = 13/9.",
            ques_resolucao_imagem_url="",
        ),
        Questao(
            ques_cont_id=conteudo4.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.MEDIO,
            ques_enunciado=(
                "(Objetiva Concursos) Considerando-se os intervalos numéricos A = [-5, 21], B = [0, 12], C = [-1, 17], analisar os itens abaixo:\n"
                "I. O intervalo A contém os valores do intervalo B, assim como o intervalo B contém os valores do intervalo C.\n"
                "II. Os valores do intervalo C estão contidos no intervalo A, mas não estão contidos no intervalo B.\n"
                "III. Os valores do intervalo B estão contidos no intervalo C, e os valores do intervalo B estão contidos no intervalo A.\n"
                "Está(ão) CORRETO(S):"
            ),
            ques_imagem_url="",
            ques_alternativas={
                "A": "A) Somente o item I.",
                "B": "B) Somente o item III.",
                "C": "C) Somente os itens I e II.",
                "D": "D) Somente os itens I e III.",
                "E": "E) Somente os itens II e III.",
            },
            ques_resposta_correta=AlternativaEnum.E,
            ques_resolucao="Na reta real, observa-se a relação de inclusão B ⊂ C ⊂ A (pois [0, 12] está dentro de [-1, 17], que está dentro de [-5, 21]). Assim, o item I é falso (B não contém C), enquanto os itens II e III são verdadeiros.",
            ques_resolucao_imagem_url="https://sabermatematica.com.br/wp-content/uploads/2022/05/intervalos-reais-exercicios.png",
        ),
    ]
    session.add_all(questoes)
    session.commit()

# CONTEÚDO 5 (Geometria Plana - Teorema de Tales, Semelhança e Relações Métricas)
def povoar_conteudo_5(session, base_url=""):
    conteudo5 = Conteudo(
        cont_nome="Geometria Plana (Teorema de Tales, Semelhança e Relações Métricas)",
        cont_etapa=EtapaEnum.ETAPA_1,
        cont_texto=(
            "1. TEOREMA DE TALES\n"
            "Um feixe de retas paralelas determina sobre duas retas transversais segmentos correspondentes proporcionais:\n"
            "• AB / BC = DE / EF   e   AB / AC = DE / DF.\n"
            "• Aplicação em Triângulos: toda reta paralela a um lado de um triângulo que intercepta os outros dois lados determina segmentos proporcionais e um triângulo menor semelhante ao original.\n\n"
            "2. SEMELHANÇA DE TRIÂNGULOS\n"
            "Dois triângulos são semelhantes (~) quando possuem ângulos correspondentes congruentes e lados homólogos proporcionais:\n"
            "• Caso AA (Ângulo-Ângulo): dois ângulos congruentes garantem a semelhança.\n"
            "• Caso LLL (Lado-Lado-Lado): os três pares de lados correspondentes são proporcionais.\n"
            "• Caso LAL (Lado-Ângulo-Lado): dois pares de lados proporcionais formando ângulos congruentes.\n\n"
            "3. RELAÇÕES MÉTRICAS NO TRIÂNGULO RETÂNGULO E PITÁGORAS\n"
            "Em um triângulo retângulo de hipotenusa a, catetos b e c, altura h relativa à hipotenusa e projeções m e n:\n"
            "• a = m + n\n"
            "• a · h = b · c\n"
            "• b² = a · n   e   c² = a · m\n"
            "• h² = m · n\n"
            "• Teorema de Pitágoras: a² = b² + c²."
        ),
        cont_texto_resumo="Estudo do Teorema de Tales, casos de semelhança de triângulos (AA, LLL, LAL), relações métricas no triângulo retângulo e Teorema de Pitágoras.",
        cont_slide_pdf=f"{base_url}/pdfs/GP-1-ANO_2.pdf",
        cont_imagem_url="",
        cont_relacionados={"topicos": ["Teorema de Tales", "Semelhança de Triângulos", "Teorema de Pitágoras", "Trigonometria no Triângulo Retângulo"]},
    )
    session.add(conteudo5)
    session.flush()

    questoes = [
        Questao(
            ques_cont_id=conteudo5.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.MEDIO,
            ques_enunciado="Considere o triângulo seguinte e determine o valor de x, sabendo que o segmento AD é a bissetriz relativa ao lado BC.",
            ques_imagem_url="https://media.brainly.com.br/image/rs:fill/w:750/q:75/plain/https://pt-static.z-dn.net/files/dc1/786cd9683719019bfe50e910819465f2.jpg",
            ques_alternativas={"A": "a) 9", "B": "b) 10", "C": "c) 11", "D": "d) 12", "E": "e) 13"},
            ques_resposta_correta=AlternativaEnum.C,
            ques_resolucao="Pelo teorema da bissetriz interna: (3x + 3) / 12 = (6x - 3) / 21 → 21(3x + 3) = 12(6x - 3) → 63x + 63 = 72x - 36 → 63 + 36 = 72x - 63x → 99 = 9x → x = 11.",
            ques_resolucao_imagem_url="",
        ),
        Questao(
            ques_cont_id=conteudo5.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.FACIL,
            ques_enunciado="As retas t, u e v são paralelas. Determine o valor da medida do segmento x.",
            ques_imagem_url="https://pt-static.z-dn.net/files/d4b/62846777c14d1b2cdf8a95a8d36ab54f.jpg",
            ques_alternativas={"A": "a) 18", "B": "b) 20", "C": "c) 21", "D": "d) 22", "E": "e) 24"},
            ques_resposta_correta=AlternativaEnum.C,
            ques_resolucao="Utilizando o Teorema de Tales, escrevemos a proporção entre os segmentos: 3/9 = 7/x → 3x = 7 · 9 → 3x = 63 → x = 63/3 → x = 21 cm.",
            ques_resolucao_imagem_url="",
        ),
        Questao(
            ques_cont_id=conteudo5.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.FACIL,
            ques_enunciado="Existem 5 bolas dispostas em uma mesa de bilhar. A reta formada entre as bolas 1 e 2 é paralela à reta formada entre as bolas 4 e 5. Conforme as medidas dispostas na imagem, responda: qual a distância entre as bolas 1 e 3?",
            ques_imagem_url="https://media.brainly.com.br/image/rs:fill/w:750/q:75/plain/https://pt-static.z-dn.net/files/d9b/d8f990ae473f5ba04045719be1ccd051.jpg",
            ques_alternativas={"A": "a) 20", "B": "b) 30", "C": "c) 40", "D": "d) 50", "E": "e) 60"},
            ques_resposta_correta=AlternativaEnum.C,
            ques_resolucao="Pelo Teorema de Tales: 75/50 = 60/x → 75x = 50 · 60 → 75x = 3000 → x = 3000/75 → x = 40. Portanto, a bola 1 está a 40 cm de distância da bola 3.",
            ques_resolucao_imagem_url="",
        ),
        Questao(
            ques_cont_id=conteudo5.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.MEDIO,
            ques_enunciado=(
                "(Colégio Pedro II - 2012) Para melhorar a qualidade do solo, aumentando a produtividade do milho e da soja, em uma fazenda é feito o rodízio entre essas culturas e a área destinada ao pasto. Com essa finalidade, a área produtiva da fazenda foi dividida em três partes conforme a figura.\n"
                "Considere que:\n"
                "- os pontos A, B, C e D estão alinhados;\n"
                "- os pontos H, G, F e E estão alinhados;\n"
                "- os segmentos AH, BG, CF e DE são, dois a dois, paralelos entre si;\n"
                "- AB = 500 m, BC = 600 m, CD = 700 m e HE = 1980 m.\n"
                "Nessas condições, a medida do segmento GF é, em metros,"
            ),
            ques_imagem_url="https://d23vy2bv3rsfba.cloudfront.net/questoes_imagens/0_c6e76cfd40197a1800252093d9f98e8e_171269.jpg.jpeg",
            ques_alternativas={"A": "a) 665.", "B": "b) 660.", "C": "c) 655.", "D": "d) 650.", "E": "e) 645."},
            ques_resposta_correta=AlternativaEnum.B,
            ques_resolucao="Como o valor informado foi do segmento HE (1980 m), que é a soma de HG, GF e FE, utilizamos também a soma de AB, BC e CD: 500 + 600 + 700 = 1800 m. Pelo Teorema de Tales: 1800/1980 = 600/GF → GF = (1980 · 600) / 1800 → GF = 660 m.",
            ques_resolucao_imagem_url="",
        ),
        Questao(
            ques_cont_id=conteudo5.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.MEDIO,
            ques_enunciado="(Enem - 2009) A rampa de um hospital tem na sua parte mais elevada uma altura de 2,2 metros. Um paciente ao caminhar sobre a rampa percebe que se deslocou 3,2 metros e alcançou uma altura de 0,8 metros. A distância em metros que o paciente ainda deve caminhar para atingir o ponto mais alto da rampa é",
            ques_imagem_url="",
            ques_alternativas={"A": "a) 1,16 metros.", "B": "b) 3,0 metros.", "C": "c) 5,4 metros.", "D": "d) 5,6 metros.", "E": "e) 7,04 metros."},
            ques_resposta_correta=AlternativaEnum.D,
            ques_resolucao="As duas alturas verticais (0,8 m e 2,2 m) formam ângulo de 90° com o solo, sendo paralelas entre si. Chamando de y o comprimento total da rampa, pelo Teorema de Tales (ou semelhança de triângulos): 3,2 / 0,8 = y / 2,2 → 0,8y = 3,2 · 2,2 → 0,8y = 7,04 → y = 7,04 / 0,8 → y = 8,8 m. Subtraindo o trecho já percorrido: x = 8,8 - 3,2 = 5,6 m.",
            ques_resolucao_imagem_url="",
        ),
        Questao(
            ques_cont_id=conteudo5.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.MEDIO,
            ques_enunciado="Existem alguns procedimentos que podem ser usados para descobrir se dois triângulos são semelhantes sem ter de analisar a proporcionalidade de todos os lados e, ao mesmo tempo, as medidas de todos os ângulos desses triângulos. A respeito desses casos, assinale a alternativa correta:",
            ques_imagem_url="",
            ques_alternativas={
                "A": "a) Para que dois triângulos sejam semelhantes, basta que eles tenham três ângulos correspondentes congruentes.",
                "B": "b) Para que dois triângulos sejam semelhantes, basta que eles tenham dois lados proporcionais e um ângulo congruente, em qualquer ordem.",
                "C": "c) Para que dois triângulos sejam congruentes, basta que eles tenham os três lados correspondentes com medidas proporcionais.",
                "D": "d) Dois triângulos que possuem dois lados correspondentes proporcionais não serão semelhantes em qualquer hipótese.",
                "E": "e) Dois triângulos que possuem apenas dois ângulos correspondentes congruentes não podem ser considerados semelhantes.",
            },
            ques_resposta_correta=AlternativaEnum.A,
            ques_resolucao="a) Correta: pelo caso AA (ou AAA), ter os ângulos correspondentes congruentes garante que os triângulos sejam semelhantes. b) Incorreta: pelo caso LAL, o ângulo congruente precisa estar entre os dois lados proporcionais. c) Incorreta: três lados proporcionais garantem semelhança (caso LLL), não necessariamente congruência. d) Incorreta: serão semelhantes se o ângulo entre esses lados for congruente. e) Incorreta: dois ângulos correspondentes congruentes já garantem a semelhança (caso AA).",
            ques_resolucao_imagem_url="",
        ),
        Questao(
            ques_cont_id=conteudo5.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.FACIL,
            ques_enunciado="Na imagem a seguir, é possível perceber dois triângulos que compartilham parte de dois lados. Sabendo que os segmentos BA e DE são paralelos, qual a medida de x?",
            ques_imagem_url="https://pt-static.z-dn.net/files/dd4/ad2dd1a3196ad410f65a4de9d807b938.jpg",
            ques_alternativas={"A": "a) 210 m", "B": "b) 220 m", "C": "c) 230 m", "D": "d) 240 m", "E": "e) 250 m"},
            ques_resposta_correta=AlternativaEnum.E,
            ques_resolucao="Quando um triângulo é cortado por um segmento paralelo a um de seus lados, forma-se um segundo triângulo menor semelhante ao primeiro. Aplicando a proporção: 400/x = 160/100 → 160x = 400 · 100 → 160x = 40000 → x = 40000/160 → x = 250 m.",
            ques_resolucao_imagem_url="",
        ),
        Questao(
            ques_cont_id=conteudo5.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.FACIL,
            ques_enunciado="Carla ao procurar seu gatinho o avistou em cima de uma árvore. Ela então pediu ajuda a sua mãe e colocaram uma escada junto à árvore para ajudar o gato a descer. Sabendo que o gato estava a 8 metros do chão e a base da escada estava posicionada a 6 metros da árvore, qual o comprimento da escada utilizada para salvar o gatinho?",
            ques_imagem_url="https://pt-static.z-dn.net/files/d4b/ac04d16bb649cb333902ae5085802d22.jpg",
            ques_alternativas={"A": "a) 8 metros.", "B": "b) 10 metros.", "C": "c) 12 metros.", "D": "d) 14 metros."},
            ques_resposta_correta=AlternativaEnum.B,
            ques_resolucao="A altura do gato (8 m) e a distância da base da escada até a árvore (6 m) formam um ângulo reto, sendo a escada a hipotenusa a do triângulo retângulo. Pelo Teorema de Pitágoras: a² = b² + c² → a² = 8² + 6² → a² = 64 + 36 → a² = 100 → a = √100 → a = 10 metros.",
            ques_resolucao_imagem_url="",
        ),
        Questao(
            ques_cont_id=conteudo5.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.DIFICIL,
            ques_enunciado="(IFRJ - 2013) O pátio de esportes do Campus Arrozal de um Instituto Federal é retangular, com 100 m de comprimento e 50 m de largura, representado pelo retângulo ABCD desta figura. Alberto e Bruno são dois alunos que estão praticando esportes no pátio. Alberto caminha do ponto A ao ponto C pela diagonal do retângulo e volta ao ponto de partida pelo mesmo caminho. Bruno parte do ponto B, dá uma volta completa no pátio, andando pelas linhas laterais, e volta ao ponto de partida. Assim, considerando √5 = 2,24, afirma-se que Bruno andou mais que Alberto",
            ques_imagem_url="https://pt-static.z-dn.net/files/dec/8d4e0057f3899c4dbf002e65095ca53b.jpg",
            ques_alternativas={"A": "a) 38 m.", "B": "b) 64 m.", "C": "c) 76 m.", "D": "d) 82 m."},
            ques_resposta_correta=AlternativaEnum.C,
            ques_resolucao="Calculando a diagonal d pelo Teorema de Pitágoras: d² = 100² + 50² = 10.000 + 2.500 = 12.500 → d = √(2² · 5⁴ · 5) = 2 · 5²√5 = 50√5. Substituindo √5 = 2,24: d = 50 · 2,24 = 112 m. Como Alberto foi e voltou, percorreu 2 · 112 = 224 m. Já Bruno percorreu o perímetro: p = 100 + 50 + 100 + 50 = 300 m. Diferença: 300 - 224 = 76 m.",
            ques_resolucao_imagem_url="",
        ),
        Questao(
            ques_cont_id=conteudo5.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.MEDIO,
            ques_enunciado=(
                "Em um triângulo retângulo ABC, com ângulo reto em A, a altura relativa à hipotenusa BC encontra-a no ponto D. Denotam-se por p = BD, q = DC as projeções dos catetos e por h = AD a altura.\n"
                "Considere as afirmações:\n"
                "I. h² = p × q\n"
                "II. AB² = BC × BD\n"
                "III. AC² = BC × DC\n"
                "IV. AB² + AC² = p × q\n"
                "É correto afirmar que são verdadeiras apenas:"
            ),
            ques_imagem_url="",
            ques_alternativas={"A": "a) I, II e III", "B": "b) I, II e IV", "C": "c) I, III e IV", "D": "d) II, III e IV"},
            ques_resposta_correta=AlternativaEnum.A,
            ques_resolucao="I. Verdadeira: o quadrado da altura relativa à hipotenusa é igual ao produto das projeções dos catetos (h² = p · q). II. Verdadeira: o quadrado de um cateto é igual ao produto da hipotenusa pela sua projeção (AB² = BC · BD). III. Verdadeira: analogamente para o outro cateto (AC² = BC · DC). IV. Falsa: pelo Teorema de Pitágoras, AB² + AC² = BC² (e não p · q).",
            ques_resolucao_imagem_url="",
        ),
    ]
    session.add_all(questoes)
    session.commit()

# CONTEÚDO 6: Trigonometria no triângulo Retângulo
def povoar_conteudo_6(session, base_url=""):
    conteudo6 = Conteudo(
        cont_nome="Trigonometria no Triângulo Retângulo",
        cont_etapa=EtapaEnum.ETAPA_1,
        cont_texto=(
            "1. RAZÕES TRIGONOMÉTRICAS NO TRIÂNGULO RETÂNGULO\n"
            "Em um triângulo retângulo, o lado oposto ao ângulo de 90° é a hipotenusa e os demais são os catetos. Para um ângulo agudo α:\n"
            "• Seno (sen α) = cateto oposto / hipotenusa\n"
            "• Cosseno (cos α) = cateto adjacente / hipotenusa\n"
            "• Tangente (tg α) = cateto oposto / cateto adjacente = sen α / cos α\n\n"
            "2. ÂNGULOS NOTÁVEIS (30°, 45° e 60°)\n"
            "• 30°: sen = 1/2 | cos = √3/2 | tg = √3/3\n"
            "• 45°: sen = √2/2 | cos = √2/2 | tg = 1\n"
            "• 60°: sen = √3/2 | cos = 1/2 | tg = √3\n\n"
            "3. RELAÇÃO FUNDAMENTAL E CÍRCULO TRIGONOMÉTRICO\n"
            "• Relação Fundamental: sen²α + cos²α = 1.\n"
            "• No círculo trigonométrico de raio unitário, o eixo vertical representa o seno e o eixo horizontal representa o cosseno."
        ),
        cont_texto_resumo="Estudo das razões trigonométricas no triângulo retângulo (seno, cosseno e tangente), ângulos notáveis (30°, 45° e 60°) e relação fundamental da trigonometria.",
        cont_slide_pdf=f"{base_url}/pdfs/IFUNÇÃO-GP2.pdf",
        cont_imagem_url=f"{base_url}/imagens/conteudos/gp2_razoes_trigonometricas_triangulo.png",
        cont_relacionados={"topicos": ["Teorema de Pitágoras", "Relações Métricas no Triângulo Retângulo", "Círculo Trigonométrico"]},
    )
    session.add(conteudo6)
    session.flush()

    questoes = [
        Questao(
            ques_cont_id=conteudo6.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.FACIL,
            ques_enunciado="Observando pela manhã a sombra de um prédio no chão, uma pessoa verificou que essa media 63 metros quando os raios de Sol faziam um ângulo de 30° com a superfície. Baseado nessas informações, calcule a altura do prédio.",
            ques_imagem_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRyJp8EPgKefa7NlH3pq6cvChphWI-xqFj_-tcm1_UhSX42_80F1Osu1-l8&s=10",
            ques_alternativas={"A": "a) 30,50 m", "B": "b) 20,10 m", "C": "c) 36,37 m", "D": "d) 38,45 m", "E": "e) 40,08 m"},
            ques_resposta_correta=AlternativaEnum.C,
            ques_resolucao="O prédio, a sombra e o raio de Sol determinam um triângulo retângulo. Utilizando o ângulo de 30° e a tangente, temos: tg 30° = h / 63 → h = 63 · (√3 / 3) → h = 21√3 → h ≈ 36,37 m.",
            ques_resolucao_imagem_url="",
        ),
        Questao(
            ques_cont_id=conteudo6.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.FACIL,
            ques_enunciado="Uma ciclista participando de um campeonato se aproxima da linha de chegada que se encontra no alto de uma ladeira. O comprimento total dessa última parte da prova é de 60 m e o ângulo formado entre a rampa e a horizontal é de 30°. Sabendo disso, calcule a altura vertical que a ciclista precisa subir.",
            ques_imagem_url="https://media.brainly.com.br/image/rs:fill/w:1920/q:75/plain/https://pt-static.z-dn.net/files/da4/1d3aed694c9bb498bbed985d9c49f0d8.jpg",
            ques_alternativas={"A": "a) 25 m", "B": "b) 30 m", "C": "c) 35 m", "D": "d) 45 m"},
            ques_resposta_correta=AlternativaEnum.B,
            ques_resolucao="A rampa representa a hipotenusa (60 m) e a altura vertical (h) é o cateto oposto ao ângulo de 30°: sen 30° = h / 60 → h = 60 · (1 / 2) → h = 30 m.",
            ques_resolucao_imagem_url="",
        ),
        Questao(
            ques_cont_id=conteudo6.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.MEDIO,
            ques_enunciado="(EPCAR-MG) Um avião decola de um ponto B sob inclinação constante de 15° com a horizontal. A 2 km de B se encontra a projeção vertical C do ponto mais alto D de uma serra de 600 m de altura, conforme a figura.\nDados: cos 15° = 0,97; sen 15° = 0,26; tg 15° = 0,27\nÉ correto afirmar que:",
            ques_imagem_url="https://media.brainly.com.br/image/rs:fill/w:1920/q:75/plain/https://pt-static.z-dn.net/files/d10/f141d1c1da53d0953f265d616bb1c769.jpg",
            ques_alternativas={
                "A": "a) Não haverá colisão do avião com a serra antes de alcançar 540 m de altura.",
                "B": "b) Haverá colisão do avião com a serra em 540 m de altura.",
                "C": "c) Haverá colisão do avião com a serra em D.",
                "D": "d) Se o avião decolar 220 m antes de B, mantendo a mesma inclinação, não haverá colisão do avião com a serra.",
            },
            ques_resposta_correta=AlternativaEnum.B,
            ques_resolucao="Passando 2 km para 2000 m e utilizando a tangente de 15° para definir a altura h: tg 15° = h / 2000 → h = 2000 · 0,27 → h = 540 m. Como a serra tem 600 m de altura, o avião colidirá com ela aos 540 m.",
            ques_resolucao_imagem_url="",
        ),
        Questao(
            ques_cont_id=conteudo6.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.FACIL,
            ques_enunciado="A figura abaixo representa um avião que decolou sob um ângulo constante de 40º e percorreu em linha reta 8000 m. Nesta situação, qual a altura que se encontrava o avião ao percorrer essa distância?\nConsidere: sen 40º = 0,64; cos 40º = 0,77; tg 40º = 0,84",
            ques_imagem_url="https://pt-static.z-dn.net/files/dcc/4f6ce275eaacdce237cc2a1fad3ee5d4.jpg",
            ques_alternativas={"A": "a) 5120 m", "B": "b) 6000 m", "C": "c) 4570 m", "D": "d) 3540 m"},
            ques_resposta_correta=AlternativaEnum.A,
            ques_resolucao="A distância percorrida representa a hipotenusa e a altura o cateto oposto ao ângulo de 40°: sen 40° = h / 8000 → 0,64 = h / 8000 → h = 8000 · 0,64 = 5120 m.",
            ques_resolucao_imagem_url="",
        ),
        Questao(
            ques_cont_id=conteudo6.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.MEDIO,
            ques_enunciado="Um menino avista o ponto mais alto de um morro, conforme figura abaixo. Considerando que ele está a uma distância de 500 m da base do morro, calcule a altura (h) deste ponto.\nConsidere: sen 20º = 0,34; cos 20º = 0,93; tg 20º = 0,36",
            ques_imagem_url="https://media.brainly.com.br/image/rs:fill/w:640/q:75/plain/https://pt-static.z-dn.net/files/dfa/720ffdffeb90dae528cd6f666f2e7478.jpg",
            ques_alternativas={"A": "a) 192,1 m", "B": "b) 131 m", "C": "c) 500,3 m", "D": "d) 181,3 m"},
            ques_resposta_correta=AlternativaEnum.D,
            ques_resolucao="Usando a tangente de 20°: tg 20° = x / 500 → x = 500 · 0,36 = 180 m. Somando a altura do menino (1,30 m): h = 180 + 1,30 = 181,3 m.",
            ques_resolucao_imagem_url="",
        ),
        Questao(
            ques_cont_id=conteudo6.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.MEDIO,
            ques_enunciado="Um terreno possui o formato de um retângulo cuja base mede 8 cm, sabendo que o ângulo formado entre a base e a diagonal é de 30º, qual o valor que mais se aproxima da diagonal? (Use √3 = 1,7)",
            ques_imagem_url="",
            ques_alternativas={"A": "a) 5", "B": "b) 6", "C": "c) 7", "D": "d) 8", "E": "e) 9"},
            ques_resposta_correta=AlternativaEnum.E,
            ques_resolucao="Seja x a diagonal: cos 30° = 8 / x → √3 / 2 = 8 / x → x = 16 / √3 = (16 · √3) / 3. Substituindo √3 = 1,7: x = (16 · 1,7) / 3 = 27,2 / 3 ≈ 9,06 cm.",
            ques_resolucao_imagem_url="",
        ),
        Questao(
            ques_cont_id=conteudo6.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.MEDIO,
            ques_enunciado="Qual deve ser o valor do seno de um ângulo, sabendo que ele se encontra no primeiro quadrante e que o cosseno desse mesmo ângulo é igual a 3/5?",
            ques_imagem_url="",
            ques_alternativas={"A": "a) 4/5", "B": "b) 2/5", "C": "c) 3/4", "D": "d) 1/5", "E": "e) 2/3"},
            ques_resposta_correta=AlternativaEnum.A,
            ques_resolucao="Pela relação fundamental sen²x + cos²x = 1: sen²x + (3/5)² = 1 → sen²x = 1 - 9/25 = 16/25 → sen x = √(16/25) = 4/5.",
            ques_resolucao_imagem_url="",
        ),
        Questao(
            ques_cont_id=conteudo6.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.FACIL,
            ques_enunciado="Um teleférico foi instalado ligando uma base ao cume de uma montanha. Para a instalação, foram utilizados 1358 m de cabos, dispostos a uma angulação de 30° em relação ao solo. Qual a altura da montanha?",
            ques_imagem_url="https://static.todamateria.com.br/upload/im/ag/image-627.jpg",
            ques_alternativas={"A": "a) 450", "B": "b) 300", "C": "c) 400", "D": "d) 579", "E": "e) 679"},
            ques_resposta_correta=AlternativaEnum.E,
            ques_resolucao="Usando o seno de 30° (0,5): sen 30° = h / 1358 → h = 1358 · 0,5 = 679 m.",
            ques_resolucao_imagem_url="",
        ),
        Questao(
            ques_cont_id=conteudo6.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.FACIL,
            ques_enunciado="Sendo o ângulo igual a 30° e a hipotenusa 47 m, calcule a medida da altura a do triângulo.",
            ques_imagem_url="https://pt-static.z-dn.net/files/df9/aa6f625a6eae79f03cd3e219340d81da.jpg",
            ques_alternativas={"A": "a) 20", "B": "b) 23,50", "C": "c) 30,50", "D": "d) 40", "E": "e) 50"},
            ques_resposta_correta=AlternativaEnum.B,
            ques_resolucao="Pelo seno de 30°: sen 30° = a / 47 → a = 47 · (1 / 2) = 23,50 m.",
            ques_resolucao_imagem_url="",
        ),
        Questao(
            ques_cont_id=conteudo6.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.DIFICIL,
            ques_enunciado="A vista superior de um parque mostra dois caminhos para se chegar ao ponto C, a partir do ponto A. Uma das opções é ir para B, onde há bebedouros e lugares de descanso e, depois, ir para C. Caso um visitante do parque queira ir direto para C, quantos metros ele terá caminhado a menos do que a primeira opção?\nConsiderar as aproximações:\n- sen 58° = 0,85\n- cos 58° = 0,53\n- tan 58° = 1,60",
            ques_imagem_url="https://pt-static.z-dn.net/files/df7/ce3f796a7eeed703aa49dca554288d73.png",
            ques_alternativas={"A": "a) 7,54", "B": "b) 3,50", "C": "c) 5", "D": "d) 6,75"},
            ques_resposta_correta=AlternativaEnum.A,
            ques_resolucao="Passo 1: sen 58° = 17 / h → h = 17 / 0,85 = 20 m.\nPasso 2: AB = 20 - 9,46 = 10,54 m.\nPasso 3: AB + BC = 10,54 + 17 = 27,54 m.\nPasso 4: Diferença (AB + BC) - AC = 27,54 - 20 = 7,54 m.",
            ques_resolucao_imagem_url="",
        ),
    ]
    session.add_all(questoes)
    session.commit()

# CONTEÚDO 7: FUNÇÕES E FUNÇÃO AFIM (FUNÇÃO DO 1º GRAU) 
def povoar_conteudo_7(session, base_url=""):
    conteudo7 = Conteudo(
        cont_nome="Funções e Função Afim (Função do 1º Grau)",
        cont_etapa=EtapaEnum.ETAPA_1,
        cont_texto=(
            "1. CONCEITO E CLASSIFICAÇÃO DE FUNÇÕES\n"
            "Uma função f: A → B associa cada elemento x do Domínio (A) a um único elemento y do Contradomínio (B). Os valores efetivamente atingidos formam o Conjunto Imagem (Im):\n"
            "• Injetora: elementos distintos do domínio possuem imagens distintas.\n"
            "• Sobrejetora: o conjunto imagem coincide com o contradomínio (Im(f) = B).\n"
            "• Bijetora: é simultaneamente injetora e sobrejetora, admitindo função inversa f⁻¹.\n\n"
            "2. FUNÇÃO AFIM (FUNÇÃO DO 1º GRAU)\n"
            "Definida por f(x) = ax + b, com a, b ∈ R e a ≠ 0:\n"
            "• Coeficiente angular (a): determina a taxa de variação e a inclinação da reta (a > 0: crescente; a < 0: decrescente).\n"
            "• Coeficiente linear (b): indica o ponto (0, b) onde o gráfico intercepta o eixo y.\n"
            "• Zero da função: raiz obtida fazendo f(x) = 0 → x = -b / a."
        ),
        cont_texto_resumo="Definição e classificação de funções (injetora, sobrejetora, bijetora e inversa), estudo da função afim f(x) = ax + b, coeficientes angular e linear, gráfico e zero da função.",
        cont_slide_pdf=f"{base_url}/pdfs/IFUNÇÃO-FA.pdf",
        cont_imagem_url=f"{base_url}/imagens/conteudos/fa_funcao_crescente_decrescente.png",
        cont_relacionados={"topicos": ["Função Quadrática", "Equação do 1º Grau", "Inequações do 1º Grau"]},
    )
    session.add(conteudo7)
    session.flush()

    questoes = [
        Questao(
            ques_cont_id=conteudo7.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.MEDIO,
            ques_enunciado=(
                "(UFMA) Considere as seguintes afirmações:\n"
                "I. Uma função é uma relação que associa a cada elemento do seu domínio um único elemento no seu contradomínio.\n"
                "II. Toda relação é uma função.\n"
                "III. Dada uma função sobrejetora, então seu contradomínio é diferente de sua imagem.\n"
                "IV. Uma função será injetora se, e somente se, elementos distintos do domínio possuírem imagens distintas.\n"
                "Assinale a alternativa correta:"
            ),
            ques_imagem_url="",
            ques_alternativas={
                "A": "a) I, II e III estão corretas.",
                "B": "b) I e II estão corretas.",
                "C": "c) III e I estão corretas.",
                "D": "d) II, III e IV estão corretas.",
                "E": "e) I e IV estão corretas.",
            },
            ques_resposta_correta=AlternativaEnum.E,
            ques_resolucao=(
                "I. Correta, pois cada elemento do domínio está associado a um único elemento do contradomínio.\n"
                "II. Incorreta, pois nem toda relação é função.\n"
                "III. Incorreta, pois na função sobrejetora a imagem é igual ao contradomínio.\n"
                "IV. Correta, pois cada elemento distinto do domínio possui imagem distinta. Portanto, apenas I e IV estão corretas."
            ),
            ques_resolucao_imagem_url="",
        ),
        Questao(
            ques_cont_id=conteudo7.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.FACIL,
            ques_enunciado="Dada a função f: N → Z definida por f(n) = 3n - 5. Podemos afirmar que f é:",
            ques_imagem_url="",
            ques_alternativas={
                "A": "a) Apenas sobrejetora",
                "B": "b) Apenas injetora",
                "C": "c) Bijetora",
                "D": "d) Nem injetora e nem sobrejetora",
                "E": "e) Injetora e sobrejetora apenas para os números ímpares",
            },
            ques_resposta_correta=AlternativaEnum.B,
            ques_resolucao="A função f(n) = 3n - 5 é injetora pois para cada dois valores distintos de n ∈ N obtemos sempre dois valores distintos de k ∈ Z, mas não é sobrejetora, pois Im(f) = {-5, -2, 1, 4, 7, ...} ≠ CD(f) = Z. Portanto, f é apenas injetora.",
            ques_resolucao_imagem_url="",
        ),
        Questao(
            ques_cont_id=conteudo7.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.MEDIO,
            ques_enunciado="Seja f(x) = √(5x - 3) inversível em todo o seu domínio. Se g(x) é função inversa de f, o valor de g(f(5)) é igual a:",
            ques_imagem_url="",
            ques_alternativas={"A": "a) 5", "B": "b) 4", "C": "c) 3", "D": "d) 2"},
            ques_resposta_correta=AlternativaEnum.A,
            ques_resolucao="O domínio de f exige 5x - 3 ≥ 0 → x ≥ 3/5. Como x = 5 pertence ao domínio de f e a função é inversível, aplicamos f⁻¹(f(x)) = x, logo g(f(5)) = 5.",
            ques_resolucao_imagem_url="",
        ),
        Questao(
            ques_cont_id=conteudo7.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.FACIL,
            ques_enunciado="Qual deve ser o valor de m para que a função definida por y = (3m - 5)x + 9 seja decrescente?",
            ques_imagem_url="",
            ques_alternativas={"A": "a) m > 5/3", "B": "b) m < -3/5", "C": "c) m < 5/3", "D": "d) m > -3/5"},
            ques_resposta_correta=AlternativaEnum.C,
            ques_resolucao="Para que a função y = ax + b seja decrescente devemos ter a < 0. Assim: 3m - 5 < 0 → 3m < 5 → m < 5/3.",
            ques_resolucao_imagem_url="",
        ),
        Questao(
            ques_cont_id=conteudo7.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.MEDIO,
            ques_enunciado=(
                "(Cefet - MG - 2015) Um motorista de táxi cobra, para cada corrida, uma taxa fixa de R$ 5,00 e mais R$ 2,00 por quilômetro rodado. "
                "O valor total arrecadado (R) num dia é função da quantidade total (x) de quilômetros percorridos e calculado por meio da função R(x) = ax + b, "
                "em que a é o preço cobrado por quilômetro e b, a soma de todas as taxas fixas recebidas no dia. Se, em um dia, o taxista realizou 10 corridas "
                "e arrecadou R$ 410,00, então a média de quilômetros rodados por corrida foi de:"
            ),
            ques_imagem_url="",
            ques_alternativas={"A": "a) 14", "B": "b) 16", "C": "c) 18", "D": "d) 20"},
            ques_resposta_correta=AlternativaEnum.C,
            ques_resolucao="Temos a = 2 e b = 10 · 5 = 50, logo R(x) = 2x + 50. Fazendo R(x) = 410: 410 = 2x + 50 → 2x = 360 → x = 180 km no dia. Dividindo pelas 10 corridas: 180 / 10 = 18 km.",
            ques_resolucao_imagem_url="",
        ),
        Questao(
            ques_cont_id=conteudo7.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.DIFICIL,
            ques_enunciado="(Unicamp - 2016) Considere a função afim f(x) = ax + b definida para todo número real x, onde a e b são números reais. Sabendo que f(4) = 2, podemos afirmar que f(f(3) + f(5)) é igual a:",
            ques_imagem_url="",
            ques_alternativas={"A": "a) 5", "B": "b) 4", "C": "c) 3", "D": "d) 2"},
            ques_resposta_correta=AlternativaEnum.D,
            ques_resolucao="Como f(4) = 4a + b = 2, temos f(f(3) + f(5)) = f((3a + b) + (5a + b)) = f(8a + 2b) = f(2(4a + b)) = f(2 · 2) = f(4) = 2.",
            ques_resolucao_imagem_url="",
        ),
        Questao(
            ques_cont_id=conteudo7.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.FACIL,
            ques_enunciado=(
                "(Encceja 2018) Uma prestadora de serviços cobra pela visita à residência do cliente e pelo tempo necessário para realizar o serviço na residência. "
                "O valor da visita é R$ 40 e o valor da hora para realização do serviço é R$ 20. Uma expressão que indica o valor a ser pago (P) em função das horas (h) necessárias à execução do serviço é:"
            ),
            ques_imagem_url="",
            ques_alternativas={"A": "a) P = 40h", "B": "b) P = 60h", "C": "c) P = 20 + 40h", "D": "d) P = 40 + 20h"},
            ques_resposta_correta=AlternativaEnum.D,
            ques_resolucao="A função é P = ah + b, em que b = 40 (taxa fixa da visita) e a = 20 (valor por hora). Substituindo, temos P = 40 + 20h.",
            ques_resolucao_imagem_url="",
        ),
        Questao(
            ques_cont_id=conteudo7.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.FACIL,
            ques_enunciado=(
                "(UFSM) Sabe-se que o preço a ser pago por uma corrida de táxi inclui uma parcela fixa, que é denominada bandeirada, e uma parcela variável, "
                "que é função da distância percorrida. Se o preço da bandeirada é de R$ 4,60 e o quilômetro rodado é R$ 0,96, a distância percorrida pelo passageiro "
                "que pagou R$ 19 para ir de sua casa ao shopping é de:"
            ),
            ques_imagem_url="",
            ques_alternativas={"A": "a) 5 km", "B": "b) 10 km", "C": "c) 15 km", "D": "d) 20 km", "E": "e) 25 km"},
            ques_resposta_correta=AlternativaEnum.C,
            ques_resolucao="Sendo d a distância em quilômetros: 19 = 0,96d + 4,6 → 14,4 = 0,96d → d = 14,4 / 0,96 = 15 km.",
            ques_resolucao_imagem_url="",
        ),
        Questao(
            ques_cont_id=conteudo7.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.FACIL,
            ques_enunciado="Podemos afirmar que o zero da função f(x) = -2x + 5 é igual a:",
            ques_imagem_url="",
            ques_alternativas={"A": "a) 2", "B": "b) 2,5", "C": "c) -2,5", "D": "d) -3", "E": "e) 3"},
            ques_resposta_correta=AlternativaEnum.B,
            ques_resolucao="Igualando a função a zero: -2x + 5 = 0 → -2x = -5 → x = (-5) / (-2) = 2,5.",
            ques_resolucao_imagem_url="",
        ),
        Questao(
            ques_cont_id=conteudo7.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.MEDIO,
            ques_enunciado=(
                "Um fazendeiro resolveu investir em uma colheitadeira para facilitar o serviço na plantação. Sabendo que o valor pago foi de R$ 300.000 no ano da compra, "
                "é bastante comum que máquinas desse porte percam o seu valor V ao decorrer dos anos t. Supondo que a taxa de depreciação de uma máquina desse porte é de "
                "R$ 22.000 por ano, devido ao seu constante uso, podemos afirmar que o valor da colheitadeira, ao final de 7 anos, será de:"
            ),
            ques_imagem_url="",
            ques_alternativas={"A": "a) R$ 154.000", "B": "b) R$ 246.000", "C": "c) R$ 146.000", "D": "d) R$ 174.000", "E": "e) R$ 210.000"},
            ques_resposta_correta=AlternativaEnum.C,
            ques_resolucao="A lei de formação é V(t) = -22.000t + 300.000. Para t = 7 anos: V(7) = -22.000 · 7 + 300.000 = -154.000 + 300.000 = R$ 146.000.",
            ques_resolucao_imagem_url="",
        ),
    ]
    session.add_all(questoes)
    session.commit()

# CONTEÚDO 8: FUNÇÃO QUADRÁTICA, EXPONENCIAL E LOGARÍTMICA 
def povoar_conteudo_8(session, base_url=""):
    conteudo8 = Conteudo(
        cont_nome="Função Quadrática, Exponencial e Logarítmica",
        cont_etapa=EtapaEnum.ETAPA_1,
        cont_texto=(
            "1. FUNÇÃO QUADRÁTICA (FUNÇÃO DO 2º GRAU)\n"
            "Definida por f(x) = ax² + bx + c, com a, b, c ∈ R e a ≠ 0. Seu gráfico é uma parábola:\n"
            "• Concavidade: para cima se a > 0 (ponto de mínimo) e para baixo se a < 0 (ponto de máximo).\n"
            "• Discriminante (Δ = b² - 4ac) e raízes: x = (-b ± √Δ) / 2a.\n"
            "• Vértice da parábola: V = (-b / 2a, -Δ / 4a).\n\n"
            "2. FUNÇÃO EXPONENCIAL\n"
            "Definida por f(x) = a^x, com a > 0 e a ≠ 1:\n"
            "• Passa pelo ponto (0, 1) e possui imagem estritamente positiva (R*+).\n"
            "• Crescente quando a > 1 e decrescente quando 0 < a < 1.\n\n"
            "3. FUNÇÃO LOGARÍTMICA\n"
            "Inversa da exponencial, definida de R*+ → R por f(x) = log_a(x) (a > 0 e a ≠ 1), em que log_a(x) = y ⇔ a^y = x:\n"
            "• Domínio: logaritmando estritamente positivo (x > 0).\n"
            "• Intercepta o eixo x no ponto (1, 0); crescente se a > 1 e decrescente se 0 < a < 1."
        ),
        cont_texto_resumo="Estudo da função quadrática (parábola, raízes e vértice), função exponencial (crescimento, decrescimento e equações) e função logarítmica (definição, domínio e propriedades).",
        cont_slide_pdf=f"{base_url}/pdfs/IFUNÇÃO-1-FQ_2.pdf",
        cont_imagem_url=f"{base_url}/imagens/conteudos/fq_parabolas_concavidade.png",
        cont_relacionados={"topicos": ["Função Afim", "Equação do 2º Grau", "Logaritmos"]},
    )
    session.add(conteudo8)
    session.flush()

    questoes = [
        Questao(
            ques_cont_id=conteudo8.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.MEDIO,
            ques_enunciado="(UERJ - 2016) Observe a função f, definida por: f(x) = x² - 2kx + 29, para x ∈ ℝ. Se f(x) ≥ 4, para todo número real x, o valor mínimo da função f é 4. Assim, o valor positivo do parâmetro k é:",
            ques_imagem_url="",
            ques_alternativas={"A": "a) 5", "B": "b) 6", "C": "c) 10", "D": "d) 15"},
            ques_resposta_correta=AlternativaEnum.A,
            ques_resolucao="Como a = 1 > 0, o vértice é ponto de mínimo e yv = 4. Usando yv = -Δ / 4a: 4 = -((-2k)² - 4 · 1 · 29) / 4 → 16 = -(4k² - 116) → 4k² = 100 → k² = 25 → k = ±5. Como pede o valor positivo, k = 5.",
            ques_resolucao_imagem_url="",
        ),
        Questao(
            ques_cont_id=conteudo8.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.FACIL,
            ques_enunciado="Dada a função f(x) = x² - 4x + 5, o valor de f(2) é:",
            ques_imagem_url="",
            ques_alternativas={"A": "a) 0.", "B": "b) 1.", "C": "c) 3.", "D": "d) 4.", "E": "e) 7."},
            ques_resposta_correta=AlternativaEnum.B,
            ques_resolucao="Calculando f(2): f(2) = 2² - 4 · 2 + 5 = 4 - 8 + 5 = 1.",
            ques_resolucao_imagem_url="",
        ),
        Questao(
            ques_cont_id=conteudo8.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.FACIL,
            ques_enunciado="A concavidade da parábola da função f(x) = -3x² + 2x + 1 é:",
            ques_imagem_url="",
            ques_alternativas={
                "A": "a) voltada para cima.",
                "B": "b) inexistente.",
                "C": "c) voltada para baixo.",
                "D": "d) vertical.",
                "E": "e) horizontal.",
            },
            ques_resposta_correta=AlternativaEnum.C,
            ques_resolucao="O que determina a concavidade da parábola é o valor do coeficiente a, que é igual a -3 (negativo); nesse caso, a parábola possui a concavidade voltada para baixo.",
            ques_resolucao_imagem_url="",
        ),
        Questao(
            ques_cont_id=conteudo8.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.MEDIO,
            ques_enunciado="A trajetória de uma bola chutada é descrita pela função h(t) = -5t² + 20t, em que h(t) é a altura em metros e t é o tempo em segundos. A altura máxima atingida pela bola é:",
            ques_imagem_url="",
            ques_alternativas={"A": "a) 10 m.", "B": "b) 15 m.", "C": "c) 20 m.", "D": "d) 25 m.", "E": "e) 30 m."},
            ques_resposta_correta=AlternativaEnum.C,
            ques_resolucao="Para calcular o vértice da parábola: Δ = b² - 4ac = 20² - 4 · (-5) · 0 = 400. Assim, yv = -Δ / 4a = -400 / (4 · (-5)) = -400 / (-20) = 20 m.",
            ques_resolucao_imagem_url="",
        ),
        Questao(
            ques_cont_id=conteudo8.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.FACIL,
            ques_enunciado="Dada a função f(x) = 2^(x+3) + 10, o valor de x para que f(x) = 42 é de:",
            ques_imagem_url="",
            ques_alternativas={"A": "a) 2", "B": "b) 3", "C": "c) 4", "D": "d) 5", "E": "e) 6"},
            ques_resposta_correta=AlternativaEnum.A,
            ques_resolucao="Igualando a lei de formação a 42: 2^(x+3) + 10 = 42 → 2^(x+3) = 32 → 2^(x+3) = 2⁵ → x + 3 = 5 → x = 5 - 3 = 2.",
            ques_resolucao_imagem_url="",
        ),
        Questao(
            ques_cont_id=conteudo8.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.MEDIO,
            ques_enunciado="O gráfico, a seguir, é a representação de uma função exponencial. Analisando o gráfico, a lei de formação dessa função exponencial é:",
            ques_imagem_url="https://media.brainly.com.br/image/rs:fill/w:828/q:75/plain/https://pt-static.z-dn.net/files/dea/fd8eba92c4770abf1bb37e9da4e81e26.jpg",
            ques_alternativas={"A": "a) f(x) = 5^x", "B": "b) f(x) = 0,2^x", "C": "c) f(x) = 2^x", "D": "d) f(x) = 0,5^x", "E": "e) f(x) = 0,5^(-x)"},
            ques_resposta_correta=AlternativaEnum.D,
            ques_resolucao="Analisando o plano cartesiano, o ponto (-1, 2) pertence à função exponencial decrescente f(x) = a^x: a⁻¹ = 2 → 1/a = 2 → a = 1/2 = 0,5. Portanto, f(x) = 0,5^x.",
            ques_resolucao_imagem_url="",
        ),
        Questao(
            ques_cont_id=conteudo8.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.FACIL,
            ques_enunciado="Dada uma função de R → R com a lei de formação f(x) = a^x, em que a é um número positivo diferente de 1, julgue as afirmativas a seguir:\nI → Essa função será crescente se a for positivo.\nII → Se x = 0, então, f(x) = 1.\nIII → Essa é uma função exponencial.\nMarque a alternativa correta:",
            ques_imagem_url="",
            ques_alternativas={
                "A": "a) Somente a afirmativa I é falsa.",
                "B": "b) Somente a afirmativa II é falsa.",
                "C": "c) Somente a afirmativa III é falsa.",
                "D": "d) Todas as afirmativas são verdadeiras.",
                "E": "e) Todas as afirmativas são falsas.",
            },
            ques_resposta_correta=AlternativaEnum.A,
            ques_resolucao="I → Falsa, pois para ser crescente a deve ser maior que 1 (se 0 < a < 1, mesmo positivo, será decrescente). II → Verdadeira, f(0) = a⁰ = 1. III → Verdadeira, pois a variável está no expoente.",
            ques_resolucao_imagem_url="",
        ),
        Questao(
            ques_cont_id=conteudo8.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.DIFICIL,
            ques_enunciado="Observe o gráfico da função logarítmica abaixo. A função g(x) representada no gráfico pode ser definida como:",
            ques_imagem_url="https://static.todamateria.com.br/upload/fu/nc/funcao-0-cke.jpg",
            ques_alternativas={"A": "a) g(x) = log₃(x)", "B": "b) g(x) = log₃(x + 4)", "C": "c) g(x) = log₂(x - 3)", "D": "d) g(x) = log₂(x + 3)"},
            ques_resposta_correta=AlternativaEnum.C,
            ques_resolucao="Observa-se que o gráfico de g(x) é uma translação horizontal de 3 unidades para a direita (assíntota vertical em x = 3 e raiz em x = 4, onde g(4) = log₂(4 - 3) = log₂(1) = 0). Logo, g(x) = log₂(x - 3).",
            ques_resolucao_imagem_url="",
        ),
        Questao(
            ques_cont_id=conteudo8.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.FACIL,
            ques_enunciado="Seja f(x) = log₂(x) e g(x) = log₃(x) a lei de formação de duas funções f(x) e g(x), então o valor de f(8) – g(9) é igual a:",
            ques_imagem_url="",
            ques_alternativas={"A": "a) 0.", "B": "b) 1.", "C": "c) 2.", "D": "d) –1.", "E": "e) –2."},
            ques_resposta_correta=AlternativaEnum.B,
            ques_resolucao="Calculando f(8) = log₂(8) = 3 e g(9) = log₃(9) = 2. Por fim, a diferença entre elas é 3 - 2 = 1.",
            ques_resolucao_imagem_url="",
        ),
        Questao(
            ques_cont_id=conteudo8.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.MEDIO,
            ques_enunciado="Durante os estudos sobre o crescimento de uma determinada árvore, foi possível modelar o crescimento dela no decorrer do tempo por meio da função A(t) = 1 + log₃(5 + t), em que t é o tempo em anos e A(t) é a altura em metros. Sendo assim, podemos afirmar que a altura dessa árvore, após 4 anos, será de:",
            ques_imagem_url="",
            ques_alternativas={"A": "a) 1 metro.", "B": "b) 2 metros.", "C": "c) 2 metros e meio.", "D": "d) 3 metros.", "E": "e) 3 metros e meio."},
            ques_resposta_correta=AlternativaEnum.D,
            ques_resolucao="Substituindo t = 4: A(4) = 1 + log₃(5 + 4) = 1 + log₃(9) = 1 + 2 = 3 metros.",
            ques_resolucao_imagem_url="",
        ),
    ]
    session.add_all(questoes)
    session.commit()

# SIMULADO 1: ETAPA 1 
def povoar_simulado_1(db: Session, base_url: str = ""):
    questoes = [
        Questao(
            ques_cont_id=None,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.FACIL,
            ques_enunciado=(
                "(Enem 2020) Uma empresa de ônibus utiliza um sistema de vendas de passagens que fornece a imagem de todos os assentos do ônibus, "
                "diferenciando os assentos já vendidos, por uma cor mais escura, dos assentos ainda disponíveis. A empresa monitora, permanentemente, "
                "o número de assentos já vendidos e compara-o com o número total de assentos do ônibus para avaliar a necessidade de alocação de veículos extras. "
                "Na imagem tem-se a informação dos assentos já vendidos e dos ainda disponíveis em um determinado instante.\n"
                "A razão entre o número de assentos já vendidos e o total de assentos desse ônibus, no instante considerado na imagem, é:"
            ),
            ques_imagem_url="https://arquivos.qconcursos.com/images/provas/78987/98d75f163cb9f8f53a4e.png",
            ques_alternativas={"A": "a) 16/42", "B": "b) 16/26", "C": "c) 26/42", "D": "d) 42/26", "E": "e) 42/16"},
            ques_resposta_correta=AlternativaEnum.A,
            ques_resolucao="Contando os assentos na imagem, há 16 assentos escuros (já vendidos) em um total de 42 lugares. Assim, a razão procurada é 16/42.",
            ques_resolucao_imagem_url="",
        ),
        Questao(
            ques_cont_id=None,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.MEDIO,
            ques_enunciado=(
                "(Enem 2020) O consumo de espumantes no Brasil tem aumentado nos últimos anos. Uma das etapas do seu processo de produção consiste no "
                "envasamento da bebida em garrafas semelhantes às da imagem. Nesse processo, a vazão do líquido no interior da garrafa é constante e cessa "
                "quando atinge o nível de envasamento.\n"
                "Qual esboço de gráfico melhor representa a variação da altura do líquido em função do tempo, na garrafa indicada na imagem?"
            ),
            ques_imagem_url="https://i0.wp.com/humorquantico.com/wp-content/uploads/2021/11/O-consumo-de-espumantes-no-Brasil-tem-aumentado.png?w=397&ssl=1",
            ques_alternativas={
                "A": "a) https://i0.wp.com/humorquantico.com/wp-content/uploads/2021/11/a.png?w=469&ssl=1",
                "B": "b) https://i0.wp.com/humorquantico.com/wp-content/uploads/2021/11/B.png?w=454&ssl=1",
                "C": "c) https://i0.wp.com/humorquantico.com/wp-content/uploads/2021/11/C.png?w=459&ssl=1",
                "D": "d) https://i0.wp.com/humorquantico.com/wp-content/uploads/2021/11/D.png?w=452&ssl=1",
                "E": "e) https://i0.wp.com/humorquantico.com/wp-content/uploads/2021/11/E.png?w=448&ssl=1",
            },
            ques_resposta_correta=AlternativaEnum.B,
            ques_resolucao=(
                "Na 1ª seção (cilíndrica), o volume por unidade de altura é constante; como a vazão é constante, a altura cresce linearmente (reta inclinada). "
                "Na 2ª seção (afunilamento da garrafa), conforme a altura aumenta o diâmetro diminui, fazendo o nível subir cada vez mais rápido (curva crescente côncava para cima)."
            ),
            ques_resolucao_imagem_url="https://sabermatematica.com.br/wp-content/uploads/2021/06/resposta-da-questao-grafico-da-funcao-garrafa-enem-2020.png",
        ),
        Questao(
            ques_cont_id=None,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.FACIL,
            ques_enunciado=(
                "O estádio do Maracanã passou por algumas modificações estruturais para a realização da Copa do Mundo de 2014, como, por exemplo, "
                "as dimensões do campo retangular. Para se adaptar aos padrões da Fifa, as dimensões do campo foram reduzidas de 110 m × 75 m para 105 m × 68 m.\n"
                "Em quantos metros quadrados a área do campo do Maracanã foi reduzida?"
            ),
            ques_imagem_url="",
            ques_alternativas={"A": "a) 24", "B": "b) 35", "C": "c) 555", "D": "d) 1110", "E": "e) 1145"},
            ques_resposta_correta=AlternativaEnum.D,
            ques_resolucao="Área original: 110 · 75 = 8.250 m². Área nova: 105 · 68 = 7.140 m². Redução: 8.250 - 7.140 = 1.110 m².",
            ques_resolucao_imagem_url="",
        ),
        Questao(
            ques_cont_id=None,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.FACIL,
            ques_enunciado=(
                "O uso de aplicativos de transporte tem sido uma alternativa à população que busca preços mais competitivos para se locomover, "
                "principalmente nas grandes cidades. Em geral, o valor V a ser pago, em real, varia em função de: tarifa base F (valor fixo), tempo T (em minuto) "
                "e distância D (em quilômetro). Um desses aplicativos cobra R$ 2,00 de valor fixo, acrescido de R$ 0,26 por minuto de viagem e de R$ 1,40 por quilômetro rodado.\n"
                "Nessas condições, a expressão que fornece o valor V a ser pago por uma viagem desse aplicativo é:"
            ),
            ques_imagem_url="",
            ques_alternativas={
                "A": "a) 2,00F + 0,26T + 1,40D",
                "B": "b) 2,00 + 0,26T + 1,40D",
                "C": "c) 2,00 + 0,26T + D",
                "D": "d) 0,26T + 1,40D",
                "E": "e) F + T + D",
            },
            ques_resposta_correta=AlternativaEnum.B,
            ques_resolucao="Somando o valor fixo de R$ 2,00 ao custo por minuto (0,26T) e ao custo por quilômetro (1,40D), temos V = 2,00 + 0,26T + 1,40D.",
            ques_resolucao_imagem_url="",
        ),
        Questao(
            ques_cont_id=None,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.FACIL,
            ques_enunciado=(
                "Os 100 funcionários de uma empresa estão distribuídos em dois setores: Produção e Administração. Os funcionários de um mesmo setor "
                "recebem salários com valores iguais. O quadro apresenta a quantidade de funcionários por setor e seus respectivos salários.\n"
                "A média dos salários dos 100 funcionários dessa empresa, em real, é:"
            ),
            ques_imagem_url="https://qcon-assets-production.s3.amazonaws.com/images/provas/101194/Captura_de%20Tela%20%283497%29.png",
            ques_alternativas={
                "A": "a) 2 000,00.",
                "B": "b) 2 500,00.",
                "C": "c) 3 250,00.",
                "D": "d) 4 500,00.",
                "E": "e) 9 000,00.",
            },
            ques_resposta_correta=AlternativaEnum.C,
            ques_resolucao="Média ponderada: (75 · 2.000 + 25 · 7.000) / 100 = (150.000 + 175.000) / 100 = 325.000 / 100 = R$ 3.250,00.",
            ques_resolucao_imagem_url="",
        ),
        Questao(
            ques_cont_id=None,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.MEDIO,
            ques_enunciado=(
                "O ideal é consumir 1 grama de carboidrato para cada minuto de caminhada. Um casal realizará diariamente 30 minutos de caminhada, "
                "ingerindo, antes dessa atividade, a quantidade ideal de carboidratos recomendada. Para ter o consumo ideal apenas por meio do consumo de "
                "pão de fôrma integral, o casal planeja garantir o suprimento de pães para um período de 30 dias ininterruptos. Sabe-se que cada pacote desse "
                "pão vem com 18 fatias, e que cada uma delas tem 15 gramas de carboidratos.\n"
                "A quantidade mínima de pacotes de pão de fôrma necessários para prover o suprimento a esse casal é:"
            ),
            ques_imagem_url="",
            ques_alternativas={"A": "a) 6", "B": "b) 7", "C": "c) 8", "D": "d) 9", "E": "e) 10"},
            ques_resposta_correta=AlternativaEnum.B,
            ques_resolucao=(
                "Consumo diário do casal: 30 g · 2 pessoas = 60 g/dia. Em 30 dias: 60 · 30 = 1.800 g. "
                "Cada pacote fornece 18 · 15 = 270 g. Dividindo: 1.800 / 270 ≈ 6,67 pacotes, sendo necessários no mínimo 7 pacotes."
            ),
            ques_resolucao_imagem_url="",
        ),
        Questao(
            ques_cont_id=None,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.FACIL,
            ques_enunciado=(
                "Um investidor iniciante observou o gráfico que apresenta a evolução dos valores de duas criptomoedas A e B em relação ao tempo.\n"
                "Durante horas consecutivas, esses valores foram observados em nove instantes, representados por horas exatas.\n"
                "Em quantos desses instantes a criptomoeda A estava mais valorizada do que a criptomoeda B?"
            ),
            ques_imagem_url="https://qcon-assets-production.s3.amazonaws.com/images/provas/101194/Captura_de%20Tela%20%283507%29.png",
            ques_alternativas={"A": "a) 3", "B": "b) 4", "C": "c) 6", "D": "d) 7", "E": "e) 9"},
            ques_resposta_correta=AlternativaEnum.B,
            ques_resolucao="Traçando a reta diagonal x = y que divide o gráfico ao meio, verifica-se que há 4 pontos abaixo/à direita dela (onde o valor de A supera o de B).",
            ques_resolucao_imagem_url="https://paperx-dex-assets.s3.sa-east-1.amazonaws.com/images/1701697515850-jXXnrFXLXG.png",
        ),
        Questao(
            ques_cont_id=None,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.MEDIO,
            ques_enunciado=(
                "Um agricultor é informado sobre um método de proteção para sua lavoura que consiste em inserir larvas específicas, de rápida reprodução. "
                "A reprodução dessas larvas faz com que sua população multiplique-se por 10 a cada 3 dias e, para evitar eventuais desequilíbrios, é possível cessar "
                "essa reprodução aplicando-se um produto X. O agricultor decide iniciar esse método com 100 larvas e dispõe de 5 litros do produto X, cuja aplicação "
                "recomendada é de exatamente 1 litro para cada população de 200 000 larvas. A quantidade total do produto X de que ele dispõe deverá ser aplicada de uma única vez.\n"
                "Quantos dias após iniciado esse método o agricultor deverá aplicar o produto X?"
            ),
            ques_imagem_url="",
            ques_alternativas={"A": "a) 2", "B": "b) 4", "C": "c) 6", "D": "d) 12", "E": "e) 18"},
            ques_resposta_correta=AlternativaEnum.D,
            ques_resolucao=(
                "Com 5 L, pode-se controlar 5 · 200.000 = 1.000.000 = 10⁶ larvas. "
                "Pela função exponencial P(t) = 100 · 10^(t/3) = 10⁶ → 10^(t/3) = 10⁴ → t/3 = 4 → t = 12 dias."
            ),
            ques_resolucao_imagem_url="",
        ),
        Questao(
            ques_cont_id=None,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.FACIL,
            ques_enunciado=(
                "Para concretar a laje de sua residência, uma pessoa contratou uma construtora. Tal empresa informa que o preço y do concreto bombeado é "
                "composto de duas partes: uma fixa, chamada de taxa de bombeamento, e uma variável, que depende do volume x de concreto utilizado. "
                "Sabe-se que a taxa de bombeamento custa R$ 500,00 e que o metro cúbico do concreto bombeado é de R$ 250,00.\n"
                "A expressão que representa o preço y em função do volume x, em metro cúbico, é:"
            ),
            ques_imagem_url="",
            ques_alternativas={
                "A": "a) y = 250x",
                "B": "b) y = 500x",
                "C": "c) y = 750x",
                "D": "d) y = 250x + 500",
                "E": "e) y = 500x + 250",
            },
            ques_resposta_correta=AlternativaEnum.D,
            ques_resolucao="A função afim é formada pela parcela variável (250x) somada à taxa fixa de bombeamento (500), resultando em y = 250x + 500.",
            ques_resolucao_imagem_url="",
        ),
        Questao(
            ques_cont_id=None,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.FACIL,
            ques_enunciado=(
                "Entre maratonistas, um parâmetro utilizado é o de economia de corrida (EC). O valor desse parâmetro é calculado pela razão entre o consumo "
                "de oxigênio, em mililitro (mL) por minuto (min), e a massa, em quilograma (kg), do atleta correndo a uma velocidade constante.\n"
                "A unidade de medida da grandeza descrita pelo parâmetro EC é:"
            ),
            ques_imagem_url="",
            ques_alternativas={
                "A": "a) min/mL.kg",
                "B": "b) mL/min . kg",
                "C": "c) min . mL/kg",
                "D": "d) min . kg/mL",
                "E": "e) mL . kg/min",
            },
            ques_resposta_correta=AlternativaEnum.B,
            ques_resolucao="Dividindo a unidade de consumo de oxigênio (mL/min) pela unidade de massa (kg), obtém-se (mL/min) / kg = mL / (min · kg).",
            ques_resolucao_imagem_url="",
        ),
        Questao(
            ques_cont_id=None,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.MEDIO,
            ques_enunciado=(
                "A figura ilustra uma roda-gigante no exato instante em que a cadeira onde se encontra a pessoa P está no ponto mais alto dessa roda-gigante.\n"
                "Com o passar do tempo, à medida que a roda-gigante gira, com velocidade angular constante e no sentido horário, a altura da cadeira onde se "
                "encontra a pessoa P, em relação ao solo, vai se alterando.\n"
                "O gráfico que melhor representa a variação dessa altura, em função do tempo, contado a partir do instante em que a cadeira da pessoa P se "
                "encontra na posição mais alta da roda-gigante, é:"
            ),
            ques_imagem_url="https://static.wixstatic.com/media/295c7b_12567336d7fb431ebbd157bc20337cae~mv2.png/v1/fill/w_299,h_314,al_c,q_85,enc_avif,quality_auto/295c7b_12567336d7fb431ebbd157bc20337cae~mv2.png",
            ques_alternativas={
                "A": "a) https://static.wixstatic.com/media/295c7b_3e76590a1f094d49ba46b9d65983890a~mv2.png/v1/fill/w_347,h_135,al_c,q_85,enc_avif,quality_auto/295c7b_3e76590a1f094d49ba46b9d65983890a~mv2.png",
                "B": "b) https://static.wixstatic.com/media/295c7b_359a976db3a54df1949adc96d3a93cce~mv2.png/v1/fill/w_342,h_131,al_c,q_85,usm_0.66_1.00_0.01,enc_avif,quality_auto/295c7b_359a976db3a54df1949adc96d3a93cce~mv2.png",
                "C": "c) https://static.wixstatic.com/media/295c7b_cba5904adc1e4953be8104d14d97e22c~mv2.png/v1/fill/w_342,h_128,al_c,q_85,usm_0.66_1.00_0.01,enc_avif,quality_auto/295c7b_cba5904adc1e4953be8104d14d97e22c~mv2.png",
                "D": "d) https://static.wixstatic.com/media/295c7b_699278815a5344bc89fc729d3711c74b~mv2.png/v1/fill/w_344,h_128,al_c,q_85,usm_0.66_1.00_0.01,enc_avif,quality_auto/295c7b_699278815a5344bc89fc729d3711c74b~mv2.png",
                "E": "e) https://static.wixstatic.com/media/295c7b_9c62c8bce3cc4c11901241d966ea1efd~mv2.png/v1/fill/w_345,h_131,al_c,q_85,usm_0.66_1.00_0.01,enc_avif,quality_auto/295c7b_9c62c8bce3cc4c11901241d966ea1efd~mv2.png",
            },
            ques_resposta_correta=AlternativaEnum.A,
            ques_resolucao="O movimento circular uniforme descreve uma função cossenoidal suave que inicia no ponto máximo, desce até o mínimo e retorna ao máximo sem quinas.",
            ques_resolucao_imagem_url="",
        ),
        Questao(
            ques_cont_id=None,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.MEDIO,
            ques_enunciado=(
                "(Enem 2017) Em um teleférico turístico, bondinhos saem de estações ao nível do mar e do topo de uma montanha. A travessia dura 1,5 minuto "
                "e ambos os bondinhos se deslocam à mesma velocidade. Quarenta segundos após o bondinho A partir da estação ao nível do mar, ele cruza com o "
                "bondinho B, que havia saído do topo da montanha.\n"
                "Quantos segundos após a partida do bondinho B partiu o bondinho A?"
            ),
            ques_imagem_url="",
            ques_alternativas={"A": "a) 5", "B": "b) 10", "C": "c) 15", "D": "d) 20", "E": "e) 25"},
            ques_resposta_correta=AlternativaEnum.B,
            ques_resolucao=(
                "A travessia total leva 1,5 min = 90 s. Como as velocidades são iguais, o ponto de encontro divide o percurso em trechos percorridos em 40 s e 50 s. "
                "Logo, B já viajava há 50 s quando cruzou com A (que viajava há 40 s), tendo partido 50 - 40 = 10 segundos antes."
            ),
            ques_resolucao_imagem_url="",
        ),
        Questao(
            ques_cont_id=None,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.DIFICIL,
            ques_enunciado=(
                "(Enem 2013) O dono de um sítio pretende colocar uma haste de sustentação para melhor firmar dois postes de comprimentos iguais a 6 m e 4 m. "
                "A figura representa a situação real na qual os postes são descritos pelos segmentos AC e BD e a haste é representada pelo segmento EF, "
                "todos perpendiculares ao solo, que é indicado pelo segmento de reta AB. Os segmentos AD e BC representam cabos de aço que serão instalados.\n"
                "Qual deve ser o valor do comprimento da haste EF?"
            ),
            ques_imagem_url="https://cdn.sanity.io/images/bpg6rp2y/production/5785709cff5f9a90a992733167bd3bf894b32e06-654x253.png?w=1200&auto=format",
            ques_alternativas={"A": "a) 1 m", "B": "b) 2 m", "C": "c) 2,4 m", "D": "d) 3 m", "E": "e) 2√6 m"},
            ques_resposta_correta=AlternativaEnum.C,
            ques_resolucao=(
                "Por semelhança de triângulos (ADB ~ AEF e ACB ~ FEB), obtém-se 6x = h(x + y) e 4y = h(x + y), logo x = (2/3)y. "
                "Substituindo, a altura EF é h = (6 · 4) / (6 + 4) = 24 / 10 = 2,4 m."
            ),
            ques_resolucao_imagem_url="https://cdn.sanity.io/images/bpg6rp2y/production/5785709cff5f9a90a992733167bd3bf894b32e06-654x253.png?w=1200&auto=format",
        ),
        Questao(
            ques_cont_id=None,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.FACIL,
            ques_enunciado=(
                "Um adolescente, tendo em vista uma alimentação saudável, consome diariamente 7,5 dL de leite durante 1 mês (30 dias). "
                "Sabe-se que o preço de um litro de leite é R$ 1,98.\n"
                "Nessas condições, o custo mensal com o consumo de leite desse adolescente é de:"
            ),
            ques_imagem_url="",
            ques_alternativas={
                "A": "a) R$ 14,85",
                "B": "b) R$ 22,50",
                "C": "c) R$ 44,55",
                "D": "d) R$ 148,50",
                "E": "e) R$ 445,50",
            },
            ques_resposta_correta=AlternativaEnum.C,
            ques_resolucao="Convertendo: 7,5 dL = 0,75 L/dia. Em 30 dias: 0,75 · 30 = 22,5 L. Custo total: 22,5 · 1,98 = R$ 44,55.",
            ques_resolucao_imagem_url="",
        ),
        Questao(
            ques_cont_id=None,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.FACIL,
            ques_enunciado=(
                "(Enem 2020) Pesquisadores da Universidade de Tecnologia de Viena, na Áustria, produziram miniaturas de objetos em impressoras 3D de alta precisão. "
                "A escultura apresentada é uma miniatura de um carro de Fórmula 1, com 100 micrômetros de comprimento. Um micrômetro é a milionésima parte de um metro.\n"
                "Usando notação científica, qual é a representação do comprimento dessa miniatura, em metro?"
            ),
            ques_imagem_url="https://arquivos.qconcursos.com/images/provas/78987/f30713e636c32a1aa668.png",
            ques_alternativas={
                "A": "a) 1,0 × 10⁻²",
                "B": "b) 1,0 × 10⁻³",
                "C": "c) 1,0 × 10⁻⁴",
                "D": "d) 1,0 × 10⁻⁵",
                "E": "e) 1,0 × 10⁻⁶",
            },
            ques_resposta_correta=AlternativaEnum.C,
            ques_resolucao="Como 1 micrômetro = 10⁻⁶ m, temos 100 micrômetros = 100 · 10⁻⁶ m = 10² · 10⁻⁶ m = 1,0 · 10⁻⁴ m.",
            ques_resolucao_imagem_url="",
        ),
        Questao(
            ques_cont_id=None,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.MEDIO,
            ques_enunciado=(
                "De forma geral, são necessários 50 kg de bauxita para produzir 10 kg de alumínio. O Brasil fechou 2020 como um dos principais líderes "
                "mundiais em reciclagem de latas de alumínio, obtendo um índice de reciclagem de 97,4% de um total de 4,0 × 10⁵ toneladas de latas vendidas. "
                "Considere que a lata é constituída de alumínio puro.\n"
                "Levando em conta apenas a reciclagem de latas, qual é o valor mais próximo da massa de bauxita, em tonelada, que deixou de ser extraída da natureza em 2020 no Brasil?"
            ),
            ques_imagem_url="",
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
            ques_resolucao_imagem_url="",
        ),
        Questao(
            ques_cont_id=None,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.MEDIO,
            ques_enunciado=(
                "Ao calcular a média de suas notas em 4 provas, um estudante dividiu, por engano, a soma das notas por 5. Com isso, a média obtida foi "
                "1 unidade menor do que deveria ser, caso fosse calculada corretamente.\n"
                "O valor correto da média das notas desse estudante é:"
            ),
            ques_imagem_url="",
            ques_alternativas={"A": "a) 4", "B": "b) 5", "C": "c) 6", "D": "d) 19", "E": "e) 21"},
            ques_resposta_correta=AlternativaEnum.B,
            ques_resolucao="Seja S a soma das notas e M a média correta: S / 4 = M → S = 4M. Pelo erro: S / 5 = M - 1 → 4M = 5M - 5 → M = 5.",
            ques_resolucao_imagem_url="",
        ),
        Questao(
            ques_cont_id=None,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.FACIL,
            ques_enunciado=(
                "O gráfico apresenta o valor total de exportações e o valor total de importações, ao longo de um período, em bilhão de dólares. "
                "O saldo da balança comercial brasileira é dado pelo valor total de exportações menos o valor total de importações num mesmo período.\n"
                "Considere que os saldos nos três meses destacados sejam: S1 (junho de 2009), S2 (janeiro de 2010) e S3 (junho de 2010).\n"
                "A ordenação dos saldos S1, S2 e S3, do maior para o menor, é:"
            ),
            ques_imagem_url="https://qcon-assets-production.s3.amazonaws.com/images/provas/126089/Captura_de%20Tela%20%287088%29.png",
            ques_alternativas={
                "A": "a) S1, S3 e S2.",
                "B": "b) S2, S1 e S3.",
                "C": "c) S2, S3 e S1.",
                "D": "d) S3, S1 e S2.",
                "E": "e) S3, S2 e S1.",
            },
            ques_resposta_correta=AlternativaEnum.A,
            ques_resolucao="Pelo gráfico: S1 ≈ 14,5 - 10 = 4,5 bi; S2 < 0 (importações superaram exportações); S3 ≈ 17,1 - 14,8 = 2,3 bi. Logo, S1 > S3 > S2.",
            ques_resolucao_imagem_url="",
        ),
        Questao(
            ques_cont_id=None,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.FACIL,
            ques_enunciado=(
                "Pesquisas indicam que o número de bactérias X é duplicado a cada quarto de hora. Um aluno resolveu fazer uma observação para verificar "
                "a veracidade dessa afirmação. Ele usou uma população inicial de 10⁵ bactérias X e encerrou a observação ao final de uma hora.\n"
                "Após uma hora do início do período de observação desse aluno, o número de bactérias X foi de:"
            ),
            ques_imagem_url="",
            ques_alternativas={
                "A": "a) 2⁻² . 10⁵",
                "B": "b) 2⁻¹ . 10⁵",
                "C": "c) 2² . 10⁵",
                "D": "d) 2³ . 10⁵",
                "E": "e) 2⁴ . 10⁵",
            },
            ques_resposta_correta=AlternativaEnum.E,
            ques_resolucao="Em 1 hora há 4 quartos de hora (4 períodos de 15 minutos). Como a população dobra 4 vezes, o total final será 2⁴ · 10⁵.",
            ques_resolucao_imagem_url="",
        ),
        Questao(
            ques_cont_id=None,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.FACIL,
            ques_enunciado=(
                "Uma pessoa ampliou uma foto no computador e, ao imprimi-la, verificou que a qualidade não estava boa. Ao pesquisar, descobriu que "
                "um parâmetro que define a qualidade da imagem, ou resolução, pode ser considerado pela quantidade de pontos, chamados pixels, que há em "
                "cada quadradinho de 1 cm de lado contido na imagem.\n"
                "Considerando a pesquisa realizada, a unidade de medida do parâmetro de qualidade de uma imagem é expressa por:"
            ),
            ques_imagem_url="",
            ques_alternativas={
                "A": "a) cm² ⋅ pixel",
                "B": "b) cm ⋅ pixel",
                "C": "c) cm / (pixel)²",
                "D": "d) pixel / cm",
                "E": "e) pixel / cm²",
            },
            ques_resposta_correta=AlternativaEnum.E,
            ques_resolucao="Um quadrado de 1 cm de lado possui área igual a 1 cm². A razão entre a quantidade de pixels e a área é expressa em pixel / cm².",
            ques_resolucao_imagem_url="",
        ),
    ]
    db.add_all(questoes)
    db.commit()


SEEDS = {
    "Grandezas e Unidades de Medida": povoar_conteudo_1,
    "Razão, Proporção e Regra de Três": povoar_conteudo_2,
    "Teoria dos Conjuntos e Conjuntos Numéricos": povoar_conteudo_3,
    "Frações Decimais, Dízimas Periódicas e Intervalos Reais": povoar_conteudo_4,
    "Geometria Plana (Teorema de Tales, Semelhança e Relações Métricas)": povoar_conteudo_5,
    "Trigonometria no Triângulo Retângulo": povoar_conteudo_6,
    "Funções e Função Afim (Função do 1º Grau)": povoar_conteudo_7,
    "Função Quadrática, Exponencial e Logarítmica": povoar_conteudo_8,
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
