import unittest
import User as u
import Travel as t
import Flights as f
import PaymentData as p
import Bank as b
import Skyscanner as s

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.users = [
            ['David','Duran','654378018','M','Española'],
            ['Xavi','Lopez','654378017','M','Mexicana'],
            ['Charly','Garay','654378016','M','Paraguaya'],
            ['Bernat','Mallol','654381965','M','China'],
            ['Ivan','Jimenez','652728162','M','Argentina']
        ]
        self.datos_pago = ['Visa','David Durán','9999 8888 7777 6666','123',500]
        self.viajeros = [1,2,3,4,5]
        self.destinos = ['Berlin','Madrid','Roma','Paris','London']
        self.testNumViajeros = [2,3,4,5,6]
        self.testEliminarViajero = [0,1,2,3,4]

    def test_reiintento_pago(self):
        tipo,titular,num,cod,imp = self.datos_pago
        datos = p.PaymentData(tipo,titular,num,cod,imp)
        nombre, apellido, telf, sex, nac = self.users[0]
        viaje = t.Travel()
        viaje.addViajero(2)
        for i in self.destinos:
            viaje.addDestino(i)
        pagament = b.Bank(nombre,datos)
        viaje.updatePrecio()
        viaje.payTravel(pagament)

    def test_reiintento_pago_confirmacion(self):
        tipo,titular,num,cod,imp = self.datos_pago
        datos = p.PaymentData(tipo,titular,num,cod,imp)
        nombre, apellido, telf, sex, nac = self.users[0]
        viaje = t.Travel()
        viaje.addViajero(2)
        for i in self.destinos:
            viaje.addDestino(i)
        pagament = b.Bank(nombre,datos)
        viaje.updatePrecio()
        viaje.payTravel(pagament)


    def test_reiintento_vuelo_confirmacion(self):
        nombre, apellido, telf, sex, nac = self.users[0]
        viaje = t.Travel()
        viaje.addViajero(2)
        user = u.User(1, nombre, apellido, telf, sex, nac)
        viaje.updatePrecio()
        viaje.realizarReservas(user)

    def test_reiintento_vuelo_confirmacion_correcta(self):
        nombre, apellido, telf, sex, nac = self.users[0]
        viaje = t.Travel()
        viaje.addViajero(2)
        for i in self.destinos:
            viaje.addDestino(i)
        user = u.User(1, nombre, apellido, telf, sex, nac)
        viaje.updatePrecio()
        viaje.realizarReservas(user)

if __name__ == '__main__':
    unittest.main()
