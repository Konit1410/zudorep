import pytest
from Task1.Special_math import Simple_math


def test_01():
    arguments = [1, 2, 3]
    assert Simple_math.square_root_of_avr(arguments) == 0, 15
