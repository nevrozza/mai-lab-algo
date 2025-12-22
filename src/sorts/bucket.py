from src.cli.errors import BashError
from src.utils.commands_abc import DefaultCommand
from src.utils.consts import ALL_NUMS_MUST_BE_IN_RANGE_01, PARAMS_MUST_BE_NUM, INPUT_MORE_THAN_ZERO, \
    BUCKETS_MUST_BE_POSITIVE_INT
from src.utils.utils import require, is_num, is_int


def bucket_sort_normalized(a: list[float], buckets: int | None = None) -> list[float]:
    if not a:
        return []

    min_val, max_val = min(a), max(a)
    if min_val == max_val:  # Все элементы одинаковые
        return a[:]

    # Нормализуем в [0, 1] – допущение 0_о
    normalized = [(x - min_val) / (max_val - min_val) for x in a]

    sorted_normalized = bucket_sort(normalized, buckets)

    # Обратная замена =)
    return [x * (max_val - min_val) + min_val for x in sorted_normalized]


def bucket_sort(a: list[float], buckets: int | None = None) -> list[float]:
    if not a:
        return []

    if buckets is None:
        buckets = len(a)

    bucket_list: list[list[float]] = [[] for _ in range(buckets)]

    for value in a:
        require(0 <= value <= 1, ALL_NUMS_MUST_BE_IN_RANGE_01)
        index = min(int(value * buckets), buckets - 1)
        bucket_list[index].append(value)

    for bucket in bucket_list:
        insertion_sort(bucket)

    result: list[float] = []
    for bucket in bucket_list:
        result.extend(bucket)

    return result


def insertion_sort(a: list[float]) -> None:
    """Изменяет входные данные!!"""
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key


class BucketSort(DefaultCommand):
    """
    flags:
        - r – raw: запускает без нормализации
        - b – buckets: позволяет ввести кастомное кол-во buckets первым параметром
    """

    def sort(self, lst: list[float], buckets: int | None) -> list[float]:
        if "r" in self._flags:
            return bucket_sort(lst, buckets)
        else:
            return bucket_sort_normalized(lst, buckets)

    def solve(self) -> str:
        is_custom_buckets = "b" in self._flags

        if is_custom_buckets:
            require(is_int(self._params[0]) and int(self._params[0]) > 0, BUCKETS_MUST_BE_POSITIVE_INT)

        lst = [float(i) for i in self._params[(1 if is_custom_buckets else 0):]]
        buckets: int | None = int(self._params[0]) if is_custom_buckets else None

        if not lst:
            raise BashError(INPUT_MORE_THAN_ZERO)

        sorted_lst = self.sort(lst, buckets)
        return " ".join(str(x) for x in sorted_lst)

    @staticmethod
    def validate_param(param: str):
        require(is_num(param), PARAMS_MUST_BE_NUM)

    @classmethod
    def name(cls) -> str:
        return "bucket"

    @property
    def _supported_flags(self) -> str:
        return "rb"
