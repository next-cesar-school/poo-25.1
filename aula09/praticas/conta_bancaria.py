#from aula09.praticas.SaldoErrors import SaldoInsuficienteError
from SaldoErrors import SaldoInsuficienteError


class ContaBancaria:
    def __init__(self, titular: str, saldo: float = 0.0) -> None:
        self.titular = titular
        self.__saldo = saldo

    def depositar(self, valor: float) -> None:
        if valor <= 0:
            raise ValueError("O valor do depósito deve ser positivo.")

        self.__saldo += valor

    def sacar(self, valor: float) -> None:
        if valor > self.__saldo:
            raise SaldoInsuficienteError(self.__saldo, valor)

        self.__saldo -= valor

    def exibir_saldo(self) -> None:
        print(f"Saldo atual: R${self.__saldo:.2f}")

try:
    conta = ContaBancaria("João", 500)
    conta.sacar(700)
except SaldoInsuficienteError as e:
    print(e)
