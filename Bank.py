import User
import PaymentData
import Flights as f

class Bank:

    def __init__(self,usuario,datos_pago):
        self.user=usuario
        self.pago=datos_pago


    def do_payment(self, user: User, pago: PaymentData):
        return True

    def do_payment(self, user: User, importe,codigo,destinos,numviajeros):
        vuelo=f.Flights(codigo,destinos,numviajeros)
        if(vuelo.precio>importe): return False
        else: return True
    """def verificarErroresPago(self,user, cod,num):
        valid = False
        if (len(user.telefono) != 9 or user.sexo != 'M' or user.sexo != 'F'):
            valid = False
        else:
            if(len(cod)!=35 or len(num)!=)
            valid = True
        return valid"""