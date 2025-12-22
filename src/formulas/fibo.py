from src.utils.commands_abc import DefaultCommand
from src.utils.consts import N_MUST_BE_GREATER_ZERO
from src.utils.utils import require


def __fibo_initial(n: int) -> int | None:
    require(n >= 0, N_MUST_BE_GREATER_ZERO)
    if n <= 1:
        return n
    return None


def fibo(n: int) -> int:
    if __fibo_initial(n) is not None:
        return n

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def fibo_recursive(n: int) -> int:
    if __fibo_initial(n) is not None:
        return n

    return fibo_recursive(n - 1) + fibo_recursive(n - 2)


class FiboCommand(DefaultCommand):
    def solve(self) -> str:
        n = int(self._params[0])
        is_recursive = "r" in self._flags
        if is_recursive:
            result = fibo_recursive(n)
        else:
            result = fibo(n)
        return str(result)

    @property
    def _supported_flags(self) -> str:
        return "r"

    @classmethod
    def name(cls) -> str:
        return "fibo"
