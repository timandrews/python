import pytest

import my_math
import math

def test_zero():
    assert my_math.my_factorial(0) == math.factorial(0)

def test_one():
    assert my_math.my_factorial(1) == math.factorial(1)

def test_greater_than_1():
    assert my_math.my_factorial(2) == math.factorial(2)

def test_raises_ValueError_on_negative():
    with pytest.raises(ValueError):
        my_math.my_factorial(-10)

def test_raises_TypeError():
    with pytest.raises(ValueError):
        my_math.my_factorial(20.2)