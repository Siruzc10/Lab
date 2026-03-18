#Arreglos
#Escribe un programa que lea un arreglo de números enteros 
#y luego muestre la suma de todos los elementos del arreglo


def validar_num(numero):
    if (numero != 0):
        return True
    return False

def sumar_arreglo (arreglo):
    total = 0
    for num in arreglo:
        total += num
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

suma = sumar_arreglo(arreglo)

print("La suma de todos los numeros ingresados es: ", suma)


