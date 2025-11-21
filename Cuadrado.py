import math
from FiguraGeometrica import FiguraGeometrica

class Cuadrado(FiguraGeometrica):
    def __init__(self, nombre):
        super().__init__(nombre)

    def area_cuadrado(self, base, altura):
       return base * altura