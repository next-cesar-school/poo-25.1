# Classe Base
class Veiculo:
    def deslocar(self):
        print("O veículo está se deslocando")

# Classe Carro
class Carro(Veiculo):
    def deslocar(self):
        print("O carro está dirigindo na estrada")

# Classe Barco
class Barco(Veiculo):
    def deslocar(self):
        print("O barco está navegando na água")

# Classe Avião
class Aviao(Veiculo):
    def deslocar(self):
        print("O avião está voando no céu")

# Bloco Principal
if __name__ == "__main__":
    # Criando a lista de veículos
    veiculos = [Carro(), Barco(), Aviao()]

    # Iterando sobre a lista e chamando o método deslocar()
    for veiculo in veiculos:
        veiculo.deslocar()
