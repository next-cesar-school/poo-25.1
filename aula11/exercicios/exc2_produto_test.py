"""Implementação dos testes unitários para a classe Produto."""

import unittest
from aula11.exercicios.exc2_produto import Produto

class TesteProduto(unittest.TestCase):
    def test_desconto_valido(self):
        p = Produto('Livro', 100.0)
        self.assertEqual(p.desconto(10), 90.0)

    def test_desconto_invalido(self):
        p = Produto('Celular', 500.0)

        with self.assertRaises(ValueError):
            p.desconto(-10)

        with self.assertRaises(ValueError):
            p.desconto(150)

if __name__ == '__main':
    unittest.main()
