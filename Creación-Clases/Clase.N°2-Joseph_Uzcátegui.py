
# 3. Crea una clase "Producto" con propiedades para el nombre, el precio y el stock disponible, 
# y métodos para aumentar o disminuir el stock.

class Producto:
    def __init__(self, nombre, precio, stock_disponible):
        
        self.nombre = nombre                    
        self.precio = precio
        self.stock_disponible = stock_disponible

    def obtener_nombre(self):
        return self.nombre

    def obtener_precio(self):
        return self.precio

    def obtener_stock_disponible(self):
        return self.stock_disponible

    def establecer_stock_disponible(self, nuevo_stock):
        self.stock_disponible = nuevo_stock




if __name__ == "__main__":
    # Creo instancia
    producto1 = Producto("PS5", 1200, "20")

    # Obtener / mostrar las propiedades
    print(f"Nombre: {producto1.obtener_nombre()}")
    print(f"Precio: {producto1.obtener_precio()}")
    print(f"Stock Disponible: {producto1.obtener_stock_disponible()}")

    nuevo_stock = int(input("Nueva cantidad en el stock: "))

    # Establecer nuevas propiedades
    producto1.establecer_stock_disponible(nuevo_stock)

    # Mostrar las propiedades actualizadas
    print("\nDespués de actualizar:")
    print(f"Nombre: {producto1.obtener_nombre()}")
    print(f"Precio: {producto1.obtener_precio()}")
    print(f"Stock Disponible: {producto1.obtener_stock_disponible()}")
 