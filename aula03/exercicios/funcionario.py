class Funcionario:
    def __init__(self, cod,nome, salario):
        self.cod = cod
        self.nome = nome
        self.__salario = salario

        def aumentar_salario(self, percentual):
        self.salario += self.salario * (percentual / 100)