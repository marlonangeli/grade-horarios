from csv import reader, writer

from models.dia_da_semana import DiaDaSemana
from models.horario import Horario


def exportar_grade_csv(grade, nome_arquivo):
    with open(nome_arquivo, 'w+', encoding='utf-8') as arquivo:
        # utf 8 encode
        escritor = writer(arquivo, delimiter=';', lineterminator='\n', quotechar='"', quoting=1)
        escritor.writerow(['Horário', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo'])

        for horario in Horario.HORARIO_AULAS.keys():
            linha = [horario]
            for dia in DiaDaSemana:
                for aula in grade:
                    if aula.horarios[0] == dia and aula.horarios[1] == horario:
                        linha.append(f'{aula.disciplina.nome} - {aula.professor.nome}')
                        break
                else:
                    linha.append('--')

            escritor.writerow(linha)
