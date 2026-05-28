#Ejercicio 6

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")


class Estudiante(Persona):
    def __init__(self, nombre, edad, carrera):
        super().__init__(nombre, edad)
        self.carrera = carrera

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Carrera: {self.carrera}")


class Profesor(Persona):
    def __init__(self, nombre, edad, materia):
        super().__init__(nombre, edad)
        self.materia = materia

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Materia: {self.materia}")


# MAIN
if __name__ == "__main__":

    e = Estudiante("Lucas", 20, "Programación")
    e.mostrar_info()

    print()

    p = Profesor("María", 45, "Matemática")
    p.mostrar_info()