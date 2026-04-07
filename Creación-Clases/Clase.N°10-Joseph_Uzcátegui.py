
# 10. Crea una clase "Libro" con propiedades para el título, el autor, el género y el número de páginas, 
# y métodos para obtener y establecer estas propiedades, así como un método para comprobar si el libro es de ficción o no.

class Libro:
    def __init__(self, titulo, autor, genero, paginas):
        # Inicializo propiedades
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.paginas = paginas

    
    def obtener_titulo(self):
        return self.titulo

    def obtener_autor(self):
        return self.autor

    def obtener_genero(self):
        return self.genero

    def obtener_paginas(self):
        return self.paginas

    
    def establecer_titulo(self, nuevo_titulo):
        self.titulo = nuevo_titulo

    def establecer_autor(self, nuevo_autor):
        self.autor = nuevo_autor

    def establecer_genero(self, nuevo_genero):
        self.genero = nuevo_genero

    def establecer_paginas(self, nuevas_paginas):
        self.paginas = nuevas_paginas

    
    def es_ficcion(self):
        return self.genero.lower() == "ficcion"


if __name__ == "__main__":
    libro1 = Libro("La Odisea", "Homero", "Poesia Epica", 557)

    print(f"Título: {libro1.obtener_titulo()}")
    print(f"Autor: {libro1.obtener_autor()}")
    print(f"Género: {libro1.obtener_genero()}")
    print(f"Páginas: {libro1.obtener_paginas()}")

    if libro1.es_ficcion():
        print("El libro es de ficción")
    else:
        print("El libro NO es de ficción")

    # modificar datos
    print("\nNuevo libro:")
    nuevo_titulo = input("Título: ")
    nuevo_autor = input("Autor: ")
    nuevo_genero = input("Género: ")
    nuevas_paginas = int(input("Páginas: "))

    libro1.establecer_titulo(nuevo_titulo)
    libro1.establecer_autor(nuevo_autor)
    libro1.establecer_genero(nuevo_genero)
    libro1.establecer_paginas(nuevas_paginas)

    print("\nDespués de actualizar:")
    print(f"Título: {libro1.obtener_titulo()}")
    print(f"Autor: {libro1.obtener_autor()}")
    print(f"Género: {libro1.obtener_genero()}")
    print(f"Páginas: {libro1.obtener_paginas()}")

    if libro1.es_ficcion():
        print("El libro es de ficción")
    else:
        print("El libro NO es de ficción")