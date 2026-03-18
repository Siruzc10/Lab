#Arreglos
# Juego de adivinanzas: Escribe un programa que genere un arreglo de palabras. 
# El programa debe elegir una palabra aleatoria y mostrar la primera letra. 
# El usuario debe adivinar la palabra ingresando una letra a la vez. 
# Si la letra ingresada es correcta, el programa debe mostrar la letra en la posición correspondiente. 
# Si la letra es incorrecta, el programa debe mostrar un mensaje de error. 
# El usuario gana cuando ha adivinado todas las letras de la palabra.


import random

palabras = ["MOUSE", "ZAPATO", "BARCELONA", "QUESO", "CELULAR", "CASA", "HOTEL", "AVION", "PUMA"]
palabra = random.choice(palabras)
progreso = ["_"] * len(palabra)

progreso[0] = palabra[0]

print("Juego de adivinanza")
print("Adivina la palabra:")
print(" ".join(progreso))

while "_" in progreso:

    try:
        posicion = int(input("Posición (1-{}): ".format(len(palabra)))) - 1
    except:
        print("Debes ingresar un numero")
        continue

    if posicion < 0 or posicion >= len(palabra):
        print("Posición inválida")
        continue

    if progreso[posicion] != "_":
        print("Esa posición ya está descubierta")
        continue

    letra = input("Letra: ").upper()

    if palabra[posicion] == letra:
        progreso[posicion] = letra
        print("Correcto")
    else:
        print("Letra incorrecta")

    print(" ".join(progreso))

print("Ganaste. La palabra era:", palabra)