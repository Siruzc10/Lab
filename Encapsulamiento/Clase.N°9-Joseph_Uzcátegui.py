# 9
#Crea una clase llamada Juego que tenga atributos nombre, género y precio. 
#Implementa un método que muestre la información del juego y otro que verifique si el juego está en oferta (si el precio es menor a un valor dado).


class Juego:
    def __init__(self, nombre, genero, precio):
        self._nombre = nombre
        self._genero = genero
        self._precio = precio


    def obtener_nombre(self):
        return self._nombre

    def obtener_genero(self):
        return self._genero

    def obtener_precio(self):
        return self._precio


    def establecer_nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre

    def establecer_genero(self, nuevo_genero):
        self._genero = nuevo_genero

    def establecer_precio(self, nuevo_precio):
        if nuevo_precio > 0:
            self._precio = nuevo_precio
        else:
            print("Precio inválido")


    def mostrar_info(self):
        return f"Juego: {self._nombre} | Género: {self._genero} | Precio: ${self._precio}"

    def en_oferta(self, valor):
        return self._precio < valor


# MAIN
if __name__ == "__main__":
    juego = Juego("FIFA", "Deportes", 20000)

    print("Datos del juego:")
    print("Nombre:", juego.obtener_nombre())
    print("Género:", juego.obtener_genero())
    print("Precio:", juego.obtener_precio())

    print("\nInformación completa:")
    print(juego.mostrar_info())

    valor = float(input("\nIngresá un precio de referencia para oferta: "))
    if juego.en_oferta(valor):
        print("El juego está en oferta")
    else:
        print("El juego NO está en oferta")

   
    print("\n--- Modificar juego ---")
    nuevo_nombre = input("Nuevo nombre: ")
    nuevo_genero = input("Nuevo género: ")
    nuevo_precio = float(input("Nuevo precio: "))

    juego.establecer_nombre(nuevo_nombre)
    juego.establecer_genero(nuevo_genero)
    juego.establecer_precio(nuevo_precio)

    print("\nDatos actualizados:")
    print(juego.mostrar_info())