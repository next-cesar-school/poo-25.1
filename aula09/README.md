# NExT | **Programação Orientada a Objetos** com Python

![CESAR School](/cesar_school.png)

## Aula 09 - Tratamento de Exceções em POO

### Na aula de hoje

- O que são Exceções
- Bloco `try`, `except`, `else` e `finally`
- Exceções Personalizadas
- Levantando Exceções com `raise`
- Boas práticas em POO

------------------

## Relembrando: Tratamento de Exceções

Em programação, exceções são eventos que ocorrem durante a execução de um programa e interrompem o fluxo normal de instruções. Elas representam erros ou situações inesperadas, como:

- Divisão por zero
- Acesso a elementos inexistentes em listas
- Arquivos não encontrados
- Conexão a banco de dados falhada...

Em Python, o tratamento de exceções é realizado usando o bloco `try` e `except`, permitindo que o programa continue executando mesmo após a ocorrência de erros.

Exemplo de Divisão por zero:

```python
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("Erro: Divisão por zero não é permitida.")
```

### Blocos `try`, `except`, `else` e `finally`

Python permite um tratamento detalhado e flexível de exceções usando diferentes blocos:

Estrutura Completa:

```python
try:
    # Código que pode gerar uma exceção
    num = int(input("Digite um número: "))
    resultado = 10 / num
except ValueError:
    print("Erro: Digite um valor numérico válido.")
except ZeroDivisionError:
    print("Erro: Não é possível dividir por zero.")
else:
    print(f"O resultado é {resultado}.")
finally:
    print("Fim da execução.")
```

Explicação:

- `try`: Bloco onde o código que pode gerar exceções é executado;
- `except`: Captura a exceção e executa um código alternativo;
- `else`: Executado apenas se nenhuma exceção for levantada;
- `finally`: Executado sempre, independentemente de ocorrer exceção ou não; Ideal para liberar recursos, fechar arquivos ou conexões.

## ⚠️ Exceções Personalizadas

Além das exceções nativas do Python, você pode criar suas próprias exceções.

Exemplo:

```python
class SaldoInsuficienteError(Exception):
    def __init__(self, saldo, valor):
        super().__init__(f"Saldo insuficiente. Saldo atual: {saldo}, Valor solicitado: {valor}")
```

As Exceções Personalizadas são classes que herdam de `Exception` e podem, ou não, usar seu contrutor original.

Uso:

```python
def sacar(saldo, valor):
    if valor > saldo:
        raise SaldoInsuficienteError(saldo, valor)
    saldo -= valor
    return saldo

try:
    saldo = sacar(500, 700)
except SaldoInsuficienteError as e:
    print(e)
```

### Levantando Exceções com `raise`

O comando `raise` permite forçar a ocorrência de uma exceção em um ponto específico do código.

Exemplo:

```python
def dividir(a, b):
    if b == 0:
        raise ZeroDivisionError("Denominador não pode ser zero.")
    return a / b

try:
    dividir(10, 0)
except ZeroDivisionError as e:
    print(e)
```

## Tratamento de Exceções em POO

No contexto da **Programação Orientada a Objetos** (POO), o tratamento de exceções pode ser incorporado diretamente nos métodos das classes, garantindo maior robustez e controle de erros.

Exemplo Prático:

```python
class ContaBancaria:
    def __init__(self, titular: str, saldo: float = 0.0) -> None:
        self.titular = titular
        self.__saldo = saldo

    def depositar(self, valor: float) -> None:
        if valor <= 0:
            raise ValueError("O valor do depósito deve ser positivo.")

        self.__saldo += valor

    def sacar(self, valor: float) -> None:
        if valor > self.__saldo:
            raise SaldoInsuficienteError(self.__saldo, valor)

        self.__saldo -= valor

    def exibir_saldo(self) -> None:
        print(f"Saldo atual: R${self.__saldo:.2f}")

try:
    conta = ContaBancaria("João", 500)
    conta.sacar(700)
except SaldoInsuficienteError as e:
    print(e)
```

## Boas Práticas no Tratamento de Exceções

- **Especifique exceções específicas**: Evite capturar exceções genéricas (`except Exception`). Isso dificulta a depuração;
- **Não oculte exceções**: Sempre informe o erro ao usuário ou registre _logs_;
- **Use finally para liberar recursos**: Feche arquivos, conexões de banco de dados e outras operações que devem ser encerradas;
- **Crie exceções personalizadas**: Isso torna o código mais legível e adaptado às regras de negócio.

## 🧱 Projetos Fundamentais

### 1. 🏠 CEP

1. Implementar a verificação de internet no arquivo `__init__.py`;
2. Verificar se o CEP informado na inicialização da Classe CEP é válido (é string, é numérico, tem 8 caracteres);
3. Lançar uma exceção `ConnectionError` se o `status_code` for diferente de 200;
4. Lançar um `ValueError` se o CEP não for encontrado.

### 2. 🪪 CPF

Implemente uma classe `CPF` que tenha os seguintes métodos:

1. `__init__(self, cpf: str)`: Inicializa o CPF, removendo caracteres não numéricos.
2. A classe deve ser capaz de ser inicializada com CPFs no formato `XXX.XXX.XXX-XX` e `XXXXXXXXXXX`;
3. `validar(self) -> bool`: Verifica se o CPF é válido com base nas regras da Receita Federal.
4. `__str__(self)`: Retorna o CPF formatado (`XXX.XXX.XXX-XX`).
5. Lançar exceções personalizadas (`CPFInvalidoError`) para CPFs que não seguem o formato correto ou que sejam inválidos.

#### Validação de CPF

A validação de um CPF consiste em verificar se ele possui 11 dígitos e se os dígitos verificadores estão corretos.

Regras de Validação:

1. Um CPF válido contém 11 dígitos. Exemplo: `529.982.247-25`
2. Desconsidere os caracteres não numéricos (`.` e `-`);
3. Calcule o primeiro dígito verificador:
    - Multiplique os 9 primeiros dígitos pela sequência decrescente de 10 a 2;
    - Some os resultados;
    - Multiplique o resultado por 10 e divida por 11. O resto da divisão define o dígito (se for maior que 9, o dígito será 0)
4. Calcule o segundo dígito verificador:
    - Multiplique os 10 primeiros dígitos (incluindo o primeiro dígito verificador) pela sequência decrescente de 11 a 2;
    - Repita o processo anterior.
