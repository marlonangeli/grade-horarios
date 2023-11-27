import os

from utils.arquivo import carregar_de_pickle
from algorithms.elitismo import Elitismo
from pprint import pprint

from view.tabela import exportar_grade_csv


def main():
    caminho = os.path.dirname(os.path.abspath(__file__)) + "/data/"
    professores = carregar_de_pickle(caminho + "professores.pickle")
    disciplinas = carregar_de_pickle(caminho + "disciplinas.pickle")

    tamanho_populacao = 100
    numero_geracoes = 50
    taxa_crossover = 0.8
    taxa_mutacao = 0.2

    algoritmo = Elitismo(disciplinas, professores, tamanho_populacao, numero_geracoes, taxa_crossover, taxa_mutacao)
    result = algoritmo.executar()

    exportar_grade_csv(result['melhor_individuo'], caminho + "grade.csv")

    pprint('=' * 50)
    pprint('Melhor Fitness: ' + str(result['melhor_fitness']))
    pprint('Tempo: ' + str(result['tempo']))


if __name__ == "__main__":
    main()
