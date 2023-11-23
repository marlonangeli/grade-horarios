import os

from utils.arquivo import ler_arquivo_json
from algorithms.elitismo import elitismo

def main():
    caminho = os.path.dirname(os.path.abspath(__file__)) + "/data/"
    disciplinas = ler_arquivo_json(caminho + "disciplinas.json")
    professores = ler_arquivo_json(caminho + "professores.json")

    print(disciplinas)
    print(professores)

    individuo = elitismo(disciplinas, professores)


if __name__ == "__main__":
    main()
