class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def checar_idade(self, teste_idade):
        if self.idade < 0:
            print('A idade está errada!')

class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo):
        super().__init__(nome, idade)
        self.cargo = cargo
    
    '''def set_cargo(self, cargo):
        self.cargo = cargo'''

#oreo = Funcionario('Oreo', 1, 'desocupado')
#ana = Funcionario('Ana Rita', 33, 'monitora')
erick = Funcionario('Erick Simões', 33, 'Professor')
erick.checar_idade()