#Ciclos de repetición (while).
#Escribe un programa que pida al usuario que ingrese una cadena de texto 
#Y luego cuente cuántas veces aparece una letra específica en la cadena.


def contar_letra(cadena, letra):
    cantidad = 0
    i = 0

    while i < len(cadena):
        if cadena[i] == letra:
            cantidad += 1
        i += 1

    return cantidad


# MAIN

print("Ingresa una cadena de texto")

cadena = input("Escribe: ")

letra = input("Ingresa una letra: ")

veces = contar_letra(cadena, letra)

print("La letra ", letra, " aparece ", veces, " veces en el texto que escribiste")


