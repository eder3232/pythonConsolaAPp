from helpers.menu import menu


def main():

    opt = ""
    while True:
        opt = menu()

        if opt == 1:
            # registrar vehiculo
            registrar_vehiculo()
        elif opt == 2:
            # borrar placa
            borrar_placa()
        elif opt == 3:
            # mostrar database
            mostrar_database()
        elif opt == 0:
            break
    return ""


main()
