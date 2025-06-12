class ContaBancaria:
    def __init__(self, titular, saldo_inicial):
        self.titular = titular
        self.__saldo = saldo_inicial  # Atributo privado

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
        else:
            print('Valor inválido para depósito.')

    def sacar(self, valor):
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor
        else:
            print('Saldo insuficiente ou valor inválido.')

    def exibir_saldo(self):
        return f'Saldo atual: R${self.__saldo:.2f}'

if __name__ == '__main__':
    # Uso
    conta = ContaBancaria('João', 500)
    conta.depositar(200)
    print(conta.exibir_saldo()) # Output: Saldo atual: R$700.00
    conta.__saldo = 1000        # Não afeta o saldo real, pois é privado.
    print(conta.exibir_saldo()) # Output: Saldo atual: R$700.00
    conta.sacar(400)
    print(conta.exibir_saldo())
    