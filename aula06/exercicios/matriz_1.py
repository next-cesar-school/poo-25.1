class Matriz:
    def __init__(self, a, b, c, d):
        self.a = a  # Elemento (1,1)
        self.b = b  # Elemento (1,2)
        self.c = c  # Elemento (2,1)
        self.d = d  # Elemento (2,2)

    def __mul__(self, other):
        # Calcula os elementos da nova matriz
        novo_a = self.a * other.a + self.b * other.c
        novo_b = self.a * other.b + self.b * other.d
        novo_c = self.c * other.a + self.d * other.c
        novo_d = self.c * other.b + self.d * other.d

        # Retorna uma nova matriz com os valores calculados
        return Matriz(novo_a, novo_b, novo_c, novo_d)

    def __str__(self):
        # Representação em formato de matriz 2x2
        return f"[ {self.a}  {self.b} ]\n[ {self.c}  {self.d} ]"

# Testando a classe Matriz
if __name__ == "__main__":
    m1 = Matriz(1, 2, 3, 4)  # Matriz 1
    m2 = Matriz(5, 6, 7, 8)  # Matriz 2

    # Multiplicando as matrizes
    m3 = m1 * m2
    print("Matriz Resultante:")
    print(m3)
