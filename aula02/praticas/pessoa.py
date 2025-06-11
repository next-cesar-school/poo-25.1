class Pessoa():
    def __init__(self, nome):
        self.nome = nome
        self.idade = 0

    def set_idade(self, idade):
        if idade >= 0:
            self.idade = idade

    def get_idade(self):
        return self.idade

lucas = Pessoa('Lucas Alcantara')

print(lucas.nome, lucas.idade)

lucas.set_idade(28)

print(lucas.get_idade())
