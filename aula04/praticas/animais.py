class Animal:
    def __init__(self, nome, habitat, habito_alimentar):
        self.nome = nome
        self.habitat = habitat
        self.habito_alimentar = habito_alimentar
    
    def mover(self):
        print(f'O {self.nome} está se movendo')

class Cachorro(Animal):
    def latir(self):
        print('Au au!')

class Cobra(Animal):
    def picar(self):
        print('Inheco')
    
    def mover(self):
        super().mover()
        print(f'{self.nome} está rastejando')

caramelo = Cachorro('triago', 'domestico', 'carnívoro')

print(caramelo.nome, caramelo.habitat, caramelo.habito_alimentar)
caramelo.mover()
caramelo.latir()

celeste = Cobra('Celeste', 'domestica', 'carnívoro')

celeste.mover()
celeste.picar()
