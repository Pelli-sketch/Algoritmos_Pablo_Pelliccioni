class Seller:
    def __init__(self, name, location):
        self.nombre = nombre
        self.lugar = lugar

class Vehiculo:
    def __init__(self, marca, modelo, tipo, seller=None):
        self.marca = marca
        self.modelo = modelo
        self.tipo = tipo
        self.seller = seller

    def __str__(self):
        return f"{self.tipo.capitalize()} {self.marca} {self.modelo} ({self.seller.name}, {self.seller.location})"

    def set_seller(self, seller):
        self.seller = seller

def registrar_venta(vehiculo):
    with open("vehiculos_vendidos.txt", "a") as archivo:
        archivo.write(str(vehiculo) + "\n")

def main():
    name = input("Nombre del concesionario: ")
    location = input("Lugar donde se ubica el concesionario: ")
    seller = Seller(name, location)

    marca = input("Marca del Vehículo: ")
    modelo = input("Modelo del Vehículo: ")
    tipo = input("Tipo de Vehículo (carro, barco, avion): ")

    carro = Vehiculo(marca, modelo, tipo, seller=seller)

    registrar_venta(carro)

if __name__ == "__main__":
    main()

'''
>Definir una clase Vendedor con los siguientes atributos:
- nombre: una cadena que representa el nombre del vendedor.
- ubicación: una cadena que representa la ubicación del vendedor.
>Definir una clase Vehiculo con los siguientes atributos:
- marca: Una cadena que representa la marca del vehículo.
- modelo: Una cadena que representa el modelo del vehículo.
- tipo: Una cadena que representa el tipo de vehículo (por ejemplo, "carro", "barco", "avion").
- vendedor: una instancia opcional de la clase Vendedor que representa al vendedor del vehículo.
>Definir un método __str__ para la clase Vehiculo que devuelva una representación en cadena del objeto en el siguiente formato: -tipo- -marca- -modelo- (-vendedor.nombre-, -vendedor.ubicación-).
>Definir un método set_seller para la clase Vehiculo que establece el atributo de vendedor del objeto.
>Definir una función registrador_venta que tome una instancia de la clase Vehiculo como argumento y escriba su representación de cadena en un archivo llamado vehiculos_vendidos.txt.
>Definir una función principal que realice los siguientes pasos:
>Solicitar al usuario que ingrese el nombre y la ubicación del vendedor y cree una instancia de la clase Vendedor con esas entradas.
>Solicitar al usuario que ingrese la marca, modelo y tipo del vehículo y cree una instancia de la clase Vehiculo con esas entradas y la instancia del Vendedor como vendedor.
>Llamar a la función registrar_venta con la instancia de Vehiculo como argumento.
'''