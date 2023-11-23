from deap import base, creator, tools, algorithms
from . import numpy as np
from . import random
from . import Disciplina, Professor, DiaDaSemana, Horario, Aula, Grade


class AlgoritmoGenetico:
    def __init__(self, disciplinas: list[Disciplina], professores: list[Professor]):
        self._tamanho_populacao = None
        self._numero_geracoes = None
        self._taxa_crossover = None
        self._taxa_mutacao = None

        self.disciplinas = disciplinas
        self.professores = professores
        self.toolbox = base.Toolbox()

        self._criar_estruturas()
        self._criar_operacoes_geneticas()

    def _criar_individuo(self):
        self.toolbox.register("attr_disciplina", random.randint, 0, len(self.disciplinas) - 1)
        self.toolbox.register("attr_professor", random.randint, 0, len(self.professores) - 1)

        self.toolbox.register("individual", tools.initCycle, creator.Individual,
                              (self.toolbox.attr_disciplina, self.toolbox.attr_professor), n=1)
        return self.toolbox.individual()

    def _criar_populacao(self):
        self.toolbox.register("population", tools.initRepeat, list, self._criar_individuo)
        return self.toolbox.population(n=self._tamanho_populacao)

    def _criar_estruturas(self):
        creator.create("FitnessMax", base.Fitness, weights=(1.0,))
        creator.create("Individual", list, fitness=creator.FitnessMax)

        self._criar_populacao()

    def _criar_operacoes_geneticas(self):
        self.toolbox.register("evaluate", self._avaliacao)
        self.toolbox.register("mate", tools.cxOnePoint)
        self.toolbox.register("mutate", tools.mutUniformInt, low=0, up=len(self.disciplinas) - 1, indpb=0.05)
        self.toolbox.register("select", tools.selTournament, tournsize=3)

    def _avaliacao(self, individuo):
        return random.randint(0, 100),

    def _criar_estatisticas(self):
        stats = tools.Statistics(key=lambda ind: ind.fitness.values)
        stats.register("avg", np.mean)
        stats.register("std", np.std)
        stats.register("min", np.min)
        stats.register("max", np.max)

        return stats

    def _criar_logbook(self, stats):
        return tools.Logbook()

    def _criar_algoritmo_genetico(self, populacao, stats, logbook):
        return algorithms.eaSimple(populacao, self.toolbox, cxpb=self._taxa_crossover, mutpb=self._taxa_mutacao,
                                   ngen=self._numero_geracoes, stats=stats, verbose=True)

    def _criar_grade(self, individuo):
        grade = Grade()
        for i in range(len(individuo)):
            disciplina = self.disciplinas[individuo[i][0]]
            professor = self.professores[individuo[i][1]]
            grade.adicionar_aula(Aula(i, disciplina, professor))
        return grade
