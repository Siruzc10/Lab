# Ejercicio 2: Sistema de Pago
# Define una clase abstracta Pago con un método abstracto procesar_pago(). 
# Luego, crea dos clases concretas, TarjetaCredito y PayPal, que implementen el método procesar_pago() de manera diferente.

# Objetivo: Aprender a abstraer el proceso de pago y cómo diferentes métodos pueden implementarse de manera específica.


from abc import ABC, abstractmethod

# Clase abstracta
class Pago(ABC):

    @abstractmethod
    def procesar_pago(self, monto):
        pass


# Clase concreta
class TarjetaCredito(Pago):

    def procesar_pago(self, monto):
        return f"Pago de ${monto} realizado con tarjeta de crédito"


# Clase concreta
class PayPal(Pago):

    def procesar_pago(self, monto):
        return f"Pago de ${monto} realizado con PayPal."


# MAIN
if __name__ == "__main__":

    tarjeta = TarjetaCredito()
    paypal = PayPal()

    print(tarjeta.procesar_pago(5000))
    print(paypal.procesar_pago(2500))