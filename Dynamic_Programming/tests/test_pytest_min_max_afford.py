"""PyTest for min_max_afford.py."""
import pytest
from Dynamic_Programming.code.min_max_afford import max_afford as min_max


@pytest.mark.parametrize("low, high, days, outputs", [([1, 5, 4, 5, 3], [3, 6, 8, 7, 6], 5, 20),
                                                      ([1, 2, 4, 2], [4, 6, 2, 3], 4, 12),
                                                      ([2], [5], 1, 5)])
def test_min_max_positive(low, high, days, outputs):
    """Test of calculating max afford number with given inputs."""
    assert min_max(low, high, days) == outputs


@pytest.mark.parametrize("low, high, days", [([1, 2, 4, 2], [4, 6, 2, 3], 0),
                                             ([3, 4, 4, 5], [1, 4, 3, 8], -1),
                                             ([6, 5], [2, 9, 1], -100)])
def test_min_max_day_res_nall(low, high, days):
    """Test of calculating max afford number with wrong inputs numbers."""
    assert min_max(low, high, days) == 0


@pytest.mark.parametrize("low, high, days, outputs", [([1, 3, 2], [5, 3], 5, IndexError),
                                                      ([3, 8, 1], [2, 3, 2, 2], '', TypeError),
                                                      (['-1'], ['-1'], 1, TypeError),
                                                      ('jdsjx', [1, 2, 3], 1, TypeError),
                                                      (-1, {1: 1}, 4, KeyError),
                                                      ('', '?', '/', TypeError)])
def test_min_max_res_nal(low, high, days, outputs):
    """Test on wrong input type."""
    with pytest.raises(outputs):
        min_max(low, high, days)
