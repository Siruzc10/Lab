# Clase base
class Pago:

    def procesarPago(self):
        raise NotImplementedError(
            "Este método debe ser sobrescrito por las subclases"
        )


# Clase TarjetaCredito
class TarjetaCredito(Pago):

    def procesarPago(self):
        return "Pago procesado con Tarjeta de Crédito."


# Clase PayPal
class PayPal(Pago):

    def procesarPago(self):
        return "Pago procesado con PayPal."


# Función principal
def main():

    pagos = [
        TarjetaCredito(),
        PayPal(),
        TarjetaCredito(),
        PayPal()
    ]

    for pago in pagos:

        print(
            f"{pago.__class__.__name__}: "
            f"{pago.procesarPago()}"
        )


if __name__ == "__main__":
    main()