from math import isqrt

class NISTPrimesGenerator:
    @staticmethod
    def get_p192() -> int:
        return 2**192 - 2**64 - 1

    @staticmethod
    def get_p224() -> int:
        return 2**224 - 2**96 + 1

    @staticmethod
    def get_p256() -> int:
        return 2**256 - 2**224 + 2**192 + 2**96 - 1

    @staticmethod
    def get_p384() -> int:
        return 2**384 - 2**128 - 2**96 + 2**32 - 1

    @staticmethod
    def get_p521() -> int:
        return 2**521 - 1
