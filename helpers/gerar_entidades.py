from models.disciplina import Disciplina
from models.professor import Professor
from utils.arquivo import escrever_arquivo_json
import os


def gerar_entidades():
    # Disciplinas

    # 1º Período
    logica_matematica = Disciplina("Lógica Matemática", 1, 4)
    fundamentos_programacao = Disciplina("Fundamentos de Programação", 1, 4)
    introducao_cc = Disciplina("Introdução à Ciência da Computação", 1, 2)
    fundamentos_eletricidade = Disciplina("Fundamentos de Eletricidade", 1, 2)
    calculo1 = Disciplina("Cálculo 1", 1, 6)
    comunicacao = Disciplina("Comunicação Linguística", 1, 2)
    fisica2 = Disciplina("Física 2", 1, 5)

    # 2º Período
    linguagem_estruturada = Disciplina("Linguagem Estruturada", 2, 3)
    circuitos_digitais = Disciplina("Circuitos Digitais", 2, 6)
    algebra_linear = Disciplina("Geometria Analítica e Álgebra Linear", 2, 6)
    calculo2 = Disciplina("Cálculo 2", 2, 4)
    metodologia = Disciplina("Metodologia da Pesquisa", 2, 2)
    probabilidade_estatistica = Disciplina("Probabilidade e Estatística", 2, 4)

    # 3º Período
    estrutura_dados = Disciplina("Estrutura de Dados", 3, 4)
    fund_banco_de_dados = Disciplina("Fundamentos de Banco de Dados", 3, 4)
    html = Disciplina("Linguagem de Estruturação e Apresentação de Conteúdos", 3, 3)
    arquitetura_computadores = Disciplina("Arquitetura de Computadores", 3, 4)
    poo = Disciplina("Programação Orientada a Objetos", 3, 4)
    calculo_numerico = Disciplina("Cálculo Numérico", 3, 4)

    # 4º Período
    po1 = Disciplina("Pesquisa Operacional 1", 4, 4)
    sgbd = Disciplina("Sistemas Gerenciadores de Banco de Dados", 4, 4)
    pesquisa_ord_dados = Disciplina("Pesquisa e Ordenação de Dados", 4, 3)
    eng_requisitos = Disciplina("Engenharia de Requisitos", 4, 3)
    ling_montagem = Disciplina("Linguagem de Montagem", 4, 3)
    comunicacao_dados = Disciplina("Comunicação de Dados", 4, 4)

    # 5º Período
    lfa = Disciplina("Linguagens Formais e Autômatos", 5, 4)
    computacao_grafica = Disciplina("Computação Gráfica", 5, 4)
    paradigmas = Disciplina("Paradigmas de Linguagens de Programação", 5, 3)
    eng_soft1 = Disciplina("Engenharia de Software 1", 5, 3)
    so = Disciplina("Sistemas Operacionais", 5, 4)
    redes1 = Disciplina("Redes de Computadores 1", 5, 4)
    arquitetura_avancada = Disciplina("Arquitetura Avançada de Hardware", 5, 3)

    # 6º Período
    ia1 = Disciplina("Fundamentos de Sistemas Inteligentes", 6, 3)
    ihc = Disciplina("Interação Humano-Computador", 6, 4)
    eng_soft2 = Disciplina("Engenharia de Software 2", 6, 3)
    tds = Disciplina("Tecnologia de Desenvolvimento de Sistemas", 6, 4)
    aspectos = Disciplina("Aspectos Formais da Computação", 6, 3)
    redes2 = Disciplina("Redes de Computadores 2", 6, 4)
    lab_so = Disciplina("Laboratório de Sistemas Operacionais", 6, 4)

    # 7º Período
    ia2 = Disciplina("Sistemas Inteligentes Aplicados", 7, 4)
    compiladores = Disciplina("Construção de Compiladores", 7, 4)
    tcc1 = Disciplina("Trabalho de Conclusão de Curso 1", 7, 4)
    seg_redes = Disciplina("Segurança em Redes de Computadores", 7, 3)
    sistemas_distribuidos = Disciplina("Sistemas Distribuídos", 7, 4)
    empreeendedorismo = Disciplina("Empreendedorismo", 7, 2)

    # 8º Período
    tcc2 = Disciplina("Trabalho de Conclusão de Curso 2", 8, 4)
    gerencia_projeto = Disciplina("Gerenciamento de Projetos", 8, 3)
    gestao_inovacao = Disciplina("Gestão da Inovação e Tecnologia", 8, 2)
    topicos_avancados = Disciplina("Tópicos Avançados em Computação", 8, 5)

    disciplinas = [
        logica_matematica,
        fundamentos_programacao,
        introducao_cc,
        fundamentos_eletricidade,
        calculo1,
        comunicacao,
        fisica2,
        linguagem_estruturada,
        circuitos_digitais,
        algebra_linear,
        calculo2,
        metodologia,
        probabilidade_estatistica,
        estrutura_dados,
        fund_banco_de_dados,
        html,
        arquitetura_computadores,
        poo,
        calculo_numerico,
        po1,
        sgbd,
        pesquisa_ord_dados,
        eng_requisitos,
        ling_montagem,
        comunicacao_dados,
        lfa,
        computacao_grafica,
        paradigmas,
        eng_soft1,
        so,
        redes1,
        arquitetura_avancada,
        ia1,
        ihc,
        eng_soft2,
        tds,
        aspectos,
        redes2,
        lab_so,
        ia2,
        compiladores,
        tcc1,
        seg_redes,
        sistemas_distribuidos,
        empreeendedorismo,
        tcc2,
        gerencia_projeto,
        gestao_inovacao,
        topicos_avancados
    ]

    # Professores
    agnaldo = Professor("Agnaldo", [lab_so, computacao_grafica])
    alan = Professor("Alan", [eng_requisitos, gerencia_projeto, tcc2])
    alessandra = Professor("Alessandra", [ihc, paradigmas, tcc1, tcc2])
    angonese = Professor("Cesar Angonese", [fundamentos_programacao, fund_banco_de_dados, sgbd])
    cesar_cardoso = Professor("Cesar Cardoso", [fundamentos_programacao])
    pessini = Professor("Evando Pessini", [estrutura_dados, lfa, aspectos])
    coimbra = Professor("Everton Coimbra de Araújo", [poo, tds])
    hamilton = Professor("Hamilton", [ling_montagem, comunicacao_dados, so, arquitetura_avancada])
    jorge = Professor("Jorge", [ia1, ia2, compiladores])
    juliano = Professor("Juliano Lamb", [linguagem_estruturada, eng_soft1, eng_soft2, pesquisa_ord_dados])
    kelyn = Professor("Kelyn", [fund_banco_de_dados])
    betzek = Professor("Nelson Betzek", [logica_matematica, arquitetura_computadores])
    neylor = Professor("Neylor", [redes1, redes2, seg_redes])
    sobjak = Professor("Ricardo Sobjak", [html, topicos_avancados])
    thiago = Professor("Thiago França Neves", [ia1, ia2])
    schutz = Professor("Fernando Schutz", [introducao_cc, sistemas_distribuidos])
    prof_calculo1 = Professor("Prof. Cálculo 1", [calculo1, calculo2, probabilidade_estatistica])
    prof_calculo2 = Professor("Prof. Cálculo 2", [calculo2, calculo_numerico, po1])
    prof_eletrica = Professor("Prof. Fundamentos de Eletricidade", [fundamentos_eletricidade, circuitos_digitais])
    prof_fisica = Professor("Prof. Física", [fisica2, algebra_linear])
    prof_metodologia = Professor("Prof. Metodologia", [metodologia, empreeendedorismo, gestao_inovacao])
    prof_comunicacao = Professor("Prof. Comunicação", [comunicacao, metodologia])

    professores = [
        agnaldo,
        alan,
        alessandra,
        angonese,
        cesar_cardoso,
        pessini,
        coimbra,
        hamilton,
        jorge,
        juliano,
        kelyn,
        betzek,
        neylor,
        sobjak,
        thiago,
        schutz,
        prof_calculo1,
        prof_calculo2,
        prof_eletrica,
        prof_fisica,
        prof_metodologia,
        prof_comunicacao
    ]

    return disciplinas, professores


def salvar_entidades(entidades):
    disciplinas, professores = entidades

    caminho = os.path.dirname(os.path.abspath(__file__)) + "/../data/"

    escrever_arquivo_json(caminho + "disciplinas.json", disciplinas)
    escrever_arquivo_json(caminho + "professores.json", professores)


def main():
    entidades = gerar_entidades()
    print("Entidades geradas com sucesso!")

    # Salvar entidades
    salvar_entidades(entidades)
    print("Entidades salvas com sucesso!")


if __name__ == "__main__":
    main()
