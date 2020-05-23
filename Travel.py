import Flights as f
import Bank as b
import Skyscanner as s
import Rentalcars as r
import Booking as b

class Travel:

    def __init__(self, vuelo=[], dest=[], viajeros=1):
        self.vuelos = vuelo
        self.destinos = dest
        self.viajeros = viajeros
        self.cars = []
        self.hoteles = []
        self.precio = 0
        self.pagado = False
        self.reservas = False
        self.updatePrecio()
        self.reintentos_vuelo = 3

    def addViajero(self, num):
        self.viajeros += num
        for i in self.vuelos:
            i.num_viajeros = self.viajeros
        self.updatePrecio()

    def delViajero(self, num):
        self.viajeros += -num
        for i in self.vuelos:
            i.num_viajeros=self.viajeros
        self.updatePrecio()

    def addDestino(self,destino):
        vuelo = f.Flights(len(self.vuelos)+1,destino,self.viajeros)
        self.vuelos.append(vuelo)
        self.destinos.append(destino)
        self.updatePrecio()

    def delDestino(self,destino):
        index = self.destinos.index(destino)
        self.vuelos.pop(index)
        self.destinos.pop(index)
        self.updatePrecio()

    def addVuelo(self,vuelo):
        self.vuelos.append(vuelo)
        self.destinos.append(vuelo.destino)
        self.updatePrecio()

    def updatePrecio(self):
        precio = 0
        for i in self.vuelos: precio += (i.precio * self.viajeros)
        for car in self.cars: precio += car.dias * car.precio_dia
        for hotel in self.hoteles: precio += (hotel.precio_dia * hotel.numero_hostes * hotel.durada_reserva)
        self.precio=precio

    def payTravel(self,bank):
        if(bank.comprobar_saldo(self.precio)):
            self.pagado=  bank.do_payment(bank.user, bank.pago)
        self.confirmacionPago(bank)

    def confirmacionPago(self,bank):
        if(self.pagado==True):
            print("El pago se ha realizado correctamente")
        else:
            print("El pago no se ha realizado correctamente, revise los datos de pago")
            while(bank.reintentos > 0):
                bank.reintentos -= 1
                self.payTravel(bank)

    def realizarReservas(self,user):
        if(len(self.vuelos) > 0):
            sky = s.Skyscanner()
            self.reservas = sky.confirm_reserve(user,self.vuelos)
        self.confirmacionReservas(user)

    def confirmacionReservas(self,user):
        if(self.reservas==True):
            print("Las reservas se han realizado correctamente")
        else:
            print("La reserva no se ha realizado correctamente, revise los datos")
            while(self.reintentos_vuelo > 0):
                self.reintentos_vuelo -= 1
                self.realizarReservas(user)

    def getVuelos(self):
        for i in self.vuelos:
            print("Vuelo con codigo: "+str(i.codigo)+", con destino: "+i.destino+", con "+str(i.num_viajeros)+" viajeros")

    def addCar(self, car):
        self.cars.append(car)
        self.updatePrecio()

    def delCar(self, car):
        self.cars.remove(car)
        self.updatePrecio()

    def addHotel(self, hotel):
        self.hoteles.append(hotel)
        self.updatePrecio()

    def delHotel(self, hotel):
        self.hoteles.remove(hotel)
        self.updatePrecio()

    def confirmCars(self, user):
        rent = r.Rentalcars()
        if len(self.cars) > 0:
            if rent.confirm_reserve(user, self.cars):
                print("Vehiculos reservados correctamente")
                return True
            else:
                 print("Error en la reserva de vehiculos")
        else:
            print("No hay vehiculos a reservar")
        return False

    def confirmHotels(self, user):
        book = b.Booking()
        if len(self.hoteles) > 0:
            if book.confirm_reserve(user, self.hoteles):
                print("Alojamientos reservados correctamente")
                return True
            else:
                 print("Error en la reserva de Alojamientos")
        else:
            print("No hay Alojamientos a reservar")
        return False

