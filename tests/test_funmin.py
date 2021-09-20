import pytest

from funmin import __version__
from funmin.funmin import fun_min, EmptyArray



def test_version():
    assert __version__ == '0.1.0'


def test_empty_array():
    arr = []
    with pytest.raises(EmptyArray):
        fun_min(arr)


def test_simple_array():
    arr = [3, 2, 1, 2, 4]
    assert fun_min(arr) == min(arr)


def test_single_array():
    arr = [10]
    assert fun_min(arr) == min(arr)


def test_two_array():
    arr = [10, 5]
    assert fun_min(arr) == min(arr)


def test_big_array():
    arr = list(range(1000, 5, -1)) + list(range(50000, 500000, 1))
    assert fun_min(arr) == min(arr)


def test_only_increasing():
    arr = list(range(10 ** 6, 5, -1))
    assert fun_min(arr) == min(arr)


def test_only_decreasing():
    arr = list(range(50, 50 ** 4, 1))
    assert fun_min(arr) == min(arr)
