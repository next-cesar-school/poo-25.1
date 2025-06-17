# NExT | **Programação Orientada a Objetos** com Python

![CESAR School](/cesar_school.png)

## Aula 05 - Polimorfismo

### Na aula de hoje

- Polimorfismo
- Ordem de Resolução de Métodos (MRO)

------------------

## O que é Polimorfismo?

**Polimorfismo**, na Programação Orientada a Objetos (POO), refere-se à capacidade de um método ou operação se comportar de maneira diferente dependendo do objeto que o invoca. Em Python, ele é implementado dinamicamente e facilita a reutilização de código.

- Em Python, polimorfismo permite que uma interface comum (como um método) seja usada para objetos de diferentes classes.

### Por que usar Polimorfismo?

- Promove flexibilidade no código;
- Permite trabalhar com diferentes classes de maneira uniforme;
- Facilita a extensão, manutenção e evolução do código ao longo do tempo.

Em Python, o polimorfismo é implementado de maneira dinâmica, ou seja, os métodos são chamados com base no objeto que invoca o método.

## Exemplo 1

```python
class Animal:
    def emitir_som(self):
        print("Som de um animal.")

class Cachorro(Animal):
    def emitir_som(self):
        print("Au au!")

class Gato(Animal):
    def emitir_som(self):
        print("Miau!")

# Polimorfismo
def fazer_animal_emitir_som(animal):
    animal.emitir_som()

# Teste
animais = [Cachorro(), Gato(), Animal()]
for animal in animais:
    fazer_animal_emitir_som(animal)
```

### Explicação

- O método `emitir_som()` existe em várias classes (`Animal`, `Cachorro`, `Gato`).
- A função `fazer_animal_emitir_som()` aceita qualquer objeto que implemente o método `emitir_som()`, demonstrando polimorfismo.

## Exemplo 2

```python
class Forma:
    def calcular_area(self):
        pass

class Retangulo(Forma):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def calcular_area(self):
        return self.largura * self.altura

class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio

    def calcular_area(self):
        from math import pi
        return pi * self.raio ** 2

# Lista de formas
formas = [Retangulo(5, 10), Circulo(7)]

for forma in formas:
    print(f"Área: {forma.calcular_area():.2f}")
```

- A classe `Forma` define o método `calcular_area()` como uma interface comum;
- As classes `Retangulo` e `Circulo` sobrescrevem o método para calcular suas respectivas áreas.

## MRO (Method Resolution Order)

O **MRO** é a **Ordem de Resolução de Métodos** em Python. Ele define a ordem na qual os métodos são buscados e chamados quando há herança múltipla.

### Regra do MRO em Python

Python utiliza o algoritmo de **C3 Linearization** para determinar a ordem de resolução de métodos. Isso garante que a busca respeite a ordem de herança e não haja ambiguidades.

Para verificar o MRO em Python, usamos o atributo especial `__mro__` ou o método `mro()`.

## Exemplo 3

```python
class A:
    def falar(self):
        print("Classe A")

class B(A):
    def falar(self):
        print("Classe B")

# Teste
b = B()
b.falar()
print(B.__mro__)  # Exibe a ordem de resolução
```

- A ordem é: B → A → object

## 🧱 Exercícios Fundamentais

> ⚠️ Sobre os exercícios desta aula:
>
> 1. Crie os arquivos e organize as classes conforme boa prática;
> 2. Use `if __name__ == '__main__'` para testes.

### 1. Instrumentos Musicais

1. Crie uma classe base `Instrumento` com um método `tocar()`, que exibe uma mensagem genérica como `"Tocando um instrumento"`
2. Implemente três classes filhas:
    - `Violao`: Sobrescreve `tocar()` para exibir `"Tocando violão"`
    - `Piano`: Sobrescreve `tocar()` para exibir `"Tocando piano"`
    - `Bateria`: Sobrescreve `tocar()` para exibir `"Tocando bateria"`
