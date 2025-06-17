from circulo import Circulo
from retangulo import Retangulo


if __name__ == "__main__":
    # Lista de formas geométricas
    formas = [
        Retangulo(5, 10),
        Retangulo(3, 7),
        Circulo(4),
        Circulo(6)
    ]

    # Iterando pelas formas e exibindo área e perímetro
    for forma in formas:
        print(forma.exibir_dados())  # Chama o método __str__
        print(f"Área: {forma.calcular_area():.2f}")
        print(f"Perímetro: {forma.calcular_perimetro():.2f}")
        print("-" * 30)
