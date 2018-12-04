"""Testing longest sequence"""

import pytest

from Dynamic_Programming.code import longest_sequence


@pytest.mark.parametrize('inputs, outputs',
                         [('1,1', 1),
                          ('-1,1,1', 1),
                          ('1,2,3,4,5,6,7,8', 8),
                          ('3, 4, 7, 8, 9', 3),
                          ])
def test_itr(inputs, outputs):
    """Tests for positive results"""
    assert longest_sequence.itr(inputs) == outputs


@pytest.mark.parametrize('inputs, outputs',
                         [('5,f,t', None),
                          ('Hi', None),
                          ('', None),
                          (' ', None)])
def test_itr(inputs, outputs):
    """Tests for negative results"""
    assert longest_sequence.itr(inputs) == outputs
