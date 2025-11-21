import math
from FiguraGeometrica import FiguraGeometrica

class Triangulo(FiguraGeometrica):
    def __init__(self, nombre):
        super().__init__(nombre)

    def area_triangulo(self, base, altura):
       return (base * altura) / 2