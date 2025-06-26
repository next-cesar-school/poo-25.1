class SaldoInsuficienteError(Exception):
    def __init__(self, saldo: float, valor: float):
        super().__init__(f'Saldo Insuficiente. Saldo: {saldo}. Valor: {valor}')

###############################################################

def sacar(saldo, valor):
    """Retorna o valor do saldo depois do saque"""

    if valor > saldo:
        raise SaldoInsuficienteError(saldo, valor)

    saldo -= valor
    return saldo

try:
    print(sacar(20, 50))
except SaldoInsuficienteError as e:
    print(f'Não foi possível realizar o saque: {e}')
