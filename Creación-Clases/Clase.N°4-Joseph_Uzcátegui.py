# 4. Crea una clase "Rectángulo" con propiedades para la longitud y la anchura, 
# y métodos para calcular el área y el perímetro del rectángulo.

class Rectangulo:

    def __init__(self, longitud, anchura):
        self._longitud = longitud
        self._anchura = anchura

    def area(self):
        return self._longitud * self._anchura

    def perimetro(self):
        return 2 * (self._longitud + self._anchura)


if __name__ == "__main__":
    rect = Rectangulo(10, 5)

    print("Área:", rect.area())
    print("Perímetro:", rect.perimetro())
