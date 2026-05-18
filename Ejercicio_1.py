#Ejercicio 1: Clase Abstracta de Vehículo
#Crea una clase abstracta llamada Vehiculo que contenga métodos abstractos como mover() y detener(). 
#Luego, crea dos clases concretas, Coche y Bicicleta, que hereden de Vehiculo e implementen estos métodos.

#Objetivo: Entender cómo se puede definir una interfaz común para diferentes tipos de vehículos.



from abc import ABC, abstractmethod

# Clase abstracta
class Vehiculo(ABC):

    @abstractmethod
    def mover(self):
        pass

    @abstractmethod
    def detener(self):
        pass


# Clase concreta
class Coche(Vehiculo):

    def mover(self):
        return "El coche está andando"

    def detener(self):
        return "El coche se frenó"


# Clase concreta
class Bicicleta(Vehiculo):

    def mover(self):
        return "La bicicleta está en movimiento"

    def detener(self):
        return "La bicicleta se detuvo"


# MAIN
if __name__ == "__main__":

    coche = Coche()
    bicicleta = Bicicleta()

    print(coche.mover())
    print(coche.detener())

    print(bicicleta.mover())
    print(bicicleta.detener())