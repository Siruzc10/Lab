#Ciclos de repetición (for).
#Escribe un programa que pida al usuario que ingrese un número y luego muestre la suma de los números impares desde 1 hasta ese número.

def suma_impares(numero):
    sumado = 0
    for i in range(1, numero):
        if i%2 != 0:
            sumado += i
    return sumado
# MAIN

numero = int(input("ingrese un numero: "))
sumar = suma_impares(numero)

print("La suma de los numeros impares hasta el numero: ", numero, ", es igual a: ", sumar)