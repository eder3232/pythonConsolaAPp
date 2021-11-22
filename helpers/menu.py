def menu():
    print('')
    print('Bienvenido al registro')
    print('')
    print('Que deeas hacer')
    print('1. Registrar un vehiculo')
    print('2. Borrar un vehiculo')
    print('3. Mostrar la base de datos')
    print('0. Salir')
    opt = int(input("Escoja una opción: "))
    if opt < 0 or opt > 3:
        print('')
        input('Introduce un valor válido (presione enter para continuar) ')
        input('')
        menu()
    return opt
