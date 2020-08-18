import pytest
from geometry_function import SpecialFunction

# Example data to test middle_section
@pytest.mark.parametrize("arg1, arg2, ans", [
    ([-25, 2], [17, 12], f"Middle X: {-4} Y: {7}"),
    ((-10, 12), (5, 6), f"Middle X: {-3} Y: {9}")
])
# test middle_section function
def test_middle(arg1, arg2, ans):
    assert SpecialFunction.middle_section(arg1, arg2) == ans


# Example data to test collision_between_rectangles
@pytest.mark.parametrize("arg1, arg2, ans", [
    ((1, 2, 4, 2), (2, 2, 5, 2), "Collision"),
    ((2, 2, 5, 2), (1, 2, 4, 2), "Collision"),
    ((1, 2, 3, 2), (15, 16, 15, 17), "There is no collision")
])

# test collision_between_rectangles function
def test_collison(arg1, arg2, ans):
    assert SpecialFunction.collision_between_rectangles(arg1, arg2) == ans
