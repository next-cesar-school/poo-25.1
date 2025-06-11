class Carro:
    quantidade_portas = 4
    ar_condicionado = True
    cor = 'azul'
    modelo = 'sedan'
    combustivel = 'eletrico'

byd_song_pro = Carro()
byd_dolphin = Carro()

print(type(byd_song_pro))
print(byd_song_pro.cor)
byd_song_pro.cor = 'verde'
print(byd_song_pro.cor)

print(byd_song_pro.quantidade_portas)
print(byd_dolphin.quantidade_portas)
