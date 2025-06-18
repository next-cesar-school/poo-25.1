class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.cadastro_ativo = True
    
    def __str__(self):
        return f'Nome: {self.nome} | idade: {self.idade}'
    
    def __repr__(self):
        return f'Pessoa(nome={self.nome}, idade={self.idade}, cadastro_ativo={self.cadastro_ativo})'
    
    def __len__(self):
        return self.idade

jamilly = Pessoa('Jamilly Silva', 30)
jorge = Pessoa('Jorge Alexandre', 44)

print(jamilly)
print(repr(jamilly))

print(len(jamilly))
#print(jamilly == jorge)