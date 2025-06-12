class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.__preco = 0

    def get_preco(self):
        return self.__preco

    def set_preco(self, preco):
        if preco > 0:
            self.__preco = preco
        else:
            print('O preço não pode ser um valor negativo')

    def exibir_dados(self):
        return f"'{self.titulo}' de {self.autor} - R${self.__preco:.2f}"
