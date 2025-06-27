from datetime import datetime

class Pessoa:
    def __init__(self, nome: str, ano_nascimento: int):
        self.nome = nome
        self.ano_nascimento = ano_nascimento

    @property
    def idade(self) -> int:
        ano_atual: int = datetime.now().year
        return ano_atual - self.__ano_nascimento

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, novo_nome) -> None:
        if len(novo_nome) < 3:
            raise ValueError('O nome precisa ter 3 ou mais caracteres!')

        if novo_nome[0] != novo_nome[0].upper():
            raise ValueError('O nome precisa começar com a primeria leta em maiusculo!')

        self.__nome = novo_nome

    @property
    def ano_nascimento(self) -> int:
        return self.__ano_nascimento

    @ano_nascimento.setter
    def ano_nascimento(self, novo_ano: int) -> None:
        if novo_ano < 0 or novo_ano > datetime.now().year:
            raise ValueError(f'O valor {novo_ano} precisa estar entre zero e o ano atual.')

        if novo_ano == 2005:
            raise ArithmeticError('Não gosto de quem nasce no ano de 2005')

        self.__ano_nascimento = novo_ano


if __name__ == '__main__':
    pessoa1 = Pessoa('Alberto', 1993)
    pessoa2 = Pessoa('Triago', 2003)
    pessoa3 = Pessoa('Cassio', 1990)
    pessoa4 = Pessoa('Da', 1990)
    #print(pessoa3.idade)
    #pessoa3.ano_nascimento = -500

    pessoa1.ano_nascimento = 1990
    #pessoa2.ano_nascimento = -12

    print(pessoa1.idade)
    print(pessoa2.idade)
    print(pessoa3.idade)
