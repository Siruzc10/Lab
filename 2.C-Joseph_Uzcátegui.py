#Ciclos de repetición (for).
#Escribe un programa que muestre las tablas de multiplicar del 1 al 10.

for i in range(1, 11):
    print("Tabla del", i)
    for j in range(1, 11):
        print(i, "x", j, "=", i*j)
    print()