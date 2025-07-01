"""Classe Calculadora com as quatro operações básicas.

Não é necessário criar uma instância.
"""

class Calculadora:
    """
    Classe que implementa uma calculadora simples com operações básicas.
    """

    @staticmethod
    def soma(a: int | float, b: int | float) -> int | float:
        """Realiza a soma de dois números."""

        return a + b

    @staticmethod
    def subtracao(a: int| float, b: int| float) -> int| float:
        """Realiza a subtração de dois números."""

        return a - b

    @staticmethod
    def multiplicacao(a: int| float, b: int| float) -> int| float:
        """Realiza a multiplicação de dois números."""

        return a * b

    @staticmethod
    def divisao(a: int| float, b: int| float) -> int| float:
        """Realiza a divisão de dois números.
        Levanta um erro se a divisão for por zero.
        """
        if b == 0:
            raise ValueError('Divisão por zero não permitida')

        return a / b
