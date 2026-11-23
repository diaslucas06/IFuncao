from sqlalchemy.orm import Session
from models import Conteudo, Questao, EtapaEnum, DificuldadeEnum, AlternativaEnum
from contextlib import contextmanager

from dependencies import pegar_sessao

sessao_seed = contextmanager(pegar_sessao)

def povoar_conteudo_1(session, base_url="https://seu-storage-publico.com"):
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
        cont_imagem_url=f"{base_url}/imagens/conteudos/gm_escala_conversao_metros.png",
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
            ques_imagem_url=None,
            ques_alternativas={"A": "a) 2,4 km e 2 h", "B": "b) 4,2 km e 0,2 h", "C": "c) 0,24 km e 0,2 h", "D": "d) 4,2 km e 2 h", "E": "e) 2,4 km e 0,2 h"},
            ques_resposta_correta=AlternativaEnum.E,
            ques_resolucao="Dividindo 2400 m por 1000, obtemos 2,4 km. Dividindo 12 min por 60, obtemos 0,2 h.",
            ques_resolucao_imagem_url=None,
        ),
        Questao(
            ques_cont_id=conteudo1.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.FACIL,
            ques_enunciado="Um aluno de Ensino Médio vai até o açougue, a pedido de seus pais, comprar 5 kg de carne para um churrasco em sua casa. Além da carne, ele compra 8 litros de refrigerante para oferecer aos convidados. Qual das alternativas a seguir possui os valores da quantidade de carne e de refrigerante, respectivamente, nas unidades tonelada (t) e mililitro (mL)?",
            ques_imagem_url=None,
            ques_alternativas={
                "A": "a) 0,005 t e 0,008 mL",
                "B": "b) 5000 t e 0,008 mL",
                "C": "c) 0,005 t e 8000 mL",
                "D": "d) 5000 t e 8000 mL",
                "E": "e) 0,005 t e 0,8 mL",
            },
            ques_resposta_correta=AlternativaEnum.C,
            ques_resolucao="Como 1 t = 1000 kg, 5 kg = 5 / 1000 = 0,005 t. Como 1 L = 1000 mL, 8 L = 8 · 1000 = 8000 mL.",
            ques_resolucao_imagem_url=None,
        ),
        Questao(
            ques_cont_id=conteudo1.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.FACIL,
            ques_enunciado="A distância em linha reta entre as cidades de São Paulo e Rio de Janeiro é de, aproximadamente, 357,37 km (quilômetros). Esta mesma distância em metros é igual a:",
            ques_imagem_url=None,
            ques_alternativas={"A": "a) 35,737 m", "B": "b) 3.573,7 m", "C": "c) 35.737 m", "D": "d) 357.370 m", "E": "e) 3.573.700 m"},
            ques_resposta_correta=AlternativaEnum.D,
            ques_resolucao="Como 1 km = 1000 m, multiplicamos 357,37 por 1000, obtendo 357.370 m.",
            ques_resolucao_imagem_url=None,
        ),
        Questao(
            ques_cont_id=conteudo1.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.FACIL,
            ques_enunciado="A carga elétrica fundamental de um elétron, após diversos experimentos, foi determinada para um valor fundamental estimado em 0,00000000000000000016 C. Seu valor, corretamente expresso em notação científica, fica:",
            ques_imagem_url=None,
            ques_alternativas={"A": "a) 16 x 10⁻¹⁸ C", "B": "b) 1,6 x 10⁻¹⁹ C", "C": "c) 160 x 10⁻¹⁷ C", "D": "d) 0,16 x 10⁻²⁰ C"},
            ques_resposta_correta=AlternativaEnum.B,
            ques_resolucao="Deslocando a vírgula 19 casas para a direita até obter um algarismo significativo antes da vírgula, temos 1,6 · 10⁻¹⁹ C.",
            ques_resolucao_imagem_url=f"{base_url}/imagens/respostas/gm_r04_notacao_eletron.png",
        ),
        Questao(
            ques_cont_id=conteudo1.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.FACIL,
            ques_enunciado="Nas escolas, é comum dividir o tempo de estudo em aulas de 50 min (minutos). Se um estudante assiste 6 aulas por dia e estuda 5 dias em uma semana, o número de horas que ele estará em sala de aula será de:",
            ques_imagem_url=None,
            ques_alternativas={"A": "a) 15 h", "B": "b) 20 h", "C": "c) 25 h", "D": "d) 30 h", "E": "e) 35 h"},
            ques_resposta_correta=AlternativaEnum.C,
            ques_resolucao="Total de aulas: 6 · 5 = 30 aulas. Tempo em minutos: 30 · 50 = 1500 min. Convertendo em horas: 1500 / 60 = 25 h.",
            ques_resolucao_imagem_url=f"{base_url}/imagens/respostas/gm_r05_horas_aula.png",
        ),
        Questao(
            ques_cont_id=conteudo1.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.MEDIO,
            ques_enunciado="Uma herança de R$ 3.000.000 será dividida de forma diretamente proporcional entre as idades dos três herdeiros. Sabendo que eles possuem 24, 28 e 44 anos, o herdeiro de maior idade receberá um total de:",
            ques_imagem_url=None,
            ques_alternativas={"A": "A) R$ 950.000", "B": "B) R$ 975.000", "C": "C) R$ 1.225.000", "D": "D) R$ 1.375.000", "E": "E) R$ 1.625.000"},
            ques_resposta_correta=AlternativaEnum.D,
            ques_resolucao="A soma das idades é 24 + 28 + 44 = 96. Pela proporção 96 / 3.000.000 = 44 / x, temos x = (44 · 3.000.000) / 96 = R$ 1.375.000.",
            ques_resolucao_imagem_url=f"{base_url}/imagens/respostas/gm_r06_divisao_heranca.png",
        ),
        Questao(
            ques_cont_id=conteudo1.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.FACIL,
            ques_enunciado="(OMNI) Grandeza é tudo aquilo que pode ser medido ou calculado, porém quando analisamos duas grandezas proporcionais, elas podem ser diretamente proporcionais ou inversamente proporcionais. Sabendo disso, analise as alternativas abaixo e marque a opção CORRETA.",
            ques_imagem_url=None,
            ques_alternativas={
                "A": "A) Distância e tempo são grandezas inversamente proporcionais, pois quanto maior a distância que precisa ser percorrida, menos tempo será gasto no percurso.",
                "B": "B) Velocidade e quantidade de alimento comprado por uma família são grandezas diretamente proporcionais.",
                "C": "C) Em um churrasco, a quantidade de carne e a quantidade de pessoas são grandezas diretamente proporcionais.",
                "D": "D) Velocidade e tempo são grandezas diretamente proporcionais, pois quanto maior a velocidade, menor o tempo gasto em um percurso.",
            },
            ques_resposta_correta=AlternativaEnum.C,
            ques_resolucao="Quanto maior a quantidade de pessoas em um churrasco, maior deve ser a quantidade de carne na mesma proporção, caracterizando grandezas diretamente proporcionais.",
            ques_resolucao_imagem_url=None,
        ),
        Questao(
            ques_cont_id=conteudo1.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.FACIL,
            ques_enunciado="Das situações abaixo, marque aquela que descreve duas grandezas inversamente proporcionais:",
            ques_imagem_url=None,
            ques_alternativas={
                "A": "A) Quantidade de pessoas em um churrasco e a quantidade de carne necessária.",
                "B": "B) Número de habitantes em uma cidade e a taxa de mortalidade.",
                "C": "C) Velocidade de um automóvel e a distância percorrida em um mesmo intervalo de tempo.",
                "D": "D) Comprimento da altura e a área de um polígono.",
                "E": "E) Vazão de um ralo e o tempo necessário para esvaziar um reservatório.",
            },
            ques_resposta_correta=AlternativaEnum.E,
            ques_resolucao="Quanto maior a vazão de água pelo ralo, menor será o tempo necessário para esvaziar o reservatório, tratando-se de grandezas inversamente proporcionais.",
            ques_resolucao_imagem_url=None,
        ),
        Questao(
            ques_cont_id=conteudo1.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.DIFICIL,
            ques_enunciado="Um triângulo possui ângulos internos inversamente proporcionais aos números 1, 3 e 6, então, o valor do seu maior ângulo é:",
            ques_imagem_url=None,
            ques_alternativas={"A": "A) 30°", "B": "B) 60°", "C": "C) 90°", "D": "D) 120°", "E": "E) 150°"},
            ques_resposta_correta=AlternativaEnum.D,
            ques_resolucao="Sendo a = k/1, b = k/3 e c = k/6, e sabendo que a + b + c = 180°, temos k + k/3 + k/6 = 180° → 9k/6 = 180° → k = 120°. Logo, o maior ângulo mede 120°.",
            ques_resolucao_imagem_url=f"{base_url}/imagens/respostas/gm_r09_angulos_triangulo.png",
        ),
        Questao(
            ques_cont_id=conteudo1.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.FACIL,
            ques_enunciado="Para fazer uma viagem da cidade A para a cidade B, um automóvel gasta cerca de 4 horas, a uma velocidade média de 75 km/h. Caso fosse necessário que essa viagem fosse feita em 3 horas, a velocidade média seria de:",
            ques_imagem_url=None,
            ques_alternativas={"A": "A) 86 km/h", "B": "B) 90 km/h", "C": "C) 95 km/h", "D": "D) 100 km/h", "E": "E) 110 km/h"},
            ques_resposta_correta=AlternativaEnum.D,
            ques_resolucao="Velocidade e tempo são inversamente proporcionais: 3x = 4 · 75 → 3x = 300 → x = 100 km/h.",
            ques_resolucao_imagem_url=None,
        ),
    ]
    session.add_all(questoes)
    session.commit()

