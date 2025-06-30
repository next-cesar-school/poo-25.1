"""
Módulo para a classe Produto.
Este módulo define a estrutura de um produto com nome e preço,
e um método para calcular seu preço com desconto.
"""

class Produto:
    """
    Representa um produto com um nome e um preço.

    Atributos:
        nome (str): O nome do produto.
        preco (float): O preço original do produto.
    """

    def __init__(self, nome: str, preco: float):
        """
        Inicializa uma nova instância de Produto.

        Args:
            nome (str): O nome do produto.
            preco (float): O preço original do produto.

        Raises:
            ValueError: Se o preço for negativo.
        """
        if not isinstance(nome, str) or not nome:
            raise ValueError("O nome do produto deve ser uma string não vazia.")
        if not isinstance(preco, (int, float)) or preco < 0:
            raise ValueError("O preço do produto deve ser um número não negativo.")

        self.nome = nome
        self.preco = preco

    def desconto(self, porcentagem: float) -> float:
        """
        Calcula o preço do produto após aplicar um determinado percentual de desconto.

        Args:
            porcentagem (float): O percentual de desconto a ser aplicado (entre 0 e 100).

        Returns:
            float: O preço do produto após o desconto.

        Raises:
            ValueError: Se a porcentagem de desconto não estiver entre 0 e 100.
        """
        if not isinstance(porcentagem, (int, float)):
            raise ValueError("A porcentagem de desconto deve ser um número.")
        if not 0 <= porcentagem <= 100:
            raise ValueError("A porcentagem de desconto deve estar entre 0 e 100.")

        # O cálculo do desconto é: preço * (1 - porcentagem / 100)
        preco_com_desconto = self.preco * (1 - porcentagem / 100)
        return round(preco_com_desconto, 2) # Arredonda para 2 casas decimais para evitar problemas de ponto flutuante
