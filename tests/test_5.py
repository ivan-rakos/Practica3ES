import unittest
from src import Flights as f, Cars as c, Hotels as h, Factura as fa, User as u, Travel as t


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.users = [
            ['David', 'Duran', '654378018', 'M', 'Española'],
            ['Xavi123', 'Lopez', '6543780A', 'M', 'Mexicana'],
            ['Charly', 'Garay', '654378016', 'M', 'Paraguaya'],
            ['Bernat', 'Mallol', '654381965', 'M', 'China'],
            ['Ivan', 'Jimenez', '652728162', 'M', 'Argentina']
        ]
        self.datos_pago = ['Visa', 'David Durán', '9999 8888 7777 6666', '123', 150]
        self.viajeros = [1, 2, 3, 4, 5]
        self.destinos = ['Berlin', 'Madrid', 'Roma', 'Paris', 'London']
        self.testNumViajeros = [2, 3, 4, 5, 6]
        self.testEliminarViajero = [0, 1, 2, 3, 4]

    '''
    Dado un viaje con múltiples destinos y más de un viajero, cuando los datos de
    facturación introducidos por el usuario son correctos, se reporta que los datos
    son correctos
    '''


    def test_datos_facturacion_OK(self):

        travel = t.Travel()
        travel.vuelos.append(f.Flights(111, "Ibiza", 2, 30))
        travel.vuelos.append(f.Flights(222, "China", 2, 30))
        travel.viajeros = 2
        nombre, apellido, telf, sex, nac = self.users[0]
        user = u.User(1, nombre, apellido, telf, sex, nac)
        factura= fa.Factura(user,'12345678A','Calle Falsa 123','fake@gmail.om')
        self.assertTrue(factura.comprobar_datos() == True)

    def test_datos_facturacion_error(self):

        travel = t.Travel()
        travel.vuelos.append(f.Flights(111, "Ibiza", 2, 30))
        travel.vuelos.append(f.Flights(222, "China", 2, 30))
        travel.viajeros = 2
        nombre, apellido, telf, sex, nac = self.users[1]
        user = u.User(2, nombre, apellido, telf, sex, nac)
        factura= fa.Factura(user,'12345678A','Calle Falsa 123','fake@gmail.com')

        self.assertTrue(factura.comprobar_datos()==False )

    '''
    Dado un viaje con múltiples destinos y más de un viajero, cuando se produce un
    error al confirmar los vehículos, se reintenta realizar la confirmación
    '''

    def test_reintentar_confirmar_vehiculo(self):
        travel = t.Travel()
        travel.vuelos.append(f.Flights(111, "Ibiza", 2, 30))
        travel.vuelos.append(f.Flights(222, "China", 2, 30))
        travel.viajeros = 2

        confirmacion = travel.confirmCars(u.User(1, 'David', 'Duran', 4545454, 'Hombre', 'Española'))

        if not confirmacion:
            print("reintentando confirmación de veiculo")
            confirmacion = travel.confirmCars(u.User(1, 'David', 'Duran', 4545454, 'Hombre', 'Española'))
        self.assertFalse(confirmacion)
    '''
    Dado un viaje con múltiples destinos y más de un viajero, cuando la
    confirmación de los vehículos se realiza correctamente en un reintento, se
    reporta que la acción se ha realizado correctamente
    '''
    def test_reintentar_confirmar_vehiculo_correcto(self):
        travel = t.Travel()
        travel.vuelos.append(f.Flights(111, "Ibiza", 2, 30))
        travel.vuelos.append(f.Flights(222, "China", 2, 30))
        travel.viajeros = 2
        car=c.Cars("11111", "Mercedes", 3, 10, "Barcelona")
        confimacion = travel.confirmCars(u.User(1, 'David', 'Duran', 4545454, 'Hombre', 'Española'))
        if not confimacion:
            print("reintentando confirmación de veiculo")
            confimacion= travel.addCar(car)
            confimacion = travel.confirmCars(u.User(1, 'David', 'Duran', 4545454, 'Hombre', 'Española'))

        self.assertTrue(confimacion == True)

    '''
    Dado un viaje con múltiples destinos y más de un viajero, cuando se produce un
    error al confirmar los vehículos, y se ha superado el número máximo de
    reintentos, se reporta que la acción no se ha podido realizar
    '''

    def test_reintentar_confirmar_vehiculo_maxIntent(self):
        travel = t.Travel()
        travel.vuelos.append(f.Flights(111, "Ibiza", 2, 30))
        travel.vuelos.append(f.Flights(222, "China", 2, 30))
        travel.viajeros = 2

        cont =0
        confimacion = travel.confirmCars(u.User(1, 'David', 'Duran', 4545454, 'Hombre', 'Española'))
        while(not confimacion and cont<5):
            print("reintentando confirmación de veiculo")
            confimacion=travel.confirmCars(u.User(1, 'David', 'Duran', 4545454, 'Hombre', 'Española'))
            cont +=1
        if  not confimacion and cont==5:
            print("Se ha superado el numero de intentos")
        self.assertTrue(confimacion == False and cont==5)
    '''
    Dado un viaje con múltiples destinos y más de un viajero, cuando se produce un
    error al confirmar los alojaminetos, se reintenta realizar la confirmación
    '''

    def test_reintentar_confirmar_alojamineto(self):
        travel = t.Travel()
        travel.vuelos.append(f.Flights(111, "Ibiza", 2, 30))
        travel.vuelos.append(f.Flights(222, "China", 2, 30))
        travel.viajeros = 2

        confimacion = travel.confirmHotels(u.User(1, 'David', 'Duran', 4545454, 'Hombre', 'Española'))

        if not confimacion:
            print("Reintentando confirmación de alojamineto")
            confimacion = travel.confirmHotels(u.User(1, 'David', 'Duran', 4545454, 'Hombre', 'Española'))

        self.assertTrue(confimacion == False)
    '''
    Dado un viaje con múltiples destinos y más de un viajero, cuando la
    confirmación de los alojaminetos se realiza correctamente en un reintento, se
    reporta que la acción se ha realizado correctamente
    '''
    def test_reintentar_confirmar_alojamineto_correcto(self):
        travel = t.Travel()
        travel.vuelos.append(f.Flights(111, "Ibiza", 2, 30))
        travel.vuelos.append(f.Flights(222, "China", 2, 30))
        travel.viajeros = 2

        hotel=h.Hotels(111, "Hotel", 2, 34, 3, 30)
        confimacion = travel.confirmHotels(u.User(1, 'David', 'Duran', 4545454, 'Hombre', 'Española'))
        if not confimacion:
            print("reintentando confirmación de alojamineto")
            confimacion = travel.addHotel(hotel)
            confimacion = travel.confirmHotels(u.User(1, 'David', 'Duran', 4545454, 'Hombre', 'Española'))

        self.assertTrue(confimacion == True)

    '''
    Dado un viaje con múltiples destinos y más de un viajero, cuando se produce un
    error al confirmar los alojaminetos, y se ha superado el número máximo de
    reintentos, se reporta que la acción no se ha podido realizar
    '''

    def test_reintentar_confirmar_alojamineto_maxIntent(self):
        travel = t.Travel()
        travel.vuelos.append(f.Flights(111, "Ibiza", 2, 30))
        travel.vuelos.append(f.Flights(222, "China", 2, 30))
        travel.viajeros = 2


        cont =0
        confimacion = travel.confirmHotels(u.User(1, 'David', 'Duran', 4545454, 'Hombre', 'Española'))
        while(not confimacion and cont<5):
            print("reintentando confirmación de veiculo")
            confimacion=travel.confirmHotels(u.User(1, 'David', 'Duran', 4545454, 'Hombre', 'Española'))
            cont +=1
        if  not confimacion and cont==5:
            print("\n Se ha superado el numero de intentos")
        self.assertTrue(confimacion == False and cont==5)


if __name__ == '__main__':
    unittest.main()