3. No bloco principal, crie uma lista de objetos de cada tipo de instrumento e chame o método `tocar()` para cada um.

### 2. Veículos

1. Crie uma classe base `Veiculo` com o método `deslocar()`, que exibe `"O veículo está se deslocando"`
2. Implemente três classes filhas:
    - Carro: Sobrescreve `deslocar()` para exibir `"O carro está dirigindo na estrada"`
    - Barco: Sobrescreve `deslocar()` para exibir `"O barco está navegando na água"`
    - Aviao: Sobrescreve `deslocar()` para exibir `"O avião está voando no céu"`
3. Crie uma lista de veículos no bloco principal e execute o método deslocar() para cada um.

### 3. Aventura Polimórfica

Você deve implementar um jogo de turno simples onde o jogador controla um **Personagem** e enfrenta um **Inimigo** em combate. Ambos compartilham atributos e métodos comuns, mas seus comportamentos são diferenciados pelo uso de polimorfismo.

#### Requisitos

1. Classe Base `Entidade`:
    - Atributos:
        - `nome`: O nome da entidade.
        - `vida`: Pontos de vida (HP) da entidade.
        - `forca`: Quantidade de dano que a entidade pode causar ao atacar.
    - Métodos:
        - `atacar()`: Retorna o dano baseado na força.
        - `defender()`: Habilita uma defesa que reduz o dano recebido no próximo ataque pela metade.
        - `receber_dano(dano)`: Reduz a vida da entidade pelo dano recebido e exibe o estado atual da vida.

2. Classe `Personagem` (herda de `Entidade`):
    - Métodos:
        - `usar_habilidade_especial()`: Retorna um dano dobrado em comparação ao método `atacar()`.

3. Classe `Inimigo` (herda de `Entidade`):
    - Métodos:
        - `agir()`: Escolhe aleatoriamente entre atacar ou defender no turno do inimigo.

4. Sistema de Turnos:
    - No turno do jogador, ele pode escolher entre:
        1. **Atacar**: Causa dano ao inimigo.
        2. **Defender**: Reduz o dano do próximo ataque pela metade.
        3. **Usar Habilidade Especial**: Causa dano dobrado.
    - O inimigo age automaticamente, atacando ou defendendo com base no método agir().

5. Condições de Vitória e Derrota:
    - O jogo termina quando a vida de uma das entidades (Personagem ou Inimigo) chega a zero.

#### Exemplo de Saída Esperada

```text
Bem-vindo ao Jogo de Turnos!

--- Turno do Jogador ---
Escolha uma ação:
1. Atacar
2. Defender
3. Usar Habilidade Especial
Digite o número da sua ação: 1
Arthur ataca causando 10 de dano!
Goblin agora tem 30 pontos de vida.

--- Turno do Inimigo ---
Goblin ataca causando 8 de dano!
Arthur agora tem 42 pontos de vida.

--- Turno do Jogador ---
Escolha uma ação:
1. Atacar
2. Defender
3. Usar Habilidade Especial
Digite o número da sua ação: 3
Arthur usou sua habilidade especial causando 20 de dano!
Goblin agora tem 10 pontos de vida.

--- Turno do Inimigo ---
Goblin está se defendendo!

--- Turno do Jogador ---
Escolha uma ação:
1. Atacar
2. Defender
3. Usar Habilidade Especial
Digite o número da sua ação: 1
Arthur ataca causando 10 de dano!
Goblin foi derrotado!

--- Fim do Jogo ---
Arthur venceu!
```

#### Desafios Adicionais (Opcional)

1. Adicione dificuldades ao jogo, onde os inimigos têm força e vida ajustadas para cada nível.
2. Crie uma lista de inimigos, permitindo batalhas consecutivas no mesmo jogo.
3. Adicione itens de cura que o jogador possa usar para recuperar pontos de vida durante a batalha.
