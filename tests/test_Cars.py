import unittest
from unittest import mock
from data_test import DataSet as data

class MyTestCase(unittest.TestCase):

    def test_addCars(self):
        datos = data.DataSet()
        travel=datos.viaje
        travel.addCar(datos.car)
        self.assertTrue(travel.precio == 210)

    def test_delCars(self):
        datos = data.DataSet()
        travel = datos.viaje
        car = datos.car
        travel.addCar(car)
        travel.delCar(car)
        self.assertTrue(travel.precio == 180)

    def test_confirm_cars(self):
        datos = data.DataSet()
        travel = datos.viaje
        travel.addCar(datos.car)
        self.assertTrue(travel.confirmCars(datos.user))

    @mock.patch("src.Travel.r.Rentalcars")
    def test_confirm_cars_error(self,mock):
        datos = data.DataSet()
        travel = datos.viaje
        mock.confirm_reserve.return_value = False
        travel.addCar(datos.car)
        self.assertFalse(travel.confirmCars(datos.user))

    #TEST V5
    '''
    Dado un viaje con múltiples destinos y más de un viajero, cuando se produce un
    error al confirmar los vehículos, se reintenta realizar la confirmación
    '''

    @mock.patch('src.Travel.r.Rentalcars')
    def test_reintentar_confirmar_vehiculo(self, mook):
        datos = data.DataSet()
        mook.confirm_reserve.return_value = False
        travel = datos.viaje
        travel.addCar(datos.car)
        confirmacion = travel.confirm_cars_reintentos(datos.user)
        self.assertFalse(confirmacion)

    '''
    Dado un viaje con múltiples destinos y más de un viajero, cuando la
    confirmación de los vehículos se realiza correctamente en un reintento, se
    reporta que la acción se ha realizado correctamente
    '''

    @mock.patch('src.Travel.r.Rentalcars')
    def test_reintentar_confirmar_vehiculo_correcto(self, mook):
        datos = data.DataSet()
        mook.confirm_reserve.side_effect = [False, True]
        travel = datos.viaje
        travel.addCar(datos.car)
        confimacion = travel.confirm_cars_reintentos(datos.user)
        self.assertEqual(mook.confirm_reserve.call_count, 2)
        self.assertTrue(confimacion)

    '''
    Dado un viaje con múltiples destinos y más de un viajero, cuando se produce un
    error al confirmar los vehículos, y se ha superado el número máximo de
    reintentos, se reporta que la acción no se ha podido realizar
    '''

    @mock.patch('src.Travel.r.Rentalcars')
    def test_reintentar_confirmar_vehiculo_maxIntent(self, mook):
        datos = data.DataSet()
        mook.confirm_reserve.return_value = False
        travel = datos.viaje
        travel.addCar(datos.car)
        confimacion = travel.confirm_cars_reintentos(datos.user)
        self.assertFalse(confimacion)


if __name__ == '__main__':
    unittest.main()
