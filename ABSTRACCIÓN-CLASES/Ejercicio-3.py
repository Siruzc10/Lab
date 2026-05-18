# Ejercicio 3: Figuras Geométricas
# Crea una clase abstracta Figura con un método abstracto calcular_area(). 
# Luego, implementa dos clases concretas, Circulo y Rectangulo, que calculen el área según su propia lógica.

# Objetivo: Comprender cómo se puede utilizar la abstracción para definir operaciones comunes en diferentes tipos de figuras.


from abc import ABC, abstractmethod
import math

# Clase abstracta
class Figura(ABC):

    @abstractmethod
    def calcular_area(self):
        pass


# Clase concreta
class Circulo(Figura):

    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return math.pi * self.radio ** 2


# Clase concreta
class Rectangulo(Figura):

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura


# MAIN
if __name__ == "__main__":

    circulo = Circulo(5)
    rectangulo = Rectangulo(4, 6)

    print("Area del circulo:", circulo.calcular_area())
    print("Area del rectangulo:", rectangulo.calcular_area())