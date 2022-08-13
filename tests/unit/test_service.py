import pytest
from test_proj.model import Request
from test_proj.service import sum_func


def test_sum_returns_valid_value():
    request = Request(3, 2)
    sum = sum_func(request)
    assert sum == 5


def test_invalid_a_raises_exception():
    a = 1
    b = 2
    with pytest.raises(Exception):
        sum_func(a, b)


def test_invalid_b_raises_value_error():
    a = 2
    b = 1
    with pytest.raises(ValueError):
        sum_func(a, b)
