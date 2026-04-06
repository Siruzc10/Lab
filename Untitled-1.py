#2. Crea una clase "Coche" con propiedades para la marca, el modelo y el año de fabricación, y un método para obtener el número de años que ha pasado desde que se fabricó el coche.

class Coche:
    def __init__(self, marca, modelo, año_fabricacion):
        """Inicializa las propiedades del coche."""
        self.marca = marca                      # Establece la marca
        self.modelo = modelo                    # Establece el modelo
        self.anio_fabricacion = año_fabricacion  # Establece el año de fabricación

    def obtener_marca(self):
        """Devuelve la marca del coche."""
        return self.marca

    def establecer_marca(self, marca):
        """Establece una nueva marca para el coche."""
        self.marca = marca

    def obtener_modelo(self):
        """Devuelve el modelo del coche."""
        return self.modelo

    def establecer_modelo(self, modelo):
        """Establece un nuevo modelo para el coche."""
        self.modelo = modelo

    def obtener_año_fabricacion(self):
        """Devuelve el año de fabricación del coche."""
        return self.año_fabricacion

    def establecer_año_fabricacion(self, año):
        """Establece un nuevo año de fabricación para el coche."""
        self.anio_fabricacion = año

    def calcular_antiguedad(self, año_actual):
        """Devuelve los años transcurridos desde la fabricación del coche."""
        return año_actual - self.año_fabricacion


# Ejemplo de uso de la clase Coche
if __name__ == "__main__":
    # Crear una instancia de Coche
    coche1 = Coche("Toyota", "Corolla", 2015)

    # Definir año actual manualmente
    año_actual = 2026

    # Obtener y mostrar las propiedades
    print(f"Marca: {coche1.obtener_marca()}")
    print(f"Modelo: {coche1.obtener_modelo()}")
    print(f"Año de fabricación: {coche1.obtener_año_fabricacion()}")
    print(f"Antigüedad: {coche1.calcular_antiguedad(año_actual)} años")

    # Establecer nuevas propiedades
    coche1.establecer_marca("Ford")
    coche1.establecer_modelo("Focus")
    coche1.establecer_año_fabricacion(2018)

    # Mostrar las propiedades actualizadas
    print("\nDespués de actualizar:")
    print(f"Marca: {coche1.obtener_marca()}")
    print(f"Modelo: {coche1.obtener_modelo()}")
    print(f"Año de fabricación: {coche1.obtener_anio_fabricacion()}")
    print(f"Antigüedad: {coche1.calcular_antiguedad(anio_actual)} años")
