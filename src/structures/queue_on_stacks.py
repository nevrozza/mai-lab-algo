from typing import List


class QueueOnStacks:
    def __init__(self) -> None:
        self._stack_in: List[int] = []
        self._stack_out: List[int] = []

    def enqueue(self, x: int) -> None:
        """Добавить элемент в конец очереди"""
        self._stack_in.append(x)

    def dequeue(self) -> int:
        """Удалить и вернуть первый элемент. Исключение при пустой очереди"""
        self._update_stack_out()
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self._stack_out.pop()

    def front(self) -> int:
        """Вернуть первый элемент без удаления. Исключение при пустой очереди"""
        self._update_stack_out()
        if self.is_empty():
            raise IndexError("front from empty queue")
        return self._stack_out[-1]

    def is_empty(self) -> bool:
        return len(self._stack_in) == 0 and len(self._stack_out) == 0

    def __len__(self) -> int:
        return len(self._stack_in) + len(self._stack_out)

    def _update_stack_out(self) -> None:
        """Переместить элементы из stack_in в stack_out, если stack_out пуст"""
        if not self._stack_out:
            while self._stack_in:
                self._stack_out.append(self._stack_in.pop())
