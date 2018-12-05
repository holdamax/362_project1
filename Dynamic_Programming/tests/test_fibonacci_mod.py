"""Testing task 2
Find which is the member of position n
 in Modification Fibonacci sequence."""


from Dynamic_Programming.code.fibonacci_mod import fibo
import pytest


def test_func():
    """Test of calculating fibonacci number with input 3."""
    assert fibo(3) == 1


def test_error():
    """Test of raising exception."""
    pytest.raises(TypeError, "fibo('wrong_value')")


@pytest.mark.xfail(raises=RecursionError)
def test_fail():
    """Expected fail of test."""
    fibo(-1)


@pytest.mark.parametrize("fibo_number, fibo_value", [(1, 1), (2, 1), (5, 3), (10, 19), (15, 129)])
def test_fibo(fibo_number, fibo_value):
    """Test of calculating fibonacci number with different inputs."""
    assert fibo(fibo_number) == fibo_value
