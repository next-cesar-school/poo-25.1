class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.__idade = idade
    
    def __fazer_algo_secreto(self):
        self.idade_daqui_5_anos = self.__idade + 5
        ...

nath = Pessoa('Nathália Monteiro', 29)
#nath.__idade = 'algo'
print(nath.__idade)
