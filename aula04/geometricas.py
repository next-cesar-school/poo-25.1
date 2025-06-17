class FormaGeometrica:
    def calcular_area():
        pass

    def calcular_perimetro():
        pass

class Retangulo(FormaGeometrica):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)
    
class Circulo(FormaGeometrica):
    def __init__(self, raio):
        self.raio = raio

    def calcular_area(self):
        return 3.14 * (self.raio ** 2)

    def calcular_perimetro(self):
        return 2 * 3.14 * self.raio
    

if __name__ == "__main__":
    retangulo = Retangulo(5, 10)
    print(f"Área do retângulo: {retangulo.calcular_area()}")
    print(f"Perímetro do retângulo: {retangulo.calcular_perimetro()}")

    circulo = Circulo(7)
    print(f"Área do círculo: {circulo.calcular_area()}")
    print(f"Perímetro do círculo: {circulo.calcular_perimetro()}")

    quadrado = Retangulo(4, 4)  # Quadrado é um caso especial de retângulo
    print(f"Área do quadrado: {quadrado.calcular_area()}")

    circulo2 = Circulo(10)  # Outro círculo
    print(f"Área do segundo círculo: {circulo2.calcular_area()}")   
    
    