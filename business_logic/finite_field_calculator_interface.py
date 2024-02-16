from abc import ABC, abstractmethod
from typing import Any


class IFiniteFieldCalculator(ABC):
    @abstractmethod
    def add(self, operand1: Any, operand2: Any, prime_num: Any) -> Any:
        pass

    @abstractmethod
    def subtract(self, operand1: Any, operand2: Any, prime_num: Any) -> Any:
        pass

    @abstractmethod
    def multiply(self, operand1: Any, operand2: Any, prime_num: Any) -> Any:
        pass

    @abstractmethod
    def divide(self, dividend: Any, divisor: Any, prime_num: Any) -> Any:
        pass

    @abstractmethod
    def exponentiate(self, base_num: Any, exponent: Any, prime_num: Any) -> Any:
        pass

    @abstractmethod
    def valid_operand(self, operand: Any, prime_num: Any) -> bool:
        pass
