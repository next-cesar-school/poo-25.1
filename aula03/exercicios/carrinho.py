class CarrinhoDeCompras:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, livro):
        for item in self.livros:
            if item.titulo == livro.titulo:
                print(f"Erro: O livro '{livro.titulo}' já está no carrinho.")
                return
        self.livros.append(livro)
        print(f"Livro '{livro.titulo}' adicionado ao carrinho.")

    def remover_livro(self, titulo):
        for livro in self.livros:
            if livro.titulo == titulo:
                self.livros.remove(livro)
                print(f"Livro '{titulo}' removido do carrinho.")
                return
        print(f"Erro: O livro '{titulo}' não está no carrinho.")

    def calcular_total(self):
        total = sum(livro.get_preco() for livro in self.livros)
        return total

    def exibir_itens(self):
        if not self.livros:
            print("O carrinho está vazio.")
        else:
            print("Livros no carrinho:")
            for livro in self.livros:
                print(f" - {livro.exibir_dados()}")
            print(f"Total: R${self.calcular_total():.2f}")
