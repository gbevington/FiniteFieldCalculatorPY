import unittest

import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../")

from business_logic.validation import ValidationMethods


class TestValidationMethods(unittest.TestCase):
    def test_is_probable_prime(self):
        # Test some known prime numbers
        self.assertTrue(ValidationMethods.is_probable_prime(2, 5))
        self.assertTrue(ValidationMethods.is_probable_prime(3, 5))
        self.assertTrue(ValidationMethods.is_probable_prime(5, 5))
        self.assertTrue(ValidationMethods.is_probable_prime(7, 5))
        self.assertTrue(ValidationMethods.is_probable_prime(11, 5))
        self.assertTrue(ValidationMethods.is_probable_prime(13, 5))

        # Test some known composite numbers
        self.assertFalse(ValidationMethods.is_probable_prime(1, 5))
        self.assertFalse(ValidationMethods.is_probable_prime(4, 5))
        self.assertFalse(ValidationMethods.is_probable_prime(6, 5))
        self.assertFalse(ValidationMethods.is_probable_prime(8, 5))
        self.assertFalse(ValidationMethods.is_probable_prime(9, 5))
        self.assertFalse(ValidationMethods.is_probable_prime(10, 5))

    def test_is_prime(self):
        # Test some known prime numbers
        self.assertTrue(ValidationMethods.is_prime(2))
        self.assertTrue(ValidationMethods.is_prime(3))
        self.assertTrue(ValidationMethods.is_prime(5))
        self.assertTrue(ValidationMethods.is_prime(7))
        self.assertTrue(ValidationMethods.is_prime(11))
        self.assertTrue(ValidationMethods.is_prime(13))

        # Test some known composite numbers
        self.assertFalse(ValidationMethods.is_prime(1))
        self.assertFalse(ValidationMethods.is_prime(4))
        self.assertFalse(ValidationMethods.is_prime(6))
        self.assertFalse(ValidationMethods.is_prime(8))
        self.assertFalse(ValidationMethods.is_prime(9))
        self.assertFalse(ValidationMethods.is_prime(10))

    def test_is_valid_operand(self):
        prime_num = 11
        # Test valid operands
        self.assertTrue(ValidationMethods.is_valid_operand(0, prime_num))
        self.assertTrue(ValidationMethods.is_valid_operand(1, prime_num))
        self.assertTrue(ValidationMethods.is_valid_operand(5, prime_num))
        self.assertTrue(ValidationMethods.is_valid_operand(10, prime_num))

        # Test invalid operands
        self.assertFalse(ValidationMethods.is_valid_operand(-1, prime_num))
        self.assertFalse(ValidationMethods.is_valid_operand(11, prime_num))
        self.assertFalse(ValidationMethods.is_valid_operand(100, prime_num))


if __name__ == '__main__':
    unittest.main()
