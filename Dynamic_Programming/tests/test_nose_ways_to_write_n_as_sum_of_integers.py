"""Nose test_nose_ways_to_write_n_as_sum_of_integers.py"""
import nose
from Dynamic_Programming.code.ways_to_write_n_as_sum_of_integers import count_ways


@nose.tools.timed(0.02)
def test_func_positive():
    """Test positive cases."""
    nose.tools.assert_equals(count_ways(20), 626)
    nose.tools.assert_equals(count_ways(6), 10)
    nose.tools.assert_equals(count_ways(456), 190581040442651931033)


@nose.tools.timed(0.02)
@nose.tools.raises(TypeError, ValueError)
def test_func_negative():
    """Test negative cases."""
    nose.tools.raises(count_ways('s'))
    nose.tools.raises(count_ways(5))
    nose.tools.raises(count_ways(-5))
    nose.tools.raises(count_ways(0))

