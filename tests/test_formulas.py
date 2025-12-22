import pytest

from src.formulas.factorial import factorial, factorial_recursive
from src.formulas.fibo import fibo, fibo_recursive
from src.utils.consts import N_MUST_BE_GREATER_ZERO


@pytest.mark.parametrize("func",
                         [factorial, factorial_recursive
                          ]
                         )
def test_factorial(func):
    assert func(0) == 1
    assert func(1) == 1
    assert func(5) == 120
    assert func(10) == 3_628_800
    with pytest.raises(ValueError, match=N_MUST_BE_GREATER_ZERO):
        func(-1)


@pytest.mark.parametrize("func",
                         [fibo, fibo_recursive
                          ]
                         )
def test_fibo(func):
    assert func(0) == 0
    assert func(1) == 1
    assert func(2) == 1
    assert func(10) == 55
    with pytest.raises(ValueError, match=N_MUST_BE_GREATER_ZERO):
        func(-1)
