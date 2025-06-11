class ContaBancaria:
    def __init__(self, titular, saldo=0.0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
        print(f'Depósito de R${valor:2.f}')
        print(f'Saldo atual: R${self.saldo:2.f}')
    
    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
        else:
            print(f'Saldo insuficiente')
            print(f'Saldo atual: R${self.saldo:2.f}')

    def exibir_saldo(self):
        print(f'Saldo atual: R${self.saldo:.2f}')
        
while True:
    print("O que você quer fazer?")
    print("1. Depositar")
    print("2. Sacar")  
    print("3. Exibir saldo")
    print("4. Sair")
    opcao = input("Digite o número da opção: ")
    
    if opcao == '1':
        valor = float(input("Digite o valor a ser depositado: "))
        conta1.depositar(valor)
    elif opcao == '2':
        valor = float(input("Digite o valor a ser sacado: "))
        conta1.sacar(valor)
    elif opcao == '3':
        conta1.exibir_saldo()
    elif opcao == '4':
        break
    else:
        print("Opção inválida!")
    # Exibir saldo após as operações
    conta1.exibir_saldo()