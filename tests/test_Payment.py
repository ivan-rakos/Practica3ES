import unittest
from src import Factura as fa
from data_test import  DataSet as data
from unittest import mock

class MyTestCase(unittest.TestCase):


    def test_MultiplesDesinosMetodoPago(self):
        datos = data.DataSet()
        viaje = datos.viaje
        self.assertTrue(viaje.payTravel(datos.user, datos.pago))

    @mock.patch("src.Travel.b.Bank")
    def test_MultiplesDestinosErrorPago(self, mock):
        datos = data.DataSet()
        viaje = datos.viaje
        mock.do_payment.return_value = False
        self.assertFalse(viaje.payTravel(datos.user, datos.pago))


    def test_reiintento_pago(self):
        datos = data.DataSet()
        viaje = datos.viaje
        pago = datos.pago
        pago.tipo_pago='Viza'
        viaje.confirmacionPago(datos.user,pago)
        self.assertLess(viaje.reintentos_pago,3)

    @mock.patch("src.Travel.b.Bank")
    def test_segundo_reintento(self, mock):
        datos = data.DataSet()
        mock.do_payment.side_effect = [False, True]
        viaje=datos.viaje
        viaje.confirmacionPago(datos.user,datos.pago)
        self.assertEqual(mock.do_payment.call_count, 2)

        '''
        Dado un viaje con múltiples destinos y más de un viajero, cuando los datos de
        facturación introducidos por el usuario son correctos, se reporta que los datos
        son correctos
        '''

    def test_datos_facturacion_OK(self):
        datos = data.DataSet()
        factura = fa.Factura(datos.user, '12345678A', 'Calle Falsa 123', 'fake@gmail.om')
        self.assertTrue(factura.comprobar_datos())

    def test_datos_facturacion_error(self):
        datos = data.DataSet()
        factura = fa.Factura(datos.user, '123456SSA', 'Calle Falsa 123', 'fake@gmail.com')
        self.assertFalse(factura.comprobar_datos())

    """    
    Dado un viaje con múltiples destinos y más de un viajero, cuando los datos de
    facturación introducidos por el usuario son correctos, la información de la
    factura está completa
    """

    def test_info_fac_completa(self):
        datos = data.DataSet()
        factura = fa.Factura(datos.user, '12345678A', 'Calle Falsa 123', 'fake@gmail.om')
        self.assertTrue(factura.inf_factura_completa())

if __name__ == '__main__':
    unittest.main()

