from deap import base, creator, tools, algorithms

from models.disciplina import Disciplina
from models.professor import Professor
from . import numpy as np
from . import random
from . import time
from . import copy
from . import math


def elitismo(disciplinas: list[Disciplina], professores: list[Professor]):
    # Criação de um objeto de tipo FitnessMax (Fitness é o tipo de dado e Max é o objetivo)
    # O objetivo é maximizar a função de avaliação
    # O peso é 1.0 pois só temos um objetivo
    creator.create("FitnessMax", base.Fitness, weights=(1.0,))

    # Criação de um objeto de tipo Individual (indivíduo)
    # O tipo de dado é uma lista
    # O fitness é um objeto do tipo FitnessMax
    creator.create("Individual", list, fitness=creator.FitnessMax)

    # Criação da toolbox
    toolbox = base.Toolbox()

    # Registro de funções
    toolbox.register("attr_disciplina", random.randint, 0, len(disciplinas) - 1)
    toolbox.register("attr_professor", random.randint, 0, len(professores) - 1)

    # Registro de estruturas
    toolbox.register("individual", tools.initCycle, creator.Individual,
                     (toolbox.attr_disciplina, toolbox.attr_professor), n=1)
    toolbox.register("population", tools.initRepeat, list, toolbox.individual)

    # Registro de operações genéticas
    toolbox.register("evaluate", avaliacao)
    toolbox.register("mate", tools.cxOnePoint)
    toolbox.register("mutate", tools.mutUniformInt, low=0, up=len(disciplinas) - 1, indpb=0.05)
    toolbox.register("select", tools.selTournament, tournsize=3)

    # Criação da população inicial
    pop = toolbox.population(n=100)

    # Criação da estatística
    stats = tools.Statistics(key=lambda ind: ind.fitness.values)
    stats.register("avg", np.mean)
    stats.register("std", np.std)
    stats.register("min", np.min)
    stats.register("max", np.max)

    # Definição do algoritmo genético
    pop, log = algorithms.eaSimple(pop, toolbox, cxpb=0.5, mutpb=0.2, ngen=100, stats=stats, verbose=True)

    # Retorno do melhor indivíduo
    return tools.selBest(pop, 1)[0]


def avaliacao(individuo):
    return random.randint(0, 100),  # Retorna um tuple
