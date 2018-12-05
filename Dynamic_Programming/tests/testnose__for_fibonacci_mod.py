"""
Find which is the member of position n
 in Fibonacci_Mod sequence."""


from fibonacci_mod import fibo
import nose


def test_func():
    """Test of calculating fibonacci number with input 3."""
    assert fibo(3) == 3


def test_func_positive():
    """Test positive cases."""
    nose.tools.assert_equals(fibo(6), 13)
    nose.tools.assert_equals(fibo(7), 21)


def test_func_negative():
    """Test negative cases."""
    nose.tools.assert_equals(fibo("wrong"), None)
    nose.tools.assert_equals(fibo(-1), None)
