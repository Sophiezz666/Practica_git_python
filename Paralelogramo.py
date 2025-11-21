import math
from FiguraGeometrica import FiguraGeometrica

class Paralelogramo(FiguraGeometrica):
    def __init__(self, nombre):
        super().__init__(nombre)

    def area_paralelogramo(self, base, altura):
        return base * altura