# CONTEÚDO 4 (Funções e Função Afim - Função do 1º Grau)
def povoar_conteudo_2(session, base_url="https://seu-storage-publico.com"):
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
        cont_imagem_url=f"{base_url}/imagens/conteudos/rp_propriedades_proporcao.png",
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
            ques_imagem_url=None,
            ques_alternativas={"A": "a) 4", "B": "b) 6", "C": "c) 8", "D": "d) 12"},
            ques_resposta_correta=AlternativaEnum.C,
            ques_resolucao="Dividindo o número de candidatos pelas vagas: 1600 / 200 = 8 candidatos por vaga.",
            ques_resolucao_imagem_url=f"{base_url}/imagens/respostas/rp_r01_razao_vagas.png",
        ),
        Questao(
            ques_cont_id=conteudo2.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.MEDIO,
            ques_enunciado="Em uma seleção, a razão entre o número de homens e mulheres candidatos a vaga é 4/7. Sabendo que 32 candidatos são do sexo masculino, o número total de participantes na seleção é:",
            ques_imagem_url=None,
            ques_alternativas={"A": "a) 56", "B": "b) 72", "C": "c) 88", "D": "d) 94"},
            ques_resposta_correta=AlternativaEnum.C,
            ques_resolucao="Pela proporção 4 / 7 = 32 / x, temos x = 56 mulheres. Total de participantes: 32 + 56 = 88.",
            ques_resolucao_imagem_url=f"{base_url}/imagens/respostas/rp_r02_proporcao_selecao.png",
        ),
        Questao(
            ques_cont_id=conteudo2.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.MEDIO,
            ques_enunciado="(UEPB/2014) A razão entre o peso de uma pessoa na Terra e o seu peso em Netuno é 5/7. Dessa forma, o peso de uma pessoa que na terra pesa 60 kg, em Netuno, está no intervalo:",
            ques_imagem_url=None,
            ques_alternativas={"A": "a) [40 kg; 45 kg]", "B": "b) [45 kg; 50 kg]", "C": "c) [55 kg; 60 kg]", "D": "d) [75 kg; 80 kg]", "E": "e) [80 kg; 85 kg]"},
            ques_resposta_correta=AlternativaEnum.E,
            ques_resolucao="Pela proporção 5 / 7 = 60 / x, temos 5x = 420 → x = 84 kg, pertencente ao intervalo [80 kg; 85 kg].",
            ques_resolucao_imagem_url=f"{base_url}/imagens/respostas/rp_r03_peso_netuno.png",
        ),
        Questao(
            ques_cont_id=conteudo2.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.FACIL,
            ques_enunciado="Sabendo que x e 6 são diretamente proporcionais aos números 6 e 18, então podemos afirmar que x vale:",
            ques_imagem_url=None,
            ques_alternativas={"A": "A) 1", "B": "B) 2", "C": "C) 3", "D": "D) 4", "E": "E) 5"},
            ques_resposta_correta=AlternativaEnum.B,
            ques_resolucao="Pela igualdade x / 6 = 6 / 18 → 18x = 36 → x = 2.",
            ques_resolucao_imagem_url=None,
        ),
        Questao(
            ques_cont_id=conteudo2.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.FACIL,
            ques_enunciado="Dados recentes mostram que 1 a cada 4 brasileiros já foi contaminado por covid-19. Se essa proporção for aplicada a um bairro de 13116 habitantes, então a quantidade de pessoas que já teve covid nesse bairro é igual a:",
            ques_imagem_url=None,
            ques_alternativas={"A": "A) 3279", "B": "B) 3490", "C": "C) 3521", "D": "D) 3674", "E": "E) 4001"},
            ques_resposta_correta=AlternativaEnum.A,
            ques_resolucao="Calculando 1/4 de 13116: 13116 / 4 = 3279 pessoas.",
            ques_resolucao_imagem_url=None,
        ),
        Questao(
            ques_cont_id=conteudo2.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.DIFICIL,
            ques_enunciado="(Vunesp) Dez funcionários de uma repartição trabalham 8 horas por dia, durante 27 dias, para atender certo número de pessoas. Se um funcionário doente foi afastado por tempo indeterminado e outro se aposentou, o total de dias que os funcionários restantes levarão para atender o mesmo número de pessoas, trabalhando uma hora a mais por dia, no mesmo ritmo de trabalho, será:",
            ques_imagem_url=None,
            ques_alternativas={"A": "a) 29", "B": "b) 30", "C": "c) 33", "D": "d) 28", "E": "e) 31"},
            ques_resposta_correta=AlternativaEnum.B,
            ques_resolucao="Restam 8 funcionários trabalhando 9 h/dia. Como funcionários e horas são inversamente proporcionais aos dias: 27 / x = (8 / 10) · (9 / 8) → x = 30 dias.",
            ques_resolucao_imagem_url=f"{base_url}/imagens/respostas/rp_r06_setas_regra_tres.png",
        ),
        Questao(
            ques_cont_id=conteudo2.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.MEDIO,
            ques_enunciado="Bruno gostaria de comprar um vídeo game, que a vista estava com 30% de desconto e, por isso, diminuía R$ 60,00 do valor da compra. A outra forma de pagamento oferecida pela loja era comprar no cartão em uma única parcela com 12% de desconto. Se Bruno escolheu pagar o vídeo game com o cartão, qual o valor em reais do desconto concedido?",
            ques_imagem_url=None,
            ques_alternativas={"A": "a) R$ 24,00", "B": "b) R$ 18,00", "C": "c) R$ 22,00", "D": "d) R$ 14,00"},
            ques_resposta_correta=AlternativaEnum.A,
            ques_resolucao="Pela regra de três direta: 30 / 12 = 60 / x → 30x = 720 → x = R$ 24,00.",
            ques_resolucao_imagem_url=f"{base_url}/imagens/respostas/rp_r07_proporcao_desconto.png",
        ),
        Questao(
            ques_cont_id=conteudo2.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.MEDIO,
            ques_enunciado="Os agentes comunitários de saúde são profissionais que, entre as suas funções, estão empenhados no combate a uma das doenças mais frequentes no Brasil: a dengue. Para isso, os agentes vão de casa em casa para identificar focos de desenvolvimento do mosquito Aedes aegypti e orientar os moradores. Sabendo que 12 profissionais necessitam de 28 dias para visitar todas as casas de 3 bairros de uma cidade, em quanto tempo um quarto da equipe consegue visitar as mesmas casas?",
            ques_imagem_url=None,
            ques_alternativas={"A": "a) 90", "B": "b) 98", "C": "c) 120", "D": "d) 112"},
            ques_resposta_correta=AlternativaEnum.D,
            ques_resolucao="Um quarto da equipe equivale a 3 agentes. Como agentes e dias são inversamente proporcionais: 28 / x = 3 / 12 → 3x = 336 → x = 112 dias.",
            ques_resolucao_imagem_url=f"{base_url}/imagens/respostas/rp_r08_agentes_saude.png",
        ),
        Questao(
            ques_cont_id=conteudo2.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.DIFICIL,
            ques_enunciado="Em uma obra, 10 homens concluíram um dos trabalhos em 6 dias, fazendo 8 horas diárias. Se apenas 5 homens estiverem trabalhando, quantos dias levarão para o mesmo trabalho ser concluído com execução de 6 horas por dia?",
            ques_imagem_url=None,
            ques_alternativas={"A": "a) 12 dias", "B": "b) 14 dias", "C": "c) 16 dias", "D": "d) 18 dias"},
            ques_resposta_correta=AlternativaEnum.C,
            ques_resolucao="Homens e horas por dia são inversamente proporcionais aos dias: 6 / x = (5 / 10) · (6 / 8) → 6 / x = 30 / 80 → x = 16 dias.",
            ques_resolucao_imagem_url=f"{base_url}/imagens/respostas/rp_r09_regra_tres_obra.png",
        ),
        Questao(
            ques_cont_id=conteudo2.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.MEDIO,
            ques_enunciado="Maria está interessada em comprar livros para a sua biblioteca pessoal. Ela percebeu que em uma livraria, os livros do mesmo autor têm um desconto progressivo, conforme a quantidade comprada. Na tabela está faltando o percentual de desconto para 3 ou mais livros. Sabe-se que a variação do desconto é proporcional ao número de livros. Se Maria comprasse 4 livros do mesmo autor pelo mesmo valor de R$ 150,00 cada, qual seria o valor total com o desconto aplicado?",
            ques_imagem_url=f"{base_url}/imagens/questoes/rp_q10_tabela_desconto.png",
            ques_alternativas={"A": "a) R$ 45,00", "B": "b) R$ 54,00", "C": "c) R$ 58,00", "D": "d) R$ 64,00"},
            ques_resposta_correta=AlternativaEnum.B,
            ques_resolucao="Pela proporção 2 / 3 = 6 / x → x = 9% de desconto. Para 4 livros de R$ 150,00 (R$ 600,00), 9% corresponde a R$ 54,00.",
            ques_resolucao_imagem_url=f"{base_url}/imagens/respostas/rp_r10_calculo_desconto.png",
        ),
    ]
    session.add_all(questoes)
    session.commit()

