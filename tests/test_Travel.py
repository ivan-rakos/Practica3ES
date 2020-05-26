import unittest
from src import Bank as b, PaymentData as p, Flights as f, Cars as c, Hotels as h, User as u, Travel as t
from unittest import mock

class MyTestCase(unittest.TestCase):
    # Dado un viaje con más de un viajero, el número de viajeros es el esperado
    def test_numViajeros(self):
        numviajeros = 2
        viaje = t.Travel([], [], numviajeros)
        self.assertEqual(numviajeros, viaje.viajeros)

    # Dado un viaje con más de un viajero, al eliminar un viajero el número de viajeros es el esperado
    def test_eliminarViajero(self):
        viaje = t.Travel([], [], 3)
        viaje.delViajero(1)
        self.assertEqual(2, viaje.viajeros)

    # Dado un viaje sin destinos, la lista de destinos está vacía
    def test_noDestinos(self):
        viaje = t.Travel([], [])
        self.assertEqual([], viaje.destinos)

    # Dado un viaje sin destinos, la lista de vuelos está vacía
    def test_noDestinosNoVuelos(self):
        viaje = t.Travel([], [])
        self.assertEqual([], viaje.vuelos)

    # Dado un viaje sin destinos, el precio del viaje es cero
    def test_noDestinosNoPrecio(self):
        viaje = t.Travel([], [])
        self.assertEqual(0, viaje.precio)

    # Dado un viaje, cuando se añaden destinos, la lista de destinos es la esperada
    def test_addDestino(self):
        res = ["Ibiza"]
        viaje = t.Travel([], [])
        viaje.addDestino("Ibiza")
        self.assertEqual(res, viaje.destinos)

    # Dado un viaje, cuando se añaden destinos, la lista de vuelos es la esperada
    def test_addDestinoVuelo(self):
        res = [1, "Ibiza"]
        viaje = t.Travel([], [])
        viaje.addDestino("Ibiza")
        data = [len(viaje.vuelos), viaje.vuelos[0].destino]
        self.assertEqual(res, data)

    # Dado un viaje, cuando se añaden destinos, el precio del viaje es el esperado
    def test_addDestinoPrecio(self):
        res = 30
        viaje = t.Travel([], [])
        viaje.addDestino("Madrid")
        self.assertEqual(res, viaje.precio)

    # Dado un viaje con más de un viajero, cuando se añaden destinos, el precio del viaje es el esperado
    def test_addDestinoPrecioViajeros(self):
        numviajeros = 2
        res = numviajeros * 2 * 30  # 2viajeros, 2 destino 30€ vuelo
        viaje = t.Travel([], [], numviajeros)
        viaje.addDestino("Madrid")
        viaje.addDestino("Berlin")
        self.assertEqual(res, viaje.precio)

    # Dado un viaje con múltiples destinos y más de un viajero, cuando se quitan destinos, la lista de destinos es la esperada
    def test_MultipleDestinosViajeros(self):
        res = ["Berlin", "Madrid"]
        viaje = t.Travel()
        viaje.addViajero(1)
        viaje.addDestino("Berlin")
        viaje.addDestino("Madrid")
        viaje.addDestino("Roma")
        viaje.delDestino("Roma")
        self.assertEqual(res, viaje.destinos)

    # Dado un viaje con múltiples destinos y más de un viajero, cuando se quitan destinos, la lista de vuelos es la esperada
    def test_MultipleDestinosViajerosVuelos(self):
        numviajeros = 2
        precio = 30
        vuelos = [f.Flights(1, "Berlin", numviajeros, precio), f.Flights(2, "Madrid", numviajeros, precio),
                  f.Flights(3, "Roma", numviajeros, precio)]
        destinos = ["Berlin", "Madrid", "Roma"]
        viaje = t.Travel(vuelos, destinos, numviajeros)
        viaje.delDestino("Roma")
        self.assertEqual(vuelos, viaje.vuelos)

    # Dado un viaje con múltiples destinos y más de un viajero, cuando se quitan destinos, el precio del viaje es el esperado
    def test_MultipleDestinosViajerosPrecio(self):
        numviajeros = 2
        precio = 30
        vuelos = [f.Flights(1, "Berlin", numviajeros, precio), f.Flights(2, "Madrid", numviajeros, precio),
                  f.Flights(3, "Roma", numviajeros, precio)]
        destinos = ["Berlin", "Madrid", "Roma"]
        viaje = t.Travel(vuelos, destinos, numviajeros)
        viaje.delDestino("Madrid")
        self.assertEqual(viaje.precio, 120)

    # Dado un viaje con múltiples destinos y más de un viajero, cuando el pago se realiza correctamente, se reporta que la acción se ha realizado correctamente
    def test_PagoViaje(self):
        numviajeros = 2
        precio = 30
        vuelos = [f.Flights(1, "Berlin", numviajeros, precio), f.Flights(2, "Madrid", numviajeros, precio),
                  f.Flights(3, "Roma", numviajeros, precio)]
        destinos = ["Berlin", "Madrid", "Roma"]
        viaje = t.Travel(vuelos, destinos, numviajeros)
        user = u.User(1, "Ivan", "Jimenez", "652748056", "M", "Española")
        pago = p.PaymentData("Visa", 'Iván Jiménez', "2000 1111 2222 3333", "123", 500)
        viaje.payTravel(user, pago)
        self.assertEqual(viaje.pagado, True)

    # Dado un viaje con múltiples destinos y más de un viajero, cuando se confirma correctamente la reserva de los vuelos, se reporta que la acción se ha realizado correctamente
    def test_ConfirmarReserva(self):
        numviajeros = 2
        precio = 30
        vuelos = [f.Flights(1, "Berlin", numviajeros, precio), f.Flights(2, "Madrid", numviajeros, precio),
                  f.Flights(3, "Roma", numviajeros, precio)]
        destinos = ["Berlin", "Madrid", "Roma"]
        viaje = t.Travel(vuelos, destinos, numviajeros)
        user = u.User(1, "Ivan", "Jimenez", "652748056", "M", "Española")
        viaje.realizarReservas(user)
        self.assertEqual(viaje.reservas, True)


    # Dado un viaje con múltiples destinos y más de un viajero, cuando se produce
    # error al confirmar los vuelos, se reporta que la acción no se ha podido realizar
    @mock.patch("src.Travel.s.Skyscanner")
    def test_MultiplesDestinosErrorConfirmVuelo(self,mock):
        mock.confirm_reserve.return_value = False
        numviajeros = 2
        precio = 30
        vuelos = [f.Flights(1, "Berlin", numviajeros, precio), f.Flights(2, "Madrid", numviajeros, precio),
                  f.Flights(3, "Roma", numviajeros, precio)]
        destinos = ["Berlin", "Madrid", "Roma"]
        viaje = t.Travel(vuelos, destinos, numviajeros)
        nombre, apellido, telf, sex, nac = ['David', 'Duran', '654378018', 'M', 'Española']
        user = u.User(1, nombre, apellido, telf, sex, nac)
        self.assertFalse(viaje.confirmacionVuelos(user))


if __name__ == '__main__':
    unittest.main()
