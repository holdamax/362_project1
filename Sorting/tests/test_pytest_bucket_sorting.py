"""Tests for bucket_sorting.py"""

import pytest
from Sorting.code.bucket_sorting import bucket_sorting


@pytest.mark.parametrize('inputs, outputs',
                         [([5, 12, 6, 34, 5, 76, 2, 1, 87, 24, 6], [1, 2, 5, 5, 6, 6, 12, 24, 34, 76, 87]),
                          ([27, 73, 88, 91, 40, 66, 72, 95, 1, 49], [1, 27, 40, 49, 66, 72, 73, 88, 91, 95]),
                          ([64, -18, -88, 17, 27, -93, -75, -79, -96, -38, 67, -7, -98, -34, 86, 60, -64,
                            11, 42, -36, -10, 18, 43, 55],
                           [-98, -96, -93, -88, -79, -75, -64, -38, -36, -34, -18, -10, -7, 11, 17, 18, 27, 42, 43, 55,
                            60, 64, 67, 86])])
def test_positive_paths_without_crossing(inputs, outputs):
    """Tests for bucket_sorting() function with positive values."""
    assert bucket_sorting(inputs) == outputs


@pytest.mark.xfail(raises=(TypeError, ValueError, IndexError, AttributeError))
@pytest.mark.parametrize('inputs, outputs',
                         [(['s', 'b', 'h'], ValueError),
                          ])
def test_negative_paths_without_crossing(inputs, outputs):
    """Tests for bucket_sorting() function with negative values."""
    assert bucket_sorting(inputs) == outputs

def test_empty_paths_without_crossing():
    """Tests for bucket_sorting() function with empty values."""
    assert bucket_sorting([]) == []
