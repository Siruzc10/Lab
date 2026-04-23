# 4
#Crea una clase llamada Libro con atributos titulo, autor y año_publicacion. 
#Implementa un método que devuelva una descripción del libro y otro que verifique si el libro es considerado un clásico (publicado hace más de 50 años).


from datetime import datetime

class Libro:
    def __init__(self, titulo, autor, año):
        self._titulo = titulo
        self._autor = autor
        self._año = año

    def obtener_titulo(self):
        return self._titulo

    def descripcion(self):
        return f"{self._titulo} - {self._autor}"

    def es_clasico(self):
        return datetime.now().year - self._año > 50


if __name__ == "__main__":
    l = Libro("Don Quijote", "Cervantes", 1605)
    print(l.descripcion())
    print("Clásico:", l.es_clasico())