# CONTEÚDO 5 (Função Quadrática, Exponencial e Logarítmica)
def povoar_conteudo_3(session, base_url="https://seu-storage-publico.com"):
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
        cont_imagem_url=f"{base_url}/imagens/conteudos/conj_diagrama_euler_venn.png",
        cont_relacionados={"topicos": ["Conjuntos", "Diagramas de Venn", "Conjuntos Numéricos"]},
    )
    session.add(conteudo3)
    session.flush()

    questoes = [
        Questao(
            ques_cont_id=conteudo3.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.MEDIO,
            ques_enunciado="Em um diagrama de Venn com três conjuntos A, B e C, a região que reúne os elementos pertencentes simultaneamente a A e B, mas que não pertencem a C, é representada por:",
            ques_imagem_url=f"{base_url}/imagens/questoes/conj_q01_diagrama_azul.png",
            ques_alternativas={"A": "a) A - B - C", "B": "b) (A ∪ B) - C", "C": "c) (A ∩ B) - C", "D": "d) (A ∩ C) - B", "E": "e) A ∩ B ∩ C"},
            ques_resposta_correta=AlternativaEnum.C,
            ques_resolucao="Os elementos comuns a A e B formam a intersecção (A ∩ B). Excluindo-se os elementos de C, obtemos (A ∩ B) - C.",
            ques_resolucao_imagem_url=None,
        ),
        Questao(
            ques_cont_id=conteudo3.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.MEDIO,
            ques_enunciado="Qual expressão representa o conjunto dos elementos que pertencem exclusivamente ao conjunto A, desconsiderando qualquer elemento de B ou C?",
            ques_imagem_url=f"{base_url}/imagens/questoes/conj_q02_area_hachurada.png",
            ques_alternativas={"A": "a) A ∩ (B ∪ C)", "B": "b) A - (B ∪ C)", "C": "c) A ∪ (B - C)", "D": "d) A ∩ (B - C)"},
            ques_resposta_correta=AlternativaEnum.B,
            ques_resolucao="Para obter os elementos exclusivos de A, retira-se de A toda a união dos demais conjuntos: A - (B ∪ C).",
            ques_resolucao_imagem_url=None,
        ),
        Questao(
            ques_cont_id=conteudo3.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.MEDIO,
            ques_enunciado="Em uma pesquisa com 180 estudantes sobre cursos de idiomas, 40 afirmaram não estudar nenhum idioma, 95 estudam inglês e 30 estudam inglês e espanhol. Quantos estudantes cursam exclusivamente espanhol?",
            ques_imagem_url=None,
            ques_alternativas={"A": "a) 35", "B": "b) 45", "C": "c) 55", "D": "d) 65"},
            ques_resposta_correta=AlternativaEnum.B,
            ques_resolucao="Dos 180 estudantes, 180 - 40 = 140 estudam ao menos um idioma. Subtraindo os 95 que estudam inglês, restam 140 - 95 = 45 que estudam apenas espanhol.",
            ques_resolucao_imagem_url=None,
        ),
        Questao(
            ques_cont_id=conteudo3.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.FACIL,
            ques_enunciado="Em uma turma de 40 alunos, todos praticam futebol ou vôlei. Sabendo que 25 jogam futebol e 22 jogam vôlei, quantos alunos praticam apenas futebol?",
            ques_imagem_url=None,
            ques_alternativas={"A": "a) 7", "B": "b) 15", "C": "c) 18", "D": "d) 22", "E": "e) 25"},
            ques_resposta_correta=AlternativaEnum.C,
            ques_resolucao="A intersecção é 25 + 22 - 40 = 7 alunos que praticam ambos. Assim, apenas futebol: 25 - 7 = 18 alunos.",
            ques_resolucao_imagem_url=None,
        ),
        Questao(
            ques_cont_id=conteudo3.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.MEDIO,
            ques_enunciado="Sejam P o conjunto dos múltiplos naturais de 6, Q o conjunto dos múltiplos naturais de 3 e R o conjunto dos números naturais ímpares. Analise as afirmações: I. P ⊂ Q; II. Q ⊂ P; III. P ∩ R = ∅. Estão corretas:",
            ques_imagem_url=None,
            ques_alternativas={"A": "a) Apenas I e II", "B": "b) Apenas II e III", "C": "c) Apenas I e III", "D": "d) Apenas I", "E": "e) Todas"},
            ques_resposta_correta=AlternativaEnum.C,
            ques_resolucao="Todo múltiplo de 6 é múltiplo de 3 (I é verdadeira) e também é par, não possuindo elementos em comum com os ímpares (III é verdadeira). A II é falsa, pois 3 ∈ Q e 3 ∉ P.",
            ques_resolucao_imagem_url=None,
        ),
        Questao(
            ques_cont_id=conteudo3.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.FACIL,
            ques_enunciado="A respeito dos conjuntos numéricos, assinale a alternativa verdadeira:",
            ques_imagem_url=None,
            ques_alternativas={
                "A": "a) Todo número real é racional.",
                "B": "b) A intersecção entre Q e I possui infinitos elementos.",
                "C": "c) A dízima periódica 2,454545... pertence ao conjunto dos números racionais.",
                "D": "d) Todo número inteiro pertence ao conjunto dos números naturais.",
            },
            ques_resposta_correta=AlternativaEnum.C,
            ques_resolucao="Toda dízima periódica pode ser escrita como fração geratriz de números inteiros, pertencendo ao conjunto Q.",
            ques_resolucao_imagem_url=None,
        ),
        Questao(
            ques_cont_id=conteudo3.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.FACIL,
            ques_enunciado="Qual notação indica corretamente uma relação de inclusão entre dois conjuntos A e B?",
            ques_imagem_url=f"{base_url}/imagens/questoes/conj_q07_quadro_inclusao.png",
            ques_alternativas={"A": "a) A ⊂ B", "B": "b) A ∈ B", "C": "c) A ∉ B", "D": "d) x ⊂ B"},
            ques_resposta_correta=AlternativaEnum.A,
            ques_resolucao="Os símbolos de inclusão (⊂, ⊃) são empregados exclusivamente para relacionar conjuntos entre si.",
            ques_resolucao_imagem_url=None,
        ),
        Questao(
            ques_cont_id=conteudo3.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.MEDIO,
            ques_enunciado="Dados A = {1, 3, 5}, B = {3, 5, 7} e C = {7, 9}, qual é o conjunto resultante da operação (A ∪ B) ∩ (B ∪ C)?",
            ques_imagem_url=None,
            ques_alternativas={"A": "a) {3, 5, 7}", "B": "b) {1, 3, 5}", "C": "c) {7, 9}", "D": "d) {1, 3, 5, 7, 9}", "E": "e) {3, 7}"},
            ques_resposta_correta=AlternativaEnum.A,
            ques_resolucao="Temos A ∪ B = {1, 3, 5, 7} e B ∪ C = {3, 5, 7, 9}. Os elementos comuns a ambos são {3, 5, 7}.",
            ques_resolucao_imagem_url=None,
        ),
        Questao(
            ques_cont_id=conteudo3.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.MEDIO,
            ques_enunciado="Em um clube, 150 sócios praticam natação ou corrida. Sabe-se que 90 praticam natação e 85 praticam corrida. Quantos sócios praticam as duas modalidades?",
            ques_imagem_url=None,
            ques_alternativas={"A": "a) 15", "B": "b) 20", "C": "c) 25", "D": "d) 30", "E": "e) 35"},
            ques_resposta_correta=AlternativaEnum.C,
            ques_resolucao="Pelo princípio da inclusão-exclusão: n(A ∩ B) = 90 + 85 - 150 = 25 sócios.",
            ques_resolucao_imagem_url=None,
        ),
        Questao(
            ques_cont_id=conteudo3.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.FACIL,
            ques_enunciado="Julgue as afirmativas: I. A soma de dois números inteiros é sempre um número inteiro; II. A diferença entre dois números naturais é sempre um número natural; III. O produto de dois números racionais é sempre racional; IV. A união Q ∪ I resulta em R. É falsa apenas:",
            ques_imagem_url=None,
            ques_alternativas={"A": "a) I", "B": "b) II", "C": "c) III", "D": "d) IV", "E": "e) Nenhuma"},
            ques_resposta_correta=AlternativaEnum.B,
            ques_resolucao="A afirmativa II é falsa, pois a subtração de dois naturais pode resultar em um inteiro negativo (ex.: 3 - 5 = -2 ∉ N).",
            ques_resolucao_imagem_url=None,
        ),
    ]
    session.add_all(questoes)
    session.commit()

