import pytest
from Task1.Special_math import SimpleMath


@pytest.mark.parametrize('arguments, ans', [
    ([1, 2, 3], 1),
    ([1], 1),
    ([1, 1, 2, 3, 3], 0.308641975308642),
    ([], None),
    ([11, 23, 45, 68, 90], 1.156985131470954e-11),
    ([-1, -2], 2.25),
    ([0], 0)
])
def test_parameterize_01(arguments, ans):
    assert Simple_math.sq_root_sum_by_product(arguments) == ans


@pytest.mark.parametrize('n_num, ans', [
    ([1, 2, 3], 3.141592653589793),
    ([2, 3, 4, 5, 6], 6.283185307179586),
    ([], None),
    ([2, 4, 6, 7, 8, 9, 10], 10.995574287564276),
    ([-1, -2, -3, -4], -3.9269908169872414),
    ([0], 2.220446049250313e-16)
])
def test_parameterize_02(n_num, ans):
    assert Simple_math.median_multiply_constants(n_num) == ans
