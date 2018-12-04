"""Testing longest sequence"""

import pytest

from Dynamic_Programming.code import longest_sequence


@pytest.mark.parametrize('inputs, outputs',
                         [('1,1', 1),
                          ('-1,1,1', 1),
                          ('1,2,3,4,5,6,7,8', 8),
                          ('3, 4, 7, 8, 9', 3),
                          ])
def test_longest_seq_with_diff_one(inputs, outputs):
    """Tests for positive results"""
    assert longest_sequence.longest_seq_with_diff_one(inputs) == outputs


@pytest.mark.parametrize('inputs, outputs',
                         [('5,f,t', "Please enter correct input."),
                          ('Hi', "Please enter correct input."),
                          (' ', "Please enter correct input.")])
def test_longest_seq_with_diff_one(inputs, outputs):
    """Tests for negative results"""
    assert longest_sequence.longest_seq_with_diff_one(inputs) == outputs
