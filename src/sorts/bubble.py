from src.utils.commands_abc import SortIntCommand


def bubble_sort(a: list[int]) -> list[int]:
    if not a:
        return []
    arr = a.copy()
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


class BubbleCommand(SortIntCommand):
    def sort(self, lst: list[int]) -> list[int]:
        return bubble_sort(lst)

    @classmethod
    def name(cls) -> str:
        return "bubble"
