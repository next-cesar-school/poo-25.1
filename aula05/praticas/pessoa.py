class Pessoa:
    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
    
    def quem_sou(self):
        print(f'Meu nome é {self.nome} e eu tenho {self.idade} anos.')
    
pessoas = []

pessoas.append(Pessoa('João da Silva', 12, '12345678'))
pessoas.append(Pessoa('Marcos dos Santos', 20, '87654321'))

pessoas[0].quem_sou()
pessoas[1].quem_sou()
#pessoas[1].upper()

print(type(pessoas))
print(type(pessoas[0]))
print(type(pessoas[0].nome))
print(type(pessoas[0].idade))

print(pessoas[0].nome.upper())

'''
nomes = []

nomes.append('banana')
nomes.append('maça')
nomes.append('uva')
nomes.append('graviola')

print(nomes[0].replace('a', '@'))'''