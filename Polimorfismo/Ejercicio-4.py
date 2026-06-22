# Clase base
class Empleado:

    def calcularSalario(self):
        raise NotImplementedError(
            "Este método debe ser sobrescrito por las subclases"
        )


# Clase EmpleadoPorHora
class EmpleadoPorHora(Empleado):

    def __init__(self, horas, pago_hora):
        self.horas = horas
        self.pago_hora = pago_hora

    def calcularSalario(self):
        return self.horas * self.pago_hora


# Clase EmpleadoFijo
class EmpleadoFijo(Empleado):

    def __init__(self, salario):
        self.salario = salario

    def calcularSalario(self):
        return self.salario


# Función principal
def main():

    empleados = [
        EmpleadoPorHora(40, 2000),
        EmpleadoFijo(150000),
        EmpleadoPorHora(30, 1800)
    ]

    total = 0

    for empleado in empleados:

        salario = empleado.calcularSalario()

        print(
            f"{empleado.__class__.__name__}: "
            f"${salario}"
        )

        total += salario

    print(f"\nSalario total: ${total}")


if __name__ == "__main__":
    main()