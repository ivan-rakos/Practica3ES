import User
import Flights as f
import Bank as b
import Skyscanner as s


class Travel:
    def __init__(self,vuelo=[],dest=[],viajeros=1):
        self.vuelos = vuelo
        self.destinos = dest
        self.viajeros=viajeros
        self.precio=0
        self.pagado=False
        self.reservas = False
        self.updatePrecio()

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
        for i in self.vuelos:
            precio += (i.precio * self.viajeros)
        self.precio=precio

    def payTravel(self,bank):
        self.pagado=  bank.do_payment(bank.user, bank.pago)
        self.confirmacionPago()

    def confirmacionPago(self):
        if(self.pagado==True): print("El pago se ha realizado correctamente")

    def realizarReservas(self,user):
        sky = s.Skyscanner()
        self.reservas = sky.confirm_reserve(user,self.vuelos)
        self.confirmacionReservas()

    def confirmacionReservas(self):
        if(self.reservas==True):print("Las reservas se han realizado correctamente")

    def getVuelos(self):
        for i in self.vuelos:
            print("Vuelo con codigo: "+str(i.codigo)+", con destino: "+i.destino+", con "+str(i.num_viajeros)+" viajeros")
