#Ejercicio 7

class Instrumento:
    def __init__(self, nombre, material):
        self.nombre = nombre
        self.material = material

    def tipo_sonido(self):
        return "Sonido musical"

    def mostrar_info(self):
        print(f"Instrumento: {self.nombre}")
        print(f"Material: {self.material}")


class Guitarra(Instrumento):
    def __init__(self, material, cuerdas):
        super().__init__("Guitarra", material)
        self.cuerdas = cuerdas

    def tocar_nota(self):
        return "La guitarra está tocando una nota."

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Cuerdas: {self.cuerdas}")
        print(self.tocar_nota())


class Piano(Instrumento):
    def __init__(self, material, teclas):
        super().__init__("Piano", material)
        self.teclas = teclas

    def tocar_nota(self):
        return "El piano está tocando una nota."

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Teclas: {self.teclas}")
        print(self.tocar_nota())


# MAIN
if __name__ == "__main__":

    guitarra = Guitarra("Madera", 6)
    guitarra.mostrar_info()

    print()

    piano = Piano("Madera", 88)
    piano.mostrar_info()