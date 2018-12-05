"""
Pytest tests for 5 task
"""

import pytest
from Dynamic_Programming.code.ways_to_sum import ways_to_sum as wts


@pytest.mark.parametrize('input_1, input_2, output',
                         [('1, 2, 3', 3, 4),
                          ('1', 1, 1),
                          ('1, 1', 2, 4),
                          ('5', 10, 1),
                          ('0', 5, 0),
                          ('1, 2', 999, 43466557686937456435688527675040625802564660517371780402481729089536555417949051890403879840079255169295922593080322634775209689623239873322471161642996440906533187938298969649928516003704476137795166849228875)])


def test_count_ways_positive(input_1, input_2, output):

    """
    Positive tests ways_to_sum function
    """
    assert wts(input_1, input_2) == output


@pytest.mark.parametrize('input_1, input_2, output',
                         [('1, 2, 3, 4, 5', 0, ValueError),
                          ('-1, 2', 2, IndexError),
                          ('','',ValueError),
                          ('*, ^, #, @, -, )', 5, ValueError),
                          ('1, 2', 1000, ValueError)])
def test_count_ways_negative(input_1, input_2, output):

    """
    Negative tests ways_to_sum function
    """
    with pytest.raises(output):
        wts(input_1, input_2)
