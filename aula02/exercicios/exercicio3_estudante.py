class Estudante:
    def __init__(self, nome, nota1, nota2):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2

    def media(self):
        return (self.nota1 + self.nota2) / 2

    def situacao(self):
        if self.media() >= 7.0:
            print(f'{self.nome} está Aprovado(a)!')
        else:
            print(f'{self.nome} está Reprovado(a).')


# Criando alguns objetos de teste
aluno1 = Estudante('Maria', 8.0, 9.5)
aluno2 = Estudante('João', 6.0, 5.0)
aluno3 = Estudante('Ana', 6.0, 8.5)

# Testando os métodos
print(f'Média de {aluno1.nome}: {aluno1.media():.2f}')
aluno1.situacao()

print(f'Média de {aluno2.nome}: {aluno2.media():.2f}')
aluno2.situacao()

print(f'Média de {aluno3.nome}: {aluno3.media():.2f}')
aluno3.situacao()
