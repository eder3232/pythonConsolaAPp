import os
def clear(): return os.system('cls')


def mostrar_database(database):
    clear()
    print('')
    print('Database')
    print('')
    for key in database:
        print("Placa: ", database[key].placa,
              "|| Marca: ", database[key].marca, " || Año: ", database[key].anio, ' || Precio: ', database[key].precio)
