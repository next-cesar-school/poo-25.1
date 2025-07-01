"""Implementação dos testes unitários para a classe SistemaLogin."""

import unittest
from aula11.exercicios.exc3_login import SistemaLogin

class TesteSistemaLogin(unittest.TestCase):
    def setUp(self):
        self.arquivo_usuarios = 'usuarios_testado.txt'

        with open(self.arquivo_usuarios, 'w', encoding='utf8') as f:
            f.write("usuario1,senha123\n")

    def test_cadastro_usuario(self):
        sistema = SistemaLogin(self.arquivo_usuarios)

        sistema.cadastrar("novo_usuario", "senha456")
        self.assertTrue(sistema.autenticar("novo_usuario", "senha456"))

    def test_login_sucesso(self):
        sistema = SistemaLogin(self.arquivo_usuarios)

        self.assertTrue(sistema.autenticar("usuario1", "senha123"))

    def test_login_falha(self):
        sistema = SistemaLogin(self.arquivo_usuarios)

        self.assertFalse(sistema.autenticar("usuario1", "senhaerrada"))
        self.assertFalse(sistema.autenticar("usuario_inexistente", "senha123"))


if __name__ == '__main__':
    unittest.main()
