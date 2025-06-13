from veiculocommotor import VeiculoComMotor


class Carro(VeiculoComMotor):
    def __init__(self, marca, modelo, combustivel, quantidade_portas):
        super().__init__(marca, modelo, combustivel)
        self.quantidade_portas = quantidade_portas

    def detalhes(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Combustível: {self.combustivel}")
        print(f"Portas: {self.quantidade_portas}")
