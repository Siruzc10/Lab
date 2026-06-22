# Clase base
class Animal:
    def hacerSonido(self):
        raise NotImplementedError(
            "Este método debe ser sobrescrito por las subclases"
        )


# Clase Perro
class Perro(Animal):

    def hacerSonido(self):
        return "Guau"


# Clase Gato
class Gato(Animal):

    def hacerSonido(self):
        return "Miau"


# Función principal
def main():

    animales = [
        Perro(),
        Gato(),
        Perro(),
        Gato()
    ]

    for animal in animales:
        print(
            f"{animal.__class__.__name__}: "
            f"{animal.hacerSonido()}"
        )


if __name__ == "__main__":
    main()