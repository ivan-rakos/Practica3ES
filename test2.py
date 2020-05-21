import unittest
import User as u
import Travel as t
import Flights as f
import PaymentData as p
import Bank as b

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.users = [
            ['David','Duran','654378018','M','Española'],
            ['Xavi','Lopez','654378017','M','Mexicana'],
            ['Charly','Garay','654378016','M','Paraguaya'],
            ['Bernat','Mallol','654381965','M','China'],
            ['Ivan','Jimenez','652728162','M','Argentina']
        ]
        self.metodo_pago=['Visa','MasterCard']
        self.datos_pago = ['Visa','David Durán','9999 8888 7777 6666','123',150]
        self.viajeros = [1,2,3,4,5]
        self.destinos = ['Berlin','Madrid','Roma','Paris','London']
        self.testNumViajeros = [2,3,4,5,6]
        self.testEliminarViajero = [0,1,2,3,4]

    def test_MultiplesDesinosMetodoPago(self):
        viaje = t.Travel()
        for i in range(2):
            viaje.addViajero(i)
        for i in self.destinos:
            viaje.addDestino(i)

        nombre, apellido, telf, sex, nac = self.users[0]
        tipo, titular, num, cod, imp = self.datos_pago
        user = u.User(1, nombre, apellido, telf, sex, nac)
        pago = p.PaymentData(tipo, titular, num, cod, imp)
        viaje.payTravel(b.Bank(user, pago))
        if(pago.tipo_pago=="Visa"):
            print("El metodo de pago es el correcto:",pago.tipo_pago)


if __name__ == '__main__':
    unittest.main()
