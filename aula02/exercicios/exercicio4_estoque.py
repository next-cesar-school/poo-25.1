class Produto:
    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque

    def adicionar_estoque(self, quantidade):
        self.estoque += quantidade

    def remover_estoque(self, quantidade):
        if self.estoque >= quantidade:
            self.estoque -= quantidade
        else:
            print('Estoque insuficiente para remover essa quantidade.')

    def exibir_produto(self):
        print(f'Produto: {self.nome}')
        print(f'Preço: R${self.preco:.2f}')
        print(f'Estoque: {self.estoque}')


# Criando alguns objetos de teste
caneta = Produto('Caneta', 1.50, 100)
caderno = Produto('Caderno', 10.00, 50)
borracha = Produto('Borracha', 0.50, 10)

# Testando os métodos do produto caneta
caneta.exibir_produto()
caneta.adicionar_estoque(50)
caneta.exibir_produto()
caneta.remover_estoque(20)
caneta.exibir_produto()
caneta.remover_estoque(200)
caneta.exibir_produto()

print('*'*20)

# Testando os métodos do produto caderno
caderno.exibir_produto()
caderno.adicionar_estoque(20)
caderno.exibir_produto()
caderno.remover_estoque(70)
caderno.exibir_produto()
caderno.remover_estoque(1)
caderno.exibir_produto()

print('*'*20)

# Testando os métodos do produto borracha
borracha.exibir_produto()
borracha.adicionar_estoque(5)
borracha.exibir_produto()
borracha.remover_estoque(10)
borracha.exibir_produto()
borracha.remover_estoque(10)
borracha.exibir_produto()
