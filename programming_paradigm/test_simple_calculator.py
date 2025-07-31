import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Create a calculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        self.assertEqual(self.calc.add(3, 2), 5)
        self.assertEqual(self.calc.add(-1, -1), -2)
        self.assertEqual(self.calc.add(-1, 1), 0)

    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(0, 5), -5)
        self.assertEqual(self.calc.subtract(-2, -2), 0)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(4, 3), 12)
        self.assertEqual(self.calc.multiply(-1, 5), -5)
        self.assertEqual(self.calc.multiply(0, 100), 0)

    def test_divide(self):
        self.assertEqual(self.calc.divide(10, 2), 5.0)
        self.assertEqual(self.calc.divide(5, -1), -5.0)
        self.assertEqual(self.calc.divide(0, 10), 0.0)

    def test_divide_by_zero(self):
        self.assertIsNone(self.calc.divide(10, 0))
