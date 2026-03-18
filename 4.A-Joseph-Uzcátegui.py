#Arreglos
#Escribe un programa que lea un arreglo de números enteros 
#y luego muestre el elemento máximo del arreglo.


def validar_num(numero):
    if (numero != 0):
        return True
    return False

def buscar_m (arreglo):
    mayor = 0
    for num in arreglo:
        if mayor <= num:
            mayor = num
    return mayor

# MAIN
arreglo = []
print("Ingresa numeros enteros")
print("Para finalizar ingresa 0")

while True:
    numero = int(input("Ingresa un numero: "))
    if validar_num(numero):
        arreglo.append(numero)
    else: break

Mayor = buscar_m(arreglo)

print("El mayor de todos los numeros ingresados es: ", Mayor)


