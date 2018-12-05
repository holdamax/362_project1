"""Nose Tests for ways_tile_floor.py."""
import nose
from Dynamic_Programming.code.ways_tile_floor import ways_tile_floor


@nose.tools.timed(0.05)
def test_func_positive():
    """Test positive cases."""
    nose.tools.assert_equals(ways_tile_floor('2', '3'), 1)
    nose.tools.assert_equals(ways_tile_floor('10', '5'), 8)
    nose.tools.assert_equals(ways_tile_floor('0', '0'), 0)


@nose.tools.timed(0.02)
@nose.tools.raises(ValueError)
def test_func_wrong_types():
    """Test cases with raises."""
    nose.tools.raises(ways_tile_floor('1 2 3', 5))
    nose.tools.assert_equals(ways_tile_floor('!, @, #', '%'), 15)
    nose.tools.assert_equals(ways_tile_floor('yaba-daba', 'dooooooo'))


@nose.tools.timed(0.02)
@nose.tools.raises(IndexError)
def test_func_negative_values():
    nose.tools.raises(ways_tile_floor('-2', '-2'))


@nose.tools.timed(0.05)
def test_func_negative():
    """Test cases where inputs are 0."""
    nose.tools.assert_equals(ways_tile_floor('0', '0'), 0)
