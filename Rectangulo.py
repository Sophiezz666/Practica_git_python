import math
from FiguraGeometrica import FiguraGeometrica

class Rectangulo(FiguraGeometrica):
    def __init__(self, nombre):
        super().__init__(nombre)

    def area_ractangulo(self, base, altura):
        return base * altura
