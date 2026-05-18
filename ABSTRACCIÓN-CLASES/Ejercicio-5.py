# Ejercicio 5: Empleados

# Crea una clase abstracta Empleado con un método abstracto calcular_sueldo(). 
# Luego, implementa dos clases concretas, EmpleadoPorHora y EmpleadoFijo, que calculen el sueldo de manera diferente.

# Objetivo: Aprender a abstraer la lógica de cálculo de sueldos en diferentes tipos de empleados.


from abc import ABC, abstractmethod

#Clase abstracta
class Empleado (ABC):
    @abstractmethod
    def calcular_sueldo(self):
        pass

#Clase concreta
class EmpleadoPorHora(Empleado):
    def __init__(self, horas, pago_hora):
        self.horas = horas
        self.pago_hora = pago_hora
    
    def calcular_sueldo(self):
        return self.horas * self.pago_hora

#Clase concreta
class EmpleadoFijo (Empleado):
    def __init__(self, sueldo_mensual):
        self.sueldo_mensual = sueldo_mensual
        
    def calcular_sueldo(self):
        return self.sueldo_mensual
    
#MAIN
if __name__ == "__main__":

    empleado1 = EmpleadoPorHora(40, 2000)
    empleado2 = EmpleadoFijo(150000)

    print("Sueldo empleado por hora:", empleado1.calcular_sueldo())
    print("Sueldo empleado fijo:", empleado2.calcular_sueldo())
    















