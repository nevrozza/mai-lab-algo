from src.utils.commands_abc import SortIntCommand


def counting_sort(a: list[int]) -> list[int]:
    if not a:
        return []

    min_val = min(a)
    max_val = max(a)
    range_of_values = max_val - min_val + 1

    freqs = [0] * range_of_values

    for num in a:
        freqs[num - min_val] += 1

    result = []
    for i in range(range_of_values):
        value = i + min_val
        result.extend([value] * freqs[i])

    return result


def counting_sort_dict(a: list[int]) -> list[int]:
    if not a:
        return []

    count: dict[int, int] = {}
    for num in a:
        count[num] = count.get(num, 0) + 1

    sorted_keys = sorted(count.keys())

    result = []
    for key in sorted_keys:
        result.extend([key] * count[key])

    return result


class CountingCommand(SortIntCommand):
    def sort(self, lst: list[int]) -> list[int]:
        if "d" in self._flags:
            return counting_sort_dict(lst)
        else:
            return counting_sort(lst)

    @property
    def _supported_flags(self) -> str:
        return "d"

    @classmethod
    def name(cls) -> str:
        return "counting"
