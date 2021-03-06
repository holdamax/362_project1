"""Nose Tests for ways_tosum.py."""
import nose
from Dynamic_Programming.code.ways_to_sum import ways_to_sum

@nose.tools.timed(0.02)
def test_func_positive():
    """Test positive cases."""
    nose.tools.assert_equals(ways_to_sum('1, 2, 3, 4', 15), 10671)
    nose.tools.assert_equals(ways_to_sum('1, 2, 3', 5), 13)


@nose.tools.timed(0.02)
@nose.tools.raises( ValueError)
def test_func_negative():
    """Test negative cases."""
    nose.tools.raises(ways_to_sum('1 2 3', 5))
    nose.tools.assert_equals(ways_to_sum('!, @, #', '%'), 15)
    nose.tools.assert_equals(ways_to_sum('yaba-daba-dooooooo', 5))
