"""PyTest for min_max_afford.py."""

from Dynamic_Programming.code.min_max_afford import max_afford as min_max
import pytest


@pytest.mark.parametrize("low, high, days, outputs", [([1, 5, 4, 5, 3], [3, 6, 8, 7, 6], 5, 20),
                                                      ([1, 2, 4, 2], [4, 6, 2, 3], 4, 12),
                                                      ([2], [5], 1, 5)])
def test_min_max_positive(low, high, days, outputs):
    """Test of calculating max afford number with  given inputs."""
    assert min_max(low, high, days) == outputs


@pytest.mark.parametrize("low, high, days, outputs", [([1, 3, 2], [5, 3], 2, None),
                                                      ([4, 3, 2], [5, 7, 8, 4], 3, None),
                                                      ([1], [5, 3], 8, None),
                                                      ('sdsd', ' ', 1, None),
                                                      (-1, {1: 1}, 4, None)])
def test_min_max_positive(low, high, days, outputs):
    """Test of calculating max afford number with  given inputs."""
    assert min_max(low, high, days) == outputs


def test_error():
    """Test of raising exception."""
    pytest.raises(TypeError, min_max(['-1'], ['-1'], -1))


@pytest.mark.xfail(raises=NameError)
def test_fail():
    """Expected fail of test."""
    min_max(['kjn gv '], ['jhg'], 'wzxcv')
