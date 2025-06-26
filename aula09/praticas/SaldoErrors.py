class SaldoInsuficienteError(Exception):
    def __init__(self, saldo: float, valor: float):
        super().__init__(f'Saldo Insuficiente. Saldo: {saldo}. Valor: {valor}')
