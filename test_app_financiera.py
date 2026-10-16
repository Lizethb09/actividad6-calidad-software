
import unittest

from app_financiera import (
    calcular_saldo,
    procesar_transferencia,
)


class TestAppFinanciera(unittest.TestCase):

    def test_calcular_saldo(self):
        resultado = calcular_saldo(
            100000,
            [25000, 15000],
            [10000, 5000],
        )
        self.assertEqual(resultado, 125000)

    def test_transferencia_exitosa(self):
        saldo, mensaje = procesar_transferencia(125000, 20000)
        self.assertEqual(saldo, 105000)
        self.assertEqual(mensaje, "Transferencia procesada")

    def test_saldo_insuficiente(self):
        saldo, mensaje = procesar_transferencia(10000, 20000)
        self.assertEqual(saldo, 10000)
        self.assertEqual(mensaje, "Saldo insuficiente")

    def test_monto_cero(self):
        saldo, mensaje = procesar_transferencia(10000, 0)
        self.assertEqual(saldo, 10000)
        self.assertEqual(mensaje, "El monto debe ser mayor que cero")


if __name__ == "__main__":
    unittest.main()
