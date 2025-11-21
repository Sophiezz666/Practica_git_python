import math
from FiguraGeometrica import FiguraGeometrica

class Trapecio(FiguraGeometrica):
    def __init__(self, nombre):
        super().__init__(nombre)

    @property
    def base_mayor(self) -> float:
        return self._base_mayor  
    @base_mayor.setter
    def base_mayor(self, base_mayor: float):
        self._base_mayor = base_mayor

    @property
    def base_menor(self) -> float:
        return self._base_menor
    @base_menor.setter
    def base_menor(self, base_menor: float):
        self._base_menor = base_menor
    
    @property
    def altura(self) -> float:
        return self._altura
    @altura.setter
    def altura(self, altura: float):
        self._altura = altura
    
    def area_trapecio(self, base_mayor, base_menor, altura):
        return (base_mayor + base_menor) * altura / 2
        