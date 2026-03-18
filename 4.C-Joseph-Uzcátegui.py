#Arreglos
#Escribe un programa que lea un arreglo de números enteros 
#y luego muestre la media (promedio) de los elementos del arreglo.


def validar_num(numero):
    if (numero != 0):
        return True
    return False

def sacar_promedio (arreglo):
    total = 0
    cantidad = 0
    for num in arreglo:
        total += num
        cantidad += 1
    return total / cantidad

# MAIN
arreglo = []
print("Ingresa numeros enteros")
print("Para finalizar ingresa 0")

while True:
    numero = int(input("Ingresa un numero: "))
    if validar_num(numero):
        arreglo.append(numero)
    else: break

if len(arreglo) > 0:
    media = sacar_promedio(arreglo)
    print("El promedio de todos los numeros ingresados es: ", media)
else:
    print("No se ingresaron numeros para calcular un promedio.")


