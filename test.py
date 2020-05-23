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
        self.datos_pago = ['Visa','David Durán','9999 8888 7777 6666','123',150]
        self.viajeros = [1,2,3,4,5]
        self.destinos = ['Berlin','Madrid','Roma','Paris','London']
        self.testNumViajeros = [2,3,4,5,6]
        self.testEliminarViajero = [0,1,2,3,4]
    # Dado un viaje con más de un viajero, el número de viajeros es el esperado
    def test_numViajeros(self):
        resultado =[]
        for i in range(5):
            viaje = t.Travel([],[],2)
            if(viaje.viajeros>1):
                viaje.addViajero(i)
                resultado.append(viaje.viajeros)
        self.assertEqual(resultado,self.testNumViajeros)
    # Dado un viaje sin destinos, la lista de destinos está vacía
    def test_noDestinos(self):
        viaje = t.Travel()
        self.assertEqual([],viaje.destinos)
    # Dado un viaje sin destinos, la lista de vuelos está vacía
    def test_noDestinosNoVuelos(self):
        viaje = t.Travel()
        self.assertEqual([],viaje.vuelos)
    # Dado un viaje sin destinos, el precio del viaje es cero
    def test_noDestinosNoPrecio(self):
        viaje = t.Travel()
        self.assertEqual(0,viaje.precio)
    # Dado un viaje, cuando se añaden destinos, la lista de destinos es la esperada
    def test_addDestino(self):
        res =["Ibiza"]
        viaje = t.Travel()
        viaje.addDestino("Ibiza")
        self.assertEqual(res,viaje.destinos)

    # Dado un viaje, cuando se añaden destinos, la lista de vuelos es la esperada

    def test_addDestinoVuelo(self):
        res =[1,"Ibiza"]
        viaje = t.Travel()
        viaje.addDestino("Ibiza")
        data =[len(viaje.vuelos),viaje.vuelos[0].destino]
        self.assertEqual(res,data)
    # Dado un viaje, cuando se añaden destinos, el precio del viaje es el esperado

    def test_addDestinoPrecio(self):
        res = len(self.destinos)*30
        viaje = t.Travel()
        for i in self.destinos:
            viaje.addDestino(i)
        self.assertEqual(res,viaje.precio)
    # Dado un viaje con más de un viajero, cuando se añaden destinos, el precio del
    # viaje es el esperado

    def test_addDestinoPrecioViajeros(self):
        res = 2*len(self.destinos)*30
        viaje =t.Travel()
        viaje.addViajero(1)
        for i in self.destinos:
            viaje.addDestino(i)
        self.assertEqual(res,viaje.precio)

    # Dado un viaje con múltiples destinos y más de un viajero, cuando se quitan
    # destinos, la lista de destinos es la esperada

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
    # Dado un viaje con múltiples destinos y más de un viajero, cuando se quitan
    # destinos, la lista de vuelos es la esperada

    def test_MultipleDestinosViajerosVuelos(self):
        viaje = t.Travel()
        viaje.addViajero(1)
        for i in self.destinos:
            viaje.addDestino(i)
        viaje.delDestino("Madrid")
        print(viaje.getVuelos())

    # Dado un viaje con múltiples destinos y más de un viajero, cuando se quitan
    # destinos, el precio del viaje es el esperado

    def test_MultipleDestinosViajerosPrecio(self):
        viaje = t.Travel()
        viaje.addViajero(1)
        for i in self.destinos:
            viaje.addDestino(i)
        viaje.delDestino("Madrid")
        print(viaje.precio)

    # Dado un viaje con múltiples destinos y más de un viajero, cuando el pago se
    # realiza correctamente, se reporta que la acción se ha realizado correctamente

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
    # Dado un viaje con múltiples destinos y más de un viajero, cuando se confirma
    # correctamente la reserva de los vuelos, se reporta que la acción se ha realizado
    # correctamente
    def test_ConfirmarReserva(self):
        viaje = t.Travel()
        viaje.addDestino("Roma")
        viaje.addDestino("Madrid")
        viaje.addViajero(1)
        nombre, apellido, telf, sex, nac = self.users[0]
        user = u.User(1, nombre, apellido, telf, sex, nac)
        viaje.realizarReservas(user)
        print(viaje.reservas)


    #Eliminar un viajero
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
