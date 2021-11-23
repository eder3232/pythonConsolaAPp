def leer_int(arg):
    while True:
        entrada = input(arg)
        try:
            entrada_int = int(entrada)
            return entrada_int
        except ValueError:
            print("ATENCIÓN: Debe ingresar un numero entero.")


def leer_float(arg):
    while True:
        entrada = input(arg)
        try:
            entrada_float = float(entrada)
            return entrada_float
        except ValueError:
            print('ATENCIÓN: Debe ingresar un número.')
