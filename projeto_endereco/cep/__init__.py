"""CEP - Código de Endereçamento Postal

Este módulo coleta dados da API ViaCEP para o preenchimento automático dos campos
de logradouro, bairro, cidade e estado.

Depende de conexão com a internet.
"""

import socket


def verificar_conexao() -> None:
    """Verifica a conexão com a internet. Tenta se conectar ao Google DNS (8.8.8.8).

    Lança:
        ConnectionError: Se não houver conexão com a internet.
    """

    try:
        socket.create_connection(("8.8.8.8", 53))
    except OSError as exc:
        # Relança a exceção original OSError (exc) como causa, permitindo rastrear a origem do erro
        raise ConnectionError("Sem conexão com a internet.") from exc


# Executa a verificação ao importar o pacote
verificar_conexao()
