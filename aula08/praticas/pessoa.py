"""Módulo Pessoa do Sistemas de Cadastro"""


class Pessoa:
    """Representa uma pessoa no sistema.

    Atributos:
        nome (str): Nome completo da pessoa.
        idade (int): Idade da pessoa.

    Métodos:
        saudacao(): Retorna uma saudação com o nome da pessoa.
    """

    def __init__(self, nome: str, idade: int) -> None:
        """Inicializa uma nova instância da classe Pessoa.

        Parâmetros:
            nome (str): O nome da pessoa.
            idade (int): A idade da pessoa.
        """
        self.nome = nome
        self.idade = idade

    def saudacao(self) -> str:
        """Retorna uma saudação personalizada com o nome da pessoa.

        Retorna:
            str: Mensagem de saudação.
        """
        return f"Olá, meu nome é {self.nome}."

if __name__ == '__main__':
    joao = Pessoa("João da Silva", 34)
    print(joao.saudacao())
