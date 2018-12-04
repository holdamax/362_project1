"""
Pytest tests for 13 task
"""

import pytest
from Dynamic_Programming.code.ways_to_sum import ways_to_sum as wts


@pytest.mark.parametrize('input_1, input_2, output',
                         [('1, 2, 3', 3, 4), ('1', 1, 1), ('1, 1', 2, 4),
                          ('-1, 1', 2, 4), ('1, 2, 3, 4, 5', 0, 0),]
                         )
def test_count_ways(input_1, input_2, output):

    """
    Tests count_ways function
    """
    assert wts(input_1, input_2) == output
