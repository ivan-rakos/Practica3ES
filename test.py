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
            ['Bernat','Mallol','654381965','China'],
            ['Ivan','Jimenez','652728162','M','Argentina']
        ]
        self.datos_pago = ['Visa','David Durán','9999 8888 7777 6666','123',150]
        self.viajeros = [1,2,3,4,5]
        self.destinos = ['Berlin','Madrid','Roma','Paris','London']
        self.testNumViajeros = [2,3,4,5]
        self.testEliminarViajero = [0,1,2,3,4]

    def test_numViajeros(self):
        resultado =[]
        for i in range(5):
            viaje = t.Travel(None,None,self.viajeros[i])
            if(viaje.viajeros>1):resultado.append(viaje.viajeros)
        self.assertEqual(resultado,self.testNumViajeros)

    def test_noDestinos(self):
        viaje = t.Travel()
        self.assertEqual([],viaje.destinos)

    def test_noDestinosNoVuelos(self):
        viaje = t.Travel()
        self.assertEqual([],viaje.vuelos)

    def test_noDestinosNoPrecio(self):
        viaje = t.Travel()
        self.assertEqual(0,viaje.precio)

    def test_addDestino(self):
        res =["Ibiza"]
        viaje = t.Travel()
        viaje.addDestino("Ibiza")
        self.assertEqual(res,viaje.destinos)

    def test_addDestinoVuelo(self):
        res =[1,"Ibiza"]
        viaje = t.Travel()
        viaje.addDestino("Ibiza")
        data =[len(viaje.vuelos),viaje.vuelos[0].destino]
        self.assertEqual(res,data)

    def test_addDestinoPrecio(self):
        res = len(self.destinos)*29
        viaje = t.Travel()
        for i in self.destinos:
            viaje.addDestino(i)
        self.assertEqual(res,viaje.precio)

    def test_addDestinoPrecioViajeros(self):
        res = 2*len(self.destinos)*29
        viaje =t.Travel()
        viaje.addViajero(1)
        for i in self.destinos:
            viaje.addDestino(i)
        self.assertEqual(res,viaje.precio)

    def test_MultipleDestinosViajeros(self):
        res = ["Berlin","Madrid"]
        viaje = t.Travel()
        viaje.addViajero(1)
        for i in range(3):
            viaje.addDestino(self.destinos[i])

        print(viaje.destinos)
        viaje.delDestino("Roma")
        print(viaje.destinos)
        self.assertEqual(res,viaje.destinos)

    def test_MultipleDestinosViajerosVuelos(self):
        viaje = t.Travel()
        viaje.addViajero()
        for i in self.destinos:
            viaje.addDestino(i)
        viaje.delDestino("Madrid")
        print(viaje.getVuelos())

    def test_MultipleDestinosViajerosPrecio(self):
        viaje = t.Travel()
        viaje.addViajero(1)
        for i in self.destinos:
            viaje.addDestino(i)
        viaje.delDestino("Madrid")
        print(viaje.precio)

    def test_PagoViaje(self):
        viaje = t.Travel()
        viaje.addDestino("Roma")
        viaje.addDestino("Madrid")
        viaje.addViajero(1)
        nombre,apellido,telf,sex,nac = self.users[0]
        tipo,titular,num,cod,imp = self.datos_pago
        user = u.User(1,nombre,apellido,telf,sex,nac)
        pago = p.PaymentData(tipo,titular,num,cod,imp)

        viaje.payTravel(b.Bank(user,pago))
        print(viaje.pagado)

    def test_ConfirmarReserva(self):
        viaje = t.Travel()
        viaje.addDestino("Roma")
        viaje.addDestino("Madrid")
        viaje.addViajero(1)
        nombre, apellido, telf, sex, nac = self.users[0]
        user = u.User(1, nombre, apellido, telf, sex, nac)
        viaje.realizarReservas(user)
        print(viaje.reservas)



    def test_eliminarViajero(self):
        resultado = []
        for i in range(5):
            vuelo = f.Flights(i,self.destinos[i],self.viajeros[i])
            viaje = t.Travel([vuelo],[self.destinos[i]],self.viajeros[i])
            viaje.delViajero(1)
            resultado.append(viaje.viajeros)
        self.assertEqual(resultado,self.testEliminarViajero)



if __name__ == '__main__':
    unittest.main()
