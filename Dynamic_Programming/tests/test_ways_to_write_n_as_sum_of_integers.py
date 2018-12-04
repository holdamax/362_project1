"""
Tests for ways_to_write_n_as_sum_of_integers.py
"""

from Dynamic_Programming.code.ways_to_write_n_as_sum_of_integers import count_ways
import pytest


@pytest.mark.xfail(raises=ValueError)
@pytest.mark.parametrize('input, output',
                         [(-1, ValueError)])
def test_count_ways(input, output):

    """
    Tests count_ways function
    """
    assert count_ways(input) == output
