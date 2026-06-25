
# 8. Crea una clase "Tienda" con propiedades para el nombre de la tienda y una lista de productos disponibles, 
# y métodos para añadir o eliminar productos de la lista y para obtener la lista completa de productos.

class Tienda:

    def __init__(self, nombre):
        self._nombre = nombre
        self._productos = []

    def agregar_producto(self, producto):
        self._productos.append(producto)

    def eliminar_producto(self, producto):
        if producto in self._productos:
            self._productos.remove(producto)

    def obtener_productos(self):
        return self._productos


if __name__ == "__main__":
    tienda = Tienda("Mi Tienda")

    tienda.agregar_producto("Mouse")
    tienda.agregar_producto("Teclado")

    print(tienda.obtener_productos())
