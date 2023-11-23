from . import dataclass, field
from .aula import Aula
from .dia_da_semana import DiaDaSemana
from .horario import Horario


@dataclass
class Grade:
    id: int
    aulas: list[Aula] = field(default_factory=list)

    @property
    def horarios_disponiveis(self):
        # Todos os horários disponíveis a partir das classes Horario e DiaDaSemana
        todos_horarios = [
            (dia, horario)
            for dia in DiaDaSemana
            for horario in Horario.HORARIO_AULAS.keys()
        ]

        # Horários disponíveis são todos os horários menos os horários ocupados
        horarios_ocupados = [
            (aula.horarios[0][0], horario)
            for aula in self.aulas
            for horario in aula.horarios[0][1]
        ]

        horarios_disponiveis = list(set(todos_horarios) - set(horarios_ocupados))
        horarios_disponiveis.sort(key=lambda x: (x[0].value, x[1].value))
        return horarios_disponiveis

    def adicionar_aula(self, aula: Aula):
        self.aulas.append(aula)

    def remover_aula(self, aula: Aula):
        self.aulas.remove(aula)
