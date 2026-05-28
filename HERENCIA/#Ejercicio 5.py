#Ejercicio 5

from datetime import datetime

class Producto:
    def __init__(self, nombre, precio, fecha_vencimiento):
        self.nombre = nombre
        self.precio = precio
        self.fecha_vencimiento = fecha_vencimiento

    def mostrar_info(self):
        print(f"Producto: {self.nombre}")
        print(f"Precio: ${self.precio}")


class ProductoAlimenticio(Producto):
    def aplicar_descuento(self):
        return self.precio * 0.15

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Descuento: ${self.aplicar_descuento()}")


class ProductoElectronico(Producto):
    def aplicar_descuento(self):
        return self.precio * 0.05

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Descuento: ${self.aplicar_descuento()}")


# MAIN
if __name__ == "__main__":

    alimento = ProductoAlimenticio("Leche", 2500, "2026-06-10")
    alimento.mostrar_info()

    print()

    pc = ProductoElectronico("Notebook", 900000, "2030-01-01")
    pc.mostrar_info()