# CONTEÚDO 6 (Geometria Plana - Teorema de Tales, Semelhança e Relações Métricas)
def povoar_conteudo_4(session, base_url="https://seu-storage-publico.com"):
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
        cont_imagem_url=f"{base_url}/imagens/conteudos/fi_intervalos_reta_real.png",
        cont_relacionados={"topicos": ["Conjuntos Numéricos", "Números Racionais e Irracionais", "Fração Geratriz", "Intervalos Reais"]},
    )
    session.add(conteudo4)
    session.flush()

    questoes = [
        Questao(
            ques_cont_id=conteudo4.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.MEDIO,
            ques_enunciado="Qual é a fração irredutível geratriz da dízima periódica composta 2,1545454...?",
            ques_imagem_url=f"{base_url}/imagens/questoes/fi_q01_dizima_composta.png",
            ques_alternativas={"A": "a) 2154/990", "B": "b) 2133/990", "C": "c) 237/100", "D": "d) 237/110"},
            ques_resposta_correta=AlternativaEnum.D,
            ques_resolucao="Aplicando a regra da dízima composta: (2154 - 21) / 990 = 2133 / 990. Dividindo numerador e denominador por 9, obtemos 237 / 110.",
            ques_resolucao_imagem_url=f"{base_url}/imagens/respostas/fi_r01_formula_geratriz.png",
        ),
        Questao(
            ques_cont_id=conteudo4.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.MEDIO,
            ques_enunciado=(
                "Analise as afirmativas sobre números decimais:\n"
                "I. Uma fração irredutível gera um decimal exato apenas quando seu denominador possui exclusivamente os fatores primos 2 e/ou 5.\n"
                "II. O número 0,2020020002... é uma dízima periódica simples.\n"
                "III. A fração geratriz de 0,555... é 5/9.\n"
                "IV. Toda dízima periódica é um número racional.\n"
                "São verdadeiras:"
            ),
            ques_imagem_url=None,
            ques_alternativas={"A": "a) I, II e III", "B": "b) I, II e IV", "C": "c) II, III e IV", "D": "d) I, III e IV"},
            ques_resposta_correta=AlternativaEnum.D,
            ques_resolucao="Apenas a II é falsa, pois 0,2020020002... não possui período fixo repetitivo, sendo um número irracional.",
            ques_resolucao_imagem_url=f"{base_url}/imagens/respostas/fi_r02_geratriz_sete_nonos.png",
        ),
        Questao(
            ques_cont_id=conteudo4.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.FACIL,
            ques_enunciado="O resultado da adição 0,343434... + 0,767676... corresponde a:",
            ques_imagem_url=f"{base_url}/imagens/questoes/fi_q03_soma_dizimas.png",
            ques_alternativas={"A": "a) 1", "B": "b) 1,0101...", "C": "c) 1,1111...", "D": "d) 1,1010..."},
            ques_resposta_correta=AlternativaEnum.C,
            ques_resolucao="Somando as frações geratrizes: 34/99 + 76/99 = 110/99 = 10/9 = 1,1111...",
            ques_resolucao_imagem_url=f"{base_url}/imagens/respostas/fi_r03_soma_fracoes.png",
        ),
        Questao(
            ques_cont_id=conteudo4.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.MEDIO,
            ques_enunciado="A soma 1,6666... + 0,16666... é igual a:",
            ques_imagem_url=None,
            ques_alternativas={"A": "a) 5/3", "B": "b) 2", "C": "c) 7/6", "D": "d) 9/5", "E": "e) 11/6"},
            ques_resposta_correta=AlternativaEnum.E,
            ques_resolucao="Convertendo em frações: 1,6666... = 5/3 e 0,16666... = 1/6. Somando: 5/3 + 1/6 = 10/6 + 1/6 = 11/6.",
            ques_resolucao_imagem_url=f"{base_url}/imagens/respostas/fi_r04_soma_puc.png",
        ),
        Questao(
            ques_cont_id=conteudo4.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.FACIL,
            ques_enunciado="Seja y = 1,245245... A diferença entre o numerador e o denominador da sua fração geratriz (antes de simplificações) é:",
            ques_imagem_url=None,
            ques_alternativas={"A": "a) 245", "B": "b) 999", "C": "c) 1244", "D": "d) 754", "E": "e) 1245"},
            ques_resposta_correta=AlternativaEnum.A,
            ques_resolucao="Temos y = 1 + 245/999 = 1244/999. Subtraindo denominador de numerador: 1244 - 999 = 245.",
            ques_resolucao_imagem_url=f"{base_url}/imagens/respostas/fi_r05_fracao_1122_999.png",
        ),
        Questao(
            ques_cont_id=conteudo4.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.FACIL,
            ques_enunciado="Observe os números: I. 5/6; II. 0,3777...; III. √3; IV. 3/4. Geram dízimas periódicas apenas:",
            ques_imagem_url=f"{base_url}/imagens/questoes/fi_q06_numeros_reais.png",
            ques_alternativas={"A": "a) II e III", "B": "b) I e II", "C": "c) III e IV", "D": "d) I, II e III", "E": "e) II, III e IV"},
            ques_resposta_correta=AlternativaEnum.B,
            ques_resolucao="5/6 = 0,8333... e 0,3777... são dízimas periódicas. √3 é irracional e 3/4 = 0,75 é decimal exato.",
            ques_resolucao_imagem_url=None,
        ),
        Questao(
            ques_cont_id=conteudo4.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.MEDIO,
            ques_enunciado="Simplificando a expressão (0,666... + 1,5) ÷ (13/6), obtém-se:",
            ques_imagem_url=f"{base_url}/imagens/questoes/fi_q07_expressao_fracionaria.png",
            ques_alternativas={"A": "a) 0", "B": "b) 1", "C": "c) 2/3", "D": "d) 3/2", "E": "e) 13/6"},
            ques_resposta_correta=AlternativaEnum.B,
            ques_resolucao="Substituindo 0,666... = 2/3 e 1,5 = 3/2, temos (2/3 + 3/2) = 13/6. Dividindo 13/6 por 13/6, o resultado é 1.",
            ques_resolucao_imagem_url=f"{base_url}/imagens/respostas/fi_r07_simplificacao_niteroi.png",
        ),
        Questao(
            ques_cont_id=conteudo4.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.FACIL,
            ques_enunciado="A fração geratriz da dízima periódica 12,4444... é:",
            ques_imagem_url=None,
            ques_alternativas={"A": "a) 124/9", "B": "b) 124/90", "C": "c) 112/9", "D": "d) 112/99", "E": "e) 12/4"},
            ques_resposta_correta=AlternativaEnum.C,
            ques_resolucao="Somando parte inteira e parte periódica: 12 + 4/9 = (108 + 4) / 9 = 112/9.",
            ques_resolucao_imagem_url=f"{base_url}/imagens/respostas/fi_r08_geratriz_137_9.png",
        ),
        Questao(
            ques_cont_id=conteudo4.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.FACIL,
            ques_enunciado="A fração geratriz da dízima periódica 2,7777... é:",
            ques_imagem_url=None,
            ques_alternativas={"A": "a) 27/9", "B": "b) 23/9", "C": "c) 19/9", "D": "d) 25/9", "E": "e) 21/9"},
            ques_resposta_correta=AlternativaEnum.D,
            ques_resolucao="Pelo método prático: 2 + 7/9 = (18 + 7) / 9 = 25/9.",
            ques_resolucao_imagem_url=f"{base_url}/imagens/respostas/fi_r09_metodos_geratriz.png",
        ),
        Questao(
            ques_cont_id=conteudo4.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.MEDIO,
            ques_enunciado=(
                "Dados os intervalos reais A = [-4, 18], B = [1, 10] e C = [-2, 15], analise os itens:\n"
                "I. A contém B e B contém C.\n"
                "II. C está contido em A, mas não está contido em B.\n"
                "III. B está contido em C e também está contido em A.\n"
                "Estão corretos:"
            ),
            ques_imagem_url=None,
            ques_alternativas={"A": "a) Apenas I", "B": "b) Apenas III", "C": "c) Apenas I e II", "D": "d) Apenas I e III", "E": "e) Apenas II e III"},
            ques_resposta_correta=AlternativaEnum.E,
            ques_resolucao="Na reta real, observa-se a relação de inclusão B ⊂ C ⊂ A. Logo, B não contém C (I falsa), enquanto II e III são verdadeiras.",
            ques_resolucao_imagem_url=f"{base_url}/imagens/respostas/fi_r10_reta_intervalos.png",
        ),
    ]
    session.add_all(questoes)
    session.commit()

