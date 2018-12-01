#!/usr/bin/env python
"""Tests for friend_pairs.py"""

import pytest
from Dynamic_Programming.code.paths_without_crossing import paths_without_crossing


@pytest.mark.parametrize('inputs, outputs',
                         [(2, 1),
                          (1, 0),
                          (6, 5),
                          (8, 14)])
def test_positive_paths_without_crossing(inputs, outputs):
    """Tests for pathsWithoutCrossing() function with positive values."""

    assert paths_without_crossing(inputs) == outputs
