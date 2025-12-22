from src.utils.commands_abc import SortIntCommand
from src.utils.consts import PARAMS_MUST_BE_INT, N_MUST_BE_GREATER_ZERO, RADIX_BASE_MUST_ME_GREATER_1
from src.utils.utils import is_int, require


def radix_sort(a: list[int], base: int = 2) -> list[int]:
    """Поразрядная сортировка для неотрицательных целых чисел"""

    if base <= 1:
        raise ValueError(RADIX_BASE_MUST_ME_GREATER_1)

    if not a:
        return []

    max_val = max(a)
    digit_place = 1

    while max_val // digit_place > 0:
        a = _counting_sort_by_digit(a, digit_place, base)
        digit_place *= base

    return a


def _counting_sort_by_digit(a: list[int], digit_place: int, base: int) -> list[int]:
    """Сортировка подсчётом по одной цифре (в заданном разряде)"""

    # Извлечение текущей цифры у каждого числа
    digits = [((num // digit_place) % base) for num in a]

    freqs = [0] * base

    for d in digits:
        freqs[d] += 1

    result = [0] * len(a)

    for i in range(1, base):
        freqs[i] += freqs[i - 1]

    for i in range(len(a) - 1, -1, -1):
        d = (a[i] // digit_place) % base
        pos = freqs[d] - 1
        result[pos] = a[i]
        freqs[d] -= 1

    return result


class RadixCommand(SortIntCommand):
    """
    flags:
        - b – base: позволяет ввести кастомное основание первым параметром
    """

    def sort(self, lst: list[int]) -> list[int]:
        is_custom_base = "b" in self._flags

        if is_custom_base:
            require(is_int(self._params[0]) and int(self._params[0]) > 0, RADIX_BASE_MUST_ME_GREATER_1)

        lst = [int(i) for i in self._params[(1 if is_custom_base else 0):]]
        base: int | None = int(self._params[0]) if is_custom_base else None
        return radix_sort(lst, base or 10)

    @property
    def _supported_flags(self) -> str:
        return "b"

    @staticmethod
    def validate_param(param: str):
        require(is_int(param), PARAMS_MUST_BE_INT)
        require(int(param) >= 0, N_MUST_BE_GREATER_ZERO)

    @classmethod
    def name(cls) -> str:
        return "radix"
