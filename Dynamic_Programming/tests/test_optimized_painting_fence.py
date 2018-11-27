"""
Testing task 14
"""

from optimized_painting_fence import find_combinations
import pytest

def test_func():
    """Test of calculating number of ways of painting the fence with input 4 and 4."""
    assert find_combinations(4, 4) == 228
def test_error():
    """Test of raising exception."""
    pytest.raises(TypeError, "find_combinations('Bad param!')")

@pytest.mark.xfail(raises=TypeError)
def test_fail():
    """Expected fail of test."""
    find_combinations(0, 4)

@pytest.mark.parametrize("number_of_posts, number_of_colors, value", [(2, 4, 16), (1, 2, 2), (3, 4, 60)])
def test_p_func(number_of_posts, number_of_colors, value):
    """Test of calculating number of ways of painting the fence with different inputs."""
    assert find_combinations(number_of_posts, number_of_colors) == value
