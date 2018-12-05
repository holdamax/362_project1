"""
Pytest tests for 12 task
"""

import pytest
from Dynamic_Programming.code.ways_tile_floor import ways_tile_floor as wtf


@pytest.mark.parametrize('input_1, input_2, output',
                         [(10, 5, 8), (1, 1, 2), (0, 0, 0), (30, 3, 58425),
                          (0, 10, 0)])
def test_wtf_positive(input_1, input_2, output):

    """
    Positive tests ways_to_sum function
    """
    assert wtf(input_1, input_2) == output


#@pytest.mark.xfail(raises=(IndexError, ValueError))

@pytest.mark.parametrize('input_1, input_2, output',
                         [(-10, 2, IndexError), ('','',ValueError),
                          ('*, ^, #, @, -, )', 5, ValueError)])
def test_wtf_negative(input_1, input_2, output):

    """
    Negative tests ways_to_sum function
    """

    with pytest.raises(output):
        wtf(input_1, input_2)
