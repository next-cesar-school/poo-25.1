# NExT | **Programação Orientada a Objetos** com Python

![CESAR School](/cesar_school.png)

## Aula 06 - Métodos Especiais (Dunder Methods)

### Na aula de hoje

- Métodos Especiais (Dunder Methods)

------------------

## Dunder Methods

Os **métodos especiais**, também conhecidos como **dunder methods** (de **double underscore**), ou ainda como **Métodos Mágicos**, são métodos identificados com dois underscores, no início e no final, como `__init__` e `__str__`. Eles permitem personalizar o comportamento de classes em Python.

### Por que usar?

- Para personalizar a inicialização e representação de objetos.
- Para modificar como objetos interagem com operadores (`+`, `-`, `*`, etc.).
- Para manipular objetos como se fossem listas, dicionários ou funções.
- Para implementar comportamentos específicos em suas classes.

### Exemplo

```python
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __str__(self):
        return f"Pessoa: {self.nome}, {self.idade} anos"


p = Pessoa("João", 25)
print(p) 
```

## Principais Dunder Methods

| Método | Descrição |
| :---: | --- |
| `__init__` | Inicializa o objeto da classe |
| `__str__` | Retorna uma string representativa do objeto (exibida por print) |
| `__repr__` | Retorna uma string oficial para representação (útil para   depuração) |
| `__len__` | Retorna o tamanho do objeto |
| `__getitem__` | Permite acessar itens de um objeto de forma indexada, como em listas ou dicionários |
| `__setitem__` | Permite definir itens de um objeto |
| `__add__` | Define o comportamento do operador `+` |
| `__sub__` | Define o comportamento do operador `-` |
| `__eq__` | Define o comportamento do operador `==` |
| `__lt__` , `__gt__` | Definem `<` e `>` |
| `__call__` | Permite que o objeto seja chamado como uma função |

## Como usar

### Inicialização e Representação de Objetos

O `__init__` é usado para inicializar objetos, e os métodos `__str__` e `__repr__` personalizam a forma como os objetos são exibidos.

```python
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __str__(self):
        return f"Nome: {self.nome}, Idade: {self.idade} anos"

    def __repr__(self):
        return f"Pessoa(nome='{self.nome}', idade={self.idade})"

# Testando
p = Pessoa("Maria", 30)
print(p)         # Output: Nome: Maria, Idade: 30 anos
print(repr(p))   # Output: Pessoa(nome='Maria', idade=30)
```

- `__str__` : Representação legível para humanos. Sugestão: Retorne uma string simples e descritiva.
- `__repr__`: Representação Oficial e Técnica. Sugestão: Apresentar os detalhes relacionados à depuração e que possa ser usada para recriar o objeto (se possível).

> 💡 Dica:
>
> - Se apenas o `__repr__` for implementado, e não o `__str__`, o Python usará o `__repr__` como substituto do `__str__`;
> - Para a maioria dos casos, implemente ambos para garantir comportamentos adequados em diferentes contextos.

### Contagem de Elementos com `len()`

O `__len__` pode ser usado para permitir que objetos retornem um tamanho, como listas.

```python
class Playlist:
    def __init__(self, nome, musicas):
        self.nome = nome
        self.musicas = musicas

    def __len__(self):
        return len(self.musicas)


# Testando
playlist = Playlist("Favoritas", ["Música 1", "Música 2", "Música 3"])
print(len(playlist))
```

### Acesso Direto aos Dados

Permite tratar objetos como se fossem listas ou dicionários.

```python
class Tabela:
    def __init__(self):
        self.dados = {}

    def __setitem__(self, chave, valor):
        self.dados[chave] = valor

    def __getitem__(self, chave):
        return self.dados.get(chave, "Não encontrado")


# Testando
t = Tabela()
t["a"] = 100
print(t["a"])
print(t["b"])
```

### Chamando Objetos como Funções

Transforma o objeto em algo que pode ser chamado como uma função.

```python
class Saudacao:
    def __init__(self, mensagem):
        self.mensagem = mensagem

    def __call__(self, nome):
        print(f"{self.mensagem}, {nome}!")


# Testando
s = Saudacao("Bem-vindo")
s("João")
```

### Tornando os Objetos Iterativos

