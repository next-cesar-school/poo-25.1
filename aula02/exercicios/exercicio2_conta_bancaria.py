class ContaBancaria:
    def __init__(self, titular, saldo=0.0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
        else:
            print('Saldo insuficiente.')

    def exibir_saldo(self):
        print(f'Saldo atual de {self.titular}: R${self.saldo:.2f}')


# Criando duas instâncias da classe ContaBancaria
conta_maria = ContaBancaria('Maria', 1000.00)
conta_joao = ContaBancaria('João', 200.00)

# Testando os métodos na conta_maria
conta_maria.exibir_saldo()
conta_maria.depositar(500.00)
conta_maria.exibir_saldo()
conta_maria.sacar(200.00)
conta_maria.exibir_saldo()
conta_maria.sacar(2000.00)
conta_maria.exibir_saldo()

print('*'*20)

# Testando os métodos na conta_joao
conta_joao.exibir_saldo()
conta_joao.depositar(300.00)
conta_joao.exibir_saldo()
conta_joao.sacar(100.00)
conta_joao.exibir_saldo()
conta_joao.sacar(500.00)
conta_joao.exibir_saldo()
