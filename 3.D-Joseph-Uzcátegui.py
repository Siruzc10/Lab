#Ciclos de repetición (while).
#Escribe un programa que pida al usuario que ingrese números enteros positivos 
#y luego calcule el producto de todos los números ingresados hasta que el usuario ingrese un número negativo


def validar_num(numero):
    if (numero >= 0):
        return True
    return False


# MAIN
producto = 1

print("Ingresa numeros enteros positivos")

while True:
    numero = int(input("Ingresa un numero: "))

    if validar_num(numero):
        producto *= numero
    else:
        print("Numero negativo no valido.")
        break

print("El producto total de los números positivos fue: ", producto)
