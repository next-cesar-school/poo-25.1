# NExT | **Programação Orientada a Objetos** com Python

![CESAR School](/cesar_school.png)

## Aula 03 - Abstração e Encapsulamento

### Na aula de hoje

- Introdução ao `__name__`
- `import` de classes
- Atributos de Classe e de Instância
- Pilares da Programação Orientada a Objetos
  - Abstração
  - Encapsulamento

------------------

## Introdução ao `__name__`

O Python usa o atributo especial `__name__` para identificar o contexto de execução de um arquivo.

Quando um arquivo Python é executado diretamente, o valor de `__name__` será `'__main__'`. Se ele for importado como módulo, o valor de `__name__` será o nome do módulo.

### Uso do `__name__`

Ajuda a separar o código principal do código auxiliar ou funções utilizadas como parte de outros scripts.

#### Exemplo - `__name__`

```python
# arquivo principal.py
def main():
    print('Este é o código principal!')

if __name__ == '__main__':
    main()
```

- Se você executar `principal.py`, o bloco dentro de `if __name__ == '__main__':` será executado.
- Se você importar `principal.py` em outro arquivo, o bloco não será executado.

## Importação de Classes entre Arquivos

Quando trabalhamos em projetos maiores, é comum dividir o código em vários arquivos. Para utilizar uma classe definida em um arquivo em outro, usamos o comando `import`.

### Exemplo - Arquivos com Classe

1. Arquivo `carro.py`:

    ```python
    class Carro:
        def __init__(self, modelo, ano):
            self.modelo = modelo
            self.ano = ano
    ```

2. Arquivo `main.py`:

    ```python
    from carro import Carro  # Importa a classe Carro do arquivo carro.py

    meu_carro = Carro('Sedan', 2020)
    print(meu_carro.modelo)  # Output: Sedan
    ```

    > 💡 Dica: Certifique-se de que os arquivos estão na mesma pasta ou configure o `PYTHONPATH` para incluir diretórios adicionais.

## Atributos de Classe e de Instância

- **Atributos de Instância**: São específicos de cada objeto. Geralmente são declarados e inicializados no método `__init__`.
- **Atributos de Classe**: Compartilhados por todas as instâncias da classe. Declarados diretamente dentro da classe, fora de qualquer método.

### Exemplo - Atributos de Classe e de Instância

```python
class Carro:
    # Atributo de classe
    n_rodas = 4

    def __init__(self, modelo, tipo, cor):
        # Atributos de instância
        self.modelo = modelo
        self.tipo = tipo
        self.cor = cor

# Instanciando objetos
carro1 = Carro('Corolla', 'Sedan', 'Vermelho')
carro2 = Carro('Pajero', 'SUV', 'Preto')

# Atributo de classe (igual para todos)
print(carro1.n_rodas)
print(carro2.n_rodas)

# Alterando o atributo de classe (diferente para cada objeto)

Carro.n_rodas = 5

print(carro1.n_rodas)
print(carro2.n_rodas)

# Alterando o atributo de instância (diferente para cada objeto)
carro1.cor = 'Azul'
print(carro1.cor)
print(carro2.cor)
```

## Pilares da Programação Orientada a Objetos

A **Programação Orientada a Objetos (POO)** é estruturada sobre pilares que facilitam a criação de sistemas robustos, escaláveis e reutilizáveis.

Os quatro pilares da POO são:

1. Abstração
2. Encapsulamento
3. Herança (abordado em aulas futuras)
4. Polimorfismo (abordado em aulas futuras)

Nesta aula, focaremos na **Abstração** e no **Encapsulamento**.

## ⚛️ Abstração

A abstração consiste em simplificar e ocultar detalhes desnecessários, expondo apenas o essencial.

![Representações de Cachorros](/aula03/dogs.png)

Ela permite representar elementos do mundo físico em termos de suas características e comportamentos relevantes.

Deste modo, tanto detalhes de complexidade como detalhes de implementação podem ser ocultados. Ela permite que os desenvolvedores foquem no "o que" precisa ser feito, sem se preocupar necessariamente com o "como".

- Objetivo: Simplificar a interação com os objetos ao expor apenas o que é necessário para sua utilização.

Imagine um carro:

- Você pode dirigir um carro sem saber como o motor funciona internamente.
- O volante, pedais e câmbio são abstrações que permitem controlar o carro sem expor a complexidade do motor.

