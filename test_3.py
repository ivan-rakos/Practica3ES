import unittest
import User as u
import Travel as t
import Flights as f
import Hotels as h
import Cars as c


class MyTestCase(unittest.TestCase):

    def test_addCars(self):
        travel = t.Travel()
        travel.vuelos = []
        travel.vuelos.append(f.Flights(111, "Ibiza", 2, 30))
        travel.viajeros = 2
        car = c.Cars("11111", "Mercedes", 3, 10, "Barcelona")
        travel.addCar(car)
        self.assertTrue(travel.precio == 90)

    def test_delCars(self):
        travel = t.Travel()  # como puede ser que este ya tenga el vuelo creado?
        travel.vuelos = []
        travel.vuelos.append(f.Flights(111, "Ibiza", 2, 30))
        travel.viajeros = 2
        car = c.Cars("11111", "Mercedes", 3, 10, "Barcelona")
        travel.cars.append(car)
        travel.delCar(car)
        self.assertTrue(travel.precio == 60)

    def test_addHotel(self):
        travel = t.Travel()
        travel.vuelos = []
        travel.vuelos.append(f.Flights(111, "Ibiza", 2, 30))
        travel.viajeros = 2
        travel.addHotel(h.Hotels(111, "Hotel", 2, 34, 3, 30))
        self.assertTrue(travel.precio == 240)

    def test_delHotel(self):
        travel = t.Travel()
        travel.vuelos = []
        travel.vuelos.append(f.Flights(111, "Ibiza", 2, 30))
        travel.viajeros = 2
        hotel = h.Hotels(111, "Hotel", 2, 34, 3, 30)
        travel.addHotel(hotel)
        travel.delHotel(hotel)
        self.assertTrue(travel.precio == 60)

    def test_confirm_cars(self):
        travel = t.Travel()
        travel.addCar(c.Cars("11111", "Mercedes", 3, 10, "Barcelona"))
        travel.confirmCars(u.User(1, 'David', 'Duran', 4545454, 'Hombre', 'Española'))

    def test_confirm_cars_error(self):
        travel = t.Travel()
        travel.confirmCars(u.User(1, 'David', 'Duran', 4545454, 'Hombre', 'Española'))

    def test_confirm_hotels(self):
        travel = t.Travel()
        travel.addHotel(h.Hotels(111, "Hotel", 2, 34, 3, 30))
        travel.confirmHotels(u.User(1, 'David', 'Duran', 4545454, 'Hombre', 'Española'))

    def test_confirm_hotels_error(self):
        travel = t.Travel()
        travel.confirmHotels(u.User(1, 'David', 'Duran', 4545454, 'Hombre', 'Española'))


if __name__ == '__main__':
    unittest.main()
