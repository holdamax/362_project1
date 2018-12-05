""" Work to be with High-effort or with Low-effort."""

import nose
from min_max_afford import max_afford



def test_func():
    """Test of calculating max_afford with input 3."""
    assert max_afford(3) == 3


def test_func_positive():
    """Test positive cases."""
    nose.tools.assert_equals(max_afford(6, 13))
    nose.tools.assert_equals(max_afford(7, 21))


def test_func_negative():
    """Test negative cases."""
    nose.tools.assert_equals(max_afford("wrong", None))
    nose.tools.assert_equals(max_afford(-1, None))
