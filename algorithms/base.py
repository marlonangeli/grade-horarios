from deap import base, creator, tools, algorithms
from . import numpy as np
from . import random
from . import Disciplina, Professor, DiaDaSemana, Horario, Aula, Grade


class AlgoritmoGenetico:
    def __init__(self, disciplinas: list[Disciplina], professores: list[Professor], tamanho_populacao: int,
                 numero_geracoes: int, taxa_crossover: float, taxa_mutacao: float):
        self.disciplinas = disciplinas
        self.professores = professores
        self._tamanho_populacao = tamanho_populacao
        self._numero_geracoes = numero_geracoes
        self._taxa_crossover = taxa_crossover
        self._taxa_mutacao = taxa_mutacao
        self.toolbox = base.Toolbox()

        self._criar_estruturas()
        self._criar_estatisticas()

    def _criar_individuo(self):
        grade = Grade()
        horarios_disponiveis = grade.horarios_disponiveis
        while horarios_disponiveis:
            horario = random.choice(horarios_disponiveis)

            disciplina = random.choice(self.disciplinas)
            professores = [professor for professor in self.professores if disciplina in professor.disciplinas]

            if not professores:
                continue

            professor = random.choice(professores)
            aula = Aula(len(grade.aulas), disciplina, professor, horario)
            grade.adicionar_aula(aula)

            horarios_disponiveis.remove(horario)

        self.toolbox.register("individual", tools.initIterate, creator.Individual, grade.aulas)
        # return self.toolbox.individual()
        return creator.Individual(grade.aulas)

    def _criar_populacao(self):
        self.toolbox.register("population", tools.initRepeat, list, self._criar_individuo)
        return self.toolbox.population(n=self._tamanho_populacao)

    def _criar_estruturas(self):
        creator.create("FitnessMax", base.Fitness, weights=(1.0,))
        creator.create("Individual", list, fitness=creator.FitnessMax)

        self._criar_populacao()

    def _criar_estatisticas(self):
        stats = tools.Statistics(key=lambda ind: ind.fitness.values)
        stats.register("avg", np.mean)
        stats.register("std", np.std)
        stats.register("min", np.min)
        stats.register("max", np.max)
        stats.register("size", len)

        return stats

    def _criar_logbook(self, stats):
        logbook = tools.Logbook()
        logbook.header = ["gen", "evals"] + stats.fields
        logbook.chapters["fitness"].header = "min", "avg", "max"
        logbook.chapters["size"].header = "min", "avg", "max"

        return logbook
