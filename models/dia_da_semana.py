from enum import Enum


class DiaDaSemana(Enum):
    SEGUNDA = 1
    TERCA = 2
    QUARTA = 3
    QUINTA = 4
    SEXTA = 5
    SABADO = 6
    DOMINGO = 0  # Não é usado, mas é necessário para o cálculo de horários

    def __str__(self):
        return self.name.title()

    def __repr__(self):
        return f"<DiaSemana.{self.name}>"
