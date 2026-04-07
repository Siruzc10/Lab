
# 6. Crea una clase "Estudiante" con propiedades para el nombre, la edad y la carrera, 
# y métodos para obtener y establecer estas propiedades, 
# así como un método para calcular la nota media de un conjunto de exámenes.

class Estudiante:
    def __init__(self, nombre, edad, carrera):
        # Inicializo propiedades
        self.nombre = nombre
        self.edad = edad
        self.carrera = carrera

    def obtener_nombre(self):
        return self.nombre

    def establecer_nombre(self, nombre_nuevo):
        self.nombre = nombre_nuevo

    def obtener_edad(self):
        return self.edad

    def establecer_edad(self, edad_nueva):
        self.edad = edad_nueva

    def obtener_carrera(self):
        return self.carrera
    
    def establecer_carrera(self, carrera_nueva):
        self.carrera = carrera_nueva

    
    def calcular_nota_media(self, notas):
        if len(notas) == 0:
            return 0
        return sum(notas) / len(notas)

if __name__ == "__main__":
    # Creo instancia
    estudiante1 = Estudiante("Joseph", 17, "Programador")

    # Mostrar propiedades
    print(f"Nombre: {estudiante1.obtener_nombre()}")
    print(f"Edad: {estudiante1.obtener_edad()}")
    print(f"Carrera: {estudiante1.obtener_carrera()}")
    print("Nota media: 9")

    # Modificar valores
    print("Establece un Nuevo Alumno:")
    nuevo_nombre = input("Nombre: ")
    nueva_edad = int(input("Edad: "))
    nueva_carrera =  input("Carrera: ")

    estudiante1.establecer_nombre(nuevo_nombre)
    estudiante1.establecer_edad(nueva_edad)
    estudiante1.establecer_carrera(nueva_carrera)

    notas = []
    print("\nIngrese las notas (ingrese -1 para terminar):")

    while True:
        nota = float(input("Nota: "))
        if nota == -1:
            break
        notas.append(nota)


    # Mostrar valores actualizados
    print("\nDespués de actualizar:")
    print(f"Nombre:{estudiante1.obtener_nombre()}")
    print(f"Edad: {estudiante1.obtener_edad()}")
    print(f"Carrera: {estudiante1.obtener_carrera()}")
    print(f"Nota media: {estudiante1.calcular_nota_media(notas)}")