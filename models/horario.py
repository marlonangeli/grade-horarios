from datetime import datetime


class Horario:
    def __init__(self):
        self.horario_aulas = {
            'M1': ('07h30', '08h20'),
            'M2': ('08h20', '09h10'),
            'M3': ('09h10', '10h00'),
            'M4': ('10h20', '11h10'),
            'M5': ('11h10', '12h00'),
            'M6': ('12h00', '12h50'),
            'T1': ('13h00', '13h50'),
            'T2': ('13h50', '14h40'),
            'T3': ('14h40', '15h30'),
            'T4': ('15h50', '16h40'),
            'T5': ('16h40', '17h30'),
            'T6': ('17h50', '18h40')
        }

    def get_horario_aula(self, codigo):
        return self.horario_aulas.get(codigo)

    @staticmethod
    def converter_para_datetime(hora_str):
        return datetime.strptime(hora_str, '%Hh%M')

    def get_horario_aulas_datetime(self):
        return {key: (self.converter_para_datetime(inicio), self.converter_para_datetime(fim))
                for key, (inicio, fim) in self.horario_aulas.items()}
