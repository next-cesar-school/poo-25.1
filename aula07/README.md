# NExT | **Programação Orientada a Objetos** com Python

![CESAR School](/cesar_school.png)

## Aula 07 - Typing

### Na aula de hoje

- Typing (Tipagem Estática)
- Guia de Estilo
- PEP 8
- Linting

------------------

## Introdução ao Typing (Tipagem Estática)

Python é uma linguagem de tipagem:

- **Dinâmica**: os tipos são "percebidos" dinamicamente, não sendo necessário defini-los explicitamente;
- **Forte**: o interpretador não faz conversões implícitas de tipos.

Por mais que isso torne o uso da linguagem mais flexível e rápido, em alguns casos, podemos ter problemas de compreensão ou interpretação do código por parte dos desenvolvedores.

A partir da versão `3.5` foi introduzido o módulo `typing`, que permite adicionar anotações de tipo ao código, conhecidos como **Type Hints**.

As anotações de tipo não alteram a execução do programa, mas ajudam a:

- Documentar melhor o código;
- Aumentar a legibilidade;
- Reduzir erros durante o desenvolvimento;
- Facilitar o uso de ferramentas de análise estática.

### 🚫 Função sem Typing

```python
def soma(a, b):
    return a + b
```

**Problema**: O código acima permite somar qualquer coisa (`str`, `int`, `float`), o que pode causar erros ou comportamentos inesperados.

### ✅ Função com Typing

```python
def soma(a: int, b: int) -> int:
    return a + b
```

**Explicação:**

- `a: int` indica que o parâmetro `a` deve ser do tipo `int`;
- `-> int` indica que a função retorna um `int`.

> ⚠️ Desta forma, se um parâmetro de um tipo diferente for usado, o código não resultará em erro. As anotações de tipo não garantem erro de execução, mas orientam o uso correto de tipos, ajudando ferramentas de análise estática a detectar inconsistências.

### Vantagens do **Type Hints**

- **Prevenção de Erros**: Detecta possíveis problemas durante o desenvolvimento;
- **Facilidade na Leitura**: O código se torna mais compreensível e explícito;
- **Melhora o Uso do Autocompletar**: IDEs e editores de texto oferecem sugestões mais precisas;
- **Refatoração Segura**: Facilita a alteração do código sem introduzir novos bugs.

## Principais Recursos do **Type Hint**

### 1. Uso de Built-in Types (tipos nativos) e Tipos Criados (Classes)

É possível usar qualquer tipo, nativo (`int`, `float`, `bool`...) ou criado por uma Classe.

```python
class Estudante:
    ...

def avaliar_estudante(pessoa: Estudante) -> None:
    if pessoa.nota >= 7.0:
        print('Passou')
    else:
        print('Reprovado')
```

### 2. Tipos Combinados (_Union_)

Quando um método puder receber mais de um tipo, é possível usar o operador `|` (_pipe_) para definir os vários tipos que são compatíveis.

```python
def divisao(a: int | float, b: int | float) -> float:
    return a / b
```

### 3. Coleções (`list`, `tuple`, `set`, `dict`)

Para definir o tipo de elementos em coleções, utilize a sintaxe `container[tipo]`. Essa abordagem facilita a compreensão do que a função espera receber ou retornar.

```python
def calcula_media(notas: tuple[int]) -> float:
    return sum(notas) / len(notas)

def buscar_dados(dados: dict[str, int], chave: str) -> int:
    return dados.get(chave, 0)
```

### 4. `None` e opcionais

- Se o método não retornar nada é possível usar o `-> None`;
- Se o método pode retornar algum tipo, ou nada, é possível usar `-> str | None`.

```python
def buscar_usuario(id: int) -> str | None:
    return "João" if id == 1 else None
```

## Type Hints em POO

Os **Type Hints** em Python não se limitam a funções e métodos. Eles também podem (e devem) ser usados na Programação Orientada a Objetos (POO), permitindo que você torne o código mais legível e ajuda ferramentas como _linters_ e IDEs a detectar erros antes mesmo da execução.

```python
class Usuario:
    nome: str
    idade: int | None  # A idade pode ser int ou None

    def __init__(self, nome: str, idade: int = None) -> None:
        self.nome = nome
        self.idade = idade

    def atualizar_idade(self, nova_idade: int) -> None:
        self.idade = nova_idade

    def saudacao(self) -> str:
        saida = f"Olá, meu nome é {self.nome}"
        saida += f' e minha idade é {self.idade} anos.' if self.idade else '.'

        return saida
```

## PEP 8

