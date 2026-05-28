#Ejercicio 9

class Tienda:
    def __init__(self, nombre):
        self.nombre = nombre
        self.inventario = []
        self.ventas = 0

    def agregar_producto(self, producto):
        self.inventario.append(producto)

    def eliminar_producto(self, producto):
        if producto in self.inventario:
            self.inventario.remove(producto)

    def calcular_ventas(self, monto):
        self.ventas += monto

    def mostrar_info(self):
        print(f"Tienda: {self.nombre}")
        print(f"Inventario: {self.inventario}")
        print(f"Ventas totales: ${self.ventas}")


class TiendaRopa(Tienda):
    def mostrar_info(self):
        print("=== Tienda de Ropa ===")
        super().mostrar_info()


class TiendaElectronica(Tienda):
    def mostrar_info(self):
        print("=== Tienda Electrónica ===")
        super().mostrar_info()


# MAIN
if __name__ == "__main__":

    ropa = TiendaRopa("PRADA")
    ropa.agregar_producto("Remera")
    ropa.agregar_producto("Pantalón")
    ropa.calcular_ventas(50000)
    ropa.mostrar_info()

    print()

    electronica = TiendaElectronica("Tech Store")
    electronica.agregar_producto("Notebook")
    electronica.agregar_producto("Mouse")
    electronica.calcular_ventas(350000)
    electronica.mostrar_info()