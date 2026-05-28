#Ejercicio 2

class Empleado:
    def __init__(self, nombre, salario, cargo):
        self.nombre = nombre
        self.salario = salario
        self.cargo = cargo

    def imprimir_detalles(self):
        print(f"Nombre: {self.nombre}")
        print(f"Cargo: {self.cargo}")
        print(f"Salario: ${self.salario}")


class Gerente(Empleado):
    def __init__(self, nombre, salario):
        super().__init__(nombre, salario, "Gerente")

    def calcular_aumento(self):
        return self.salario * 0.20

    def imprimir_detalles(self):
        super().imprimir_detalles()
        print(f"Aumento: ${self.calcular_aumento()}")


class EmpleadoTemporal(Empleado):
    def __init__(self, nombre, salario):
        super().__init__(nombre, salario, "Empleado Temporal")

    def calcular_aumento(self):
        return self.salario * 0.10

    def imprimir_detalles(self):
        super().imprimir_detalles()
        print(f"Aumento: ${self.calcular_aumento()}")


# MAIN
if __name__ == "__main__":

    g = Gerente("Carlos", 200000)
    g.imprimir_detalles()

    print()

    e = EmpleadoTemporal("Ana", 120000)
    e.imprimir_detalles()