# CONTEÚDO 7 (Frações Decimais, Dízimas Periódicas e Intervalos Reais)
def povoar_conteudo_5(session, base_url="https://seu-storage-publico.com"):
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
        cont_imagem_url=f"{base_url}/imagens/conteudos/gp1_teorema_tales_relacoes_metricas.png",
        cont_relacionados={"topicos": ["Teorema de Tales", "Semelhança de Triângulos", "Teorema de Pitágoras", "Trigonometria no Triângulo Retângulo"]},
    )
    session.add(conteudo5)
    session.flush()

    questoes = [
        Questao(
            ques_cont_id=conteudo5.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.MEDIO,
            ques_enunciado="Em um triângulo ABC, a bissetriz interna AD divide o lado BC em dois segmentos de medidas 8 cm e 12 cm. Sabendo que o lado AB mede 10 cm, qual é a medida do lado AC?",
            ques_imagem_url=f"{base_url}/imagens/questoes/gp1_q01_triangulo_bissetriz.png",
            ques_alternativas={"A": "a) 13 cm", "B": "b) 14 cm", "C": "c) 15 cm", "D": "d) 16 cm", "E": "e) 18 cm"},
            ques_resposta_correta=AlternativaEnum.C,
            ques_resolucao="Pelo teorema da bissetriz interna: AB / 8 = AC / 12 → 10 / 8 = AC / 12 → 8 · AC = 120 → AC = 15 cm.",
            ques_resolucao_imagem_url=None,
        ),
        Questao(
            ques_cont_id=conteudo5.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.FACIL,
            ques_enunciado="Três retas paralelas cortam duas transversais. Na primeira transversal determinam segmentos de 6 cm e 9 cm; na segunda, segmentos de 10 cm e x. O valor de x é:",
            ques_imagem_url=f"{base_url}/imagens/questoes/gp1_q02_retas_paralelas.png",
            ques_alternativas={"A": "a) 12 cm", "B": "b) 14 cm", "C": "c) 15 cm", "D": "d) 16 cm", "E": "e) 18 cm"},
            ques_resposta_correta=AlternativaEnum.C,
            ques_resolucao="Pelo Teorema de Tales: 6 / 9 = 10 / x → 6x = 90 → x = 15 cm.",
            ques_resolucao_imagem_url=f"{base_url}/imagens/respostas/gp1_r02_proporcao_tales.png",
        ),
        Questao(
            ques_cont_id=conteudo5.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.FACIL,
            ques_enunciado="Uma reta paralela à base de um triângulo divide um dos lados em segmentos de 12 cm e 8 cm. Se o segmento superior do outro lado mede 18 cm, quanto mede o segmento inferior x?",
            ques_imagem_url=f"{base_url}/imagens/questoes/gp1_q03_mesa_bilhar.png",
            ques_alternativas={"A": "a) 8 cm", "B": "b) 10 cm", "C": "c) 12 cm", "D": "d) 14 cm", "E": "e) 16 cm"},
            ques_resposta_correta=AlternativaEnum.C,
            ques_resolucao="Aplicando o Teorema de Tales: 12 / 8 = 18 / x → 12x = 144 → x = 12 cm.",
            ques_resolucao_imagem_url=f"{base_url}/imagens/respostas/gp1_r03_distancia_bolas.png",
        ),
        Questao(
            ques_cont_id=conteudo5.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.MEDIO,
            ques_enunciado="Uma quadra situada entre duas ruas não paralelas é dividida por muros paralelos em três lotes cujas frentes na Rua A medem 20 m, 30 m e 50 m. Sabendo que a frente total da quadra na Rua B mede 150 m, qual é a medida da frente do lote central na Rua B?",
            ques_imagem_url=f"{base_url}/imagens/questoes/gp1_q04_terreno_fazenda.png",
            ques_alternativas={"A": "a) 40 m", "B": "b) 45 m", "C": "c) 50 m", "D": "d) 55 m", "E": "e) 60 m"},
            ques_resposta_correta=AlternativaEnum.B,
            ques_resolucao="A frente total na Rua A é 20 + 30 + 50 = 100 m. Pelo Teorema de Tales: 30 / 100 = x / 150 → x = 45 m.",
            ques_resolucao_imagem_url=f"{base_url}/imagens/respostas/gp1_r04_segmento_fg.png",
        ),
        Questao(
            ques_cont_id=conteudo5.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.MEDIO,
            ques_enunciado="Uma rampa retilínea atinge altura máxima de 1,8 m. Após percorrer 4,0 m sobre ela, um pedestre encontra-se a 0,6 m de altura. Quantos metros ainda faltam para alcançar o topo?",
            ques_imagem_url=None,
            ques_alternativas={"A": "a) 6,0 m", "B": "b) 7,2 m", "C": "c) 7,5 m", "D": "d) 8,0 m", "E": "e) 12,0 m"},
            ques_resposta_correta=AlternativaEnum.D,
            ques_resolucao="Por semelhança de triângulos: 4,0 / 0,6 = L / 1,8 → L = 12,0 m. O trecho restante é 12,0 - 4,0 = 8,0 m.",
            ques_resolucao_imagem_url=f"{base_url}/imagens/respostas/gp1_r05_esquema_rampa.png",
        ),
        Questao(
            ques_cont_id=conteudo5.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.MEDIO,
            ques_enunciado="Sobre os critérios de semelhança de triângulos, assinale a afirmação correta:",
            ques_imagem_url=None,
            ques_alternativas={
                "A": "a) Dois triângulos com dois ângulos correspondentes congruentes são semelhantes pelo caso AA.",
                "B": "b) Dois triângulos semelhantes possuem necessariamente o mesmo perímetro.",
                "C": "c) Ter três lados proporcionais garante a congruência entre os triângulos.",
                "D": "d) Triângulos retângulos são sempre semelhantes entre si.",
            },
            ques_resposta_correta=AlternativaEnum.A,
            ques_resolucao="Como a soma dos ângulos internos é 180°, dois ângulos correspondentes congruentes garantem o terceiro e asseguram a semelhança (caso AA).",
            ques_resolucao_imagem_url=None,
        ),
        Questao(
            ques_cont_id=conteudo5.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.FACIL,
            ques_enunciado="No mesmo instante em que um poste vertical de 6 m projeta uma sombra de 4 m, um prédio próximo projeta uma sombra de 20 m. Qual é a altura do prédio?",
            ques_imagem_url=f"{base_url}/imagens/questoes/gp1_q07_triangulos_paralelos.png",
            ques_alternativas={"A": "a) 22 m", "B": "b) 24 m", "C": "c) 26 m", "D": "d) 28 m", "E": "e) 30 m"},
            ques_resposta_correta=AlternativaEnum.E,
            ques_resolucao="Por semelhança de triângulos: H / 20 = 6 / 4 → 4H = 120 → H = 30 m.",
            ques_resolucao_imagem_url=None,
        ),
        Questao(
            ques_cont_id=conteudo5.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.FACIL,
            ques_enunciado="Uma escada apoiada em uma parede vertical atinge 12 m de altura, com sua base afastada 5 m da parede. Qual é o comprimento dessa escada?",
            ques_imagem_url=f"{base_url}/imagens/questoes/gp1_q08_escada_arvore.png",
            ques_alternativas={"A": "a) 11 m", "B": "b) 13 m", "C": "c) 15 m", "D": "d) 17 m"},
            ques_resposta_correta=AlternativaEnum.B,
            ques_resolucao="Pelo Teorema de Pitágoras: x² = 12² + 5² = 144 + 25 = 169 → x = 13 m.",
            ques_resolucao_imagem_url=f"{base_url}/imagens/respostas/gp1_r08_pitagoras_escada.png",
        ),
        Questao(
            ques_cont_id=conteudo5.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.DIFICIL,
            ques_enunciado="Uma quadra poliesportiva retangular mede 80 m de comprimento por 60 m de largura. Um atleta atravessa a diagonal ida e volta, enquanto outro dá uma volta completa pelo contorno da quadra. Quantos metros o segundo atleta percorreu a mais que o primeiro?",
            ques_imagem_url=f"{base_url}/imagens/questoes/gp1_q09_patio_retangular.png",
            ques_alternativas={"A": "a) 40 m", "B": "b) 60 m", "C": "c) 80 m", "D": "d) 100 m"},
            ques_resposta_correta=AlternativaEnum.C,
            ques_resolucao="Diagonal: d = √(80² + 60²) = 100 m (ida e volta = 200 m). Perímetro: 2 · (80 + 60) = 280 m. Diferença: 280 - 200 = 80 m.",
            ques_resolucao_imagem_url=f"{base_url}/imagens/respostas/gp1_r09_diagonal_patio.png",
        ),
        Questao(
            ques_cont_id=conteudo5.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.MEDIO,
            ques_enunciado="Em um triângulo retângulo de hipotenusa a, catetos b e c, altura h e projeções m e n, considere: I. h² = m · n; II. b² = a · n; III. c² = a · m; IV. a + h = b + c. São verdadeiras apenas:",
            ques_imagem_url=None,
            ques_alternativas={"A": "a) I, II e III", "B": "b) I, II e IV", "C": "c) I, III e IV", "D": "d) II, III e IV"},
            ques_resposta_correta=AlternativaEnum.A,
            ques_resolucao="As relações I, II e III são válidas no triângulo retângulo. A IV é incorreta, pois a relação métrica verdadeira é a · h = b · c.",
            ques_resolucao_imagem_url=None,
        ),
    ]
    session.add_all(questoes)
    session.commit()

