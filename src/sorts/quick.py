from src.utils.commands_abc import SortIntCommand


def quick_sort(a: list[int]) -> list[int]:
    if len(a) <= 1:
        return a

    pivot = a[len(a) // 2]

    left = [x for x in a if x < pivot]
    middle = [x for x in a if x == pivot]
    right = [x for x in a if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


class QuickCommand(SortIntCommand):
    def sort(self, lst: list[int]) -> list[int]:
        return quick_sort(lst)

    @classmethod
    def name(cls) -> str:
        return "quick"
