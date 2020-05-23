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
        self.datos_pago = ['Visa','David Durán','9999 8888 7777 6666','123',150]
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
        if(len(viaje.destinos) > 1 and len(viaje.viajeros) > 1):
            viaje.payTravel(pagament)
            while(viaje.pagado != True):
                viaje.payTravel(pagament)
                print("Error al realizar el pago, reintentado realizar el pago de nuevo")

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
        if(len(viaje.destinos) > 1 and viaje.viajeros > 1):
            viaje.payTravel(pagament)
            while (viaje.pagado != True or pagament.comprobar_intentos() == False):
                viaje.payTravel(pagament)
                print("Error al realizar el pago, reintentado realizar el pago de nuevo")
                pagament.reintentos -= 1
            if(pagament.reintentos > 3 and pagament.reintentos > 0):
                total = 3-pagament.reintentos
                print("Pago Realizado con exito tras" + total + "reintentos")

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
        if(len(viaje.destinos) > 1 and len(viaje.viajeros) > 1):
            viaje.payTravel(pagament)
            while(viaje.pagado != True or pagament.comprobar_intentos() == False):
                print("Error al realizar el pago, reintentado realizar el pago de nuevo")
                pagament.reintentos -= 1
            if(pagament.reintentos == 0):
                print("Se ha superado el numero maximo de reiintentos de pago")

if __name__ == '__main__':
    unittest.main()
