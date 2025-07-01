"""Implementação dos testes unitários para a classe Calculadora."""

import unittest
from aula11.exercicios.exc1_calculadora import Calculadora


class TesteCalculadora(unittest.TestCase):
    def test_soma(self):
        self.assertEqual(Calculadora.soma(2, 3), 5)
        self.assertEqual(Calculadora.soma(-1, 5), 4)

    def test_subtracao(self):
        self.assertEqual(Calculadora.subtracao(10, 5), 5)
        self.assertEqual(Calculadora.subtracao(0, 3), -3)

    def test_multiplicacao(self):
        self.assertEqual(Calculadora.multiplicacao(4, 3), 12)
        self.assertEqual(Calculadora.multiplicacao(-1, 5), -5)

    def test_divisao(self):
        self.assertEqual(Calculadora.divisao(10, 2), 5)
        with self.assertRaises(ValueError):
            Calculadora.divisao(10, 0)

if __name__ == '__main':
    unittest.main()
