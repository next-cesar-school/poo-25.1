# NExT | **Programação Orientada a Objetos** com Python

![CESAR School](/cesar_school.png)

## Aula 10 - Classes Abstratas e Decorators

### Na aula de hoje

- Classes Abstratas
- Decorators

------------------

## Relembrando os Pilares da Programação Orientada a Objetos (POO)

A Programação Orientada a Objetos (POO) se baseia em quatro pilares fundamentais:

- Encapsulamento
- Herança
- Polimorfismo
- **Abstração**

Nesta aula, o foco será na **Abstração** e em como ela se conecta ao conceito de **classes abstratas**, além de aprofundarmos o uso de **_decorators_** para encapsulamento e propriedades avançadas.

### O Que é Abstração?

A **abstração** é o processo de ocultar detalhes internos e expor apenas as funcionalidades essenciais de um objeto. Ela permite simplificar a complexidade ao lidar apenas com características importantes para o funcionamento do sistema.

> **Exemplo:**
> Um carro possui um motor, mas o motorista não precisa entender como o motor funciona para dirigir. O motorista utiliza abstrações como o volante e os pedais.

Em POO, a **abstração** é implementada por meio de **classes abstratas** e **métodos abstratos**.

## Implementação de Abstração em Python

Em Python, a abstração é implementada através do módulo `abc` (**Abstract Base Class**).

### O Módulo `abc`

O módulo `abc` fornece a infraestrutura para definir classes abstratas. Sua principal característica é que uma classe abstrata **não pode ser instanciada diretamente**, servindo apenas como modelo para outras classes.

#### Exemplo de Classe Abstrata

Considere o Diagrama de Classe a seguir:

![Diagrama de Classe: Pessoa, Estudante e Professor](dc_pessoa_estudante_professor.png)

Usando apenas herança, é possível que alguém crie uma instância de `Pessoa`:

```python
joão = Pessoa('João da Silva', '84396114478', '34353665')
```

É possível que isso cause uma série de inconsistências na aplicação, que pode estar preparada para tratar apenas das classes mais específicas como `Estudante` e `Professor`.

Neste caso, é necessário tornar `Pessoa` uma classe **abstrata**:

```python
from abc import ABC, abstractmethod


class Pessoa(ABC):
    def __init__(self, nome: str, cpf:str, telefone: str) -> None:
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone

    @abstractmethod
    def listar_disciplinas(self) -> None:
        pass


class Estudante(Pessoa):
    ...

class Professor(Pessoa):
    ...

joao = Pessoa('João da Silva', '123456', '34353637') # Isso vai dar erro
```

**Explicação:**

- A classe `Pessoa` é abstrata porque herda de `ABC`. Isso faz com que ela não possa ser instanciada;
- O método `listar_disciplinas()` está decorado com o `@abstractmethod`. Isso faz com que ele precise ser implementado na classe que herda de `Pessoa`;
- As classes `Estudante` e `Professor` herdam de `Pessoa` e são obrigados a implementar o método `listar_disciplinas()`. Estas podem ser instanciadas.

## Decorators

### O que são Decorators?

**Decorators** são funções que recebem outra função ou método como argumento, estendem seu comportamento sem modificar diretamente seu código-fonte e retornam a função modificada.

Eles são amplamente utilizados para modificar ou ampliar funcionalidades de métodos e classes de forma limpa e reutilizável.

## Decorators Mais Usados na POO

Decorators como `@property`, `@valor.setter` e `@classmethod` facilitam o encapsulamento, acesso controlado a atributos e métodos de classe. Eles tornam o código mais legível e robusto ao encapsular lógica repetitiva.

### `@property`

Transforma um método em um atributo acessível diretamente.

```python
from datetime import datetime


class Pessoa:
    def __init__(self, nome: str, ano_nascimento: int):
        self.nome = nome
        self.ano_nascimento = ano_nascimento

    @property
    def idade(self) -> int:
        ano_atual: int = datetime.now().year
        return ano_atual - self.ano_nascimento


if __name__ == '__main__':
    pessoa1 = Pessoa('Alberto', 1993)
    pessoa2 = Pessoa('Triago', 2005)

    print(pessoa1.idade)
    print(pessoa2.idade)
```

### `@valor.setter`

Permite definir um método **setter** para modificar valores com regras de encapsulamento. A depender da forma como ele é aplicado, em conjunto com o `@property`, podem ser usados como **getters** e **setters**.

