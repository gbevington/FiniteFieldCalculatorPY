import unittest

import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../")

from business_logic.nist_prime_generator import NISTPrimesGenerator


class TestNISTPrimesGenerator(unittest.TestCase):
    def test_p192(self):
        p192 = NISTPrimesGenerator.get_p192()
        self.assertTrue(self.is_prime(p192))

    def test_p224(self):
        p224 = NISTPrimesGenerator.get_p224()
        self.assertTrue(self.is_prime(p224))

    def test_p256(self):
        p256 = NISTPrimesGenerator.get_p256()
        self.assertTrue(self.is_prime(p256))

    def test_p384(self):
        p384 = NISTPrimesGenerator.get_p384()
        self.assertTrue(self.is_prime(p384))

    def test_p521(self):
        p521 = NISTPrimesGenerator.get_p521()
        self.assertTrue(self.is_prime(p521))

    def is_prime(self, n):
        """Check if a number is prime"""
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True


if __name__ == '__main__':
    unittest.main()
