#Ciclos de repetición (for).
#Escribe un programa que pida al usuario que ingrese una palabra y luego muestre cada letra de la palabra en una línea separada.

def separar(palabra):
    for pal in palabra:
        print(pal)
    
# MAIN

palabra = input("ingrese una palabra: ")
if palabra.isalpha():
    letras = separar(palabra)
else: print("Ingreso no valido")