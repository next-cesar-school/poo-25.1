"""Representação do Login."""

class SistemaLogin:
    """Classe que implementa um sistema básico de login."""

    def __init__(self, arquivo_usuarios: str) -> None:
        """Inicializa o sistema com o caminho do arquivo de usuários."""

        self.arquivo_usuarios = arquivo_usuarios

    def cadastrar(self, usuario: str, senha: str) -> None:
        """Cadastra um novo usuário e senha no arquivo."""

        with open(self.arquivo_usuarios, 'a', encoding='utf8') as f:
            f.write(f'{usuario},{senha}\n')

    def autenticar(self, usuario: str, senha: str) -> bool:
        """Autentica um usuário verificando nome e senha.
        Retorna True se as credenciais estiverem corretas, False caso contrário.
        """

        with open(self.arquivo_usuarios, 'r', encoding='utf8') as f:
            for linha in f:
                u, s = linha.strip().split(',')
                if u == usuario and s == senha:
                    return True
        return False
