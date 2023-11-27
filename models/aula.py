from . import dataclass, field
from .dia_da_semana import DiaDaSemana
from .disciplina import Disciplina
from .horario import Horario
from .professor import Professor


@dataclass
class Aula:
    id: int
    disciplina: Disciplina
    professor: Professor
    horarios: list[tuple[DiaDaSemana, list[str]]] = field(default_factory=list)
