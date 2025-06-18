class Saudacao:
    def __init__(self, mensagem):
        self.mensagem = mensagem

    def __call__(self, nome):
        print(f"{self.mensagem}, {nome}!")


# Testando
cumprimento = Saudacao("Bem-vindo")

cumprimento("João")
cumprimento("Nathália")
cumprimento('Edu')
