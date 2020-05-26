import unittest
from src import Travel as t
from unittest import mock
from data_test import DataSet as data

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
        datos = data.DataSet()
        res = ["Berlin", "Madrid"]
        viaje = datos.viaje
        viaje.delDestino("Roma")
        self.assertEqual(res, viaje.destinos)

    # Dado un viaje con múltiples destinos y más de un viajero, cuando se quitan destinos, la lista de vuelos es la esperada
    def test_MultipleDestinosViajerosVuelos(self):
        datos= data.DataSet()
        viaje = datos.viaje
        viaje.delDestino("Roma")
        self.assertEqual(['Berlin','Madrid'], viaje.destinos)

    # Dado un viaje con múltiples destinos y más de un viajero, cuando se quitan destinos, el precio del viaje es el esperado
    def test_MultipleDestinosViajerosPrecio(self):
        datos = data.DataSet()
        viaje = datos.viaje
        viaje.delDestino("Madrid")
        self.assertEqual(viaje.precio, 120)

    # Dado un viaje con múltiples destinos y más de un viajero, cuando el pago se realiza correctamente, se reporta que la acción se ha realizado correctamente
    def test_PagoViaje(self):
        datos = data.DataSet()
        viaje = datos.viaje
        viaje.payTravel(datos.user, datos.pago)
        self.assertEqual(viaje.pagado, True)

    # Dado un viaje con múltiples destinos y más de un viajero, cuando se confirma correctamente la reserva de los vuelos, se reporta que la acción se ha realizado correctamente
    def test_ConfirmarReserva(self):
        datos = data.DataSet()
        viaje = datos.viaje
        res = viaje.confirmacionVuelos(datos.user)
        self.assertEqual(res, True)


    # Dado un viaje con múltiples destinos y más de un viajero, cuando se produce
    # error al confirmar los vuelos, se reporta que la acción no se ha podido realizar
    @mock.patch("src.Travel.s.Skyscanner")
    def test_MultiplesDestinosErrorConfirmVuelo(self,mock):
        datos = data.DataSet()
        mock.confirm_reserve.return_value = False
        viaje = datos.viaje
        self.assertFalse(viaje.confirmacionVuelos(datos.user))

    @mock.patch("src.Travel.s.Skyscanner")
    def test_reintento_vuelo(self, mock2):
        datos = data.DataSet()
        mock2.confirm_reserve.return_value = False
        viaje=datos.viaje
        viaje.confirm_Vuelos_reintentos(datos.user)
        self.assertLess(viaje.reintentos_vuelo, 3)

    @mock.patch("src.Travel.s.Skyscanner")
    def test_reintento_vuelo(self, mock):
        datos = data.DataSet()
        mock.confirm_reserve.side_effect = [False, True]
        viaje=datos.viaje
        viaje.confirm_Vuelos_reintentos(datos.user)
        self.assertEqual(mock.confirm_reserve.call_count, 2)

if __name__ == '__main__':
    unittest.main()
