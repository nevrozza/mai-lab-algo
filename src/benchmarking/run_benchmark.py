from collections.abc import Callable

from src.benchmarking.benchmark import benchmark_sorts, timeit_once
from src.benchmarking.generators import rand_int_array, nearly_sorted, many_duplicates, reverse_sorted, rand_float_array
from src.formulas.factorial import factorial, factorial_recursive
from src.formulas.fibo import fibo, fibo_recursive
from src.sorts.bubble import bubble_sort
from src.sorts.bucket import bucket_sort_normalized
from src.sorts.counting import counting_sort, counting_sort_dict
from src.sorts.heap import heap_sort
from src.sorts.quick import quick_sort
from src.sorts.radix import radix_sort


def main():
    SEED = 42

    default_sorts_benchmark(SEED)
    bubble_sort_benchmark(SEED)
    bucket_sort_benchmark(SEED)

    factorial_benchmark()
    fibo_benchmark()
    print("\nПу-пу-пу")


def default_sorts_benchmark(SEED: int):
    N = 100_000
    arrays = {
        "random_10k": rand_int_array(N, 0, 10_000, seed=SEED),
        "nearly_sorted": nearly_sorted(N, swaps=N // 100, seed=SEED),
        "many_duplicates": many_duplicates(N, k_unique=10, seed=SEED),
        "reverse_sorted": reverse_sorted(N),
    }

    algos: dict[str, Callable] = {
        "Sorted()": lambda arr: sorted(arr),
        "Radix Sort": radix_sort,
        "Counting Sort": counting_sort,
        "Counting Sort (Dict)": counting_sort_dict,
        "Quick Sort": quick_sort,
        "Heap Sort": heap_sort,
    }

    print("Мурчим...\n")
    results_fast: dict[str, dict[str, float]] = benchmark_sorts(arrays, algos)

    print(f"Основные сортировки, N={N}")
    _print_results(results_fast, arrays.keys())


def bubble_sort_benchmark(SEED: int):
    name = "Bubble Sort"
    N = 1_000
    arrays = {
        "random_1k": rand_int_array(N, 0, 10_000, seed=SEED),
        "nearly_1k": nearly_sorted(N, swaps=N // 100, seed=SEED),
        "dups_1k": many_duplicates(N, k_unique=10, seed=SEED),
        "reverse_1k": reverse_sorted(N),
    }

    algos = {
        name: bubble_sort,
    }

    print(f"\nЗапуск бенчмарка для {name}...\n")
    results_bubble = benchmark_sorts(arrays, algos)

    print(f"{name}, N={N}")
    _print_results(results_bubble, arrays.keys())


def bucket_sort_benchmark(SEED):
    name = "Bucket Sort"
    N = 10_000
    arrays = {
        "random_10k float": rand_float_array(N, 0, 10_000, seed=SEED),
    }

    algos = {
        name: bucket_sort_normalized,
    }

    print(f"\nЗапуск бенчмарка для {name}...\n")
    results = benchmark_sorts(arrays, algos)

    print(f"{name}, N={N}")
    _print_results(results, arrays.keys())


def factorial_benchmark():
    name = "factorial"
    n = 500
    print(f"\nFactorial, n = {n}")

    t_iter = timeit_once(factorial, n)
    t_rec = timeit_once(factorial_recursive, n)

    print("-" * 40)
    print(f"{f'{name} (iter)':<20} {t_iter:>10.6f} сек")
    print(f"{f'{name} (rec)':<20} {t_rec:>10.6f} сек")
    print("-" * 40)


def fibo_benchmark():
    name = "fibo"
    n = 35
    print(f"\nFibonacci, n = {n}")

    t_iter = timeit_once(fibo, n)
    t_rec = timeit_once(fibo_recursive, n)
    print("-" * 40)
    print(f"{f'{name} (iter)':<20} {t_iter:>10.6f} сек")
    print(f"{f'{name} (rec)':<20} {t_rec:>10.6f} сек")
    print("-" * 40)


def _print_results(results: dict, dataset_names):
    header = f"{'Алгоритм':<20}" + "".join(f"{name:>18}" for name in dataset_names)
    print(header)
    print("-" * len(header))
    for algo, times in results.items():
        row = f"{algo:<20}"
        for ds in dataset_names:
            row += f"{times[ds]:>18.6f}"
        print(row)
    print("-" * len(header))


if __name__ == "__main__":
    main()
