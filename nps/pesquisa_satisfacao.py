from nps import Nps


print('--- Pesquisa de Satisfação ---')

pesquisa_nps = Nps()

while True:
    nota = input('Em uma escala de 0 a 10, o quanto você recomendaria nossa empresa a um amigo ou colega?'
                 '\nDigite "sair" para encerrar a pesquisa')
    
    if nota.lower() == 'sair':
        break
    
    pesquisa_nps.adicionar_nota(int(nota))

pesquisa_nps.avaliar_classificacao()
