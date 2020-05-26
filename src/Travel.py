from src import Bank as b, Booking as bo, Flights as f, Rentalcars as r, Skyscanner as s


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
        self.reintentos_vehiculo = 3
        self.reintentos_hoteles = 3
        self.reintentos_pago = 3

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

    def payTravel(self,user, pago):
        if pago.tipo_pago == 'VISA' or pago.tipo_pago == 'Mastercard':
            self.pagado = b.Bank.do_payment(0,user, pago)
        if self.pagado:
            print("Pago realizado correctamente")
        else:
            print("Error de pago")
        return self.pagado

    def confirmacionPago(self,user, pago):
        while not self.payTravel(user,pago) and self.reintentos_pago > 0:
            self.reintentos_pago -= 1
            print("Reintentando...")

        if self.reintentos_pago == 0:
            print("Superado el número máximo de reintentos\n")
            return False
        else:
            return True

    def realizarReservas(self,user):
        if(len(self.vuelos) > 0):
            self.reservas = s.Skyscanner.confirm_reserve(0,user,self.vuelos)
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
        if len(self.cars) > 0:
            if r.Rentalcars.confirm_reserve(0, user, self.cars):
                print("Vehiculos reservados correctamente\n")
                return True
            print("Error en la reserva del vehiculo")
        else:
            print("No hay vehiculos a reservar")
        return False

    def confirm_cars_reintentos(self, user):
        while not self.confirmCars(user) and self.reintentos_vehiculo > 0:
            self.reintentos_vehiculo -=1
            print("Reintentando...")

        if self.reintentos_vehiculo == 0:
            print("Superado el número máximo de reintentos\n")
            return False
        else:
            print("Vehiculos reservados correctamente\n")
            return True

    def confirmHotels(self, user):
        if len(self.hoteles) > 0:
            if bo.Booking.confirm_reserve(0, user, self.hoteles):
                print("Alojamientos reservados correctamente\n")
                return True
            print("Error en la reserva")
        else:
            print("No hay Alojamientos a reservar")
        return False

    def confirm_Hotels_reintentos(self, user):
        while not self.confirmHotels(user) and self.reintentos_hoteles > 0:
            self.reintentos_hoteles -=1
            print("Reintentando...")

        if self.reintentos_hoteles == 0:
            print("Superado el número máximo de reintentos\n")
            return False
        else:
            print("Vehiculos reservados correctamente\n")
            return True

    def confirmacionVuelos(self,user):
        if (len(self.vuelos)>0):
            sky = s.Skyscanner.confirm_reserve(0,user,self.vuelos)
            if sky:
                print("Reserva realizada correctamente")
                return True
        print("La acción no se ha podido realizar")
        return False

    def confirm_Vuelos_reintentos(self, user):
        while not self.confirmacionVuelos(user) and self.reintentos_vuelo > 0:
            self.reintentos_vuelo -= 1
            print("Reintentando...")

        if self.reintentos_vuelo == 0:
            print("Superado el número máximo de reintentos\n")
            return False
        else:
            print("Vuelos reservados correctamente\n")
            return True

