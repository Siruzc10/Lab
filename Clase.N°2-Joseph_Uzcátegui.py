# 2
#Crea una clase llamada Persona con atributos nombre, edad y sexo. 
#Implementa un método que permita cambiar la edad de la persona y otro que muestre la información de la persona.

class Persona:
    def __init__(self, nombre, edad, sexo):
        self._nombre = nombre
        self._edad = edad
        self._sexo = sexo

    def obtener_nombre(self):
        return self._nombre

    def obtener_edad(self):
        return self._edad

    def establecer_edad(self, edad):
        if edad > 0:
            self._edad = edad

    def mostrar_info(self):
        return f"{self._nombre} - {self._edad} - {self._sexo}"


if __name__ == "__main__":
    p = Persona("Juan", 20, "Masculino")
    print(p.mostrar_info())

    edad = int(input("Nueva edad: "))
    p.establecer_edad(edad)
    print(p.mostrar_info())