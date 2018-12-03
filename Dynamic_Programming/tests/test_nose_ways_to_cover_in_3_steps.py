"""Testing task .
Ways to cover in 3 steps."""


from ways_to_cover_in_3_steps import count_ways
import nose


def test_func():
    """Test with given input 3."""
    assert count_ways(3) == 4


def test_func_positive():
    """Test positive cases."""
    nose.tools.assert_equals(count_ways(6), 24)
    nose.tools.assert_equals(count_ways(7), 44)


def test_func_negative():
    """Test negative cases."""
    nose.tools.assert_equals(count_ways("wrong"), None)
    nose.tools.assert_equals(count_ways(-1), None)
