from entidade import Entidade


class Personagem(Entidade):
    def usar_habilidade_especial(self):
        dano = self.forca * 2
        print(f"{self.nome} usou sua habilidade especial causando {dano} de dano!")
        return dano
