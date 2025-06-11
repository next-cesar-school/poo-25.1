class Nps:
    def __init__(self):
        self.notas = []
    
    def adicionar_nota(self, nota):
        if 0 <= nota <= 10:
            self.notas.append(nota)
        else:
            print('A nota precisa ser um valor entre 0 e 10')
    
    def calcular_nps(self):
        detratores = [n for n in self.notas if n <= 6]
        promotores = [n for n in self.notas if n >= 9]
        
        percentual_detratores = (len(detratores) / len(self.notas)) * 100
        percentual_promotores = (len(promotores) / len(self.notas)) * 100
        
        nps = percentual_promotores - percentual_detratores
        return nps
    
    def avaliar_classificacao(self):
        nps = self.calcular_nps()
        
        if nps < 0:
            print('Zona Crítica')
        elif nps < 50:
            print('Zona Neutra (Razoável)')
        elif nps < 75:
            print('Zona de Qualidade (Muito bom)')
        else:
            print('Zona de Excelência (Excelente)')

if __name__ == '__main__':
    print('Rodando teste do NPS')
    avaliacao1 = Nps()

    avaliacao1.adicionar_nota(8)
    avaliacao1.adicionar_nota(9)
    avaliacao1.adicionar_nota(7)
    avaliacao1.adicionar_nota(8)
    avaliacao1.adicionar_nota(9)
    avaliacao1.adicionar_nota(8)
    avaliacao1.adicionar_nota(9)
    avaliacao1.adicionar_nota(10)
    avaliacao1.adicionar_nota(8)
    avaliacao1.adicionar_nota(9)

    '''for _ in range(100):
        avaliacao1.adicionar_nota(int(input()))'''

    print(avaliacao1.calcular_nps())
    avaliacao1.avaliar_classificacao()
