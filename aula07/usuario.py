class Usuario:
    nome: str
    idade: int | None  # A idade pode ser int ou None

    def __init__(self, nome: str, idade: int = None) -> None:
        self.nome = nome
        self.idade = idade

    def atualizar_idade(self, nova_idade: int) -> None:
        self.idade = nova_idade

    def saudacao(self) -> str:
        saida = f"Olá, meu nome é {self.nome}"
        saida += f' e minha idade é {self.idade} anos.' if self.idade else '.'

        return saida

joao = Usuario("João da Silva")
