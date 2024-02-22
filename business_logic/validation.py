import random
from math import isqrt

import tkinter as tk
from tkinter import messagebox

class ValidationMethods:
    @staticmethod
    def is_probable_prime(n: int, certainty: int) -> bool:
        if n <= 1:
            return False
        if n == 2 or n == 3:
            return True
        if n % 2 == 0:
            return False
        
        d = n - 1
        s = 0
        while d % 2 == 0:
            d //= 2
            s += 1
        
        for _ in range(certainty):
            a = random.randint(2, n - 2)
            x = pow(a, d, n)
            if x == 1 or x == n - 1:
                continue
            for _ in range(1, s):
                x = pow(x, 2, n)
                if x == 1:
                    return False
                if x == n - 1:
                    break
            if x != n - 1:
                return False
        
        return True

    @staticmethod
    def is_prime(number: int) -> bool:
        return ValidationMethods.is_probable_prime(number, 5)  # Adjust certainty as needed

    @staticmethod
    def is_valid_operand(operand: int, prime_num: int) -> bool:
        if not (0 <= operand < prime_num):
            messagebox.showerror("Invalid Operand", "Operand must be between zero and the prime input number minus one.")
            return False
        return True