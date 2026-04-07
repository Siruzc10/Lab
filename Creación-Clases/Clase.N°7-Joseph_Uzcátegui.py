
# 7. Crea una clase "Banco" con propiedades para el nombre del banco y la tasa de interés, 
# y métodos para calcular el interés que se obtendría en una cantidad determinada de dinero 
# y el tiempo que se tardaría en duplicar esa cantidad.

class Banco:
    def __init__(self, nombre, tasa_interes):
        # Inicializo propiedades
        self.nombre = nombre
        self.tasa_interes = tasa_interes  # en decimal (0.10 = 10%)

    def obtener_nombre(self):
        return self.nombre

    def establecer_nombre(self, nombre_nuevo):
        self.nombre = nombre_nuevo

    def obtener_tasa_interes(self):
        return self.tasa_interes

    def establecer_tasa_interes(self, nueva_tasa):
        self.tasa_interes = nueva_tasa

    def calcular_interes(self, capital, tiempo):
        # Interes simple: Interes = Capital * tasa * tiempo(años)
        return capital * self.tasa_interes * tiempo

    def calcular_tiempo_duplicar(self):
        # Tiempo aprox para duplicar el capital (2 dividido la tasa de interes)
        return 2 / self.tasa_interes


if __name__ == "__main__":
    # Crear instancia
    banco1 = Banco("Banco Nación", 0.10)

    print(f"Banco: {banco1.obtener_nombre()}")
    print(f"Tasa de interés anual: {banco1.obtener_tasa_interes() * 100}%")

    capital = float(input("Ingrese capital: "))
    tiempo = float(input("Ingrese tiempo (años): "))

    interes = banco1.calcular_interes(capital, tiempo)
    print(f"Interes generado: {interes}")

    tiempo_dup = banco1.calcular_tiempo_duplicar()
    print(f"Tiempo para duplicar el capital: {tiempo_dup} años")

    # Modificar valores
    print("\nModificar banco:")
    nuevo_nombre = input("Nombre: ")
    nueva_tasa = float(input("Tasa de interés (ej: 0.15 para 15%): "))

    banco1.establecer_nombre(nuevo_nombre)
    banco1.establecer_tasa_interes(nueva_tasa)

    print("\nDespués de actualizar:")
    print(f"Banco: {banco1.obtener_nombre()}")
    print(f"Tasa interes anual: {banco1.obtener_tasa_interes() * 100}%")