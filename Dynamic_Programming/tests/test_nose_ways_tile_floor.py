"""Nose Tests for ways_tile_floor.py."""
import nose
from Dynamic_Programming.code.ways_tile_floor import ways_tile_floor


@nose.tools.timed(0.02)
def test_func_positive():
    """Test positive cases."""
    nose.tools.assert_equals(ways_tile_floor('2', '3'), 1)
    nose.tools.assert_equals(ways_tile_floor('10', '5'), 8)


@nose.tools.timed(0.02)
def test_func_negative():
    """Test negative cases."""
    nose.tools.assert_equals(ways_tile_floor('йцу', 'wed'), None)
    nose.tools.assert_equals(ways_tile_floor('1 2 3', 5), None)
