"""Decorador para medir o tempo de execução de uma função."""

import time


def medir_tempo(func):
    """Decorador que mede o tempo de execução de uma função.

    Este decorador executa a função decorada cinco vezes e calcula o tempo total 
    necessário para concluir todas as execuções. Em seguida, exibe o tempo decorrido.
    """

    def wrapper(*args): # Permite passar argumentos para a função decorada
        inicio = time.time()
        for _ in range(5): # Executa a função 5 vezes para medir o tempo total
            func(*args)
        fim = time.time()

        print(f'A função "{func.__name__}" executou em {fim - inicio:.4f} segundos.')
    return wrapper
