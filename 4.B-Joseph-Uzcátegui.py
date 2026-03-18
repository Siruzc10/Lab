#Arreglos
#Escribe un programa que lea un arreglo de números enteros 
#y luego muestre el elemento mínimo del arreglo.


def validar_num(numero):
    if (numero != 0):
        return True
    return False

def buscar_menor (arreglo):
    menor = 0
    for num in arreglo:
        if menor >= num:
            menor = num
    return menor

# MAIN
arreglo = []
print("Ingresa numeros enteros")
print("Para finalizar ingresa 0")

while True:
    numero = int(input("Ingresa un numero: "))
    if validar_num(numero):
        arreglo.append(numero)
    else: break

Menor = buscar_menor(arreglo)

print("El menor de todos los numeros ingresados es: ", Menor)


