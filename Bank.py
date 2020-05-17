from . import User
from . import PaymentData


class Bank:

    def __init__(self,usuario,datos_pago):
        self.user=usuario
        self.pago=datos_pago
        pass

    def do_payment(self, user: User, payment_data: PaymentData):
        return True