class Factura:

    def __init__(self, user,DNI, direc,email):

        self.nombre_completo = user.nombre +user.apellidos
        self.DNI = DNI
        self.direccio=direc
        self.telefono = user.telefono
        self.email = email


    def comprobar_datos(self):
        datos_OK=True
        error="El"
        if not self.nombre_completo.isalpha():
            error +=" nombre "
            datos_OK= False

        numeros_dni= self.DNI[0:-1]
        caracter= self.DNI[-1:]
        if not numeros_dni.isalnum() or not caracter.isalpha() or len(self.DNI)!=9:
            error += " DNI "
            datos_OK= False
        if not self.telefono.isalnum() or len(self.telefono)!=9:
            error += " Telefono "
            datos_OK= False
        if self.email.find("@")==-1:
            error += " email "
            datos_OK= False

        if datos_OK:
            print("Los datos de la facturación han sido introducidos correctamente")
        else:
            print(error+" no tiene un formato correcto")
        return datos_OK