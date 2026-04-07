
# 3. Crea una clase "Producto" con propiedades para el nombre, el precio y el stock disponible, 
# y métodos para aumentar o disminuir el stock.

class Rectangulo:
    def __init__(self, longitud, anchura):
        # Inicializo las propiedades del rectángulo
        self.longitud = longitud
        self.anchura = anchura

    def obtener_longitud(self):
        return self.longitud

    def establecer_longitud(self, longitud_nueva):
        self.longitud = longitud_nueva

    def obtener_anchura(self):
        return self.anchura

    def establecer_anchura(self, anchura_nueva):
        self.anchura = anchura_nueva

    def calcular_area(self):
        # area = longitud * anchura
        return self.longitud * self.anchura

    def calcular_perimetro(self):
        # Perimetro = 2 * (longitud + anchura)
        return 2 * (self.longitud + self.anchura)


if __name__ == "__main__":
    # Creo instancia de Rectangulo
    rectangulo1 = Rectangulo(10, 5)

    # Mostrar propiedades
    print(f"Longitud: {rectangulo1.obtener_longitud()}")
    print(f"Anchura: {rectangulo1.obtener_anchura()}")

    # Mostrar los calculos
    print(f"Area: {rectangulo1.calcular_area()}")
    print(f"Perimetro: {rectangulo1.calcular_perimetro()}")

    # Modificar valores
    print("Establece nuevos valores")
    nueva_longitud = int(input("Longitud: "))
    nueva_anchura = int(input("Anchura: "))

    rectangulo1.establecer_longitud(nueva_longitud)
    rectangulo1.establecer_anchura(nueva_anchura)

    # Mostrar valores actualizados
    print("\nDespues de actualizar:")
    print(f"Longitud: {rectangulo1.obtener_longitud()}")
    print(f"Anchura: {rectangulo1.obtener_anchura()}")
    print(f"Area: {rectangulo1.calcular_area()}")
    print(f"Perímetro: {rectangulo1.calcular_perimetro()}")
 