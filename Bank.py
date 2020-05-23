import User
import PaymentData
import Flights as f

class Bank:

    def __init__(self,usuario,datos_pago):
        self.user=usuario
        self.pago=datos_pago
        self.reintentos = 3

    def do_payment(self, user: User, pago: PaymentData):
        return True

    def comprobar_saldo(self,precio):
        if(self.pago.importe>=precio):
            return True
        else:
            return False
