import os

from utils.arquivo import carregar_de_pickle
from algorithms.elitismo import Elitismo
from pprint import pprint

from view.grafico import gerar_grafico_evolucao
from view.tabela import exportar_grade_csv


def main():
    caminho = os.path.dirname(os.path.abspath(__file__)) + "/data/"
    professores = carregar_de_pickle(caminho + "professores.pickle")
    disciplinas = carregar_de_pickle(caminho + "disciplinas.pickle")

    tamanho_populacao = 50
    numero_geracoes = 500
    taxa_crossover = 0.7
    taxa_mutacao = 0.3

    algoritmo = Elitismo(disciplinas, professores, tamanho_populacao, numero_geracoes, taxa_crossover, taxa_mutacao)
    result = algoritmo.executar()

    exportar_grade_csv(result['melhor_individuo'], caminho + "grade.csv")
    gerar_grafico_evolucao(result['estatisticas'], caminho + "grafico.png")

    print('=' * 50)
    print('Melhor Fitness: ' + str(result['melhor_fitness']))
    print('Tempo: ' + str(result['tempo']))


if __name__ == "__main__":
    main()
