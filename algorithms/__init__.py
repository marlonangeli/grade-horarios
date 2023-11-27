import deap
import numpy
import pandas
import random
import time
import copy
import math

from models.disciplina import Disciplina
from models.professor import Professor
from models.horario import Horario
from models.aula import Aula
from models.dia_da_semana import DiaDaSemana
from models.grade import Grade
from .base import AlgoritmoGenetico