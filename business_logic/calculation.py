class Calculation:
    def __init__(self, prime_num: int) -> None:
        self.prime_num = prime_num

    def add(self, operand1: int, operand2: int) -> int:
        return (operand1 + operand2) % self.prime_num

    def subtract(self, operand1: int, operand2: int) -> int:
        return (operand1 - operand2 + self.prime_num) % self.prime_num

    def multiply(self, operand1: int, operand2: int) -> int:
        return (operand1 * operand2) % self.prime_num

    def divide(self, dividend: int, divisor: int) -> int:
        if divisor == 0:
            raise ValueError("Cannot divide by zero in the finite field.")
        inverse = self._mod_inv(divisor)
        return (dividend * inverse) % self.prime_num

    def exponentiate(self, base_num: int, exponent: int) -> int:
        return pow(base_num, exponent, self.prime_num)

    def valid_operand(self, operand: int) -> bool:
        return 0 <= operand < self.prime_num

    def _mod_inv(self, a: int) -> int:
        m = self.prime_num
        m0, x0, x1 = m, 0, 1
        while a > 1:
            q = a // m
            m, a = a % m, m
            x0, x1 = x1 - q * x0, x0
        return x1 + m0 if x1 < 0 else x1
