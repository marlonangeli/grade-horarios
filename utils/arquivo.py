from . import json, os, sys


def converter_objeto_para_json(objeto: object) -> str:
    return json.dumps(objeto, default=lambda o: o.__dict__, indent=2, ensure_ascii=False).encode('utf-8').decode(
        'utf-8')


def converter_json_para_objeto(json_string: str) -> object:
    return json.loads(json_string)


def ler_arquivo_json(nome_arquivo: str) -> object:
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
        conteudo = arquivo.read()
    return converter_json_para_objeto(conteudo)


def escrever_arquivo_json(nome_arquivo: str, objeto: object) -> None:
    with open(nome_arquivo, 'w+', encoding='utf-8') as arquivo:
        obj_json = converter_objeto_para_json(objeto)
        arquivo.write(obj_json)
