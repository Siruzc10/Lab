
# 3. Crea una clase "Producto" con propiedades para el nombre, el precio y el stock disponible, 
# y métodos para aumentar o disminuir el stock.

class Producto:

    def __init__(self, nombre, precio, stock):
        self._nombre = nombre
        self._precio = precio
        self._stock = stock

    def aumentar_stock(self, cantidad):
        self._stock += cantidad

    def disminuir_stock(self, cantidad):
        if cantidad <= self._stock:
            self._stock -= cantidad

    def obtener_stock(self):
        return self._stock


if __name__ == "__main__":
    producto = Producto("Mouse", 5000, 10)

    producto.aumentar_stock(5)
    producto.disminuir_stock(3)

    print("Stock:", producto.obtener_stock())
 
