# 5
#Crea una clase llamada Estudiante que tenga atributos como nombre, edad y notas (una lista de números). 
#Implementa métodos para agregar una nota y calcular el promedio de las notas.


class Estudiante:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad
        self._notas = []

    def agregar_nota(self, nota):
        if 0 <= nota <= 10:
            self._notas.append(nota)

    def promedio(self):
        if len(self._notas) == 0:
            return 0
        return sum(self._notas) / len(self._notas)


if __name__ == "__main__":
    e = Estudiante("Paulo", 18)

    for i in range(3):
        nota = float(input("Nota: "))
        e.agregar_nota(nota)

    print("Promedio:", e.promedio())