class Pessoa:
    def falar(self):
        print('Sou uma pessoa')

class Humano:
    def falar(self):
        print('Sou um ser humano')

class Estudande(Humano, Pessoa):
    ...

joao = Estudande()
joao.falar()
print(Estudande.__mro__)