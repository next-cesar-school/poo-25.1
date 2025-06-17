from veiculo import Veiculo


class VeiculoSemMotor(Veiculo):
    def __init__(self, marca, modelo, tipo_propulsao):
        super().__init__(marca, modelo)
        self.tipo_propulsao = tipo_propulsao

    def movimentar(self):
        print(f"A {self.marca} {self.modelo} está se movendo usando {self.tipo_propulsao}.")
