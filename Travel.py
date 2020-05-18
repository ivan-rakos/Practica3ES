import User
import Flights as f


class Travel:
    def __init__(self,vuelo=[],dest=[],viajeros=1,precio=0):
        self.vuelos = vuelo
        self.destinos = dest
        self.viajeros=viajeros
        self.precio=precio
        self.updatePrecio()

    def addViajero(self):
        self.viajeros += 1
        for i in self.vuelos:
            i.num_viajeros = self.viajeros
        self.updatePrecio()

    def delViajero(self):
        self.viajeros += -1
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


