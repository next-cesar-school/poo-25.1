class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def movimentar(self):
        print(f"O veículo {self.marca} {self.modelo} está se movendo.")
