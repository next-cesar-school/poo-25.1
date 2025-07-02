# NExT | **Programação Orientada a Objetos** com Python

![CESAR School](/cesar_school.png)

## Aula 12 - Portifólio de Projetos

### Na aula de hoje

- Revisar os projetos que foram desenvolvidos durante a disciplina
- Novo Projeto: Análise de Dados

------------------

## Objetivo

Parabéns por chegarem à reta final do módulo de Programação Orientada a Objetos com Python!

Esta aula consolida todos os conceitos de POO aprendidos ao longo do curso, testes unitários, dunder methods, type hints, tratamento de exceções, integração com APIs externas e boas práticas de código, por meio da montagem de um portifólio técnico, com diversos projetos no GitHub.

## Check-list: o que você deve fazer em todos os projetos

- [ ] Tudo baseado em OO
- [ ] Design de código: revise seu código buscando eventuais melhorias em como você realizou as relações entre as classes, nomes de variáveis, nomes de métodos, estruturas de repetição
- [ ] Documentação completa: documente os módulos, classes e os métodos públicos de forma adequada; ([PEP 257](https://peps.python.org/pep-0257/))
- [ ] Use PEP 8 ou Formatadores Lint
- [ ] Type Hints completos
- [ ] 0 alertas e 0 erros de lint
- [ ] Métodos especiais quando fizer sentido (`__str__`, `__repr__`, ordenação...)
- [ ] Tratamento claro de exceções: implemente Exceções personalizadas, trazendo mais robustez para seu código;
- [ ] Testes unitários usando unittest (cobertura mínima 80 %).
- [ ] README.md bem estruturado: explique do que se trata o projeto e pontue que você está iniciando seus estudos em programação;
- [ ] Versione o código com cuidado, usando mensagens de commit claras e bem estruturadas;
- [ ] LinkedIn: registre esta sua conquista no LinkedIn fazendo uma postagem com texto breve, explicando o que você aprendeu com o projeto, e adicionando um link para o repositório.
- [ ] Impressione pela excelência!

### 🧾 Projeto 1: NPS

Calculadora do Net Promoter Score, com importação de respostas e geração de relatório.

| | |
| - | - |
|👨‍🏫|Aula 3|
|💎|Mostra domínio de classes básicas e encapsulamento em métrica de negócio real, com manipulação de arquivos e modularização|
|🧩|Use Dunder Methods e Decorators para deixar a classe NPS o mais robusta|

### 📚 Projeto 2: Livraria/Biblioteca

Cadastro de livros, autores e estoque, incluindo regras de empréstimo/devolução.

| | |
| - | - |
|👨‍🏫|Aula 3|
|💎|Demonstra modelagem de objetos compostos, listas/dicionários e regras de negócio|
|🧩|Crie uma classe abstrata para leitura e escrita dos dados. Implemente agora com manipulação de arquivos|

### 🕹️ Projeto 3: Aventura Polimórfica

Mini-jogo de texto baseado tem turnos.

| | |
| - | - |
|👨‍🏫|Aula 5|
|💎|Vitrine clara de polimorfismo e extensibilidade (ponto-chave para dev de jogos)|
|🧩|Permita a customização de atributos do herói por tipos de personagem (Guerreiro, Mago e Arqueiro), o que vai influenciar nos seus atributos|

### 🗺️ Projeto 4: Endereço

Classe que normaliza CEPs, integra com ViaCEP e permite a geração de entereços.

| | |
| - | - |
|👨‍🏫|Aulas 8 e 9|
|💎|Evidencia o uso de APIs externas|
|🧩|Formate este projeto como um módulo utilitário, que pode ser importado em qualquer sistema|

### 🙋 Projeto 5: CPF

Validador/formatador de CPF com cálculo de dígitos verificadores.

| | |
| - | - |
|👨‍🏫|Aula 9|
|💎|Exercício clássico de algoritmos + testes unitários|
|🧩|Foque em otimizações. Deixe o algoritmo o mais enxuto possível. Use Dunder Methods e Decorators|

### ⏱️ Projeto 6: Medidor de Tempo

Decorator que mede tempo de execução de funções.

| | |
| - | - |
|👨‍🏫|Aula 10|
|💎|Demonstra preocupação com performance|
|🧩|Desenvolva um relatório apresentando os resultados dos testes com manipulação de listas com `for`, `while`, `lambda` e `list comprehension`|

### 📝 Projeto 6: LOG do Sistema em Arquivo

Handler customizado que grava logs JSON em arquivos.

| | |
| - | - |
|👨‍🏫|Aula 10|
|💎|Mostra boas práticas de observabilidade exigidas em produção|
|🧩|Crie exemplos de uso e casos de teste elaborados|

### 🔥 Projeto 7: FORJA Contatos

Gerenciamento de status de desenvolvedores, jogos e Game Studios.

| | |
| - | - |
|👨‍🏫|Aulas 2, 4 e 7|
|💎|Baseado em problema real que une parsing, OO e validação de dados|
|🧩|Foque na arquitetura das informações e na automatização de ações. Liste todos os requisitos antes de começar a implementação|

### 📊 Projeto 8: Análise de Dados

Crie um sistema que analise os dados contidos no arquivo [lista_clientes.csv](/aula12/lista_clientes.csv) e, usando POO, implemente as seguintes _features_:

1. Normalização dos dados

    | Campo | Regras e validações|
    | ----- | ------------------ |
    | **Nome**        | • Extraia o **nome completo**, **primeiro nome** e **segundo nome**.<br>• Os nomes devem estar registrado em “Camel Case”, com preposições (“da”, “de”, “do”, “das”, “dos”, “e”), que devem estar em minúsculo. |
    | **Gênero**      | • Inferir pelo **primeiro nome**.<br>• Disponibilize **3 estratégias** de API: `genderize.io`, `genderapi.io`, `gender-api.com`.<br>• O usuário escolhe qual API usar em tempo de execução.<br>• Caso a API exija token, leia‐o de variável de ambiente (_pesquise sobre isso_). |
    | **Celular**     | • Formato final: `"DD 9XXXXXXXX"`.<br>• Se faltar **DDD**, infira‐o pelo **CEP** (dica: utilize o serviço ViaCEP).<br>• Se o dígito **9** estiver ausente, adicione-o.<br>• Campo vazio → adicionar nota em `observacoes`.<br>• Número inválido → adicionar nota em `observacoes`. |
    | **CPF**         | • Formato final: apenas dígitos (`XXXXXXXXXXX`).<br>• Valide dígitos verificadores; CPF inválido → nota em `observacoes`.  |
    | **CEP**         | • Formato final: apenas dígitos (`XXXXXXXX`).<br>• Use ViaCEP (ou equivalente) para obter **Bairro, Cidade, Estado**. |
    | **Observações** | • Liste problemas detectados (ex.: “CPF inválido”, “telefone ausente”). |

2. Arquivo de saída (`.json`)

    O arquivo de saída será em formato '.json' e deve conter uma lista de usuários, organizados por **ordem alfabética**, seguindo o modelo a seguir:

    ```json
    {
      "users":
        [
          {
            "nome_completo": "André de Bifur Gomes Ribeiro",
            "primeiro_nome": "André",
            "segundo_nome": "de Bifur",
            "genero": "male",
            "email": "andrebifur@testmail.org",
            "celular": "51 952127281",
            "interesse": "Desenvolvimento de Jogos Digitais",
            "cpf": "94097729828",
            "bairro": "Petrópolis",
            "cidade": "Porto Alegre",
            "estado": "RS",
            "observacoes": "CPF Inválido"
          },
          ...
        ]
    }
    ```

3. Relatório de saída

    Além do arquivo de saída, exiba no console uma análise dos dados processados, informando:

    - Distribuição de gênero: % de homens e mulheres
    - Distribuição geográfica: % por região
    - Qualidades dos dados: CPFs inválidos, números de telefones ausentes...
    - Percentual das áreas de interesse (geral)
    - Quais áreas de intersse são mais desejadas por homens e mulheres (percentual)

4. Estrutura

    ```text
    analise_dados/
    │
    ├── src/                        # Código-fonte da aplicação
    │   ├── models/                 # Classes que representam entidades de negócio
    │   │   ├── pessoa.py
    │   │   ├── endereco.py
    │   │   └── cpf.py
    │   ├── services/               # Regras de negócio que dependem de recursos externos
    │   │   ├── gender_service.py
    │   │   └── cpf_service.py
    │   ├── repo/                   # Funções responsáveis por ler/gravar dados
    │   │   ├── csv_repo.py
    │   │   └── json_repo.py
    │   └── main.py
    │
    ├── tests/                      # Testes unitários
    │   ├── test_cpf_service.py
    │   ├── test_phone_service.py
    │   ├── test_gender_service.py
    │   └── ...
    └── README.md
    ```

    > 💡 Sinta-se livre para adaptar.

5. Dicas

- Token de API
  - Algumas APIs exige o uso de Tokens (como senhas únicas para cada usuário);
  - Se esse for o caso, não versione o seu token no GitHub, use variáveis de ambiente ou alguma solução semelhante (`os.getenv()`);
- Limites de uso das APIs
  - Algumas APIs tem limite de uso mensal (100 requisições por mês);
  - Não ultrapassar esses limites, procure fazer testes com quantidades menores de dados, no lugar de testar sempre com o arquivo todo.
- Documentação:
  - Não negligencie o poder de uma boa documentação;
  - Explique de forma técnica a abordagem adotada para desenvolver este sistema no `README.md`

## 📤 Entrega da Atividade

Realize o envio do link público do repositório do **Projeto 8: Análise de Dados** no formulário disponível [aqui](https://forms.gle/asyy1JPMfR92Jfzv5).

## Achou pouco?

Segue uma lista com dezenas de ideias de apps que você pode desenvolver para continuar treinando: [App Ideas Collection](https://github.com/florinpop17/app-ideas)

![This Party's Over](/aula12/xepy.gif)

### Cabô 🥳

_🤳P.S.: link para nossa fotos [aqui](/aula12/next-2025.1-1.png) e [aqui](/aula12/next-2025.1-2.png)._