def povoar_conteudo_6(session, base_url="https://seu-storage-publico.com"):
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
            ques_enunciado="A sombra de uma torre horizontal mede 30 m no momento em que os raios solares formam um ângulo de 60° com o solo. Adotando √3 ≈ 1,73, qual é a altura aproximada da torre?",
            ques_imagem_url=None,
            ques_alternativas={"A": "a) 17,3 m", "B": "b) 30,0 m", "C": "c) 51,9 m", "D": "d) 60,0 m", "E": "e) 73,2 m"},
            ques_resposta_correta=AlternativaEnum.C,
            ques_resolucao="Pela tangente de 60°: tg 60° = h / 30 → √3 = h / 30 → h = 30 · 1,73 = 51,9 m.",
            ques_resolucao_imagem_url=f"{base_url}/imagens/respostas/gp2_r01_altura_predio.png",
        ),
        Questao(
            ques_cont_id=conteudo6.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.FACIL,
            ques_enunciado="Uma rampa retilínea possui 40 m de comprimento e forma um ângulo de 30° com o plano horizontal. Qual é a altura vertical vencida ao final da rampa?",
            ques_imagem_url=None,
            ques_alternativas={"A": "a) 15 m", "B": "b) 20 m", "C": "c) 25 m", "D": "d) 30 m"},
            ques_resposta_correta=AlternativaEnum.B,
            ques_resolucao="Usando o seno de 30°: sen 30° = h / 40 → 1/2 = h / 40 → h = 20 m.",
            ques_resolucao_imagem_url=f"{base_url}/imagens/respostas/gp2_r02_altura_ladeira.png",
        ),
        Questao(
            ques_cont_id=conteudo6.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.MEDIO,
            ques_enunciado="Um drone decola em trajetória retilínea inclinada a 30° com o solo a partir de um ponto situado a 1000 m de distância horizontal de uma torre de 600 m de altura. Adotando √3 ≈ 1,73, ao cruzar a vertical da torre o drone estará:",
            ques_imagem_url=f"{base_url}/imagens/questoes/gp2_q03_aviao_serra.png",
            ques_alternativas={
                "A": "a) Acima do topo da torre, a 650 m.",
                "B": "b) Abaixo do topo da torre, a aproximadamente 576,7 m.",
                "C": "c) Exatamente no topo da torre, a 600 m.",
                "D": "d) A 500 m de altura.",
            },
            ques_resposta_correta=AlternativaEnum.B,
            ques_resolucao="Temos tg 30° = h / 1000 → h = 1000 · (√3 / 3) ≈ 1000 · 0,5767 = 576,7 m, abaixo dos 600 m da torre.",
            ques_resolucao_imagem_url=f"{base_url}/imagens/respostas/gp2_r03_trajetoria_aviao.png",
        ),
        Questao(
            ques_cont_id=conteudo6.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.FACIL,
            ques_enunciado="Uma pipa está presa por uma linha esticada de 100 m que forma 37° com o solo horizontal. Sabendo que sen 37° = 0,60 e cos 37° = 0,80, a altura da pipa em relação ao solo é:",
            ques_imagem_url=f"{base_url}/imagens/questoes/gp2_q04_decolagem_aviao.png",
            ques_alternativas={"A": "a) 60 m", "B": "b) 75 m", "C": "c) 80 m", "D": "d) 90 m"},
            ques_resposta_correta=AlternativaEnum.A,
            ques_resolucao="Aplicando o seno: sen 37° = h / 100 → 0,60 = h / 100 → h = 60 m.",
            ques_resolucao_imagem_url=f"{base_url}/imagens/respostas/gp2_r04_altura_aviao.png",
        ),
        Questao(
            ques_cont_id=conteudo6.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.MEDIO,
            ques_enunciado="Um topógrafo de 1,70 m de altura observa o topo de um farol a 200 m de distância horizontal sob um ângulo de elevação de 25°. Dado tg 25° = 0,47, a altura total do farol é:",
            ques_imagem_url=f"{base_url}/imagens/questoes/gp2_q05_menino_morro.png",
            ques_alternativas={"A": "a) 94,00 m", "B": "b) 92,30 m", "C": "c) 98,50 m", "D": "d) 95,70 m"},
            ques_resposta_correta=AlternativaEnum.D,
            ques_resolucao="A altura acima da linha de visão é x = 200 · 0,47 = 94,00 m. Somando a altura do observador: 94,00 + 1,70 = 95,70 m.",
            ques_resolucao_imagem_url=f"{base_url}/imagens/respostas/gp2_r05_altura_morro.png",
        ),
        Questao(
            ques_cont_id=conteudo6.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.MEDIO,
            ques_enunciado="Um terreno retangular tem 12 m de frente e sua diagonal forma um ângulo de 30° com essa frente. Usando √3 ≈ 1,7, qual valor mais se aproxima do comprimento da diagonal?",
            ques_imagem_url=None,
            ques_alternativas={"A": "a) 10 m", "B": "b) 11 m", "C": "c) 12 m", "D": "d) 13 m", "E": "e) 14 m"},
            ques_resposta_correta=AlternativaEnum.E,
            ques_resolucao="Pelo cosseno de 30°: cos 30° = 12 / d → 1,7 / 2 = 12 / d → d = 24 / 1,7 ≈ 14,1 m (mais próximo de 14 m).",
            ques_resolucao_imagem_url=f"{base_url}/imagens/respostas/gp2_r06_diagonal_retangulo.png",
        ),
        Questao(
            ques_cont_id=conteudo6.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.MEDIO,
            ques_enunciado="Sabendo que α é um ângulo do primeiro quadrante e que sen α = 5/13, qual é o valor de cos α?",
            ques_imagem_url=None,
            ques_alternativas={"A": "a) 12/13", "B": "b) 8/13", "C": "c) 5/12", "D": "d) 1/13", "E": "e) 7/13"},
            ques_resposta_correta=AlternativaEnum.A,
            ques_resolucao="Pela relação fundamental sen²α + cos²α = 1: (5/13)² + cos²α = 1 → cos²α = 1 - 25/169 = 144/169 → cos α = 12/13.",
            ques_resolucao_imagem_url=f"{base_url}/imagens/respostas/gp2_r07_relacao_fundamental.png",
        ),
        Questao(
            ques_cont_id=conteudo6.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.FACIL,
            ques_enunciado="Um cabo de sustentação de 80 m liga o topo de uma antena ao solo horizontal, formando um ângulo de 30° com o chão. Qual é a altura da antena?",
            ques_imagem_url=None,
            ques_alternativas={"A": "a) 20 m", "B": "b) 25 m", "C": "c) 30 m", "D": "d) 35 m", "E": "e) 40 m"},
            ques_resposta_correta=AlternativaEnum.E,
            ques_resolucao="Pelo seno de 30°: sen 30° = h / 80 → 0,5 = h / 80 → h = 40 m.",
            ques_resolucao_imagem_url=f"{base_url}/imagens/respostas/gp2_r08_altura_teleferico.png",
        ),
        Questao(
            ques_cont_id=conteudo6.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.FACIL,
            ques_enunciado="Em um triângulo retângulo com hipotenusa medindo 36 cm e um ângulo agudo de 30°, o cateto oposto a esse ângulo mede:",
            ques_imagem_url=None,
            ques_alternativas={"A": "a) 12 cm", "B": "b) 18 cm", "C": "c) 24 cm", "D": "d) 27 cm", "E": "e) 30 cm"},
            ques_resposta_correta=AlternativaEnum.B,
            ques_resolucao="Usando o seno de 30°: sen 30° = x / 36 → 1/2 = x / 36 → x = 18 cm.",
            ques_resolucao_imagem_url=f"{base_url}/imagens/respostas/gp2_r09_cateto_oposto.png",
        ),
        Questao(
            ques_cont_id=conteudo6.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.DIFICIL,
            ques_enunciado="Para ir do ponto A ao ponto C, um pedestre pode caminhar 30 m até B e depois virar 90° e caminhar mais 40 m até C. Se optar por seguir em linha reta de A até C, quantos metros economizará?",
            ques_imagem_url=f"{base_url}/imagens/questoes/gp2_q10_vista_parque.png",
            ques_alternativas={"A": "a) 20 m", "B": "b) 25 m", "C": "c) 30 m", "D": "d) 50 m"},
            ques_resposta_correta=AlternativaEnum.A,
            ques_resolucao="O atalho AC é a hipotenusa: AC = √(30² + 40²) = 50 m. O caminho via B soma 30 + 40 = 70 m. A economia é 70 - 50 = 20 m.",
            ques_resolucao_imagem_url=f"{base_url}/imagens/respostas/gp2_r10_caminhos_parque.png",
        ),
    ]
    session.add_all(questoes)
    session.commit()

