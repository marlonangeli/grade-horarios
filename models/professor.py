from . import dataclass, field
from .disciplina import Disciplina


@dataclass
class Professor:
    nome: str
    disciplinas: list[Disciplina] = field(default_factory=list)

    @property
    def carga_horaria(self):
        return sum(disciplina.carga_horaria for disciplina in self.disciplinas)

    def __hash__(self):
        return hash(self.nome)

    def __eq__(self, other):
        return self.nome == other.nome
