from src.utils.consts import FACTORIAL_MUST_BE_POSITIVE
from src.utils.utils import require


def factorial(n: int) -> int:
    require(n > 0, FACTORIAL_MUST_BE_POSITIVE)
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def factorial_recursive(n: int) -> int:
    require(n > 0, FACTORIAL_MUST_BE_POSITIVE)
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)
