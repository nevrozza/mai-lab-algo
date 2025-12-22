from abc import ABC, abstractmethod

from src.cli.command import BashCommand
from src.cli.errors import BashError
from src.utils.consts import PARAMS_MUST_BE_INT, INPUT_MORE_THAN_ZERO
from src.utils.utils import require, is_int


class DefaultCommand(BashCommand, ABC):

    @abstractmethod
    def solve(self) -> str:
        pass

    def _exec(self) -> tuple[list[BashError], str | None] | None:
        return [], self.solve()

    @staticmethod
    def validate_param(param: str):
        require(is_int(param), PARAMS_MUST_BE_INT)

    def _validate_params(self) -> list[BashError]:
        if not self._params:
            raise BashError(INPUT_MORE_THAN_ZERO)
        for p in self._params:
            self.validate_param(p)
        return []


class SortIntCommand(DefaultCommand):

    @abstractmethod
    def sort(self, lst: list[int]) -> list[int]:
        pass

    def solve(self) -> str:
        sorted_lst = self.sort([int(i) for i in self._params])
        return " ".join(str(x) for x in sorted_lst)
