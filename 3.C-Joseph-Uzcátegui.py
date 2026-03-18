#Ciclos de repetición (while).
#Escribe un programa que simule una carrera entre dos corredores. 
#Cada corredor avanza un número de metros generado aleatoriamente en cada iteración del ciclo. 
#El programa debe mostrar quién ganó la carrera y en cuántos segundos.


import random

corredorN1 = 0
corredorN2 = 0
Meta = 100
Tiempo = 0


print("Bienvenidos a las Olimpiadas. Carrera de 100 mts.")
print("Usain Bolt contra GERONIMO BENAVIDES!!"\n)

while (corredorN1 < Meta) and (corredorN2 <Meta):
    Tiempo += 1
    avance1 = random.randint(0, 20)
    avance2 = random.randint(0, 20)

    corredorN1 += avance1
    corredorN2 += avance2

    print("SEGUNDO: ", Tiempo)
    print(" MOMO avanza: ", avance1 , "mts.  Y lleva ", corredorN1, "mts de carrera!!" )
    print(" Usain Bolt avanza: ", avance2 , "mts. Y lleva", corredorN2, "mts de carrera!!")

if corredorN1 >= Meta and corredorN2 >= Meta:
    print("Empatee ambos llegaron en", Tiempo, "segundos")
elif corredorN1 >= Meta:
    print("GANÓ EL ITALIANOO!! En ", Tiempo, "segundos")
else:
    print("Ganó Usain Bolt (robo) en", Tiempo, "segundos")

print("Gracias por ver")


