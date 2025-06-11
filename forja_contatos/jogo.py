class Jogo:
    def __init__(self, nome, sinopse, genero, plataforma, engine, status):
        self.nome = nome
        self.sinopse = sinopse
        self.genero = genero
        self.plataforma = plataforma
        self.engine = engine
        self.status = status
        self.ativo = True
    
    def set_ativo(self, ativo):
        # definir o valor do atributo ativo
        self.ativo = ativo
    
    def is_ativo(self):
        # retorna o valor do atributo ativo
        return self.ativo
