def dividir(a, b):
    if b == 0:
        raise ZeroDivisionError("Denominador não pode ser zero.")
    return a / b

dividir(10, 0)

try:
    dividir(10, 0)
except ZeroDivisionError as e:
    print(e)
    #print('Esquece isso, não teve nada aqui...')
