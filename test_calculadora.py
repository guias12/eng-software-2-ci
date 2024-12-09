from calculadora import Calculadora
import unittest

class TestCalculadora(unittest.TestCase):
    def setUp(self):
        self.calc = Calculadora()

    def test_somar(self):
        self.assertEqual(self.calc.somar(2, 3), 5)
        self.assertEqual(self.calc.somar(-1, 1), 0)
        self.assertEqual(self.calc.somar(0, 0), 0)

    def test_subtrair(self):
        self.assertEqual(self.calc.subtrair(5, 3), 2)
        self.assertEqual(self.calc.subtrair(0, 3), -3)
        self.assertEqual(self.calc.subtrair(-3, -3), 0)

    def test_multiplicar(self):
        self.assertEqual(self.calc.multiplicar(2, 3), 6)
        self.assertEqual(self.calc.multiplicar(-2, 3), -6)
        self.assertEqual(self.calc.multiplicar(0, 3), 0)

    def test_dividir(self):
        self.assertEqual(self.calc.dividir(6, 3), 2)
        self.assertEqual(self.calc.dividir(-6, 3), -2)
        with self.assertRaises(ValueError):
            self.calc.dividir(5, 0)

if __name__ == "__main__":
    unittest.main()
