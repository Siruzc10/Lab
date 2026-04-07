
# 9. Crea una clase "Empleado" con propiedades para el nombre, la edad, el salario y el cargo, 
# y métodos para obtener y establecer estas propiedades, así como un método para calcular el salario anual.

class Empleado:
    def __init__(self, nombre, edad, salario, cargo):
        # Inicializo propiedades
        self.nombre = nombre
        self.edad = edad
        self.salario = salario
        self.cargo = cargo

    def obtener_nombre(self):
        return self.nombre

    def establecer_nombre(self, nombre_nuevo):
        self.nombre = nombre_nuevo

    def obtener_edad(self):
        return self.edad

    def establecer_edad(self, edad_nueva):
        self.edad = edad_nueva

    def obtener_salario(self):
        return self.salario
    
    def establecer_salario(self, salario_nuevo):
        self.salario = salario_nuevo

    def calcular_s_anual(self):
        return self.salario * 12
    
    def obtener_cargo(self):
        return self.cargo
    
    def establecer_cargo(self, cargo_nuevo):
        self.cargo = cargo_nuevo


if __name__ == "__main__":
    Empleado1 = Empleado("Pepe", 18, 900, "Cajero")

    print(f"Nombre: {Empleado1.obtener_nombre()}")
    print(f"Edad: {Empleado1.obtener_edad()}")
    print(f"Salario: {Empleado1.obtener_salario()}")
    print(f"Cargo: {Empleado1.obtener_cargo()}")
    print(f"Salario Anual: {Empleado1.calcular_s_anual()}")

   # Modificar valores
    print("\nNuevo Empleado:")
    nuevo_nombre = input("Nombre: ")
    nueva_edad = int(input("Edad: "))
    nuevo_salario = int(input("Salario: "))
    nuevo_cargo = input("Cargo: ")

    Empleado1.establecer_nombre(nuevo_nombre)
    Empleado1.establecer_edad(nueva_edad)
    Empleado1.establecer_salario(nuevo_salario)
    Empleado1.establecer_cargo(nuevo_cargo)

    print("\nDespues de actualizar:")
    print(f"Nombre: {Empleado1.obtener_nombre()}")
    print(f"Edad: {Empleado1.obtener_edad()}")
    print(f"Cargo: {Empleado1.obtener_cargo()}")
    print(f"Salario: {Empleado1.obtener_salario()}")
    print(f"Salario Anual: {Empleado1.calcular_s_anual()}")