from . import dataclass, field
from .dia_da_semana import DiaDaSemana
from .disciplina import Disciplina
from .horario import Horario
from .professor import Professor


@dataclass
class Grade:
    id: int
    disciplina: Disciplina
    professor: Professor
    dia_semana: list[DiaDaSemana] = field(default_factory=list)
    horario: list[Horario] = field(default_factory=list)
