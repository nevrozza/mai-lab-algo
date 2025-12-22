import random

from src.utils.utils import require


def rand_int_array(
        n: int,
        lo: int,
        hi: int,
        *,
        distinct: bool = False,
        seed: int | None = None
) -> list[int]:
    """
     Генерирует список случайных целых чисел.

     Аргументы:
         n (int): количество элементов в массиве.
         lo (int): нижняя граница значений (включительно).
         hi (int): верхняя граница значений (включительно).
         distinct (bool): если True — все элементы должны быть различны (без повторов).
         seed (int | None): значение для инициализации генератора случайных чисел
                            (нужно для воспроизводимости при тестах).

     Возвращает:
         List[int]: список из n случайных целых чисел в диапазоне [lo, hi].
     """
    if seed is not None:
        random.seed(seed)
    if n < 0:
        raise ValueError("n must be non-negative")
    if lo > hi:
        raise ValueError("lo must be <= hi")
    if distinct:
        total_values = hi - lo + 1
        if n > total_values:
            raise ValueError(f"Cannot generate {n} distinct integers in range [{lo}, {hi}]")
        return random.sample(range(lo, hi + 1), k=n)
    else:
        return [random.randint(lo, hi) for _ in range(n)]


def nearly_sorted(
        n: int,
        swaps: int,
        *,
        seed: int | None = None
) -> list[int]:
    """
    Создаёт почти отсортированный массив.

    Аргументы:
        n (int): размер массива.
        swaps (int): количество случайных перестановок (пар элементов), которые вносят "нарушения" в порядок.
        seed (int | None): значение для фиксирования генератора случайных чисел.

    Возвращает:
        List[int]: почти отсортированный список длиной n.
    """
    if seed is not None:
        random.seed(seed)
    require(n >= 0, "n must be non-negative")
    require(swaps >= 0, "swaps must be non-negative")
    arr = list(range(1, n + 1))
    for _ in range(swaps):
        i, j = random.sample(range(n), 2)
        arr[i], arr[j] = arr[j], arr[i]
    return arr


def many_duplicates(
        n: int,
        k_unique: int = 5,
        *,
        seed: int | None = None
) -> list[int]:
    """
    Генерирует массив с большим количеством повторяющихся значений.

    Аргументы:
        n (int): длина массива.
        k_unique (int): количество различных значений, из которых формируется массив.
        seed (int | None): значение для фиксирования случайности.

    Возвращает:
        List[int]: список длиной n, где встречаются только k_unique различных чисел.
    """
    if seed is not None:
        random.seed(seed)
    require(n >= 0, "n must be non-negative")
    require(k_unique > 0, "k_unique must be positive")

    unique_vals = list(range(k_unique))
    return [random.choice(unique_vals) for _ in range(n)]


def reverse_sorted(n: int) -> list[int]:
    """
    Возвращает обратно отсортированный массив.

    Аргументы:
        n (int): длина массива.

    Возвращает:
        List[int]: список чисел от n до 1, например [5, 4, 3, 2, 1].
    """
    require(n >= 0, "n must be non-negative")
    return list(range(n, 0, -1))


def rand_float_array(
        n: int,
        lo: float = 0.0,
        hi: float = 1.0,
        *,
        seed: int | None = None
) -> list[float]:
    """
    Генерирует список случайных вещественных чисел (float).

    Аргументы:
        n (int): количество элементов.
        lo (float): нижняя граница диапазона значений.
        hi (float): верхняя граница диапазона значений.
        seed (int | None): значение для инициализации генератора случайных чисел.

    Возвращает:
        List[float]: список из n случайных чисел в диапазоне [lo, hi].
                     Подходит для тестов bucket sort.
    """
    if seed is not None:
        random.seed(seed)

    require(n >= 0, "n must be non-negative")
    require(lo <= hi, "lo must be <= hi")
    return [random.uniform(lo, hi) for _ in range(n)]
