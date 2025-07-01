# NExT | **Programação Orientada a Objetos** com Python

![CESAR School](/cesar_school.png)

## Aula 11 - Testes Unitários

### Na aula de hoje

- O que são Testes Unitários?
- Introdução ao módulo unittest
- Testes de Exceção
- Boas Práticas para Testes Unitários
- Cobertura de Testes

------------------

## O que são Testes Unitários?

Testes unitários são testes automatizados que verificam se pequenas partes do código (unidades) funcionam como esperado. Em Python, utilizamos a biblioteca `unittest` para criar e organizar esses testes de forma padronizada.

### Por que usar Testes Unitários?

- **Detecção de Erros Precoce**: Identifica falhas no código logo durante o desenvolvimento.
- **Facilidade de Manutenção**: Permite que futuras alterações no código sejam testadas automaticamente.
- **Refatoração Segura**: Modificações no código podem ser feitas sem medo de quebrar funcionalidades já existentes.
- **Documentação**: Os testes servem como uma forma prática de documentar o comportamento esperado do código.

## Introdução ao módulo `unittest`

O módulo `unittest` é uma biblioteca padrão do Python que facilita a criação de testes automatizados.

### Estrutura Básica

Um teste com `unittest` segue a estrutura:

1. Importação do módulo `unittest`.
2. Criação de uma classe de teste que herda de `unittest.TestCase`.
3. Definição de métodos que realizam as verificações (`assert`).

```python
import unittest

class TesteExemplo(unittest.TestCase):
    def test_soma(self):
        resultado = 2 + 2
        self.assertEqual(resultado, 4)
```

### Rodando Testes

Os testes podem ser executados diretamente usando:

`python -m unittest nome_do_arquivo.py`

## Criando Testes Simples

Exemplo básico de teste para uma função de soma:

```python
def soma(a, b):
    return a + b

import unittest

class TestSoma(unittest.TestCase):
    def test_soma_positiva(self):
        self.assertEqual(soma(2, 3), 5)

    def test_soma_negativa(self):
        self.assertEqual(soma(-1, -1), -2)
```

Explicação:

- `assertEqual(a, b)`: Verifica se `a` é igual a `b`;
- `assertNotEqual(a, b)`: Verifica se `a` não é igual a `b`;
- `assertTrue(x)`: Verifica se `x` é verdadeiro;
- `assertFalse(x)`: Verifica se `x` é falso.

## Testes de Exceção

Testamos se uma função levanta uma exceção esperada.

```python
def dividir(a, b):
    if b == 0:
        raise ValueError("Divisão por zero não permitida")
    return a / b

class TestDivisao(unittest.TestCase):
    def test_divisao_por_zero(self):
        with self.assertRaises(ValueError):
            dividir(10, 0)
```

Explicação:

- `assertRaises` verifica se uma exceção específica é levantada durante a execução.

## Boas Práticas para Testes Unitários

1. **Independência dos Testes**: Cada teste deve ser isolado e não depender de outros testes.
2. **Nomes Descritivos**: O nome do teste deve indicar claramente o que está sendo verificado.
3. **Cobertura de Casos Limite**: Teste cenários normais e também os extremos (valores nulos, negativos, etc.).
4. **Automatização**: Integre a execução dos testes no fluxo de desenvolvimento (CI/CD).
5. **Teste Pequenas Partes**: Evite testar grandes blocos de código; foque em funções ou métodos individuais.

## Cobertura de Testes

A cobertura de testes mede o quanto do código foi executado durante os testes. Ferramentas como [`Coverage.py`](https://coverage.readthedocs.io) permitem verificar essa métrica.

Exemplo de Uso:

```bash
pip install coverage
coverage run -m unittest nome_do_arquivo.py
coverage report
```

## 🧱 Exercícios Fundamentais

### 1. Calculadora

- Implemente uma calculadora com as operações básicas (`soma`, `subtração`, `multiplicação`, `divisão`). Use **Type Hints** e **Docstrings**;
- Crie testes unitários para cada operação, validando diferentes cenários.

### 2. Classe Produto

- Crie uma classe `Produto` com os atributos `nome` e `preco`;
- Adicione um método `desconto(porcentagem)`;
- Crie testes para garantir que o desconto é calculado corretamente e que valores inválidos não são aplicados.

### 3. Sistema de Login com Arquivo

- Implemente um sistema básico de login com usuários e senhas. Os dados devem ser armazenados em um arquivo;
- Crie testes para verificar login bem-sucedido, falha por senha incorreta e usuário inexistente.
