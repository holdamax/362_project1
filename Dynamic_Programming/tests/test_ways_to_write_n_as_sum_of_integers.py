"""
Tests for ways_to_write_n_as_sum_of_integers.py
"""

from ways_to_write_n_as_sum_of_integers import count_ways
import pytest


@pytest.mark.parametrize('input, output',
                         [(1, 0), (10, 41), (-1, 'Please enter integer number > 0'),
                          (0, 'Please enter integer number > 0'),
                          ('12', 'Please enter integer number > 0')])
def test_count_ways(input, output):

    """
    Tests count_ways function
    """
    assert count_ways(input) == output
