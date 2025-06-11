class Carro:
    quantidade_rodas = 4
    def __init__(self, quant_portas, cor, modelo, combustivel):
        self.quantidade_portas = quant_portas
        self.cor = cor
        self.modelo = modelo
        self.combustivel = combustivel
byd_song_pro = Carro(4, 'prata', 'suv', 'hibrido')
uno = Carro(4, 'branco', 'hatch', 'gasolina')
marea = Carro(4, 'bege', 'sedan', 'gasolina')
print(byd_song_pro.cor, uno.cor, marea.cor)
print(byd_song_pro.modelo, uno.modelo, marea.modelo)
print(byd_song_pro.combustivel, uno.combustivel, marea.combustivel)
print(byd_song_pro.quantidade_rodas, uno.quantidade_rodas, marea.quantidade_rodas)
uno.quantidade_rodas = 6
print(byd_song_pro.quantidade_rodas, uno.quantidade_rodas, marea.quantidade_rodas)