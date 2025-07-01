from math import pi


class Util:

    @staticmethod
    def area_triangulo(base: float, altura: float) -> float:
        return (base * altura) / 2

    @staticmethod
    def area_quadrado(lado: float) -> float:
        return lado ** 2

    @staticmethod
    def area_retangulo(base: float, altura: float) -> float:
        return base * altura

    @staticmethod
    def area_circunferencia(raio: float) -> float:
        return pi * (raio ** 2)

if __name__ == '__main__':
    print(Util.area_triangulo(20, 30))
    print(Util.area_quadrado(10))
