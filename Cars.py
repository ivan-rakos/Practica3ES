class Cars:

    def __init__(self, matricula, modelo, dias, precio_dia, recogida):
        self.matricula = matricula
        self.modelo = modelo
        self.estado = True
        self.dias = dias
        self.precio_dia = precio_dia
        self.recogida = recogida

    def Consulta_estado(self):
        return self.estado

    def Cambia_estado(self):
        self.estado = not self.estado
