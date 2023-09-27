import unittest
from unittest.mock import patch
from cli import consultar_precio

class TestStockBot(unittest.TestCase):

    @patch('cli.requests.get')
    def test_consultar_precio_valido(self, mock_get):
        # Simular una respuesta exitosa de la solicitud HTTP
        mock_get.return_value.status_code = 200
        mock_get.return_value.text = 'Symbol,Date,Time,Open,High,Low,Close,Volume\nAAPL.US,2023-01-01,00:00:00,150.0,155.0,148.0,152.0,100000\n'

        # Probar consultar_precio para un código de acción válido
        price = consultar_precio("AAPL")
        self.assertIsNotNone(price)
        self.assertTrue(price != "")  # Verificar que el precio no sea una cadena vacía

    @patch('cli.requests.get')
    def test_consultar_precio_invalido(self, mock_get):
        # Simular una respuesta 404 para un código de acción inválido
        mock_get.return_value.status_code = 404

        # Probar consultar_precio para un código de acción inválido
        price = consultar_precio("INVALID")
        self.assertIsNone(price)


if __name__ == '__main__':
    unittest.main()