Implemente objetos que podem ser iterados como listas.

```python
class Estudante:
    def __init__(self):
        self.__notas = []
        self.__nota_atual = 0

    def add_nota(self, nota):
        if len(self.__notas) < 4:
            self.__notas.append(nota)

    def __iter__(self):
        return self

    def __next__(self):
        if self.__nota_atual < 4:
            nota = self.__notas[self.__nota_atual]
            self.__nota_atual += 1
            return nota
        else:
            raise StopIteration


# Testando
joao = Estudante()

joao.add_nota(10)
joao.add_nota(9)
joao.add_nota(8)
joao.add_nota(7)

for nota in joao:
    print(nota)
```

### Somando Objetos

```python
class ListaCompras:
    def __init__(self, nome, data):
        self.nome = nome
        self.data = data
        self.__itens = []

    def add_item(self, item):
        self.__itens.append(item)

    def get_itens(self):
        return self.__itens

    def __add__(self, other):
        new_list = ListaCompras(self.nome, self.data)

        for item in self.__itens + other.get_itens():
            new_list.add_item(item)

        return new_list

feira_da_fruta = ListaCompras('Lista de Frutas', '20/12')
feira_da_fruta.add_item('banana')
feira_da_fruta.add_item('maça')
feira_da_fruta.add_item('tangerina')
feira_da_fruta.add_item('morango')

natal = ListaCompras('Compras de Natal', '31/01')
natal.add_item('chocotone')
natal.add_item('peru')
natal.add_item('uva passa')

nova_lista = feira_da_fruta + natal

print(nova_lista.get_itens())
```

> 💡 Dica:
> Veja mais sobre todos os Dunder Methods do Python [aqui](https://www.pythonmorsels.com/every-dunder-method/).

## 🧱 Exercícios Fundamentais

### 1. Soma de Coordenadas

Implemente uma classe `Coordenada` com atributos `x` e `y`.

- Configure o operador `+` com `__add__` para somar duas coordenadas, retornando um novo objeto `Coordenada`;
- Personalize o método `__str__` para exibir o objeto no formato `(x, y)`.

**Exemplo de Uso:**

```python
c1 = Coordenada(2, 3)
c2 = Coordenada(4, 5)

c3 = c1 + c2

print(c3)  # Saída: (6, 8)
```

### 2. Multiplicação de Matrizes com `__mul__`

Crie uma classe `Matriz` que representa uma matriz 2x2.

- Pesquise sobre como é feito multiplicação de matrizes (pode usar [esta referência](https://www.somatematica.com.br/emedio/matrizes/matrizes4.php))
- Faça uso do operador `*` com `__mul__` para multiplicar duas matrizes;
- Adicione o método `__str__` para exibir a matriz no formato:

```text
[ a  b ]
[ c  d ]
```

### 3. Comparação de Produtos

Implemente uma classe `Produto` com atributos `nome` e `preco`.

- Use o operador `==` com `__eq__` para verificar se dois produtos têm o mesmo nome e preço.
- Adicione o método `__repr__` para exibir o produto como no exemplo Exemplo: `Produto(nome='Camiseta', preco=49.90)`

**Exemplo de Uso:**

```python
p1 = Produto("Camiseta", 49.90)
p2 = Produto("Camiseta", 49.90)
print(p1 == p2)
```

### 4. Carrinho de Compras

Implemente uma classe `CarrinhoDeCompras` que armazena produtos e suas quantidades.

- Use `__getitem__` para acessar a quantidade de um produto específico no carrinho.
- Adicione `__setitem__` para atualizar a quantidade de um produto.

**Exemplo de Uso:**

```python
carrinho = CarrinhoDeCompras()
carrinho["Camiseta"] = 2
print(carrinho["Camiseta"])
```

------------------

<!--
# To Do List de Final de Ano 🎉

- [ ] Fazer todos os exercícios
- [ ] Organizar os exercícios no GitHub
- [ ] Revisar os exercícios PyFinanceiro e PyVotação e aplicar OO neles
- [ ] Sono de Vingança (quando você dorme pra compensar o sono que você não pode dormir antes)
- [ ] Checar com uma voadora em 2025 🦵
-->
------------------

![Dunder Methods](/aula06/dundermethods.jpg)
