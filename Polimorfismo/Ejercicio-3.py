# Clase base
class Vehiculo:

    def mover(self):
        raise NotImplementedError(
            "Este método debe ser sobrescrito por las subclases"
        )


# Clase Coche
class Coche(Vehiculo):

    def mover(self):
        return "El coche se mueve por la carretera."


# Clase Bicicleta
class Bicicleta(Vehiculo):

    def mover(self):
        return "La bicicleta se mueve pedaleando."


# Función principal
def mostrar_movimiento(vehiculos):

    for vehiculo in vehiculos:
        print(
            f"{vehiculo.__class__.__name__}: "
            f"{vehiculo.mover()}"
        )


def main():

    vehiculos = [
        Coche(),
        Bicicleta(),
        Coche(),
        Bicicleta()
    ]

    mostrar_movimiento(vehiculos)


if __name__ == "__main__":
    main()