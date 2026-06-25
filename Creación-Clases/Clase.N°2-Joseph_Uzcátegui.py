
# 2. Crea una clase "Coche" con propiedades para la marca, el modelo y el año de fabricación, 
# y un método para obtener el número de años que ha pasado desde que se fabricó el coche.

from datetime import datetime

class Coche:

    def __init__(self, marca, modelo, año):
        self._marca = marca
        self._modelo = modelo
        self._año = año

    def obtener_marca(self):
        return self._marca

    def obtener_modelo(self):
        return self._modelo

    def obtener_año(self):
        return self._año

    def años_transcurridos(self):
        return datetime.now().year - self._año


if __name__ == "__main__":
    coche = Coche("Toyota", "Corolla", 2020)

    print("Marca:", coche.obtener_marca())
    print("Años:", coche.años_transcurridos())
