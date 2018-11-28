#!/usr/bin/env python
"""Tests for friend_pairs.py"""

import pathsWithoutCrossing
import pytest


@pytest.mark.parametrize('input, output',
                         [(2, 1),
                          (4, 2),
                          (6, 5),
                          (8, 14)])
def test_positive_paths_without_crossing(input, output):
    """Tests for pathsWithoutCrossing() function with positive values."""

    assert pathsWithoutCrossing.pathsWithoutCrossing(input) == output


@pytest.mark.parametrize('input, output',
                         [(0, None),
                          (-1, None),
                          ('w', None),
                          ((1, 2, 3), None)])
def test_negative_paths_without_crossing(input, output):
    """Tests for itr() function with negative values."""

    assert pathsWithoutCrossing.pathsWithoutCrossing(input) == output
