from math import pi
from formageometrica import FormaGeometrica


class Circulo(FormaGeometrica):
    def __init__(self, raio):
        if raio <= 0:
            raise ValueError("O raio deve ser um valor positivo.")
        self.raio = raio

    def calcular_area(self):
        return pi * (self.raio ** 2)

    def calcular_perimetro(self):
        return 2 * pi * self.raio

    def exibir_dados(self):
        return f"Círculo - Raio: {self.raio}"
