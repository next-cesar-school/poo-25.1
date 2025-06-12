class Funcionario:
    def __init__(self, nome, cod, salario_inicial):
        self.nome = nome
        self.cod = cod
        self.__salario = salario_inicial if salario_inicial > 0 else 0
        self.__historico_aumentos = []

    def get_salario(self):
        return self.__salario

    def set_salario(self, novo_salario):
        if novo_salario < 0:
            print("Erro: O salário não pode ser negativo.")
        elif novo_salario < self.__salario:
            print("Erro: O novo salário não pode ser menor que o salário atual.")
        else:
            self.__salario = novo_salario
            print(f"Salário atualizado para R${self.__salario:.2f}")

    def aumentar_salario(self, percentual):
        if percentual <= 0:
            print("Erro: O percentual de aumento deve ser positivo.")
            return

        aumento = self.__salario * (percentual / 100)
        novo_salario = self.__salario + aumento
        self.__salario = novo_salario
        self.__historico_aumentos.append({"percentual": percentual, "novo_salario": novo_salario})
        print(f"Salário aumentado em {percentual}%. Novo salário: R${self.__salario:.2f}")

    def exibir_informacoes(self):
        print(f"Nome: {self.nome}")
        print(f"ID: {self.cod}")
        print(f"Salário Atual: R${self.__salario:.2f}")
        print("Histórico de Aumentos:")
        for aumento in self.__historico_aumentos:
            print(f" - {aumento['percentual']}% -> R${aumento['novo_salario']:.2f}")


if __name__ == '__main__':
    funcionario = Funcionario("João Silva", 101, 3000)
    funcionario.exibir_informacoes()
    funcionario.set_salario(2500)
    funcionario.set_salario(3500)
    funcionario.aumentar_salario(10)
    funcionario.exibir_informacoes()
