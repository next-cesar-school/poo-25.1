"""Representação do Produto."""


class Produto:
    """Classe que representa um produto com nome e preco."""

    def __init__(self, nome: str, preco: float) -> None:
        """Inicializa um produto com nome e preco."""

        self.nome = nome
        self.preco = preco

    def desconto(self, porcentagem: float) -> float:
        """Aplica um desconto ao preço do produto.
        Levanta um erro se a porcentagem for inválida.
        """

        if porcentagem < 0 or porcentagem > 100:
            raise ValueError("A porcentagem deve estar entre 0 e 100")

        return self.preco * (1 - porcentagem / 100)
