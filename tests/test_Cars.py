import unittest
from unittest import mock
from src import Flights as f, Cars as c, User as u, Travel as t

class MyTestCase(unittest.TestCase):

    def test_addCars(self):
        vuelos, destinos = [], []
        travel = t.Travel(vuelos, destinos)
        codigo, destino, viajeros, precio = 111, "Ibiza", 2, 30
        travel.addVuelo(f.Flights(codigo, destino, viajeros, precio))
        travel.viajeros = viajeros
        codigo, modelo, dias_reerva, precio_dia, lugar_recogida = "11111", "Mercedes", 3, 10, "Barcelona"
        car = c.Cars(codigo, modelo, dias_reerva, precio_dia, lugar_recogida)
        travel.addCar(car)
        self.assertTrue(travel.precio == 90)

    def test_delCars(self):
        vuelos, destinos = [], []
        travel = t.Travel(vuelos, destinos)
        codigo, destino, viajeros, precio = 111, "Ibiza", 2, 30
        travel.addVuelo(f.Flights(codigo, destino, viajeros, precio))
        travel.viajeros = viajeros
        codigo, modelo, dias_reerva, precio_dia, lugar_recogida = "11111", "Mercedes", 3, 10, "Barcelona"
        car = c.Cars(codigo, modelo, dias_reerva, precio_dia, lugar_recogida)
        travel.addCar(car)
        travel.delCar(car)
        self.assertTrue(travel.precio == 60)

    def test_confirm_cars(self):
        travel = t.Travel()
        codigo, modelo, dias_reerva, precio_dia, lugar_recogida = "11111", "Mercedes", 3, 10, "Barcelona"
        car = c.Cars(codigo, modelo, dias_reerva, precio_dia, lugar_recogida)
        travel.addCar(car)
        dni, nombre, apellido, tlf, sexo, nacionalidad = 1, 'David', 'Duran', 4545454, 'Hombre', 'Española'
        self.assertTrue(travel.confirmCars(u.User(dni, nombre, apellido, tlf, sexo, nacionalidad)))

    @mock.patch("src.Travel.r.Rentalcars")
    def test_confirm_cars_error(self,mock):
        travel = t.Travel()
        mock.confirm_reserve.return_value = False
        codigo, modelo, dias_reerva, precio_dia, lugar_recogida = "11111", "Mercedes", 3, 10, "Barcelona"
        car = c.Cars(codigo, modelo, dias_reerva, precio_dia, lugar_recogida)
        travel.addCar(car)
        dni, nombre, apellido, tlf, sexo, nacionalidad = 1, 'David', 'Duran', 4545454, 'Hombre', 'Española'
        self.assertFalse(travel.confirmCars(u.User(dni, nombre, apellido, tlf, sexo, nacionalidad)))

    #TEST V5
    '''
    Dado un viaje con múltiples destinos y más de un viajero, cuando se produce un
    error al confirmar los vehículos, se reintenta realizar la confirmación
    '''

    @mock.patch('src.Travel.r.Rentalcars')
    def test_reintentar_confirmar_vehiculo(self, mook):
        mook.confirm_reserve.return_value = False
        travel = t.Travel()
        travel.vuelos.append(f.Flights(111, "Ibiza", 2, 30))
        travel.vuelos.append(f.Flights(222, "China", 2, 30))
        travel.viajeros = 2
        car = c.Cars("11111", "Mercedes", 3, 10, "Barcelona")
        travel.addCar(car)
        confirmacion = travel.confirm_cars_reintentos(u.User(1, 'David', 'Duran', 4545454, 'Hombre', 'Española'))
        self.assertFalse(confirmacion)

    '''
    Dado un viaje con múltiples destinos y más de un viajero, cuando la
    confirmación de los vehículos se realiza correctamente en un reintento, se
    reporta que la acción se ha realizado correctamente
    '''

    @mock.patch('src.Travel.r.Rentalcars')
    def test_reintentar_confirmar_vehiculo_correcto(self, mook):
        mook.confirm_reserve.side_effect = [False, True]
        travel = t.Travel()
        travel.vuelos.append(f.Flights(111, "Ibiza", 2, 30))
        travel.vuelos.append(f.Flights(222, "China", 2, 30))
        travel.viajeros = 2
        car = c.Cars("11111", "Mercedes", 3, 10, "Barcelona")
        travel.addCar(car)
        confimacion = travel.confirm_cars_reintentos(u.User(1, 'David', 'Duran', 4545454, 'Hombre', 'Española'))
        self.assertEqual(mook.confirm_reserve.call_count, 2)
        self.assertTrue(confimacion)

    '''
    Dado un viaje con múltiples destinos y más de un viajero, cuando se produce un
    error al confirmar los vehículos, y se ha superado el número máximo de
    reintentos, se reporta que la acción no se ha podido realizar
    '''

    @mock.patch('src.Travel.r.Rentalcars')
    def test_reintentar_confirmar_vehiculo_maxIntent(self, mook):
        mook.confirm_reserve.return_value = False
        travel = t.Travel()
        travel.vuelos.append(f.Flights(111, "Ibiza", 2, 30))
        travel.vuelos.append(f.Flights(222, "China", 2, 30))
        travel.viajeros = 2
        car = c.Cars("11111", "Mercedes", 3, 10, "Barcelona")
        travel.addCar(car)
        confimacion = travel.confirm_cars_reintentos(u.User(1, 'David', 'Duran', 4545454, 'Hombre', 'Española'))
        self.assertFalse(confimacion)


if __name__ == '__main__':
    unittest.main()
