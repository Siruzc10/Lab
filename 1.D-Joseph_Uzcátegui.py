#Toma de decisión.
#Escribe un programa que pida al usuario que ingrese una letra del alfabeto y determine si es una vocal o una consonante.

def validar_letra(letra):
    if letra.upper() == "A" or letra.upper() == "E" or letra.upper() == "I" or letra.upper() == "O" or letra.upper() == "U":
            return True
    return False
   
    
# MAIN

Letra = input("Ingresa una letra del alfabeto: ")

if not Letra.isalpha():
    print("Ingreso no valido")
elif validar_letra(Letra):
    print("La letra es una vocal")
else:
    print("La letra es una consonante")
        
        