from src.factorial.factorial import factorial_recursive, factorial
from src.utils.commands_abc import DefaultCommand


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
