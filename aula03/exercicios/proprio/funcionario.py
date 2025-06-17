class Funcionario:
    def __init__(self, cod, nome, salario):
        self.codigo = cod
        self.nome = nome
        self.__salario = 0.0
        self.historico_aumentos = []

    def get_salario(self):
        return self.__salario
        