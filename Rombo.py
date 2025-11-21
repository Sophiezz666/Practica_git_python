import math
from FiguraGeometrica import FiguraGeometrica 

class Rombo(FiguraGeometrica):
    def __init__(self, nombre):
        super().__init__(nombre)

    @property
    def D(self) -> float:
        return self._D
    @D.setter
    def D(self, D: float):
        self._D = D
    
    @property
    def d(self) -> float:
        return self._d
    @d.setter
    def d(self,d: float):
        self._d = d
    
    def area_rombo(self, D, d):
        return(D * d) / 2