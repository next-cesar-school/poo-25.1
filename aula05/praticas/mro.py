class A:
    def falar(self):
        print("Classe A")
    
    def coisar(self):
        print('Fazendo alguma coisa')

class B(A):
    def falar(self):
        print("Classe B")
        #super().falar()

class C(B):
    ...

# Teste
b = B()
b.falar()
b.coisar()
print(B.__mro__)  # Exibe a ordem de resolução

c = C()
c.falar()
c.coisar()
print(C.__mro__)