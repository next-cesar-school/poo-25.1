from abc import ABC, abstractmethod


class Forma(ABC):
    @abstractmethod
    def calcular_area(self):
        pass

class Retangulo(Forma):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def calcular_area(self):
        return self.largura * self.altura

class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio

    def calcular_area(self):
        from math import pi
        return pi * self.raio ** 2

# Lista de formas
formas = [Retangulo(5, 10), Circulo(7), Retangulo(10, 10), Circulo(20)]

for forma in formas:
    print(f"Área: {forma.calcular_area():.2f}")
