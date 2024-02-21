class Seller:
    def __init__(self, nombre, lugar):
        self.nombre = nombre
        self.lugar = lugar

class Vehiculo:
    def __init__(self, marca, modelo, tipo, seller=None):
        self.marca = marca
        self.modelo = modelo
        self.tipo = tipo
        self.seller = seller

    def __str__(self):
        return f"{self.tipo.capitalize()} {self.marca} {self.modelo}"

    def set_seller(self, seller):
        self.seller = seller

def registrar_venta(vehiculo):
    with open("vehiculos_vendidos.txt", "a") as archivo:
        archivo.write(str(vehiculo) + "\n")

def main():
    seller1 = Seller("Concesionario X", "Ciudad X")
    seller2 = Seller("Concesionario Y", "Ciudad Y")

    carro1 = Carro("Toyota", "Corolla", seller=seller1)
    carro2 = Carro("Honda", "Civic", seller=seller2)

    registrar_venta(carro1)
    registrar_venta(carro2)

if __name__ == "__main__":
    main()

'''
Pseudocódigo
Definir una clase "Vendedor" con "atributos" de nombre y ubicación.
Definir una clase "Vehiculo" con "atributos" marca, modelo, tipo y vendedor.
Definir un "método" __str__ para la clase Vehiculo que devuelva una representación de cadena del objeto.
Definie un "método" set_seller para la clase Vehiculo que establece el atributo de vendedor del objeto.
Definir una función registrador_venta que tome un objeto vehículo como "argumento" y escriba su representación de cadena en un archivo llamado "vehiculos_vendidos.txt".
Definir una función principal que cree dos objetos Vendedor, vendedor1 y vendedor2, con nombres "Concesionario X" y "Concesionario Y" y ubicaciones "Ciudad X" y "Ciudad Y", respectivamente.
Crear dos objetos Carro, carro1 y carro2, con las marcas "Toyota" y "Honda", los modelos "Corolla" y "Civic" y los vendedores seller1 y seller2, respectivamente.
Llamar a la función registrar_venta con carro1 y carro2 como argumentos.
Llamar a la función principal si el script se ejecuta como programa principal.
'''