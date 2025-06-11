class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def exibir_informacoes(self):
        print(f'Título: {self.titulo}\nAutor: {self.autor}')


cod_limpo = Livro('Código Limpo', 'Robert C. Martin')
mindset = Livro('Mindset: A nova psicologia dop sucesso', 'Carol S. Dweck')
startup = Livro('A Startup Enxuta', 'Eric Ries')

cod_limpo.exibir_informacoes()
mindset.exibir_informacoes()
startup.exibir_informacoes()
