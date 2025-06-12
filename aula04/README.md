# NExT | **Programação Orientada a Objetos** com Python

![CESAR School](/cesar_school.png)

## Aula 04 - Herança

### Na aula de hoje

- Herança
- Herança Simples e Herança Múltipla
- Métodos de Classe e Sobrescrita
- Uso de `super()`

------------------

## Introdução à Herança

A **Herança** é um dos pilares fundamentais da Programação Orientada a Objetos (POO).
Ela permite que uma classe herde atributos e métodos de outra classe, promovendo reutilização de código e evitando duplicidade.

- **Classe Pai** (ou classe base): a classe que fornece os atributos e métodos.
- **Classe Filha** (ou classe derivada): a classe que herda da classe pai.

### Por que usar herança?

1. Reduz duplicação de código ao reaproveitar funcionalidades existentes.
2. Facilita a manutenção do código ao organizar hierarquias lógicas entre classes.
3. Permite personalizar ou estender funcionalidades de uma classe.

## Como funciona a Herança em Python

Em Python, a herança é indicada ao passar a classe pai como parâmetro para a classe filha.

```python
class ClassePai:
    # Atributos e métodos da classe pai
    pass

class ClasseFilha(ClassePai): # <-- ClasseFilha herda de ClassePai
    # Atributos e métodos da classe filha
    pass
```

### Exemplo

```python
# Classe Pai
class Animal:
    def __init__(self, nome):
        self.nome = nome

    def mover(self):
        print(f'{self.nome} está se movendo.')

# Classe Filha
class Cachorro(Animal):
    def latir(self):
        print(f'{self.nome} está latindo!')

# Uso
meu_cachorro = Cachorro('Rex')
meu_cachorro.mover()
meu_cachorro.latir()
```

**Explicação**:

- A classe `Cachorro` herda o método `mover()` da classe `Animal`, mas também define seu próprio comportamento com o método `latir()`.

## Removendo Duplicidade

Um dos usos mais comuns de **Herança**, é na remoção de atributos ou métodos repetidos.

![Diagrama de Classe: Estudante e Professor](/aula04/dc_estudante_professor.png)

Neste exemplo, tanto a classe `Estudante` como a classe `Professor` possuem atributos repetidos.

![Diagrama de Classe: Pessoa, Estudante e Professor](/aula04/dc_pessoa_estudante_professor.png)

Desta forma, a classe pessoa é base para as demais classes, e concentra os atributos que são comuns a elas.

## Herança Simples e Herança Múltipla

### Herança Simples

Na herança simples, a classe filha herda de apenas uma classe pai.

```python
class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def ligar(self):
        print(f'{self.marca} {self.modelo} está ligado.')

class Carro(Veiculo):
    def acelerar(self):
        print(f'{self.marca} {self.modelo} está acelerando!')
```

### Herança Múltipla

Python suporta herança múltipla, onde uma classe pode herdar de múltiplas classes pais.

```python
class Mamifero:
    def amamentar(self):
        print('Amamentando filhotes.')

class Ave:
    def voar(self):
        print('Voando alto.')

class Morcego(Mamifero, Ave):
    pass

morcego = Morcego()
morcego.amamentar()
morcego.voar()
```

> ⚠️ Nota:
>
> - Use herança múltipla com cuidado, pois pode tornar o código difícil de entender e manter;
> - Use herança apenas quando existir uma relação real de "é um" (ex.: `Carro` é um `Veiculo`).

## Métodos de Classe e Sobrescrita

### Sobrescrita de Métodos

Uma classe filha pode redefinir métodos da classe pai para alterar seu comportamento.

```python
class Animal:
    def emitir_som(self):
        print('Som genérico de animal.')

class Gato(Animal):
    def emitir_som(self):
        print('Miau!')

# Uso
gato = Gato()
gato.emitir_som()
```

**Por que sobrescrever métodos?**

- Personalizar o comportamento de uma classe filha sem modificar a classe pai.

### Uso de super()

O método `super()` é usado para chamar métodos da classe pai na classe filha, especialmente o construtor (`__init__`).

```python
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo):
        super().__init__(nome, idade)  # Chama o construtor da classe pai
        self.cargo = cargo

    def exibir_detalhes(self):
        print(f'Nome: {self.nome}, Idade: {self.idade}, Cargo: {self.cargo}')

# Uso
f = Funcionario('Ana', 30, 'Engenheira')
f.exibir_detalhes()
```

**Vantagens do `super()`:**

- Facilita a reutilização de código na hierarquia de classes.
- Reduz a repetição de lógica presente na classe pai.

## 🔥🔨 FORJA Contato

Vamos atualizar as classes do projeto FORJA Contato.

No modelo original, as classes `Pessoa` e `Jogo` possuíam atributos iguais.

![Diagrama de Classes: Pessoa e Jogo](/aula04/dc_pessoa_jogo.png)

Usando **Herança**, podemos concentrar os atributos iguais em uma classe base.

![Diagrama de Classes: Pessoa e Jogo](/aula04/dc_entidade_pessoa_jogo.png)

## 🧱 Exercícios Fundamentais

> ⚠️ Sobre os exercícios desta aula:
>
> 1. Crie os arquivos e organize as classes conforme boa prática;
> 2. Use `if __name__ == '__main__'` para testes.

### 1. Veículos

Crie uma hierarquia de classes para representar veículos. A hierarquia deve ser organizada da seguinte forma:

1. Classe `Veiculo`:
    - Atributos: `marca`, `modelo`.
    - Métodos:
        - `__init__(marca, modelo)`: Inicializa os atributos.
        - `movimentar()`: Exibe uma mensagem indicando que o veículo está se movendo.

2. Classe `VeiculoSemMotor` (herda de `Veiculo`):
    - Atributos: `tipo_propulsao` (ex.: pedal, remo).
    - Métodos:
        - Sobrescreva `movimentar()` para exibir uma mensagem indicando o tipo de propulsão.

3. Classe `VeiculoComMotor` (herda de `Veiculo`):
    - Atributos: `combustivel` (ex.: gasolina, elétrico).
    - Métodos:
        - Sobrescreva `movimentar()` para exibir uma mensagem indicando o tipo de combustível.

4. Classe `Carro` (herda de `VeiculoComMotor`):
    - Atributos: `quantidade_portas`.
    - Métodos:
        - Implemente um método `detalhes()` que exibe todas as informações do carro.
5. Teste:
    - Crie instâncias de `Carro` e `VeículoSemMotor` para realizar testes com as funções e atributos.

### 2. Formas Geométricas

Crie um conjunto de classes que representem formas geométricas bidimensionais. Essas formas vão ser capazes de calcular sua área e perímetro.

1. Classe `FormaGeometrica`:
    - Métodos:
        - `calcular_area()`
        - `calcular_perimetro()`
2. Classe `Retangulo` (herda de `FormaGeometrica`):
    - Atributos: `largura`, `altura`
    - Métodos:
        - Sobrescrição de `calcular_area()` e `calcular_perimetro()`
3. Classe `Circulo` (herda de `FormaGeometrica`):
    - Atributos: `raio`
    - Métodos:
        - Sobrescrição de `calcular_area()` e `calcular_perimetro()`
4. Teste:
    - Crie uma lista de formas geométricas diversas e execute o cálculo de área e perímetro de todas elas.
