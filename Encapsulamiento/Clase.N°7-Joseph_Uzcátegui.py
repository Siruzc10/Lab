# 7
#Crea una clase llamada Empleado con atributos nombre, salario y departamento. 
#Implementa un método que aumente el salario en un porcentaje dado y otro que muestre la información del empleado.


class Empleado:
    def __init__(self, nombre, salario, depto):
        self._nombre = nombre
        self._salario = salario
        self._depto = depto

    def aumentar_salario(self, porcentaje):
        if porcentaje > 0:
            self._salario += self._salario * porcentaje / 100

    def mostrar_info(self):
        return f"{self._nombre} - {self._salario} Departamento: {self._depto}"


if __name__ == "__main__":
    emp = Empleado("Tao", 100000, "IT")
    porc = float(input("Aumento %: "))
    emp.aumentar_salario(porc)
    print(emp.mostrar_info())
            