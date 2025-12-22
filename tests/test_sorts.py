import pytest

from src.benchmarking.generators import reverse_sorted, many_duplicates, nearly_sorted, rand_int_array, rand_float_array
from src.sorts.bubble import bubble_sort
from src.sorts.bucket import bucket_sort_normalized
from src.sorts.counting import counting_sort, counting_sort_dict
from src.sorts.heap import heap_sort
from src.sorts.quick import quick_sort
from src.sorts.radix import radix_sort

DEFAULT_SORTING_ALGOS = [
    radix_sort,
    counting_sort,
    counting_sort_dict,
    quick_sort,
    heap_sort,
    bubble_sort
]

N = 1_000
SEED = 42

DEFAULT_TEST_ARRAYS = [
    [], [42], [1, 2, 3, 4, 5], [5, 4, 3, 2, 1],
    [3, 1, 4, 1, 5, 9, 2, 6, 5], [7, 7, 7],
    reverse_sorted(N), many_duplicates(N, k_unique=10, seed=SEED),
    nearly_sorted(N, swaps=N // 100, seed=SEED), rand_int_array(N, 0, 10_000, seed=SEED)
]

DEFAULT_PARAMS = [(f, arr) for f in DEFAULT_SORTING_ALGOS for arr in DEFAULT_TEST_ARRAYS]


@pytest.mark.parametrize("func, array", DEFAULT_PARAMS)
def test_default_sorts(func, array):
    assert func(array) == sorted(array)


def test_bucket_sort():
    array = rand_float_array(N, 0, 10_000, seed=SEED)
    for r, e in zip(bucket_sort_normalized(array), sorted(array)):
        assert abs(r - e) < 1e-9
