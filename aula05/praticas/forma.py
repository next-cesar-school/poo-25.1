class Forma:
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
        return 3.14 * self.raio ** 2

class Quadrado(Forma):
    def __init__(self, lado):
        self.lado = lado
    
    def calcular_area(self):
        return self.lado ** 2


# Lista de formas
formas = [Retangulo(5, 10), Circulo(7), Quadrado(10)]

for forma in formas:
    print(f"Área: {forma.calcular_area():.2f}")
