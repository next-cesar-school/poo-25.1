# Classe Base
class Instrumento:
    def tocar(self):
        print("Tocando um instrumento")

# Classe Violão
class Violao(Instrumento):
    def tocar(self):
        print("Tocando violão")

# Classe Piano
class Piano(Instrumento):
    def tocar(self):
        print("Tocando piano")

# Classe Bateria
class Bateria(Instrumento):
    def tocar(self):
        print("Tocando bateria")

# Bloco Principal
if __name__ == "__main__":
    # Criando a lista de instrumentos
    instrumentos = [Violao(), Piano(), Bateria()]

    # Iterando sobre a lista e chamando o método tocar()
    for instrumento in instrumentos:
        instrumento.tocar()
