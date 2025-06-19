class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def __str__(self):
        return f"Nome: {self.nome} | idade: {self.idade}"
    
    def __len__(self):
        return self.idade
    
    jamilly = Pessoa('Jamilly', 30)