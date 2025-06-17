from veiculo import Veiculo


class VeiculoComMotor(Veiculo):
    def __init__(self, marca, modelo, combustivel):
        super().__init__(marca, modelo)
        self.combustivel = combustivel

    def movimentar(self):
        print(f"O {self.marca} {self.modelo} está se movendo com combustível {self.combustivel}.")
