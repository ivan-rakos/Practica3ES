import unittest
from src import Bank as b, PaymentData as p, Flights as f, Cars as c, Hotels as h, User as u, Travel as t
from unittest import mock

class MyTestCase(unittest.TestCase):


    def test_MultiplesDesinosMetodoPago(self):
        viaje = t.Travel()
        nombre, apellido, telf, sex, nac = ['David', 'Duran', '654378018', 'M', 'Española']
        tipo, titular, num, cod, imp = ['VISA', 'David Durán', '9999 8888 7777 6666', '123', 150]
        user = u.User(1, nombre, apellido, telf, sex, nac)
        pago = p.PaymentData(tipo, titular, num, cod, imp)
        self.assertTrue(viaje.payTravel(user, pago))

    @mock.patch("src.Travel.b.Bank")
    def test_MultiplesDestinosErrorPago(self, mock):
        viaje = t.Travel()
        mock.do_payment.return_value = False
        nombre, apellido, telf, sex, nac = ['David', 'Duran', '654378018', 'M', 'Española']
        tipo, titular, num, cod, imp = ['Visa', 'David Durán', '9999 8888 7777 6666', '123', 150]
        user = u.User(1, nombre, apellido, telf, sex, nac)
        pago = p.PaymentData(tipo, titular, num, cod, imp)
        self.assertFalse(viaje.payTravel(user, pago))


    def test_reiintento_pago(self):
        tipo,titular,num_tarjeta,cod_seg,imp = 'Visa','Xavi Lopez','9999 8888 7777 6661','123',-1
        datos = p.PaymentData(tipo,titular,num_tarjeta,cod_seg,imp)
        id, nombre, apellido, telf, sex, nac = 1,'Xavi','Lopez','654378017','M','Mexicana'
        numviajeros = 2
        precio = 30
        vuelos = [f.Flights(1, "Berlin", numviajeros, precio), f.Flights(2, "Madrid", numviajeros, precio), f.Flights(3, "Roma", numviajeros, precio)]
        destinos = ["Berlin","Madrid","Roma"]
        viaje = t.Travel(vuelos,destinos,numviajeros)
        user = u.User(id, nombre, apellido, telf, sex, nac)
        viaje.confirmacionPago(user,datos)
        self.assertLess(viaje.reintentos_pago,3)

    @mock.patch("src.Travel.b.Bank")
    def test_segundo_reintento(self, mock):
        mock.do_payment.side_effect = [False, True]
        tipo,titular,num_tarjeta,cod_seg,imp = 'VISA','Xavi Lopez','9999 8888 7777 6661','123',-1
        datos = p.PaymentData(tipo,titular,num_tarjeta,cod_seg,imp)
        id, nombre, apellido, telf, sex, nac = 1,'Xavi','Lopez','654378017','M','Mexicana'
        numviajeros = 2
        precio = 30
        vuelos = [f.Flights(1, "Berlin", numviajeros, precio), f.Flights(2, "Madrid", numviajeros, precio), f.Flights(3, "Roma", numviajeros, precio)]
        destinos = ["Berlin","Madrid","Roma"]
        viaje = t.Travel(vuelos,destinos,numviajeros)
        user = u.User(id, nombre, apellido, telf, sex, nac)
        viaje.confirmacionPago(user,datos)
        self.assertEqual(mock.do_payment.call_count, 2)

if __name__ == '__main__':
    unittest.main()

