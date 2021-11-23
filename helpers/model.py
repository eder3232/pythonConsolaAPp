class Vehiculo:
    placa = ""
    marca = ""
    anio = 0
    precio = 0

    # creando el método constructor
    def __init__(self, placa, marca, anio, precio):
        self.placa = placa
        self.marca = marca
        self.anio = anio
        self.precio = precio
