from . import dataclass


@dataclass
class Disciplina:
    nome: str
    periodo: int
    carga_horaria: int

    def __hash__(self):
        return hash(self.nome)

    def __eq__(self, other):
        return self.nome == other.nome

    def __str__(self):
        return self.nome
