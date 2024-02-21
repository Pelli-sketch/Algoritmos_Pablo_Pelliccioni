class Vehiculo:
    def __init__(self, marca, modelo, tipo):
        self.marca = marca
        self.modelo = modelo
        self.tipo = tipo

    def __str__(self):
        return f"{self.tipo.capitalize()} {self.marca} {self.modelo}"

class Carro(Vehiculo):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo, "carro")

class Barco(Vehiculo):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo, "barco")

class Avion(Vehiculo):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo, "avion")

def registrar_vehiculo(vehiculo):
    with open("vehiculos.txt", "a") as archivo:
        archivo.write(str(vehiculo) + "\n")

def main():
    carro1 = Carro("Toyota", "Corolla")
    carro2 = Carro("Honda", "Civic")
    registrar_vehiculo(carro1)
    registrar_vehiculo(carro2)

    barco1 = Barco("Yamaha", "2000")
    barco2 = Barco("Bayliner", "3000")
    registrar_vehiculo(barco1)
    registrar_vehiculo(barco2)

    avion1 = Avion("Boeing", "737")
    avion2 = Avion("Airbus", "A320")
    registrar_vehiculo(avion1)
    registrar_vehiculo(avion2)

if __name__ == "__main__":
    main()