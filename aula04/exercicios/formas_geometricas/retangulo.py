from formageometrica import FormaGeometrica


class Retangulo(FormaGeometrica):
    def __init__(self, largura, altura):
        if largura <= 0 or altura <= 0:
            raise ValueError("Largura e altura devem ser valores positivos.")
        self.largura = largura
        self.altura = altura

    def calcular_area(self):
        return self.largura * self.altura

    def calcular_perimetro(self):
        return 2 * (self.largura + self.altura)

    def exibir_dados(self):
        return f"Retângulo - Largura: {self.largura}, Altura: {self.altura}"
