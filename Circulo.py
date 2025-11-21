import math
from FiguraGeometrica import FiguraGeometrica

class Circulo(FiguraGeometrica):
    def __init__(self, nombre):
        super().__init__(nombre)

    def area_circulo(self, radio):
      return math.pi * (radio ** 2)
