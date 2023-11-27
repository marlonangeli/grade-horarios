from . import dataclass, field
from .aula import Aula
from .dia_da_semana import DiaDaSemana
from .disciplina import Disciplina
from .horario import Horario


@dataclass
class Grade:
    aulas: list[Aula] = field(default_factory=list)

    @property
    def horarios_disponiveis(self):
        # Todos os horários disponíveis a partir das classes Horario e DiaDaSemana, exceto sábados e domingos
        todos_horarios = [
            (dia, horario)
            for dia in DiaDaSemana
            for horario in Horario.HORARIO_AULAS
            if dia != DiaDaSemana.SABADO and dia != DiaDaSemana.DOMINGO
        ]

        # Horários disponíveis são todos os horários menos os horários ocupados
        horarios_ocupados = [
            (aula.horarios[0], aula.horarios[1])
            for aula in self.aulas
        ]

        horarios_disponiveis = list(set(todos_horarios) - set(horarios_ocupados))

        return horarios_disponiveis

    def adicionar_aula(self, aula: Aula):
        self.aulas.append(aula)

    def remover_aula(self, aula: Aula):
        self.aulas.remove(aula)

    @staticmethod
    def encontrar_disciplina(disciplina: Disciplina, aulas: list[Aula]):
        return [aula for aula in aulas if aula.disciplina == disciplina]
