#Toma de decisión.
#Escribe un programa que pida al usuario que ingrese dos números y determine cuál es el número más grande.

def validar_num(numeros):
    Mayor = numeros[0]
    for n in numeros:
        if n > Mayor:
            Mayor = n
    return Mayor
    
# MAIN
numeros = []
for i in range(2):
    numero = int(input("Ingrese un numero: "))
    numeros.append(numero)

Mayor =  validar_num(numeros)
print("El numero mayor es:", Mayor) 
    
        
        