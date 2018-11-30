"""
Testing task 14
"""

import pytest
import Dynamic_Programming.code.optimized_painting_fence as opt

def test_func():
    """Test of calculating number of ways of painting the fence with input 4 and 4."""
    assert opt.find_combinations(4, 4) == 228
def test_error():
    """Test of raising exception."""
    pytest.raises(TypeError, "opt.find_combinations('Bad param!')")

@pytest.mark.parametrize("number_of_posts, number_of_colors, value", [(2, 4, 16),
                                                                      (1, 2, 2),
                                                                      (3, 4, 60)])
def test_p_func(number_of_posts, number_of_colors, value):
    """Test of calculating number of ways of painting the fence with different inputs."""
    assert opt.find_combinations(number_of_posts, number_of_colors) == value

