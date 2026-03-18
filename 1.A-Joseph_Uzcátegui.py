#Toma de decisión.
# A. Escribe un programa que lea un número entero y determine si es positivo, negativo o cero.

def validar_num(numero):
    if (numero > 0):
        print("Numero positivo")
    elif (numero == 0):
        print("El numero es 0")
    else: print("El numero es negativo")
    
# MAIN

numero = int(input("Ingrese un numero: "))

validar_num(numero)  
    
        
        