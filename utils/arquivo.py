from . import pickle, os, sys


def salvar_em_pickle(objeto: object, nome_arquivo: str) -> None:
    if not os.path.exists(os.path.dirname(nome_arquivo)):
        os.makedirs(os.path.dirname(nome_arquivo))
    with open(nome_arquivo, 'wb') as arquivo:
        pickle.dump(objeto, arquivo, pickle.HIGHEST_PROTOCOL)


def carregar_de_pickle(nome_arquivo: str) -> object:
    if not os.path.exists(nome_arquivo):
        print(f"O arquivo {nome_arquivo} não existe.")
        sys.exit(1)
    with open(nome_arquivo, 'rb') as arquivo:
        return pickle.load(arquivo)
