from helpers.menu import menu, detener_ejecucion
from helpers.registrar_vehiculo import registrar_vehiculo
from helpers.borrar_placa import borrar_placa
from helpers.mostrar_database import mostrar_database
import os
def clear(): return os.system('cls')


def main():
    database = {}
    opt = ""

    while True:
        clear()
        opt = menu()

        if opt == 1:
            # registrar vehiculoe
            nuevo_vehiculo = registrar_vehiculo()
            database[nuevo_vehiculo.placa] = nuevo_vehiculo
        elif opt == 2:
            # borrar placa
            borrar_placa(database)
        elif opt == 3:
            # mostrar database
            mostrar_database(database)
            continuar = detener_ejecucion()
            if(continuar == 0):
                break
        elif opt == 0:
            clear()
            break
    return ""


main()
