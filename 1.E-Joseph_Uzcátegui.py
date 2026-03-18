#Toma de decisión.
#Escribe un programa que pida al usuario que ingrese un número del 1 al 7 y determine a qué día de la semana corresponde (1 es lunes, 2 es martes, etc.). 
#Si el número no está en ese rango, el programa debe mostrar un mensaje de error.

diccionario  = {
    1 : "lunes",
    2 : "martes",
    3 : "miercoles",
    4 : "jueves",
    5 : "viernes",
    6 : "sabado",
    7 : "domingo"
}

def buscar_dia(diccionario, dia):
    if dia in diccionario:
        return diccionario[dia]
    return None
# MAIN

dia = int(input("Ingresa un numero entre 1-7: "))

fecha = buscar_dia(diccionario, dia)

if fecha:
    print("El numero ingresado corresponde al dia: ", fecha)
else: 
    print("ERROR. numero fuera de rango")
        
        