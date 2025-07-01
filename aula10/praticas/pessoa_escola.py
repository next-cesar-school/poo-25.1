from abc import ABC, abstractmethod


class Pessoa(ABC):
    def __init__(self, nome: str, cpf:str, telefone: str) -> None:
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone

    @abstractmethod
    def listar_disciplinas(self) -> None:
        ...

class Estudante(Pessoa):
    def listar_disciplinas(self):
        print('Imagine que eu implementei algo aqui para estudante')

class Professor(Pessoa):
    def listar_disciplinas(self):
        print('Imagine que eu implementei algo aqui para professor')

#joao = Pessoa('João da Silva', '123456', '34353637') # Isso vai dar erro
camila = Estudante('Camila Santos', '12345678', '34353435')
jorge = Professor('Jorge Alexandre', '32165487', '43546576')
