"""
Testing task 14
"""

import pytest
import Dynamic_Programming.code.ways_to_write_n_as_sum_of_integers as wtw


@pytest.mark.parametrize("number_of_posts, value", [(5, 6),
                                                    (40, 37337),
                                                    (195, 2580840212972)])
def test_p_func(number_of_posts, value):
    """Test of calculating number of ways of painting the fence with different inputs."""
    assert wtw.count_ways(number_of_posts) == value


@pytest.mark.parametrize('input1, output1',
                         [(-1, ValueError), ('a', TypeError), (0, ValueError)])
def test_count_ways(input1, output1):

    """
    Tests count_ways function with fail inputs
    """
    with pytest.raises(output1):
        wtw.count_ways(input1)
