#Arreglos
# Piedra, papel o tijeras: Escribe un programa que permita al usuario jugar piedra, papel o tijeras contra el programa. 
# El usuario debe ingresar su elección y el programa debe generar una elección aleatoria. 
# El programa debe determinar quién gana la partida y mostrar el resultado.

import random

usuario = ["tijeras", "piedra", "papel"]
cpu = ["tijeras", "piedra", "papel"]

# MAIN

print("Piedra, Papel o Tijeras contra CPU")

while True:
    intento = input("Ingresa tu eleccion: ")
    intento = intento.lower()

    if intento in usuario:
        Bot = random.choice(cpu)

        if intento == Bot:
            print("Empate")

        elif (intento == usuario[0] and Bot == cpu[1]) or \
            (intento == usuario[1] and Bot == cpu[2]) or \
             (intento == usuario[2] and Bot == cpu[0]):

            print("Gana el CPU. Eligio:", Bot)

        else:
            print("Ganaste! El CPU eligio:", Bot)

    else:
        print("Ingreso no valido")