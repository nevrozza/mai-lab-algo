from src.utils.commands_abc import DefaultCommand
from src.utils.consts import N_MUST_BE_GREATER_ZERO
from src.utils.utils import require


def factorial(n: int) -> int:
    require(n >= 0, N_MUST_BE_GREATER_ZERO)
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def factorial_recursive(n: int) -> int:
    require(n >= 0, N_MUST_BE_GREATER_ZERO)
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)


class FactorialCommand(DefaultCommand):
    def solve(self) -> str:
        n = int(self._params[0])
        is_recursive = "r" in self._flags
        if is_recursive:
            result = factorial_recursive(n)
        else:
            result = factorial(n)
        return str(result)

    @property
    def _supported_flags(self) -> str:
        return "r"

    @classmethod
    def name(cls) -> str:
        return "factorial"
