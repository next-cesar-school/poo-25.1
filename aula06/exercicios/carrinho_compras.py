class CarrinhoDeCompras:
    def __init__(self):
        # Armazena os produtos e suas quantidades
        self.itens = {}

    def __getitem__(self, produto):
        # Retorna a quantidade do produto ou 0 se não estiver no carrinho
        return self.itens.get(produto, 0)

    def __setitem__(self, produto, quantidade):
        if quantidade < 0:
            print("A quantidade não pode ser negativa. Valor ignorado.")
        else:
            self.itens[produto] = quantidade

    def __str__(self):
        # Representação dos itens no carrinho
        if not self.itens:
            return "O carrinho está vazio."
        return "\n".join(f"{produto}: {quantidade}" for produto, quantidade in self.itens.items())

# Testando a classe CarrinhoDeCompras
if __name__ == "__main__":
    carrinho = CarrinhoDeCompras()

    # Adicionando produtos ao carrinho
    carrinho["Camiseta"] = 2
    carrinho["Calça"] = 1
    carrinho["Tênis"] = 3

    # Exibindo o carrinho
    print("Carrinho de Compras:")
    print(carrinho)

    # Acessando a quantidade de um produto
    print("\nQuantidade de Camisetas:", carrinho["Camiseta"])  # Output: 2

    # Tentativa de adicionar uma quantidade negativa
    carrinho["Camiseta"] = -1  # Output: A quantidade não pode ser negativa. Valor ignorado.

    # Atualizando a quantidade de um produto
    carrinho["Camiseta"] = 5
    print("\nCarrinho atualizado:")
    print(carrinho)

    # Acessando um produto inexistente
    print("\nQuantidade de Meias:", carrinho["Meias"])  # Output: 0
