#Arreglos
# Juego de memoria: Escribe un programa que genere un arreglo de números aleatorios.
# El programa debe mostrar el arreglo por unos segundos y luego ocultar los números. 
# El usuario debe ingresar los números en el orden correcto. 
# Si el usuario ingresa los números en el orden correcto, gana. 
# Si el usuario se equivoca en algún número, pierde.

import random
import time
import os

print("Juego de memoria, intenta copiar el arreglo")

while True:
    arreglo = []
    copia_arreglo = []

    for i in range(6):
        arreglo.append(random.randint(1, 100))

    print("Memoriza este arreglo:")
    print(arreglo)

    time.sleep(10)

    os.system("cls")

    print("Ingresa los números en el mismo orden")

    for i in range(len(arreglo)):
        numero = int(input("Ingresa numero: "))
        copia_arreglo.append(numero)

    if copia_arreglo == arreglo:
        print("Ganaste! Lo copiaste bien")
        break
    else:
        print("No es igual al arreglo. Intenta otra vez")