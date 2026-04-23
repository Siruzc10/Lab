# 8
#Crea una clase llamada Producto que tenga atributos nombre, precio y stock. 
#Implementa métodos para aumentar y disminuir el stock, asegurándote de que no se pueda tener un stock negativo.


class Producto:
    def __init__(self, nombre, precio, stock):
        self._nombre = nombre
        self._precio = precio
        self._stock = stock

    def aumentar_stock(self, cant):
        if cant > 0:
            self._stock += cant

    def disminuir_stock(self, cant):
        if 0 < cant <= self._stock:
            self._stock -= cant


if __name__ == "__main__":
    p = Producto("Mouse", 5000, 10)
    cant = 0
    x = []
    while x != 0:
        print("Ingrese 1 para disminuir Stock.\n")
        print("Ingrese 2 para aumentar Stock.\n")
        print("Ingrese 0 para finalizar.\n")
        x = int(input("Ingrese la opción: "))
        
        if x == 1:
            cant = int(input("Quitar stock: "))
            p.disminuir_stock(cant)
            print("Stock:", p._stock)
        elif x == 2:
            cant = int(input("Aumentar stock: "))
            p.aumentar_stock(cant)
            print("Stock: ", p._stock)
        else: 
            break
            