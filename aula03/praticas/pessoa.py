class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.__idade = idade
    
    def definir_idade(self, idade):
        if 0 <= idade <= 130:
            self.__idade = idade
    
    def exibir_idade(self):
        print(self.__idade)

if __name__ == '__main__':
    gean = Pessoa('Gean Carlos', 55)
    nathalia = Pessoa('Nathália Monteiro', 29)
    
    gean.__idade = -200
    gean.exibir_idade()
    gean.definir_idade(56)
    gean.exibir_idade()
