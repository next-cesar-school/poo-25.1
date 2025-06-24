#from projeto_endereco.cep.cep import CEP
from cep.cep import CEP


class Endereco(CEP):
    """Classe que representa um endereço, herdando da classe CEP.
    
    Atributos:
        cep (str): CEP do endereço.
        numero (int): Número do endereço.
        complemento (str, opcional): Complemento do endereço.
    """

    def __init__(self, cep: str, numero: int, complemento: str = ''):
        super().__init__(cep)

        self.numero = numero
        self.complemento = complemento

    @property
    def numero(self) -> int:
        """Retorna o número do endereço."""
        return self.__numero

    @numero.setter
    def numero(self, numero: int) -> None:

        if numero <= 0:
            raise ValueError("Número do endereço deve ser maior que zero")

        self.__numero = numero

    @property
    def complemento(self) -> str:
        """Retorna o complemento do endereço."""
        return self._complemento

    @complemento.setter
    def complemento(self, valor: str) -> None:
        self._complemento = valor

    def __str__(self) -> str:
        return f'{super().__str__()}, Nº: {self.numero}{', complemento: ' + self.complemento if self.complemento else ''}'


if __name__ == '__main__':
    apolo = Endereco('50030220', 463)

    print(apolo)
