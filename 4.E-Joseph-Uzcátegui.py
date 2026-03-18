#Arreglos
#Adivina el número: Escribe un programa que genere un número aleatorio entre 1 y 100. 
#El usuario debe adivinar el número y el programa debe decir si el número ingresado es mayor o menor al número generado. 
#El usuario gana cuando adivina el número.

import random
numero = random.randint(1, 100)

# MAIN

print("Adivina el numero entre 1 y 100")

while True:
    intento = int(input("Ingresa un numero: "))
    if intento < numero:
        print("El numero es mayor")
    elif intento > numero:
        print("El numero es menor")
    else: 
            print("Ganaste! El numero era ", intento)
            break
