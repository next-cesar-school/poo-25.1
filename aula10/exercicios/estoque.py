"""Implementa a classe Estoque, que representa um produto no estoque."""

class Estoque:
    """Classe que representa o controle de estoque de um produto.

    A classe permite a gestão da quantidade de produtos disponíveis,
    oferecendo métodos para vender, repor e garantir que o estoque
    não fique negativo.
    """

    def __init__(self, produto: str, quantidade: int = 0) -> None:
        """Inicializa o estoque com o produto e sua quantidade inicial.

        Args:
            produto (str): O nome do produto.
            quantidade (int): A quantidade inicial do produto no estoque. O padrão é 0.
        """

        self.produto = produto
        self.__quantidade = quantidade

    @property
    def quantidade(self):
        """Retorna a quantidade atual em estoque.

        Returns:
            int: Quantidade atual do produto em estoque.
        """
        return self.__quantidade

    @quantidade.setter
    def quantidade(self, nova_quantidade: int) -> None:
        """Define uma nova quantidade para o estoque.
        
        Garante que a quantidade não seja negativa. Se um valor negativo
        for passado, uma exceção será levantada.

        Args:
            nova_quantidade (int): Nova quantidade do produto.

        Raises:
            ValueError: Se a nova quantidade for menor que zero.
        """

        if nova_quantidade < 0:
            raise ValueError('Erro: O estoque não pode ser negativo.')

        self.__quantidade = nova_quantidade

    def vender(self, quantidade_vendida: int) -> None:
        """Diminui o estoque com base na quantidade vendida.

        Se a venda resultar em um valor negativo, uma exceção será levantada.

        Args:
            quantidade_vendida (int): A quantidade de produtos vendidos.
        
        Raises:
            ValueError: Se a venda deixar o estoque negativo.
        """

        self.quantidade -= quantidade_vendida

    def repor(self, quantidade_reposta: int) -> None:
        """Aumenta o estoque com base na quantidade de produtos repostos.

        Args:
            quantidade_reposta (int): A quantidade de produtos a serem adicionados ao estoque.
        """
        self.quantidade += quantidade_reposta


if __name__ == "__main__":
    estoque = Estoque("Camiseta", 50)
    estoque.vender(20)
    print(estoque.quantidade)  # Saída: 30

    estoque.vender(40)  # Erro: Estoque não pode ser negativo
    print(estoque.quantidade)  # Saída: 30

    estoque.repor(25)
    print(estoque.quantidade)  # Saída: 55
