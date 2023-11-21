from . import dataclass, field
from .disciplina import Disciplina


@dataclass
class Professor:
    nome: str
    disciplinas: list[Disciplina] = field(default_factory=list)

    @property
    def carga_horaria(self):
        return sum(disciplina.carga_horaria for disciplina in self.disciplinas)
