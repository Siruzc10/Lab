#Arreglos
# Palabras cruzadas: Escribe un programa que genere una palabra aleatoria y la muestre con una letra oculta en cada posición. 
# El usuario debe ingresar una letra para cada posición oculta. 
# Si la letra ingresada es correcta, el programa debe mostrar la letra en la posición correspondiente. 
# Si la letra es incorrecta, el programa debe mostrar un mensaje de error. 
# El usuario gana cuando ha adivinado todas las letras de la palabra.

import random

palabras = ["PELOTA", "CODIGO", "JUEGO", "LETRA", "MESSI", "COMPUTADORA", "AUTO"]
palabra = random.choice(palabras)
adivinado = set()


print("Adivina la palabra:")
print("_ " * len(palabra))

while len(adivinado) < len(palabra):

    posicion = int(input("Posición (1-{}): ".format(len(palabra)))) - 1

    if posicion < 0 or posicion >= len(palabra):
        print("Posición inválida")
        continue

    letra = input("Letra: ").upper()

    if palabra[posicion] == letra:
        adivinado.add(posicion)
        print("Correcto")
    else:
        print("Incorrecto")

    print(" ".join([l if p in adivinado else "_" for p, l in enumerate(palabra)]))

print("¡Ganaste! La palabra era:", palabra)