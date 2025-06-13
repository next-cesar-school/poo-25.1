from veiculocommotor import VeiculoComMotor
from veiculosemmotor import VeiculoSemMotor
from carro import Carro


if __name__ == "__main__":
    # Criando um VeiculoSemMotor
    bicicleta = VeiculoSemMotor("Caloi", "Bike X", "pedais")
    bicicleta.movimentar()

    # Criando um VeiculoComMotor
    moto = VeiculoComMotor("Honda", "CG 160", "gasolina")
    moto.movimentar()

    # Criando um Carro
    carro = Carro("Fiat", "Uno", "gasolina", 4)
    carro.movimentar()
    print("\nDetalhes do carro:")
    carro.detalhes()
