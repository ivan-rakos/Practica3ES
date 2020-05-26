
from src import Factura as fa, PaymentData as p, Flights as f, User as u, Travel as t,Hotels as h, Cars as c

class DataSet:
    def __init__(self):
        self.precio = 30
        self.viajeros = 2
        self.vuelos = [f.Flights(1, "Berlin", self.viajeros, self.precio), f.Flights(2, "Madrid", self.viajeros, self.precio), f.Flights(3, "Roma", self.viajeros, self.precio)]
        self.destinos = ["Berlin", "Madrid", "Roma"]
        self.viaje = t.Travel(self.vuelos, self.destinos, self.viajeros)
        self.user = u.User(1, "Ivan", "Jimenez", "652748056", "M", "Española")
        self.pago = p.PaymentData("VISA", 'Iván Jiménez', "2000 1111 2222 3333", "123", 500)
        self.hotel = h.Hotels(111, "Hotel", 2, 34, 3, 30)
        self.car = c.Cars('AAA','Mercedes',3,10,'Barcelona')