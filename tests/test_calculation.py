import unittest

import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../")

from business_logic.calculation import Calculation

class TestCalculation(unittest.TestCase):
    def setUp(self):
        # Initialize a Calculation object with a prime number
        self.calc = Calculation(prime_num=11)

    def test_add(self):
        # Test addition method
        result = self.calc.add(3, 4)
        self.assertEqual(result, 7)

    def test_subtract(self):
        # Test subtraction method
        result = self.calc.subtract(10, 5)
        self.assertEqual(result, 5)

    def test_multiply(self):
        # Test multiplication method
        result = self.calc.multiply(2, 3)
        self.assertEqual(result, 6)

    def test_divide(self):
        # Test division method
        result = self.calc.divide(10, 2)
        self.assertEqual(result, 5)

    def test_exponentiate(self):
        # Test exponentiation method
        result = self.calc.exponentiate(2, 3)
        self.assertEqual(result, 8)

    def test_valid_operand(self):
        # Test valid_operand method
        self.assertTrue(self.calc.valid_operand(7))
        self.assertFalse(self.calc.valid_operand(11))  # Outside range

if __name__ == '__main__':
    unittest.main()
