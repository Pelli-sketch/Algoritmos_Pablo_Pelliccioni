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
    def __init__(self, marca, modelo, eslora, capacidad):
        super().__init__(marca, modelo, "barco")
        self.eslora = eslora
        self.capacidad = capacidad

    def __str__(self):
        return super().__str__() + f" (Eslora: {self.eslora} m, Capacidad: {self.capacidad} personas)"

class Avion(Vehiculo):
    def __init__(self, marca, modelo, capacidad):
        super().__init__(marca, modelo, "avion")
        self.capacidad = capacidad

    def __str__(self):
        return super().__str__() + f" (Capacidad: {self.capacidad} personas)"

def registrar_vehiculo(vehiculo):
    with open("vehiculos.txt", "a") as archivo:
        archivo.write(str(vehiculo) + "\n")

def main():
    carro1 = Carro("Toyota", "Corolla")
    carro2 = Carro("Honda", "Civic")
    registrar_vehiculo(carro1)
    registrar_vehiculo(carro2)

    barco1 = Barco("Yamaha", "2000", 20, 10)
    barco2 = Barco("Bayliner", "3000", 30, 20)
    registrar_vehiculo(barco1)
    registrar_vehiculo(barco2)

    avion1 = Avion("Boeing", "737", 180)
    avion2 = Avion("Airbus", "A320", 200)
    registrar_vehiculo(avion1)
    registrar_vehiculo(avion2)

if __name__ == "__main__":
    main()