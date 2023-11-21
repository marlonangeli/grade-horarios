import os

from utils.arquivo import ler_arquivo_json

def main():
    caminho = os.path.dirname(os.path.abspath(__file__)) + "/data/"
    disciplinas = ler_arquivo_json(caminho + "disciplinas.json")
    professores = ler_arquivo_json(caminho + "professores.json")

    print(disciplinas)
    print(professores)


if __name__ == "__main__":
    main()
