class Matriz:
    def __init__(self, a, b, c, d):
        self.valores = [[a, b], [c, d]]

    def __mul__(self, other):
        # Calcula os elementos da nova matriz
        novo_a = self.valores[0][0] * other.valores[0][0] + self.valores[0][1] * other.valores[1][0]
        novo_b = self.valores[0][0] * other.valores[0][1] + self.valores[0][1] * other.valores[1][1]
        novo_c = self.valores[1][0] * other.valores[0][0] + self.valores[1][1] * other.valores[1][0]
        novo_d = self.valores[1][0] * other.valores[0][1] + self.valores[1][1] * other.valores[1][1]
        
        # Retorna uma nova matriz com os valores calculados
        return Matriz(novo_a, novo_b, novo_c, novo_d)

    def __str__(self):
        # Representação em formato de matriz 2x2
        return f"[ {self.valores[0][0]}  {self.valores[0][1]} ]\n[ {self.valores[1][0]}  {self.valores[1][1]} ]"

# Testando a classe Matriz
if __name__ == "__main__":
    m1 = Matriz(1, 2, 3, 4)  # Matriz 1
    m2 = Matriz(5, 6, 7, 8)  # Matriz 2

    # Multiplicando as matrizes
    m3 = m1 * m2
    print("Matriz Resultante:")
    print(m3)
