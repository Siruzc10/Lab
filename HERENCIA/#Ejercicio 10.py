#Ejercicio 10

class Pago:
    def __init__(self, monto, fecha):
        self.monto = monto
        self.fecha = fecha

    def mostrar_detalles(self):
        print(f"Monto: ${self.monto}")
        print(f"Fecha: {self.fecha}")


class PagoTarjeta(Pago):
    def procesar_pago(self):
        return "Pago realizado con tarjeta."

    def generar_recibo(self):
        return f"Recibo de pago con tarjeta por ${self.monto}"

    def mostrar_detalles(self):
        print("=== Pago con Tarjeta ===")
        super().mostrar_detalles()
        print(self.procesar_pago())
        print(self.generar_recibo())


class PagoPayPal(Pago):
    def procesar_pago(self):
        return "Pago realizado con PayPal."

    def generar_recibo(self):
        return f"Recibo de pago con PayPal por ${self.monto}"

    def mostrar_detalles(self):
        print("=== Pago con PayPal ===")
        super().mostrar_detalles()
        print(self.procesar_pago())
        print(self.generar_recibo())


# MAIN
if __name__ == "__main__":

    tarjeta = PagoTarjeta(15000, "28/05/2026")
    tarjeta.mostrar_detalles()

    print()

    paypal = PagoPayPal(8000, "28/05/2026")
    paypal.mostrar_detalles()