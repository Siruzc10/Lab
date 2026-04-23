# 6
#Crea una clase llamada Rectángulo que tenga atributos base y altura. 
#Implementa métodos para calcular el área y el perímetro del rectángulo


class Rectangulo:
    def __init__(self, base, altura):
        if base > 0 and altura > 0:
            self._base = base
            self._altura = altura
        else:
            self._base = 1
            self._altura = 1


    def obtener_base(self):
        return self._base

    def obtener_altura(self):
        return self._altura


    def establecer_base(self, base):
        if base > 0:
            self._base = base
        else:
            print("Base inválida")

    def establecer_altura(self, altura):
        if altura > 0:
            self._altura = altura
        else:
            print("Altura inválida")


    def area(self):
        return self._base * self._altura

    def perimetro(self):
        return 2 * (self._base + self._altura)


# MAIN
if __name__ == "__main__":
    r = Rectangulo(5, 3)

    print("Base:", r.obtener_base())
    print("Altura:", r.obtener_altura())
    print("Área:", r.area())
    print("Perímetro:", r.perimetro())

    nueva_base = float(input("\nNueva base: "))
    nueva_altura = float(input("Nueva altura: "))

    r.establecer_base(nueva_base)
    r.establecer_altura(nueva_altura)

    print("\nDatos actualizados:")
    print("Área:", r.area())
    print("Perímetro:", r.perimetro())