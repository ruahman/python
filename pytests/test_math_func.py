""""test"""

import math_func
import pytest


def test_add():
    """pytest test_math_func.py -v -s"""
    assert math_func.add(7, 3) == 10
    assert math_func.add(7) == 9
    assert math_func.add(5) == 7

    print("------------- testing print ====================")
    print("------------- testing print ====================")
    print("------------- testing print ====================")
    print("------------- testing print ====================")


def test_product():
    assert math_func.product(5, 5) == 25
    assert math_func.product(5) == 10
    assert math_func.product(7) == 14


@pytest.mark.parametrize('num1,num2,result', [
    (7, 3, 10),
    (3, 4, 7),
    (5, 6, 11)
])
def test_add_params(num1, num2, result):
    assert math_func.add(num1, num2) == result
