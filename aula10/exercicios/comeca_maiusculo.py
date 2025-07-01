"""Diferentes implementações de funções que recebem como parâmetro uma listra de strings
e exibem como resultado quantas delas possuem a primeira letra em maúsculo.
"""


def comeca_maiusculo1(textos: list[str]) -> None:
    """Conta e imprime a quantidade de strings cuja primeira letra é maiúscula.

    Estratégia:
        Compara diretamente o primeiro caractere com sua versão em caixa alta,
        usando um for.
    """

    contador = 0
    for texto in textos:
        if texto[0] == texto[0].upper():
            contador += 1

    print(contador)


def comeca_maiusculo2(textos: list[str]) -> None:
    """Conta e imprime a quantidade de strings cuja primeira letra é maiúscula.
    
    Estratégia:
        Utiliza valores ASCII (A-Z correspondem a 65-90).
    """

    contador = 0
    for texto in textos:
        if 65 <= ord(texto[0]) <= 90:
            contador += 1

    print(contador)


def comeca_maiusculo3(textos: list[str]) -> None:
    """Conta e imprime a quantidade de strings cuja primeira letra é maiúscula.
    
    Estratégia:
        Utiliza o método isupper() do str.
    """

    contador = 0
    for texto in textos:
        if texto[0].isupper():
            contador += 1

    print(contador)


def comeca_maiusculo4(textos: list[str]) -> None:
    """Conta e imprime a quantidade de strings cuja primeira letra é maiúscula.
    
    Estratégia:
        Utiliza compreensão de lista e a função sum().
    """
    print(sum(1 for t in textos if t[0].isupper()))


def comeca_maiusculo5(textos: list[str]) -> None:
    """Conta e imprime a quantidade de strings cuja primeira letra é maiúscula.
    
    Estratégia:
        Utiliza a função filter().
    """
    print(len(list(filter(lambda t: t[0].isupper(), textos))))


def comeca_maiusculo6(textos: list[str]) -> None:
    """Conta e imprime a quantidade de strings cuja primeira letra é maiúscula.
    
    Estratégia:
        Utiliza a função map().
    """
    print(sum(map(lambda t: 1 if t[0].isupper() else 0, textos)))

if __name__ == '__main__':
    strings_de_teste = [
        "Banana", "laranja", "Cachorro", "gato", "Elefante",
        "tigre", "Abacaxi", "morango", "Uva", "pera",
        "Carro", "bicicleta", "Moto", "avião", "Trem",
        "barco", "Navio", "canoa", "Peixe", "Tubarão",
        "Golfinho", "Arara", "papagaio", "Falcão", "águia",
        "Gorila", "macaco", "Cavalo", "Zebra", "leão",
        "Girafa", "hipopótamo", "Rinoceronte", "Formiga",
        "abelha", "Borboleta", "escorpião", "Cobra",
        "Jacaré", "lagarto", "Tartaruga", "Lobo", "urso",
        "Raposa", "sapo", "Pato", "Galo", "galinha",
        "Vaca", "boi", "Porco", "ovelha", "Cordeiro",
        "Morango", "Melancia", "Pêssego", "kiwi", "Framboesa",
        "Tomate", "Pimenta", "Manga", "Carambola", "Coco",
        "Amora", "Cereja", "Limão", "Mamão", "Jabuticaba",
        "Pinhão", "Mandioca", "Cebola", "Alho", "Chuchu",
        "Abóbora", "Beterraba", "Alface", "Couve", "Espinafre",
        "Berinjela", "Repolho", "Rabanete", "Gengibre", "Pepino",
        "Pimentão", "Brócolis", "Quiabo", "Jiló", "Maxixe",
        "Nabo", "Cará", "Ervilha", "Graviola", "Pitanga",
        "Lichia", "Guaraná", "Tâmara", "Mexerica", "Noz",
        "Castanha", "Amêndoa", "Avelã", "Pistache", "Macadâmia",
        "Salsa", "Coentro", "Manjericão", "Orégano", "Alecrim",
        "Tomilho", "Louro", "Cebolinha", "Hortelã", "Sálvia",
        "Canela", "Cravo", "Noz-moscada", "Anis", "Cardamomo",
        "Erva-doce", "Mostarda", "Páprica", "Cominho", "Goiaba"
    ]

    comeca_maiusculo1(strings_de_teste * 10)
    comeca_maiusculo2(strings_de_teste * 10)
    comeca_maiusculo3(strings_de_teste * 10)
    comeca_maiusculo4(strings_de_teste * 10)
    comeca_maiusculo5(strings_de_teste * 10)
    comeca_maiusculo6(strings_de_teste * 10)
