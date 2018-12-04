#!/usr/bin/env python
"""Tests for friend_pairs.py"""

import pytest
from Dynamic_Programming.code import friend_pairs


@pytest.mark.parametrize('inputs, outputs',
                         [('3', 4),
                          ('5', 26),
                          ('64', 135041388282796985771272553475002706667235246080),
                          ('-9', None),
                          ('Yo', None])
def test_itr(inputs, outputs):
    """Tests for itr() function."""
    assert friend_pairs.itr(inputs) == outputs
