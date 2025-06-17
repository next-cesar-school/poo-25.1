class Entidade:
    def __init__(self, nome, vida, forca):
        self.nome = nome
        self.vida = vida
        self.forca = forca
        self.defendendo = False

    def atacar(self):
        dano = self.forca
        print(f"{self.nome} ataca causando {dano} de dano!")
        return dano

    def defender(self):
        self.defendendo = True
        print(f"{self.nome} está se defendendo e reduzirá o próximo dano pela metade!")

    def receber_dano(self, dano):
        if self.defendendo:
            dano //= 2
            print(f"{self.nome} reduziu o dano para {dano} ao se defender.")
        self.vida -= dano
        self.defendendo = False
        if self.vida <= 0:
            print(f"{self.nome} foi derrotado!")
            self.vida = 0
        else:
            print(f"{self.nome} agora tem {self.vida} pontos de vida.")