def povoar_conteudo_7(session, base_url="https://seu-storage-publico.com"):
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
                "Analise as afirmações sobre funções:\n"
                "I. Toda função associa cada elemento do domínio a um único elemento do contradomínio.\n"
                "II. Em uma função sobrejetora, o conjunto imagem é igual ao contradomínio.\n"
                "III. Toda função injetora admite função inversa.\n"
                "Estão corretas:"
            ),
            ques_imagem_url=None,
            ques_alternativas={"A": "a) Apenas I", "B": "b) Apenas II", "C": "c) Apenas III", "D": "d) Apenas II e III", "E": "e) Apenas I e II"},
            ques_resposta_correta=AlternativaEnum.E,
            ques_resolucao="I e II correspondem às definições formais de função e sobrejetividade. III é falsa, pois apenas funções bijetoras admitem inversa.",
            ques_resolucao_imagem_url=None,
        ),
        Questao(
            ques_cont_id=conteudo7.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.FACIL,
            ques_enunciado="Considere a função f: N → N definida por f(x) = 3x. Essa função é:",
            ques_imagem_url=f"{base_url}/imagens/questoes/fa_q02_funcao_inteiros.png",
            ques_alternativas={"A": "a) Apenas sobrejetora", "B": "b) Apenas injetora", "C": "c) Bijetora", "D": "d) Nem injetora nem sobrejetora"},
            ques_resposta_correta=AlternativaEnum.B,
            ques_resolucao="Valores distintos de x geram múltiplos distintos de 3 (injetora), mas o contradomínio N contém números que não são múltiplos de 3 (não sobrejetora).",
            ques_resolucao_imagem_url=f"{base_url}/imagens/respostas/fa_r02_imagem_funcao.png",
        ),
        Questao(
            ques_cont_id=conteudo7.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.MEDIO,
            ques_enunciado="Seja f: R → R definida por f(x) = 2x + 1 e g(x) sua função inversa. O valor de g(f(7)) é:",
            ques_imagem_url=f"{base_url}/imagens/questoes/fa_q03_funcao_inversa.png",
            ques_alternativas={"A": "a) 7", "B": "b) 15", "C": "c) 3", "D": "d) 1"},
            ques_resposta_correta=AlternativaEnum.A,
            ques_resolucao="Pela propriedade da composição de funções inversas, f⁻¹(f(x)) = x para todo x real, logo g(f(7)) = 7.",
            ques_resolucao_imagem_url=f"{base_url}/imagens/respostas/fa_r03_funcao_inversa.png",
        ),
        Questao(
            ques_cont_id=conteudo7.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.FACIL,
            ques_enunciado="Para que valores reais de k a função afim f(x) = (3k - 12)x + 5 é decrescente?",
            ques_imagem_url=f"{base_url}/imagens/questoes/fa_q04_funcao_decrescente.png",
            ques_alternativas={"A": "a) k < 4", "B": "b) k > 4", "C": "c) k = 4", "D": "d) k ≤ 4"},
            ques_resposta_correta=AlternativaEnum.A,
            ques_resolucao="Uma função afim é decrescente quando seu coeficiente angular é negativo: 3k - 12 < 0 → 3k < 12 → k < 4.",
            ques_resolucao_imagem_url=f"{base_url}/imagens/respostas/fa_r04_coeficiente_angular.png",
        ),
        Questao(
            ques_cont_id=conteudo7.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.MEDIO,
            ques_enunciado="Um entregador recebe R$ 4,00 fixos por entrega realizada mais R$ 1,50 por quilômetro rodado. Em um dia em que fez 8 entregas e recebeu R$ 152,00 no total, quantos quilômetros ele percorreu?",
            ques_imagem_url=None,
            ques_alternativas={"A": "a) 60 km", "B": "b) 72 km", "C": "c) 80 km", "D": "d) 96 km"},
            ques_resposta_correta=AlternativaEnum.C,
            ques_resolucao="Montando a equação: 8 · 4 + 1,5x = 152 → 32 + 1,5x = 152 → 1,5x = 120 → x = 80 km.",
            ques_resolucao_imagem_url=f"{base_url}/imagens/respostas/fa_r05_calculo_taxista.png",
        ),
        Questao(
            ques_cont_id=conteudo7.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.DIFICIL,
            ques_enunciado="Seja f(x) = ax + b uma função afim tal que f(3) = 4. O valor de f((f(1) + f(5)) / 2) é igual a:",
            ques_imagem_url=None,
            ques_alternativas={"A": "a) 1", "B": "b) 2", "C": "c) 3", "D": "d) 4"},
            ques_resposta_correta=AlternativaEnum.D,
            ques_resolucao="Temos (f(1) + f(5)) / 2 = ((a + b) + (5a + b)) / 2 = (6a + 2b) / 2 = 3a + b = f(3) = 4.",
            ques_resolucao_imagem_url=f"{base_url}/imagens/respostas/fa_r06_soma_funcoes.png",
        ),
        Questao(
            ques_cont_id=conteudo7.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.FACIL,
            ques_enunciado="Um técnico de informática cobra R$ 50,00 pela visita e R$ 35,00 por hora de atendimento. A lei que expressa o custo total C em função das horas h trabalhadas é:",
            ques_imagem_url=None,
            ques_alternativas={"A": "a) C = 50h", "B": "b) C = 85h", "C": "c) C = 35 + 50h", "D": "d) C = 50 + 35h"},
            ques_resposta_correta=AlternativaEnum.D,
            ques_resolucao="O valor fixo de R$ 50,00 é o coeficiente linear e R$ 35,00 é o coeficiente angular, resultando em C = 50 + 35h.",
            ques_resolucao_imagem_url=None,
        ),
        Questao(
            ques_cont_id=conteudo7.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.FACIL,
            ques_enunciado="Uma corrida de aplicativo tem tarifa base de R$ 5,00 mais R$ 1,20 por quilômetro percorrido. Se o valor final pago foi R$ 23,00, qual foi a distância da viagem?",
            ques_imagem_url=None,
            ques_alternativas={"A": "a) 10 km", "B": "b) 12 km", "C": "c) 15 km", "D": "d) 18 km", "E": "e) 20 km"},
            ques_resposta_correta=AlternativaEnum.C,
            ques_resolucao="Resolvendo 5 + 1,2d = 23 → 1,2d = 18 → d = 18 / 1,2 = 15 km.",
            ques_resolucao_imagem_url=None,
        ),
        Questao(
            ques_cont_id=conteudo7.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.FACIL,
            ques_enunciado="O zero da função afim f(x) = -4x + 10 é:",
            ques_imagem_url=None,
            ques_alternativas={"A": "a) 2", "B": "b) 2,5", "C": "c) -2,5", "D": "d) 4", "E": "e) -4"},
            ques_resposta_correta=AlternativaEnum.B,
            ques_resolucao="Fazendo f(x) = 0: -4x + 10 = 0 → 4x = 10 → x = 10 / 4 = 2,5.",
            ques_resolucao_imagem_url=None,
        ),
        Questao(
            ques_cont_id=conteudo7.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.MEDIO,
            ques_enunciado="Uma máquina industrial adquirida por R$ 200.000,00 sofre depreciação linear de R$ 15.000,00 por ano de uso. Qual será o valor contábil dessa máquina após 6 anos?",
            ques_imagem_url=None,
            ques_alternativas={"A": "a) R$ 90.000,00", "B": "b) R$ 100.000,00", "C": "c) R$ 110.000,00", "D": "d) R$ 125.000,00", "E": "e) R$ 140.000,00"},
            ques_resposta_correta=AlternativaEnum.C,
            ques_resolucao="Pela função V(t) = 200.000 - 15.000t, temos V(6) = 200.000 - 15.000 · 6 = 200.000 - 90.000 = R$ 110.000,00.",
            ques_resolucao_imagem_url=None,
        ),
    ]
    session.add_all(questoes)
    session.commit()

