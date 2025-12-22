from src.fibo.fibo import fibo_recursive, fibo
from src.utils.commands_abc import DefaultCommand


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
