"""Representação de um Endereço por CEP"""

import requests


class CEP:
    """Representa um endereço obtido através do CEP usando a API ViaCEP.

    Atributos:
        cep (str): Código de Endereçamento Postal.
        logradouro (str): Nome da rua/avenida.
        bairro (str): Bairro do endereço.
        cidade (str): Cidade referente ao CEP.
        estado (str): Estado correspondente.
    """

    def __init__(self, cep: str) -> None:
        """Inicializa a classe CEP com base no valor do CEP informado.

        Parâmetros:
            cep (str): O CEP do endereço a ser buscado. Deve ter 8 dígitos numéricos.
        """

        self.cep = cep
        self.logradouro = ''
        self.bairro = ''
        self.cidade = ''
        self.estado = ''

        self.__validar_cep()
        self.__buscar_cep()

    def __buscar_cep(self) -> None:
        """Faz a requisição à API ViaCEP e preenche os atributos com os dados retornados.
        
        Lança:
            ConnectionError: Caso não seja possível conectar à API ViaCEP.
            ValueError: Caso o CEP não seja encontrado.
        """

        url = f'https://viacep.com.br/ws/{self.cep}/json/'
        resposta = requests.get(url, timeout=5)

        if resposta.status_code != 200:
            print('Algo de errado aconteceu')
            raise ConnectionError("Erro ao conectar com a API ViaCEP.")

        dados = resposta.json()

        if 'erro' in dados:
            print('CEP não encontrado')
            raise ValueError("CEP não encontrado. Verifique se o CEP está correto.")

        self.logradouro = dados.get('logradouro', '')
        self.bairro = dados.get('bairro', '')
        self.cidade = dados.get('localidade', '')
        self.estado = dados.get('estado', '')

    def __validar_cep(self) -> None:
        """Verifica se o CEP válido.
        
        O CEP é tido como válido quando ele é uma string, formada apenas
        por números, com exatos 8 caracteres.
        """
        if not isinstance(self.cep, str):
            raise TypeError('O CEP precisa ser uma string.')

        if not self.cep.isnumeric():
            raise ValueError('O CEP deve ser formado apenas por números.')

        if len(self.cep) != 8:
            raise ValueError('O CEP precisa ter exatamente 8 números.')

    def __repr__(self) -> str:
        return f'cep: {self.cep}, '\
            f'logradouro: {self.logradouro}, '\
                f'bairro: {self.bairro}, '\
                f'cidade: {self.cidade}, '\
                f'estado: {self.estado}'


if __name__ == '__main__':
    #casa = CEP(50030220)
    #casa = CEP('500302-20')
    #casa = CEP('5003022')
    casa = CEP('50030220')

    print(casa)
