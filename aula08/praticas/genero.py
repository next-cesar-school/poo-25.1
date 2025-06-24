import requests


nome = input('Qual nome você quer pesquisar? ')

url = f"https://api.genderize.io/?name={nome}"
resposta = requests.get(url)


dados = resposta.json()
print(dados)
