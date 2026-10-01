import unittest
from validacao import validar_quantidade


class TestValidacao(unittest.TestCase):
    def test_comum(self):
        self.assertEqual(validar_quantidade(8), True)

    def test_limite(self):
        self.assertEqual(validar_quantidade(0), True)

    def test_invalido(self):
        with self.assertRaises(ValueError):
            validar_quantidade(-1)