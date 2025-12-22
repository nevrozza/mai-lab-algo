from collections.abc import Callable
from time import perf_counter


def timeit_once(func: Callable, *args, **kwargs) -> float:
    """
    Возвращает время в секундах для одного вызова func(*args, **kwargs)
    Аргументы копируются, чтобы избежать побочных эффектов
    """
    new_args = [arg for arg in args]
    start = perf_counter()
    func(*new_args, **kwargs)
    end = perf_counter()
    return end - start


def benchmark_sorts(
    arrays: dict[str, list],
    algos: dict[str, Callable]
) -> dict[str, dict[str, float]]:
    """
    Возвращает словарь: алгоритм -> (имя набора -> время)
    Каждый алгоритм запускается один раз на копии массива
    """
    report: dict[str, dict[str, float]] = {}
    for algo_name, algo_func in algos.items():
        report[algo_name] = {}
        for arr_name, arr in arrays.items():
            t = timeit_once(algo_func, arr)
            report[algo_name][arr_name] = t
    return report
