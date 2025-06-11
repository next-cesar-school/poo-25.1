class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def exibir_informacoes(self):
        print(f'Título: {self.titulo}, Autor: {self.autor}')

