from helpers.model import Vehiculo
from helpers.validacion_datos import leer_float, leer_int
import os
def clear(): os.system('cls')


def registrar_vehiculo():
    clear()
    print('')
    placa = input('Introduce la placa del vehiculo: ')
    print('')
    marca = input('Introduce la marca del vehiculo: ')
    print('')
    anio = leer_int('Introduce el anio del vehiculo: ')
    print('')
    precio = leer_float('Introduce el precio del vehiculo: ')
    print('')
    nuevo_vehiculo = Vehiculo(placa, marca, anio, precio)
    return nuevo_vehiculo
