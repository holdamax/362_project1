"""
Testing task 14
"""

import pytest
import Dynamic_Programming.code.ways_to_write_n_as_sum_of_integers as wtw

# def test_func():
#     """Test of calculating number of ways of painting the fence with input 4 and 4."""
#     assert wtw.count_ways(4) == 4
def test_typeerror():
    """Test of raising exception."""
    pytest.raises(TypeError)

def test_valerror():
    pytest.raises(ValueError)

def test_штвerror():
    pytest.raises(IndexError)

@pytest.mark.parametrize("number_of_posts, value", [(5, 6),
                                                    (40, 37337),
                                                    (195, 2580840212972)])
def test_p_func(number_of_posts, value):
    """Test of calculating number of ways of painting the fence with different inputs."""
    assert wtw.count_ways(number_of_posts) == value
