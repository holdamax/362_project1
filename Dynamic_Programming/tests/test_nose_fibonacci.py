"""Testing task 1.
Find which is the member of position n
 in Fibonacci sequence."""


from Dynamic_Programming.code.fibonacci import fibord
import nose


def test_func():
    """Test of calculating fibonacci number with input 3."""
    assert fibord(3) == 3


def test_func_positive():
    """Test positive cases."""
    nose.tools.assert_equals(fibord(6), 13)
    nose.tools.assert_equals(fibord(7), 21)


def test_func_negative():
    """Test negative cases."""
    nose.tools.assert_equals(fibord("wrong"), None)
    nose.tools.assert_equals(fibord(-1), None)
