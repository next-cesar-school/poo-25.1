from funcionario import Funcionario
from livro import Livro
from carrinho import CarrinhoDeCompras

#  --- Funcionário ---
joao = Funcionario("João Silva", 101, 3000)
joao.exibir_informacoes()
print()

joao.set_salario(2500)      # Erro: salário menor que o atual
joao.set_salario(3500)      # Atualiza salário
joao.aumentar_salario(10)   # Aumenta em 10%
joao.aumentar_salario(5)    # Aumenta em 10%
joao.aumentar_salario(10)   # Aumenta em 10%
joao.exibir_informacoes()

# --- Livraria  ---
livro1 = Livro("Python para Iniciantes", "João Silva") #, 50.0
livro1.set_preco(50.0)

livro2 = Livro("Algoritmos Avançados", "Maria Oliveira") #, 80.0
livro2.set_preco(-80.0)
livro2.set_preco(80)

livro3 = Livro("Inteligência Artificial", "Ana Costa") #, 120.0
livro3.set_preco(120.0)

carrinho = CarrinhoDeCompras()

# Adicionando livros
carrinho.adicionar_livro(livro1)
carrinho.adicionar_livro(livro2)
carrinho.adicionar_livro(livro3)

# Exibindo itens no carrinho
carrinho.exibir_itens()

# Removendo um livro
carrinho.remover_livro("Algoritmos Avançados")

# Exibindo itens novamente
carrinho.exibir_itens()

# Tentando adicionar um livro já existente
carrinho.adicionar_livro(livro1)
