import random
from entidade import Entidade


class Inimigo(Entidade):
    def agir(self):
        # Escolhe aleatoriamente entre atacar e defender
        return random.choice(["atacar", "defender"])