```python
from datetime import datetime


class Pessoa:
    def __init__(self, nome: str, ano_nascimento: int):
        self.nome = nome
        self.ano_nascimento = ano_nascimento

    @property
    def idade(self) -> int:
        ano_atual: int = datetime.now().year
        return ano_atual - self.__ano_nascimento

    @property
    def ano_nascimento(self) -> int:
        return self.__ano_nascimento

    @ano_nascimento.setter
    def ano_nascimento(self, novo_ano: int) -> None:
        if novo_ano < 0 or novo_ano > datetime.now().year:
            raise ValueError(f'O valor {novo_ano} precisa estar entre zero e o ano atual.')
        self.__ano_nascimento = novo_ano


if __name__ == '__main__':
    pessoa1 = Pessoa('Alberto', 1993)
    pessoa2 = Pessoa('Triago', 2005)
    #pessoa3 = Pessoa('Cassio', -100)

    pessoa1.ano_nascimento = 1990
    #pessoa2.ano_nascimento = -12

    print(pessoa1.idade)
    print(pessoa2.idade)
    #print(pessoa3.idade)
```

> 💡 Desta forma, quando a classe pessoa é instanciada, já ocorre a validação do `ano_nascimento`.

### `@staticmethod`

Define um método que **não recebe referência para a instância ou classe**. É usado quando o método não precisa acessar atributos de instância ou de classe.

```python
from math import pi


class Util:

    @staticmethod
    def area_triangulo(base: float, altura: float) -> float:
        return (base * altura) / 2

    @staticmethod
    def area_quadrado(lado: float) -> float:
        return lado ** 2

    @staticmethod
    def area_retangulo(base: float, altura: float) -> float:
        return base * altura

    @staticmethod
    def area_circunferencia(raio: float) -> float:
        return pi * (raio ** 2)
```

Desta forma, quando a classe `Util` for importada, não se faz necessário criar ums intância dela. Basta usar os métodos como `Util.area_triangulo(x, y)`.

## Criando seus próprios Decorators

É possível criar seus próprios decorators implementando uma função que recebe como parâmetro outra função, que retorna uma _innner function_ que executa a função passada como parâmetro.

```python
def marcador(func):
    def wrapper():
        print('== Executando antes da função. ==')
        func()
        print('== Executando após a função. ==')
    return wrapper

@marcador
def saudacao():
    print('Olá, mundo!')

saudacao()
```

## 🧱 Projetos Fundamentais

### 1. 📈 Medir Tempo

Crie um decorator que mede o tempo de execução de uma função e imprime o resultado no console.

#### Requisitos

- O decorator deve funcionar com funções que tenham parâmetros.
- O decorador deve rodar a mesma função 5 vezes, para contar o tempo total.
- O nome da função deve ser exibido
  - É possível acessar o nome da função com o dunder methods `__name__`:
    - `func.__name__` acessa o nome da função.
- Para testar, use as funções disponíveis no arquivo [`começa_maiusculo.py`](/aula10/praticas/comeca_maiusculo.py). Neste arquivos, todas as funções fazem a mesma coisa, mas usando estratégias diferentes.

#### Uso

O decorator deve ser usado do seguinte modo:

```python
@medir_tempo
def funcao_exemplo(a: int, b: float) -> None:
    ...
```

#### Saída

A mensagem exibida deve seguir o formato:

```A função "<nome_da_funcao>" executou em <tempo:.4> segundos.```

### 2. 📝 LOG do Sistema em Arquivo

Crie um decorator que registra a execução de funções em um arquivo de log.

**Descrição:**

Implemente um decorator chamado `registrar_log` que:

1. Cria (ou adiciona) um log em um arquivo `log.txt` sempre que a função decorada for executada;
2. Registra a data e a hora de execução da função;
3. Inclui o nome da função que foi executada.

#### Exemplo de Registro

Cada linha do arquiovo de log deve seguir o formato:

```[2025-01-03 15:45:23] A função <nome_da_funcao> foi executada.```

### 3. 🛍️ Controle de Estoque de Produto

Criar uma classe `Estoque` que armazena a quantidade de um determinado produto. **Cada instância deve representar apenas um produto**. Use o decorador `@property` e `@setter` para validar que o estoque não fique abaixo de zero.

**Descrição:**

- A classe deve ter um atributo privado `_quantidade`;
- O método `setter` deve impedir que a quantidade no estoque fique negativa;
- Se o valor for inválido, uma mensagem de erro deve ser exibida;
- Implemente as funções `vender()` e `repor()` para manipular a quantidade do produto no estoque.
