import unittest


def soma(n1: int, n2: int) -> int:
    return n1 + n2

def dividir(n1: int, n2: int) -> int:
    return n1 / n2

class SomaTest(unittest.TestCase):

    def test_soma_simples(self):
        resultado = soma(5, 5)
        self.assertEqual(resultado, 10)

    def test_soma_negativos(self):
        resultado = soma(-10, -20)
        self.assertEqual(resultado, -30)

    def test_soma_pos_neg(self):
        resultado = soma(10, -8)
        self.assertEqual(resultado, 2)

    def test_lancar_excecao(self):
        with self.assertRaises(ZeroDivisionError):
            dividir(10, 0)
