class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def __eq__(self, outro):
        return self.nome == outro.nome and self.preco == outro.preco

    def __repr__(self):
        return f"Produto(nome='{self.nome}', preco={self.preco:.2f})"

# Testando a classe Produto
if __name__ == "__main__":
    produto1 = Produto("Camiseta", 49.90)
    produto2 = Produto("Camiseta", 49.90)
    produto3 = Produto("Calça", 99.90)

    # Comparação de produtos
    print(produto1 == produto2)
    print(produto1 == produto3)

    # Representação dos produtos
    print(produto1)
    print(produto2)
    print(produto3)
