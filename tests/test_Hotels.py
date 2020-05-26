import unittest
from unittest import mock
from src import Flights as f, Travel as t, Hotels as h, User as u

class MyTestCase(unittest.TestCase):
    def test_addHotel(self):
        vuelos, destinos = [], []
        travel = t.Travel(vuelos, destinos)
        codigo, destino, viajeros, precio = 111, "Ibiza", 2, 30
        travel.addVuelo(f.Flights(codigo, destino, viajeros, precio))
        travel.viajeros = viajeros
        codigo, nombre, personas, habitacion, dias, precio_dia = 111, "Hotel", 2, 34, 3, 30
        travel.addHotel(h.Hotels(codigo, nombre, personas, habitacion, dias, precio_dia))
        self.assertTrue(travel.precio == 240)

    def test_delHotel(self):
        vuelos, destinos = [], []
        travel = t.Travel(vuelos, destinos)
        codigo, destino, viajeros, precio = 111, "Ibiza", 2, 30
        travel.addVuelo(f.Flights(codigo, destino, viajeros, precio))
        travel.viajeros = viajeros
        codigo, nombre, personas, habitacion, dias, precio_dia = 111, "Hotel", 2, 34, 3, 30
        hotel = h.Hotels(codigo, nombre, personas, habitacion, dias, precio_dia)
        travel.addHotel(hotel)
        travel.delHotel(hotel)
        self.assertTrue(travel.precio == 60)

    def test_confirm_hotels(self):
        travel = t.Travel()
        codigo, nombre, personas, habitacion, dias, precio_dia = 111, "Hotel", 2, 34, 3, 30
        hotel = h.Hotels(codigo, nombre, personas, habitacion, dias, precio_dia)
        travel.addHotel(hotel)
        dni, nombre, apellido, tlf, sexo, nacionalidad = 1, 'David', 'Duran', 4545454, 'Hombre', 'Española'
        self.assertTrue(travel.confirmHotels(u.User(dni, nombre, apellido, tlf, sexo, nacionalidad)))

    @mock.patch("src.Travel.bo.Booking")
    def test_confirm_hotels_error(self, mock):
        travel = t.Travel()
        mock.confirm_reserve.return_value = False
        codigo, nombre, personas, habitacion, dias, precio_dia = 111, "Hotel", 2, 34, 3, 30
        travel.addHotel(h.Hotels(codigo, nombre, personas, habitacion, dias, precio_dia))
        dni, nombre, apellido, tlf, sexo, nacionalidad = 1, 'David', 'Duran', 4545454, 'Hombre', 'Española'
        self.assertFalse(travel.confirmHotels(u.User(dni, nombre, apellido, tlf, sexo, nacionalidad)))

    @mock.patch("src.Travel.bo.Booking")
    def test_confirm_hotels_reintentos(self, mock):
        travel = t.Travel()
        mock.confirm_reserve.return_value = False
        codigo, nombre, personas, habitacion, dias, precio_dia = 111, "Hotel", 2, 34, 3, 30
        travel.addHotel(h.Hotels(codigo, nombre, personas, habitacion, dias, precio_dia))
        dni, nombre, apellido, tlf, sexo, nacionalidad = 1, 'David', 'Duran', 4545454, 'Hombre', 'Española'
        self.assertFalse(travel.confirm_Hotels_reintentos(u.User(dni, nombre, apellido, tlf, sexo, nacionalidad)))


if __name__ == '__main__':
    unittest.main()
