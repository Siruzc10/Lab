#Ejercicio 4

class Vehiculo:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año

    def mostrar_info(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Año: {self.año}")


class Automovil(Vehiculo):
    def __init__(self, marca, modelo, año, km_litro):
        super().__init__(marca, modelo, año)
        self.km_litro = km_litro

    def combustible_necesario(self, distancia):
        return distancia / self.km_litro

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Eficiencia: {self.km_litro} km/l")


class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, año, km_litro):
        super().__init__(marca, modelo, año)
        self.km_litro = km_litro

    def combustible_necesario(self, distancia):
        return distancia / self.km_litro

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Eficiencia: {self.km_litro} km/l")


# MAIN
if __name__ == "__main__":

    auto = Automovil("Toyota", "Corolla", 2022, 15)
    auto.mostrar_info()
    print("Combustible necesario:", auto.combustible_necesario(300), "litros")

    print()

    moto = Motocicleta("Honda", "CBR", 2021, 25)
    moto.mostrar_info()
    print("Combustible necesario:", moto.combustible_necesario(300), "litros")