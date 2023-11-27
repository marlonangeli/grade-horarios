from deap import tools, algorithms

from constants import regras
from models.dia_da_semana import DiaDaSemana
from models.disciplina import Disciplina
from models.grade import Grade
from models.horario import Horario
from models.professor import Professor
from . import AlgoritmoGenetico
from . import random
from . import time


class Elitismo(AlgoritmoGenetico):
    def __init__(self, disciplinas: list[Disciplina], professores: list[Professor], tamanho_populacao: int,
                 numero_geracoes: int, taxa_crossover: float, taxa_mutacao: float):
        super().__init__(disciplinas, professores, tamanho_populacao, numero_geracoes, taxa_crossover, taxa_mutacao)
        self._criar_operacoes_geneticas()
        self._melhor_individuo = None
        self._melhor_fitness = None
        self._melhor_geracao = None
        self._melhor_tempo = None
        self._melhor_logbook = None

    def executar(self):
        populacao = self._criar_populacao()
        stats = self._criar_estatisticas()
        logbook = self._criar_logbook(stats)

        tempo_inicial = time.time()
        populacao, logbook = self._criar_algoritmo_genetico(populacao, stats, logbook)
        tempo_final = time.time()

        self._melhor_individuo = tools.selBest(populacao, 1)[0]

        # ordena as aulas por horário
        self._melhor_individuo.sort(key=lambda aula: aula.horarios)

        self._melhor_fitness = self._melhor_individuo.fitness.values[0]
        self._tempo = tempo_final - tempo_inicial
        self._logbook = logbook

        return {
            'melhor_individuo': self._melhor_individuo,
            'melhor_fitness': self._melhor_fitness,
            'tempo': self._tempo,
            'estatisticas': self._logbook
        }

    def _crossover_aulas(self, ind1, ind2):
        # Escolhe um ponto de crossover
        crossover_point = random.randint(1, min(len(ind1), len(ind2)) - 1)

        # Realiza o crossover de ponto único
        ind1[crossover_point:], ind2[crossover_point:] = ind2[crossover_point:], ind1[crossover_point:]

        return ind1, ind2

    def _mutacao_aulas(self, individuo, indpb):
        # Escolhe um ponto de mutação

        def mutacao(ind1, ind2):
            prob_professor = 0.3
            prob_disciplina = 0.5
            prob_horario = 0.5

            if random.random() < prob_professor:
                ind1.professor, ind2.professor = ind2.professor, ind1.professor

            if random.random() < prob_disciplina:
                ind1.disciplina, ind2.disciplina = ind2.disciplina, ind1.disciplina

            if random.random() < prob_horario:
                ind1.horarios, ind2.horarios = ind2.horarios, ind1.horarios

            return ind1, ind2

        tamanho_individuo = len(individuo)

        for i in range(tamanho_individuo):
            if random.random() < indpb:
                swap_indx = random.randint(0, tamanho_individuo - 2)
                if swap_indx >= i:
                    swap_indx += 1

                individuo[i], individuo[swap_indx] = mutacao(individuo[i], individuo[swap_indx])

        return individuo,

    def _avaliacao(self, individuo):

        # Faz as validações das regras de negócio
        # 1. Um professor não pode dar aula em dois lugares ao mesmo tempo
        # 2. Uma disciplina não pode ter mais que quatro aulas seguidas (carga horária máxima por dia)
        # 3. Uma disciplina não pode ter aula em mais de dois dias da semana
        # 4. Uma disciplina não pode ter aula em mais de dois turnos (periodos diferentes)
        # 5. Um professor não pode dar aula que não seja da sua área de atuação
        # 6. Prioridade para aulas em sequência
        # 7. Toda a carga horária de uma disciplina deve ser cumprida
        # 8. Todos os horários devem ter aulas

        fitness = 1
        pesos = [10, 10, 15, 15, 20, 30, 35, 50]

        # 1
        fitness += self.__professor_nao_da_aula_em_dois_lugares_ao_mesmo_tempo(individuo) * pesos[0]

        # 2
        fitness += self.__disciplina_nao_tem_mais_que_quatro_aulas_seguidas(individuo) * pesos[1]

        # 3
        fitness += self.__disciplina_nao_tem_aula_em_mais_de_dois_dias(individuo) * pesos[2]

        # 4
        fitness += self.__disciplina_nao_tem_aula_em_mais_de_dois_turnos(individuo) * pesos[3]

        # 5
        fitness += self.__professor_nao_da_aula_que_nao_seja_da_sua_area_de_atuacao(individuo) * pesos[4]

        # 6
        fitness += self.__prioridade_para_aulas_em_sequencia(individuo) * pesos[5]

        # 7
        fitness += self.__toda_carga_horaria_de_uma_disciplina_deve_ser_cumprida(individuo) * pesos[6]

        # 8
        fitness += self.__todos_horarios_tem_aulas(individuo) * pesos[7]

        return fitness,

    def _criar_operacoes_geneticas(self):
        print("Criando operações genéticas...")
        self.toolbox.register("evaluate", self._avaliacao)
        self.toolbox.register("mate", self._crossover_aulas)
        self.toolbox.register("mutate", self._mutacao_aulas, indpb=self._taxa_mutacao)
        # self.toolbox.register("select", tools.selTournament, tournsize=10)
        self.toolbox.register("select", tools.selDoubleTournament, fitness_size=10, parsimony_size=1.2, fitness_first=True)

    def _criar_algoritmo_genetico(self, populacao, stats, logbook):
        return algorithms.eaSimple(populacao, self.toolbox, cxpb=self._taxa_crossover, mutpb=self._taxa_mutacao,
                                   ngen=self._numero_geracoes, stats=stats, halloffame=tools.HallOfFame(5),
                                   verbose=True)

        # return algorithms.eaMuPlusLambda(populacao, self.toolbox, mu=self._tamanho_populacao, lambda_=self._tamanho_populacao,
        #                                  cxpb=self._taxa_crossover, mutpb=self._taxa_mutacao,
        #                                  ngen=self._numero_geracoes, stats=stats, halloffame=tools.HallOfFame(5),
        #                                  verbose=True)

        # return algorithms.eaMuCommaLambda(populacao, self.toolbox, mu=self._tamanho_populacao, lambda_=self._tamanho_populacao,
        #                                   cxpb=self._taxa_crossover, mutpb=self._taxa_mutacao,
        #                                   ngen=self._numero_geracoes, stats=stats, halloffame=tools.HallOfFame(5),
        #                                   verbose=True)

    def __professor_nao_da_aula_em_dois_lugares_ao_mesmo_tempo(self, individuo):
        # 1. Um professor não pode dar aula em dois lugares ao mesmo tempo

        quantidade_validos = 0

        try:
            for i, aula in enumerate(individuo):
                for j, outra_aula in enumerate(individuo):
                    if not (i == j or not (
                            aula.horarios[0] == outra_aula.horarios[0] and aula.horarios[1] == outra_aula.horarios[1])
                            or aula.professor != outra_aula.professor):
                        quantidade_validos -= 1
                quantidade_validos += 1
        except Exception as e:
            print(e)

        return quantidade_validos

    def __disciplina_nao_tem_mais_que_quatro_aulas_seguidas(self, individuo):
        # 2. Uma disciplina não pode ter mais que quatro aulas seguidas (carga horária máxima por dia)

        quantidade_validos = 0

        try:
            # Ordena as aulas por horário
            aulas_ordenadas = sorted(individuo, key=lambda aula: aula.horarios)

            # Dicionário para rastrear a quantidade de aulas consecutivas para cada disciplina
            aulas_consecutivas_por_disciplina = {}

            # Percorre as aulas ordenadas
            for i, aula in enumerate(aulas_ordenadas):
                disciplina = aula.disciplina

                # Inicializa a contagem para a disciplina se ainda não estiver no dicionário
                if disciplina not in aulas_consecutivas_por_disciplina:
                    aulas_consecutivas_por_disciplina[disciplina] = 1
                else:
                    # Se a aula for consecutiva à anterior, incrementa a contagem
                    disciplina_anterior = aulas_ordenadas[i - 1].disciplina

                    if disciplina == disciplina_anterior:
                        aulas_consecutivas_por_disciplina[disciplina] += 1
                    else:
                        aulas_consecutivas_por_disciplina[disciplina] = 1

                # Verifica se a disciplina tem mais de quatro aulas consecutivas
                if aulas_consecutivas_por_disciplina[disciplina] > regras.CARGA_HORARIA_MAXIMA_DISCIPLINA_POR_DIA:
                    quantidade_validos -= 1

                quantidade_validos += 1
        except Exception as e:
            print(e)

        return quantidade_validos

    def __disciplina_nao_tem_aula_em_mais_de_dois_dias(self, individuo):
        # 3. Uma disciplina não pode ter aula em mais de dois dias da semana

        quantidade_validos = 0

        # Ordena as aulas por horário
        aulas_ordenadas = sorted(individuo, key=lambda aula: aula.horarios)

        # Dicionário para rastrear a quantidade de dias que a disciplina tem aula
        dias_por_disciplina = {}

        # Percorre as aulas ordenadas
        for i, aula in enumerate(aulas_ordenadas):
            disciplina = aula.disciplina

            # Inicializa a contagem para a disciplina se ainda não estiver no dicionário
            if disciplina not in dias_por_disciplina:
                dias_por_disciplina[disciplina] = 1
            else:
                # Se a aula for em um dia diferente da anterior, incrementa a contagem
                horarios_anteriores = Grade.encontrar_disciplina(disciplina, aulas_ordenadas[:i])

                # Faz a contagem de dias diferentes
                dias_anteriores = set([horario.horarios[0] for horario in horarios_anteriores])
                if aula.horarios[0] not in dias_anteriores:
                    dias_anteriores.add(aula.horarios[0])
                    dias_por_disciplina[disciplina] = len(dias_anteriores)

            # Verifica se a disciplina tem aula em mais de dois dias
            if dias_por_disciplina[disciplina] > regras.MAXIMO_DIAS_DE_DISCIPLINA_POR_SEMANA:
                quantidade_validos -= 1

            quantidade_validos += 1

        return quantidade_validos

    def __disciplina_nao_tem_aula_em_mais_de_dois_turnos(self, individuo):
        # 4. Uma disciplina não pode ter aula em mais de dois turnos (periodos diferentes)

        quantidade_validos = 0

        # Ordena as aulas por horário
        aulas_ordenadas = sorted(individuo, key=lambda aula: aula.horarios)

        # Dicionário para rastrear a quantidade de turnos que a disciplina tem aula
        turnos_por_disciplina = {}

        # Percorre as aulas ordenadas
        for i, aula in enumerate(aulas_ordenadas):
            disciplina = aula.disciplina

            # Inicializa a contagem para a disciplina se ainda não estiver no dicionário
            if disciplina not in turnos_por_disciplina:
                turnos_por_disciplina[disciplina] = 1
            else:
                # Se a aula for em um turno diferente da anterior, incrementa a contagem
                horarios_anteriores = Grade.encontrar_disciplina(disciplina, aulas_ordenadas[:i])

                # Faz a contagem de turnos diferentes
                turnos_anteriores = set([Horario.get_turno(horario.horarios[1]) for horario in horarios_anteriores])
                if aula.horarios[1][0] not in turnos_anteriores:
                    turnos_anteriores.add(aula.horarios[1])
                    turnos_por_disciplina[disciplina] = len(turnos_anteriores)

            # Verifica se a disciplina tem aula em mais de dois turnos
            if turnos_por_disciplina[disciplina] > 1:
                quantidade_validos -= 1

            quantidade_validos += 1

        return quantidade_validos

    def __professor_nao_da_aula_que_nao_seja_da_sua_area_de_atuacao(self, individuo):
        # 5. Um professor não pode dar aula que não seja da sua área de atuação

        quantidade_validos = 0

        for i, aula in enumerate(individuo):
            professor = aula.professor
            disciplina = aula.disciplina
            if disciplina not in professor.disciplinas:
                quantidade_validos -= 1
            quantidade_validos += 1

        return quantidade_validos

    def __prioridade_para_aulas_em_sequencia(self, individuo):
        # 6. Toda a carga horária de uma disciplina deve ser cumprida

        quantidade_validos = 0

        # Ordena as aulas por horário
        aulas_ordenadas = sorted(individuo, key=lambda aula: aula.horarios)

        # Dicionário para rastrear a quantidade de aulas por disciplina
        aulas_em_sequencia_por_disciplina = {}

        # Percorre as aulas ordenadas e separa sequencia por dia
        for i, aula in enumerate(aulas_ordenadas):
            disciplina = aula.disciplina
            dia = aula.horarios[0]

            # Inicializa a contagem para a disciplina se ainda não estiver no dicionário
            if disciplina not in aulas_em_sequencia_por_disciplina:
                aulas_em_sequencia_por_disciplina[disciplina] = {dia: 1}
            else:
                if dia not in aulas_em_sequencia_por_disciplina[disciplina]:
                    aulas_em_sequencia_por_disciplina[disciplina][dia] = 1
                else:
                    aulas_em_sequencia_por_disciplina[disciplina][dia] += 1

        # soma as aulas com a sequencia maior que 1
        for disciplina in aulas_em_sequencia_por_disciplina:
            for dia in aulas_em_sequencia_por_disciplina[disciplina]:
                if aulas_em_sequencia_por_disciplina[disciplina][dia] > 1:
                    quantidade_validos -= 1
                quantidade_validos += 1

        return quantidade_validos





    def __toda_carga_horaria_de_uma_disciplina_deve_ser_cumprida(self, individuo):
        # 7. Toda a carga horária de uma disciplina deve ser cumprida

        quantidade_validos = 0

        # Ordena as aulas por horário
        aulas_ordenadas = sorted(individuo, key=lambda aula: aula.horarios)

        # Dicionário para rastrear a quantidade de aulas por disciplina
        aulas_por_disciplina = {}

        # Percorre as aulas ordenadas
        for i, aula in enumerate(aulas_ordenadas):
            disciplina = aula.disciplina

            # Inicializa a contagem para a disciplina se ainda não estiver no dicionário
            if disciplina not in aulas_por_disciplina:
                aulas_por_disciplina[disciplina] = 1
            else:
                aulas_por_disciplina[disciplina] += 1

        for disciplina in aulas_por_disciplina:
            # Verifica se a disciplina tem mais de quatro aulas consecutivas
            if aulas_por_disciplina[disciplina] != disciplina.carga_horaria:
                quantidade_validos -= 1

            quantidade_validos += 1

        return quantidade_validos

    def __todos_horarios_tem_aulas(self, individuo):
        # 8. Todos os horários devem ter aulas

        quantidade_validos = 0

        # Ordena as aulas por horário
        aulas_ordenadas = sorted(individuo, key=lambda aula: aula.horarios)

        for horario in Horario.HORARIO_AULAS:
            for dia in DiaDaSemana:
                for aula in aulas_ordenadas:
                    if aula.horarios[0] == dia and aula.horarios[1] == horario:
                        quantidade_validos += 1
                        break
                else:
                    quantidade_validos -= 1

        return quantidade_validos

