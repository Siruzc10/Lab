# 3
#Crea una clase llamada CuentaBancaria que tenga atributos como titular, saldo y numero_cuenta. 
#Implementa métodos para depositar y retirar dinero, asegurándote de que el saldo no se vuelva negativo.


class CuentaBancaria:
    def __init__(self, titular, saldo, numero):
        self._titular = titular
        self._saldo = saldo
        self._numero = numero

    def obtener_saldo(self):
        return self._saldo

    def depositar(self, monto):
        if monto > 0:
            self._saldo += monto

    def retirar(self, monto):
        if 0 < monto <= self._saldo:
            self._saldo -= monto

if __name__ == "__main__":
    c = CuentaBancaria("Ana", 1000, "123")

    dep = float(input("Depositar: "))
    c.depositar(dep)

    ret = float(input("Retirar: "))
    c.retirar(ret)

    print("Saldo:", c.obtener_saldo())