### Importância

- Garante que classes derivadas implementem comportamentos essenciais.
- Simplifica o desenvolvimento ao lidar apenas com o essencial.

## 🔒 Encapsulamento

O encapsulamento protege os dados de um objeto, limitando o acesso direto e permitindo modificações apenas através de métodos apropriados.

- **Objetivo**: Proteger os dados e garantir que sejam acessados ou modificados apenas de maneira controlada.

### Modificadores de Acesso em Python

Embora Python não tenha modificadores explícitos como `private` ou `public`, utiliza convenções para indicar o nível de acesso:

- **Público**: Atributos ou métodos acessíveis por qualquer parte do código.
- **Protegido**: Usado para indicar que o atributo/método deve ser acessado apenas pela classe ou suas subclasses (prefixo `_`, ex: `_idade`).
- **Privado**: Restringe o acesso apenas à classe onde foi definido (prefixo `__`, ex: `__saldo`).

### Exemplo - Conta Bancária

Uma conta bancária:

- O saldo não deve ser acessado diretamente para evitar manipulações incorretas.
- Métodos como `depositar()` e `sacar()` controlam o acesso e garantem a consistência dos dados.

```python
class ContaBancaria:
    def __init__(self, titular, saldo_inicial):
        self.titular = titular
        self.__saldo = saldo_inicial  # Atributo privado

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
        else:
            print('Valor inválido para depósito.')

    def sacar(self, valor):
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor
        else:
            print('Saldo insuficiente ou valor inválido.')

    def exibir_saldo(self):
        return f'Saldo atual: R${self.__saldo:.2f}'

# Uso
conta = ContaBancaria('João', 500)
conta.depositar(200)
print(conta.exibir_saldo()) # Output: Saldo atual: R$700.00
conta.__saldo = 1000        # Não afeta o saldo real, pois é privado.
print(conta.exibir_saldo()) # Output: Saldo atual: R$700.00
```

- Restringe acessos indesejados.
- Ajuda a garantir consistência e segurança dos dados.

## 🧱 Exercícios Fundamentais

> ⚠️ Sobre os exercícios desta aula:
>
> 1. Todos devem ser feitos em classes separadas;
> 2. Implemente testes na própria classe usando `if __name__ == '__main__'`;
> 3. Crie um arquivo `main.py` e nele implemente os exercícios propostos.

### 1. **Funcionário**

Crie uma classe `Funcionario` com atributos cod, nome e salario. Atenção às regras de negócio:

- O salário é um atributo privado, mas deve ser informado no momento de criação da instância.
- Quando o salário for alterado, não é possível definir um valor menor que o salário atual;
- Implemente o método `aumentar_salario(percentual)` que aumenta o salário do funcionário com base em uma porcentagem fornecida;
- A classe deve manter um histórico dos aumentos aplicados em uma lista. Cada aumento deve ser armazenado com o percentual aplicado e o novo salário após o aumento.
- Um método `exibir_informacoes()` deve imprimir os dados do funcionário (`nome`, `cod`, `salario atual`) e o histórico de aumentos.

### 2. Carrinho de Compras da Livraria

Você deve criar um programa que simule um sistema de livraria, onde é possível gerenciar livros e um carrinho de compras. O programa deve ser composto por duas classes principais:

1. Classe `Livro`:

    - Representa um livro com os seguintes atributos:
        - `titulo` (string): O título do livro.
        - `autor` (string): O autor do livro.
        - `preco` (float): O preço do livro.

2. Classe `CarrinhoDeCompras`:

    - Representa o carrinho de compras com os seguintes atributos e métodos:
        - `livros` (lista): Uma lista que armazenará os objetos da classe Livro adicionados ao carrinho.
        - `adicionar_livro(livro)`: Adiciona um livro ao carrinho.
        - `remover_livro(titulo)`: Remove um livro do carrinho pelo título.
        - `calcular_total()`: Calcula e retorna o valor total de todos os livros no carrinho.
        - `exibir_itens()`: Exibe a lista de livros no carrinho, incluindo título, autor e preço.

- Regras:
  - O preço do livro deve ser um valor positivo.
  - Um livro com o mesmo título não deve ser adicionado ao carrinho mais de uma vez.
  - Crie métodos para facilitar a manipulação do carrinho.
  - Use boas práticas de encapsulamento, se necessário.