def povoar_conteudo_8(session, base_url="https://seu-storage-publico.com"):
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
            ques_enunciado="A função quadrática f(x) = x² - 2kx + 20 assume valor mínimo igual a 4. Qual é o valor positivo do parâmetro k?",
            ques_imagem_url=f"{base_url}/imagens/questoes/fq_q01_lei_funcao.png",
            ques_alternativas={"A": "a) 4", "B": "b) 5", "C": "c) 8", "D": "d) 16"},
            ques_resposta_correta=AlternativaEnum.A,
            ques_resolucao="Usando yv = -Δ / 4a = 4: -(4k² - 80) / 4 = 4 → -k² + 20 = 4 → k² = 16 → k = 4.",
            ques_resolucao_imagem_url=f"{base_url}/imagens/respostas/fq_r01_vertice_yv.png",
        ),
        Questao(
            ques_cont_id=conteudo8.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.FACIL,
            ques_enunciado="Dada a função f(x) = x² - 5x + 7, o valor numérico de f(3) é:",
            ques_imagem_url=None,
            ques_alternativas={"A": "a) 0", "B": "b) 1", "C": "c) 3", "D": "d) 7", "E": "e) 13"},
            ques_resposta_correta=AlternativaEnum.B,
            ques_resolucao="Substituindo x = 3: f(3) = 3² - 5 · 3 + 7 = 9 - 15 + 7 = 1.",
            ques_resolucao_imagem_url=None,
        ),
        Questao(
            ques_cont_id=conteudo8.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.FACIL,
            ques_enunciado="Sobre o gráfico da função f(x) = -2x² + 4x - 1, pode-se afirmar que a parábola possui:",
            ques_imagem_url=None,
            ques_alternativas={
                "A": "a) Concavidade voltada para cima.",
                "B": "b) Ponto de mínimo no vértice.",
                "C": "c) Concavidade voltada para baixo.",
                "D": "d) Interseção com o eixo y em (0, 4).",
            },
            ques_resposta_correta=AlternativaEnum.C,
            ques_resolucao="Como o coeficiente a = -2 é negativo, a parábola tem concavidade voltada para baixo.",
            ques_resolucao_imagem_url=None,
        ),
        Questao(
            ques_cont_id=conteudo8.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.MEDIO,
            ques_enunciado="A altura h (em metros) de um projétil lançado verticalmente após t segundos é dada por h(t) = -5t² + 30t. Qual é a altura máxima atingida?",
            ques_imagem_url=None,
            ques_alternativas={"A": "a) 30 m", "B": "b) 40 m", "C": "c) 45 m", "D": "d) 50 m", "E": "e) 60 m"},
            ques_resposta_correta=AlternativaEnum.C,
            ques_resolucao="Calculando yv = -Δ / 4a: Δ = 30² - 4·(-5)·0 = 900 → yv = -900 / (-20) = 45 m.",
            ques_resolucao_imagem_url=f"{base_url}/imagens/respostas/fq_r04_altura_maxima.png",
        ),
        Questao(
            ques_cont_id=conteudo8.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.FACIL,
            ques_enunciado="Dada a função exponencial f(x) = 3^(x+1) + 5, qual valor de x satisfaz f(x) = 32?",
            ques_imagem_url=None,
            ques_alternativas={"A": "a) 2", "B": "b) 3", "C": "c) 4", "D": "d) 5", "E": "e) 6"},
            ques_resposta_correta=AlternativaEnum.A,
            ques_resolucao="Resolvendo 3^(x+1) + 5 = 32 → 3^(x+1) = 27 → 3^(x+1) = 3³ → x + 1 = 3 → x = 2.",
            ques_resolucao_imagem_url=None,
        ),
        Questao(
            ques_cont_id=conteudo8.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.MEDIO,
            ques_enunciado="Uma função exponencial do tipo f(x) = a^x possui gráfico decrescente e passa pelo ponto (-1, 4). Sua lei de formação é:",
            ques_imagem_url=f"{base_url}/imagens/questoes/fq_q06_grafico_exponencial.png",
            ques_alternativas={"A": "a) f(x) = 4^x", "B": "b) f(x) = 2^x", "C": "c) f(x) = 0,5^x", "D": "d) f(x) = 0,25^x", "E": "e) f(x) = 0,2^x"},
            ques_resposta_correta=AlternativaEnum.D,
            ques_resolucao="Substituindo (-1, 4): a⁻¹ = 4 → 1/a = 4 → a = 1/4 = 0,25. Portanto, f(x) = 0,25^x.",
            ques_resolucao_imagem_url=f"{base_url}/imagens/respostas/fq_r06_lei_exponencial.png",
        ),
        Questao(
            ques_cont_id=conteudo8.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.FACIL,
            ques_enunciado="Sobre f(x) = a^x (com a > 0 e a ≠ 1), julgue: I. A função é crescente para todo a > 0; II. f(0) = 1; III. O gráfico não corta o eixo x. É falsa apenas:",
            ques_imagem_url=None,
            ques_alternativas={"A": "a) I", "B": "b) II", "C": "c) III", "D": "d) Nenhuma", "E": "e) Todas"},
            ques_resposta_correta=AlternativaEnum.A,
            ques_resolucao="A afirmação I é falsa porque a função é crescente apenas quando a > 1 (para 0 < a < 1, ela é decrescente).",
            ques_resolucao_imagem_url=None,
        ),
        Questao(
            ques_cont_id=conteudo8.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.DIFICIL,
            ques_enunciado="Qual lei define a função logarítmica cujo domínio real é D = {x ∈ R | x > 2} e cuja raiz ocorre em x = 3?",
            ques_imagem_url=f"{base_url}/imagens/questoes/fq_q08_grafico_logaritmica.png",
            ques_alternativas={"A": "a) f(x) = log₂(x - 2)", "B": "b) f(x) = log₂(x + 2)", "C": "c) f(x) = log₂(x - 3)", "D": "d) f(x) = log₂(x + 3)"},
            ques_resposta_correta=AlternativaEnum.A,
            ques_resolucao="A condição x - 2 > 0 define o domínio x > 2, e para x = 3 temos log₂(3 - 2) = log₂(1) = 0.",
            ques_resolucao_imagem_url=f"{base_url}/imagens/respostas/fq_r08_translacao_log.png",
        ),
        Questao(
            ques_cont_id=conteudo8.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.FACIL,
            ques_enunciado="Dadas f(x) = log₂(x) e g(x) = log₅(x), o valor de f(16) - g(25) é:",
            ques_imagem_url=None,
            ques_alternativas={"A": "a) 1", "B": "b) 2", "C": "c) 3", "D": "d) 4", "E": "e) 6"},
            ques_resposta_correta=AlternativaEnum.B,
            ques_resolucao="Como 2⁴ = 16 e 5² = 25, temos f(16) = 4 e g(25) = 2. Logo, 4 - 2 = 2.",
            ques_resolucao_imagem_url=None,
        ),
        Questao(
            ques_cont_id=conteudo8.cont_id,
            ques_etapa=EtapaEnum.ETAPA_1,
            ques_nivel_dificuldade=DificuldadeEnum.MEDIO,
            ques_enunciado="O crescimento de uma cultura em laboratório é modelado por P(t) = 2 + log₂(4 + t), em que t é o tempo em horas e P(t) é a massa em gramas. Após 12 horas, a massa será de:",
            ques_imagem_url=None,
            ques_alternativas={"A": "a) 3 g", "B": "b) 4 g", "C": "c) 5 g", "D": "d) 6 g", "E": "e) 8 g"},
            ques_resposta_correta=AlternativaEnum.D,
            ques_resolucao="Substituindo t = 12: P(12) = 2 + log₂(4 + 12) = 2 + log₂(16) = 2 + 4 = 6 g.",
            ques_resolucao_imagem_url=None,
        ),
    ]
    session.add_all(questoes)
    session.commit()

def povoar_simulado_1(db: Session, base_url: str = "https://seu-storage-publico.com"):
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
                "(Enem 2020) O consumo de espumantes no Brasil tem aumentado nos últimos anos. Uma das etapas do seu processo de produção consiste no "
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
                "O estádio do Maracanã passou por algumas modificações estruturais para a realização da Copa do Mundo de 2014, como, por exemplo, "
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
                "O uso de aplicativos de transporte tem sido uma alternativa à população que busca preços mais competitivos para se locomover, "
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
                "Os 100 funcionários de uma empresa estão distribuídos em dois setores: Produção e Administração. Os funcionários de um mesmo setor "
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
                "O ideal é consumir 1 grama de carboidrato para cada minuto de caminhada. Um casal realizará diariamente 30 minutos de caminhada, "
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
                "Um investidor iniciante observou o gráfico que apresenta a evolução dos valores de duas criptomoedas A e B em relação ao tempo.\n"
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
                "Um agricultor é informado sobre um método de proteção para sua lavoura que consiste em inserir larvas específicas, de rápida reprodução. "
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
                "Para concretar a laje de sua residência, uma pessoa contratou uma construtora. Tal empresa informa que o preço y do concreto bombeado é "
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
                "Entre maratonistas, um parâmetro utilizado é o de economia de corrida (EC). O valor desse parâmetro é calculado pela razão entre o consumo "
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
                "A figura ilustra uma roda-gigante no exato instante em que a cadeira onde se encontra a pessoa P está no ponto mais alto dessa roda-gigante.\n"
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
                "(Enem 2017) Em um teleférico turístico, bondinhos saem de estações ao nível do mar e do topo de uma montanha. A travessia dura 1,5 minuto "
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
                "(Enem 2013) O dono de um sítio pretende colocar uma haste de sustentação para melhor firmar dois postes de comprimentos iguais a 6 m e 4 m. "
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
                "Um adolescente, tendo em vista uma alimentação saudável, consome diariamente 7,5 dL de leite durante 1 mês (30 dias). "
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
                "(Enem 2020) Pesquisadores da Universidade de Tecnologia de Viena, na Áustria, produziram miniaturas de objetos em impressoras 3D de alta precisão. "
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
                "De forma geral, são necessários 50 kg de bauxita para produzir 10 kg de alumínio. O Brasil fechou 2020 como um dos principais líderes "
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
                "1o calcular a média de suas notas em 4 provas, um estudante dividiu, por engano, a soma das notas por 5. Com isso, a média obtida foi "
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
                "O gráfico apresenta o valor total de exportações e o valor total de importações, ao longo de um período, em bilhão de dólares. "
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
            ques_resolucao="Pelo gráfico: S1 ≈ 14,10 = 4,5 bi; S2 < 0 (importações superaram exportações); S3 ≈ 17,1 - 14,8 = 2,3 bi. Logo, S1 > S3 > S2.",
            ques_resolucao_imagem_url=None,
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
                "Uma pessoa ampliou uma foto no computador e, ao imprimi-la, verificou que a qualidade não estava boa. Ao pesquisar, descobriu que "
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