#Ejercicio 3

class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar_detalles(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")


class Perro(Animal):
    def emitir_sonido(self):
        return "Guau Guau"

    def mostrar_detalles(self):
        super().mostrar_detalles()
        print(f"Sonido: {self.emitir_sonido()}")


class Gato(Animal):
    def emitir_sonido(self):
        return "Miau"

    def mostrar_detalles(self):
        super().mostrar_detalles()
        print(f"Sonido: {self.emitir_sonido()}")


# MAIN
if __name__ == "__main__":

    perro = Perro("Max", 4)
    perro.mostrar_detalles()

    print()

    gato = Gato("Michi", 2)
    gato.mostrar_detalles()