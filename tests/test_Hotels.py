import unittest
from unittest import mock
from data_test import  DataSet as data

class MyTestCase(unittest.TestCase):

    def test_addHotel(self):
        datos = data.DataSet()
        viaje = datos.viaje
        viaje.addHotel(datos.hotel)
        self.assertTrue(viaje.precio == 360)

    def test_delHotel(self):
        datos = data.DataSet()
        travel = datos.viaje
        hotel = datos.hotel
        travel.addHotel(hotel)
        travel.delHotel(hotel)
        self.assertTrue(travel.precio == 180)

    def test_confirm_hotels(self):
        datos = data.DataSet()
        travel = datos.viaje
        travel.addHotel(datos.hotel)
        self.assertTrue(travel.confirmHotels(datos.user))

    @mock.patch("src.Travel.bo.Booking")
    def test_confirm_hotels_error(self, mock):
        datos = data.DataSet()
        travel = datos.viaje
        mock.confirm_reserve.return_value = False
        travel.addHotel(datos.hotel)
        self.assertFalse(travel.confirmHotels(datos.user))

    @mock.patch("src.Travel.bo.Booking")
    def test_confirm_hotels_reintentos(self, mock):
        datos = data.DataSet()
        travel = datos.viaje
        mock.confirm_reserve.return_value = False
        travel.addHotel(datos.hotel)
        self.assertFalse(travel.confirm_Hotels_reintentos(datos.user))


if __name__ == '__main__':
    unittest.main()
