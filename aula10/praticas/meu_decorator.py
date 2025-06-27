def marcador(func):
    def wrapper():
        print(f'=== Início da função: {func.__name__} ===')
        func()
        print('=== Fim da função ===')
    return wrapper


@marcador
def ola():
    print('Oi, meu nome é Erick')

@marcador
def eita():
    print(10 + 5)

@marcador
def oxe():
    print(f'Olha que massa isso aqui: {__name__}')

ola()
eita()
oxe()
