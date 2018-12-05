#!/usr/bin/env python
"""Tests for friend_pairs.py by Serge Kutwicki"""

import pytest
from Dynamic_Programming.code import longest_sequence as ls

def test_longest_seq_with_diff_one_negative():
    """Tests for negative results"""
    assert ls.longest_seq_with_diff_one('h',-9,2,3,-5) == "Please enter correct input."
    assert ls.longest_seq_with_diff_one() == "Please enter correct input."

@pytest.mark.parametrize('inputs, outputs',
                         [('0', 1),
                          ('3, 7, 1, -5, 0', 2),
                          ('3, 4, 7, 8, 9', 3),
                          ('3, 9, 5, -5, -3, -7, 25, 31, 5, 1', 1)
                          ])
def test_longest_seq_with_diff_one_positive(inputs, outputs):
    """Tests for positive results"""
    assert ls.longest_seq_with_diff_one(inputs) == outputs

#To do
#Add test for None input
#[(('h',-9,2,3,-5), "Please enter correct input.")])-