"""Decorador para registrar a execução de funções em um log."""

from datetime import datetime


def registrar_log(func):
    """Decorador que registra a execução de uma função em um arquivo de log."""

    def wrapper(*args, **kwargs):
        with open('log.txt', 'a', encoding='utf8') as arquivo_log:
            data_hora = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            arquivo_log.write(f'[{data_hora}] A função {func.__name__} foi executada.\n')
        return func(*args, **kwargs)
    return wrapper

@registrar_log
def enviar_email(destinatario: str) -> None:
    """Simula o envio de um e-mail para o destinatário especificado."""

    print(f"Enviando e-mail para {destinatario}...")

@registrar_log
def calcular_salario(horas_trabalhadas: int, valor_hora: float) -> None:
    """Calcula o salário de um funcionário com base nas horas trabalhadas e no valor da hora."""

    print(f"O salário do funcionário é de {horas_trabalhadas * valor_hora}.")

if __name__ == "__main__":
    enviar_email("joao@example.com")
    calcular_salario(200, 30.5)
    enviar_email("joao@example.com")
