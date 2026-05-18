# Ejercicio 4: Sistema de Notificaciones
# Define una clase abstracta Notificacion con un método abstracto enviar(). 
# Crea dos clases concretas, Email y SMS, que implementen el método enviar() de manera diferente.

# Objetivo: Ver cómo la abstracción permite manejar diferentes tipos de notificaciones de manera uniforme.



from abc import ABC, abstractmethod

# Clase abstracta
class Notificacion(ABC):

    @abstractmethod
    def enviar(self):
        pass


# Clase concreta
class Email(Notificacion):

    def enviar(self):
        return "Email enviado correctamente."


# Clase concreta
class SMS(Notificacion):

    def enviar(self):
        return "SMS enviado correctamente."


# MAIN
if __name__ == "__main__":

    email = Email()
    sms = SMS()

    print(email.enviar())
    print(sms.enviar())