class Playlist:
    def __init__(self, nome, musicas):
        self.nome = nome
        self.musicas = musicas
    
    def __len__(self):
        return len(self.musicas)
    
    def __setitem__(self, pos, valor):
        self.musicas[pos] = valor
    
    def __getitem__(self, pos):
        return self.musicas[pos]

sj = Playlist('São João NExT', ['aaaa', 'bbbb', 'cccc', 'dddd'])
print(len(sj))
#print(sj.musicas[2])
print(sj[2])
print(sj[0])

sj[1] = 'outra música'
print(sj.nome)
print(sj[1])

print(sj.musicas)