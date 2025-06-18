class Coordenada:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        novo_x = self.x + other.x
        novo_y = self.y + other.y
        return Coordenada(novo_x, novo_y)

    def __str__(self):
        return f"({self.x}, {self.y})"

# Testando a classe Coordenada
if __name__ == "__main__":
    c1 = Coordenada(2, 3)
    c2 = Coordenada(4, 5)
    c3 = c1 + c2
    print(c3)
