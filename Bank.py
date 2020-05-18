import User
import PaymentData


class Bank:

    def __init__(self,usuario,datos_pago):
        self.user=usuario
        self.pago=datos_pago


    def do_payment(self, user: User, payment_data: PaymentData):
        return True