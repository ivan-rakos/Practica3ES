import unittest
import User as u
import Travel as t
import Flights as f
import PaymentData as p
import Bank as b

class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.precio =30
        self.viajeros=2
        self.vuelos = [f.Flights(1,"Berlin",self.viajeros,self.precio),f.Flights(2,"Madrid",self.viajeros,self.precio),f.Flights(3,"Roma",self.viajeros,self.precio)]
        self.destinos = ["Berlin","Madrid","Roma"]
        self.viaje = t.Travel(self.vuelos,self.destinos,self.viajeros)
        self.user = u.User(1,"Ivan","Jimenez","652748056","M","Española")
        self.pago = p.PaymentData("VISA",'Iván Jiménez',"2000 1111 2222 3333","123",500)



    #Dado un viaje con más de un viajero, el número de viajeros es el esperado
    def test_numViajeros(self):
        numviajeros=2
        viaje = t.Travel([],[],numviajeros)
        self.assertEqual(numviajeros,viaje.viajeros)
    #Dado un viaje con más de un viajero, al eliminar un viajero el número de viajeros es el esperado
    def test_eliminarViajero(self):
        viaje = t.Travel([],[],3)
        viaje.delViajero(1)
        self.assertEqual(2,viaje.viajeros)
    #Dado un viaje sin destinos, la lista de destinos está vacía
    def test_noDestinos(self):
        viaje = t.Travel([],[])
        self.assertEqual([],viaje.destinos)
    #Dado un viaje sin destinos, la lista de vuelos está vacía
    def test_noDestinosNoVuelos(self):
        viaje = t.Travel([],[])
        self.assertEqual([],viaje.vuelos)
    #Dado un viaje sin destinos, el precio del viaje es cero
    def test_noDestinosNoPrecio(self):
        viaje = t.Travel([],[])
        self.assertEqual(0,viaje.precio)
    #Dado un viaje, cuando se añaden destinos, la lista de destinos es la esperada
    def test_addDestino(self):
        res =["Ibiza"]
        viaje = t.Travel([],[])
        viaje.addDestino("Ibiza")
        self.assertEqual(res,viaje.destinos)

    #Dado un viaje, cuando se añaden destinos, la lista de vuelos es la esperada
    def test_addDestinoVuelo(self):
        res =[1,"Ibiza"]
        viaje = t.Travel([],[])
        viaje.addDestino("Ibiza")
        data =[len(viaje.vuelos),viaje.vuelos[0].destino]
        self.assertEqual(res,data)

    #Dado un viaje, cuando se añaden destinos, el precio del viaje es el esperado
    def test_addDestinoPrecio(self):
        res = 30
        viaje = t.Travel([],[])
        viaje.addDestino("Madrid")
        self.assertEqual(res,viaje.precio)
    #Dado un viaje con más de un viajero, cuando se añaden destinos, el precio del viaje es el esperado
    def test_addDestinoPrecioViajeros(self):
        numviajeros=2
        res = numviajeros*2*30 # 2viajeros, 2 destino 30€ vuelo
        viaje =t.Travel([],[],numviajeros)
        viaje.addDestino("Madrid")
        viaje.addDestino("Berlin")
        self.assertEqual(res,viaje.precio)

    #Dado un viaje con múltiples destinos y más de un viajero, cuando se quitan destinos, la lista de destinos es la esperada
    def test_MultipleDestinosViajeros(self):
        res = ["Berlin","Madrid"]
        viaje = self.viaje
        viaje.delDestino("Roma")
        self.assertEqual(res,viaje.destinos)
    #Dado un viaje con múltiples destinos y más de un viajero, cuando se quitan destinos, la lista de vuelos es la esperada
    def test_MultipleDestinosViajerosVuelos(self):
        viaje = self.viaje
        viaje.delDestino("Roma")
        self.assertEqual(["Berlin","Madrid"],viaje.destinos)

    #Dado un viaje con múltiples destinos y más de un viajero, cuando se quitan destinos, el precio del viaje es el esperado
    def test_MultipleDestinosViajerosPrecio(self):
        viaje = self.viaje
        viaje.delDestino("Madrid")
        self.assertEqual(viaje.precio,120)
    # Dado un viaje con múltiples destinos y más de un viajero, cuando el pago se realiza correctamente, se reporta que la acción se ha realizado correctamente
    def test_PagoViaje(self):
        viaje = self.viaje
        viaje.payTravel(self.user,self.pago)
        self.assertEqual(viaje.pagado,True)

    #Dado un viaje con múltiples destinos y más de un viajero, cuando se confirma correctamente la reserva de los vuelos, se reporta que la acción se ha realizado correctamente
    def test_ConfirmarReserva(self):
        viaje = self.viaje
        user = u.User(1,"Ivan","Jimenez","652748056","M","Española")
        viaje.realizarReservas(user)
        self.assertEqual(viaje.reservas,True)


if __name__ == '__main__':
    unittest.main()
