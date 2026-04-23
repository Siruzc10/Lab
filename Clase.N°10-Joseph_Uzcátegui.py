# 10
#Crea una clase llamada Circulo que tenga un atributo radio. 
#Implementa métodos para calcular el área y la circunferencia del círculo, y asegúrate de que el radio no pueda ser negativo.


import math

class Circulo:
    def __init__(self, radio):
        if radio > 0:
            self._radio = radio
        else:
            self._radio = 1

    
    def obtener_radio(self):
        return self._radio

    
    def establecer_radio(self, radio):
        if radio > 0:
            self._radio = radio
        else:
            print("Radio inválido")

    
    def area(self):
        return math.pi * self._radio ** 2

    def circunferencia(self):
        return 2 * math.pi * self._radio


# MAIN
if __name__ == "__main__":
    c = Circulo(5)

    print("Radio:", c.obtener_radio())
    print("Área:", c.area())
    print("Circunferencia:", c.circunferencia())

    nuevo_radio = float(input("\nNuevo radio: "))
    c.establecer_radio(nuevo_radio)

    print("\nDatos actualizados:")
    print("Radio:", c.obtener_radio())
    print("Área:", c.area())
    print("Circunferencia:", c.circunferencia())