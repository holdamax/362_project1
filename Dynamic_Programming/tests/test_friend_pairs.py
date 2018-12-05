#!/usr/bin/env python
"""Tests for friend_pairs.py by Serge Kutwicki"""

import pytest
from Dynamic_Programming.code import friend_pairs as fp


@pytest.mark.parametrize('inputs, outputs',
                         [('3', 4),
                          ('5', 26),
                          ('64', 135041388282796985771272553475002706667235246080)
                          ])
def test_itr_positive(inputs, outputs):
    """Tests for positive results"""
    assert fp.itr(inputs) == outputs


@pytest.mark.parametrize('inputs, outputs',
                         [('', "You gave wrong input. Try again."),
                          ('-9', "You gave wrong input. Try again."),
                          ('Yo', "You gave wrong input. Try again."),
                          (-5, "You gave wrong input. Try again.")])
def test_itr_negative(inputs, outputs):
    """Tests for negative results"""
    assert fp.itr(inputs) == outputs

