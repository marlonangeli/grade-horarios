import matplotlib.pyplot as plt

def gerar_grafico_evolucao(geracoes, nome_arquivo):
    media = [geracao['avg'] for geracao in geracoes]
    melhor = [geracao['max'] for geracao in geracoes]
    pior = [geracao['min'] for geracao in geracoes]

    plt.plot(media, label='Média')
    plt.plot(melhor, label='Melhor')
    plt.plot(pior, label='Pior')

    plt.title('Evolução da População')
    plt.xlabel('Geração')
    plt.ylabel('Fitness')
    plt.legend()

    plt.savefig(nome_arquivo)
    plt.show()
