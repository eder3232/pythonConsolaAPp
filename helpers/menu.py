from helpers.validacion_datos import leer_int


def menu():
    print('')
    print('Bienvenido al registro')
    print('')
    print('Que deeas hacer')
    print('1. Registrar un vehiculo')
    print('2. Borrar un vehiculo')
    print('3. Mostrar la base de datos')
    print('0. Salir')
    opt = leer_int("Escoja una opción. ")
    if opt < 0 or opt > 3:
        print('')
        input('Introduce un valor válido (presione enter para continuar) ')
        input('')
        menu()
    return opt


def detener_ejecucion():
    print('')
    print('Desea realizar otra operación: ')
    print('')
    print('1. Presiona "1" para continuar. ')
    print('0. Presiona "0" para salir. ')
    print('')
    opt = leer_int("Escoje una opción. ")
    if opt < 0 or opt > 1:
        print('')
        input('Introduce un valor válido (presione enter para continuar) ')
        print('')
        detener_ejecucion()
    return opt
