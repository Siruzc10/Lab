#Arreglos
#Escribe un programa que lea un arreglo de números enteros 
#y luego muestre cuántos elementos del arreglo son pares.


def validar_num(numero):
    if (numero != 0):
        return True
    return False

def contar_par (arreglo):
    total = 0
    for num in arreglo:
        if num %2 == 0:
            total += 1
    return total

# MAIN
arreglo = []
print("Ingresa numeros enteros")
print("Para finalizar ingresa 0")

while True:
    numero = int(input("Ingresa un numero: "))
    if validar_num(numero):
        arreglo.append(numero)
    else: break

pares = contar_par(arreglo)
print("La cantidad de numeros pares en el arreglo es de: ", pares)

