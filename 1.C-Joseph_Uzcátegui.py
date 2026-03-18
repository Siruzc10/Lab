#Toma de decisión.
#Escribe un programa que pida al usuario que ingrese su edad y determine si es mayor de edad (18 años o más) o menor de edad

def validar_edad(edad):
    Mayoria = False
    if (edad >= 18):
        Mayoria = True
    return Mayoria
   
    
# MAIN

Edad = int(input("Ingresa tu edad: "))

if validar_edad(Edad):
    print("Eres mayor de edad")
else:
    print("No eres mayor de edad")
        
        