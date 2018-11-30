#!/usr/bin/env python
"""Tests for friend_pairs.py"""

import pytest
from Dynamic_Programming.code.paths_without_crossing import _paths_without_crossing


@pytest.mark.parametrize('inputs, outputs',
                         [(2, 1),
                          (4, 2),
                          (6, 5),
                          (8, 14),
                          (1038, 1.4023904365091493e+308)])
def test_positive_paths_without_crossing(inputs, outputs):
    """Tests for pathsWithoutCrossing() function with positive values."""

    assert _paths_without_crossing(inputs) == outputs
