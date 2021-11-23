from typing import Counter
from helpers.mostrar_database import mostrar_database
from helpers.menu import detener_ejecucion
import os
def clear(): return os.system('cls')


def borrar_placa(database):
    clear()
    while True:
        mostrar_database(database)
        print('')
        placa_borrar = input(
            'Inserte la placa del vehículo que desea borrar: ')

        response = database.pop(placa_borrar, False)
        if(response != False):
            print('El vehiculo con la placa: ',
                  response, ' ha sido eliminado.')
            return response
        else:
            print('')
            print('Ingrese una placa válida')
            continuar = detener_ejecucion()
            if continuar == 0:
                break


# database = {"eder": 23, "zxc": 456}

# print(borrar_placa(database))
# print(database)