No desenvolvimento de software, a consistência e a legibilidade do código são fundamentais para facilitar a manutenção e a colaboração entre desenvolvedores. Em Python, o **PEP 8** é o guia de estilo oficial que define convenções para a formatação do código, promovendo um padrão uniforme na comunidade.

### Sobre o **PEP 8**

O [**PEP 8** (_Python Enhancement Proposal 8_)](https://peps.python.org/pep-0008/) é um documento que estabelece diretrizes de estilo para a escrita de código Python. Seu objetivo é melhorar a legibilidade e a consistência do código, facilitando a compreensão e a colaboração entre desenvolvedores.

Algumas das Principais Diretrizes do **PEP 8**:

- **Indentação**: Utilizar 4 espaços por nível de indentação; não usar tabulações;
- **Comprimento de Linhas**: Manter linhas com no máximo 79 caracteres;
- **Espaços em Branco**: Evitar espaços em branco desnecessários em expressões e instruções;
- **Nomenclatura**: Seguir convenções como `snake_case` para funções e variáveis, e `CamelCase` para classes;
- **Importações**: Realizar importações em linhas separadas e no início do arquivo.

> 💡 Seguir o **PEP 8** contribui para a criação de um código mais limpo e padronizado, facilitando a leitura e a manutenção.

## Linting

Linting é o processo de análise estática do código-fonte para identificar erros, más práticas, padrões inconsistentes e possíveis bugs antes da execução. Ferramentas de linting verificam o código em busca de desvios das convenções estabelecidas, como as do **PEP 8**, e fornecem feedback imediato ao desenvolvedor.

### Como Funciona o Linting?

As ferramentas de linting analisam o código estático, ou seja, sem executá-lo, e identificam:

- **Erros de Sintaxe**: Como parênteses não fechados ou uso incorreto de operadores;
- **Violações de Estilo**: Desvios das convenções do **PEP 8**, como indentação incorreta ou nomes de variáveis inadequados;
- **Problemas Potenciais**: Como variáveis não utilizadas ou importações desnecessárias.

> 💡 Ao integrar o linting no fluxo de trabalho, é possível detectar e corrigir problemas precocemente, melhorando a qualidade do código.

### Benefícios do Linting

- **Consistência**: Garante que o código siga padrões uniformes, facilitando a colaboração.
- **Qualidade**: Ajuda a identificar e corrigir erros antes da execução.
- **Produtividade**: Fornece feedback imediato, permitindo correções rápidas.
- **Manutenção**: Facilita a leitura e a compreensão do código por outros desenvolvedores.

## Principais Extensões de Linting Python para VS Code

O **Visual Studio Code** (VS Code) oferece diversas extensões que auxiliam no linting e na formatação do código Python. Aqui estão algumas recomendadas:

- [Pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance)
- [Pylint](https://marketplace.visualstudio.com/items?itemName=ms-python.pylint)
- [Flake8](https://marketplace.visualstudio.com/items?itemName=ms-python.flake8)
- [Black Formatter](https://marketplace.visualstudio.com/items?itemName=ms-python.black-formatter)
- [autopep8](https://marketplace.visualstudio.com/items?itemName=ms-python.autopep8)
- [Ruff](https://marketplace.visualstudio.com/items?itemName=charliermarsh.ruff)

> Instale um desses no seu ambiente de desenvolvimento e experimente as sugestões de melhoria que ele oferece.

## 🧱 Projetos Fundamentais

### 1. 🔥🔨 FORJA Contato

Vamos dar continuidade à implementação do projeto de registro de pessoas e jogos da FORJA.

Implemente:

1. Refatore a classe `Jogo`, adicionanto **Type Hints**;
2. Implemente a classe `GameStudio`:
    1. Esta classe deve ser inicializada com os atributos nome e link;
    2. Ela deve possuir uma lista de jogos privada;
    3. Ela deve possuir um atributo booleano `__ativo` privado;
    4. Crie um conjunto de métodos para adicionar, acessar e listar os jogos que o `GameStudio` possui. Deve ser exibido o nome do jogo e se ele está está ou não;
    5. Crie um método `set_ativo` para definir se o `GameStudio` está ativio.
3. Implemente a classe `Pessoa`:
    1. O nome, email e endereço devem ser definidos no momento da criação do objeto;
    2. A lista de habilidades deve ser inicialmente vazia;
    3. Ao adicionar uma habilidade, verifique se ela já existe na lista antes de inseri-la;
    4. O método `listar_habilidades` deve retornar a lista de habilidades;
    5. Ao imprimir o objeto `Pessoa`, deve-se exibir o nome e as habilidades formatadas.

### 2. Refatoração

Refatore e atualize seus últimos projetos com o uso de **Type Hints** e **Linting**.
