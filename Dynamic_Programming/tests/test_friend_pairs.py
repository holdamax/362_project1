#!/usr/bin/env python
"""Tests for friend_pairs.py"""

import pytest
import friend_pairs


@pytest.mark.parametrize('input, output',
                         [('3', 4),
                          ('5', 26),
                          ('64', 135041388282796985771272553475002706667235246080),
                          ('-9', None),
                          ('Yo', None)])
def test_itr(input, output):
    """Tests for itr() function."""
    assert friend_pairs.itr(input) == output
