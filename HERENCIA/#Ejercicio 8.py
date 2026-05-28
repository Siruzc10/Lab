#Ejercicio 8

class Transporte:
    def __init__(self, capacidad, velocidad_maxima):
        self.capacidad = capacidad
        self.velocidad_maxima = velocidad_maxima

    def mostrar_info(self):
        print(f"Capacidad: {self.capacidad} pasajeros")
        print(f"Velocidad máxima: {self.velocidad_maxima} km/h")


class Avion(Transporte):
    def calcular_tiempo_viaje(self, distancia):
        return distancia / self.velocidad_maxima

    def mostrar_info(self):
        print("=== Avión ===")
        super().mostrar_info()


class Barco(Transporte):
    def calcular_tiempo_viaje(self, distancia):
        return distancia / self.velocidad_maxima

    def mostrar_info(self):
        print("=== Barco ===")
        super().mostrar_info()


# MAIN
if __name__ == "__main__":

    avion = Avion(180, 900)
    avion.mostrar_info()
    print("Tiempo de viaje:", avion.calcular_tiempo_viaje(1800), "horas")

    print()

    barco = Barco(500, 80)
    barco.mostrar_info()
    print("Tiempo de viaje:", barco.calcular_tiempo_viaje(800), "horas")