from src.utils.commands_abc import SortIntCommand


def _heapify(arr: list[int], n: int, i: int):
    """
    Преобразует поддерево с корнем в i в кучу
    n – размер кучи (не обязательно длина всего массива)
    """
    maximum = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[maximum]:
        maximum = left

    if right < n and arr[right] > arr[maximum]:
        maximum = right

    if maximum != i:
        arr[i], arr[maximum] = arr[maximum], arr[i]
        _heapify(arr, n, maximum)


def heap_sort(a: list[int]) -> list[int]:
    """Heap sort: сначала построение кучи, затем последовательные извлечения"""
    if not a:
        return []

    arr = a[:]
    n = len(arr)

    # Построение кучи
    for i in range((n // 2) - 1, -1, -1):
        _heapify(arr, n, i)

    # Извлечения элементов
    for i in range(n - 1, 0, -1):
        # Перемещаем текущий максимум (корень) в конец
        arr[0], arr[i] = arr[i], arr[0]
        # Восстанавливаем кучу для оставшейся части массива
        _heapify(arr, i, 0)

    return arr


class HeapCommand(SortIntCommand):
    def sort(self, lst: list[int]) -> list[int]:
        return heap_sort(lst)

    @classmethod
    def name(cls) -> str:
        return "heap"
