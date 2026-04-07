
# 5. Crea una clase "Círculo" con propiedades para el radio y el diámetro, 
# y métodos para calcular el área y la circunferencia del círculo.

class Circulo:
    def __init__(self, radio):
        # Inicializo la propiedad del circulo
        self.radio = radio

    def obtener_radio(self):
        return self.radio

    def establecer_radio(self, radio_nuevo):
        self.radio = radio_nuevo

    def obtener_diametro(self):
        return self.radio * 2

    def calcular_area(self):
        # pi * radio al cuadrado
        return 3.1416 * (self.radio ** 2)

    def calcular_circunferencia(self):
        # 2 * pi * radio
        return 2 * 3.1416 * self.radio


if __name__ == "__main__":
    # Creo instancia
    circulo1 = Circulo(5)

    print(f"Radio: {circulo1.obtener_radio()}")
    print(f"Diámetro: {circulo1.obtener_diametro()}")

    print(f"Área: {circulo1.calcular_area()}")
    print(f"Circunferencia: {circulo1.calcular_circunferencia()}")

    print("Establece nuevo radio")
    nuevo_radio = int(input("Radio: "))
    circulo1.establecer_radio(nuevo_radio)

    print("\nDespués de actualizar:")
    print(f"Radio: {circulo1.obtener_radio()}")
    print(f"Diámetro: {circulo1.obtener_diametro()}")
    print(f"Área: {circulo1.calcular_area()}")
    print(f"Circunferencia: {circulo1.calcular_circunferencia()}")