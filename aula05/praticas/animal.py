class Animal:
    def emitir_som(self):
        print("Som de um animal.")

class Cachorro(Animal):
    def emitir_som(self):
        print("Au au!")

class Gato(Animal):
    def emitir_som(self):
        print("Miau!")

class Raposa(Animal):
    ...

class Cobra(Animal):
    def emitir_som(self):
        print('Siiiisiiisiiisiiii')

# Polimorfismo
def fazer_animal_emitir_som(animal):
    animal.emitir_som()

# Teste
animais = [Cachorro(), Gato(), Animal(), Raposa(), Cobra()]

for bicho in animais:
    fazer_animal_emitir_som(bicho)
