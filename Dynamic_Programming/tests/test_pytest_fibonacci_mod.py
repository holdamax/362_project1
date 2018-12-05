"""PyTest for fibonacci_mod.py."""
import pytest
import Dynamic_Programming.code.fibonacci_mod as f_mod


@pytest.mark.xfail(raises=(TypeError, ValueError, RecursionError))
@pytest.mark.parametrize("inputs", [(4, 2, 3, 4), [0, 2, 1, 6, 1], {1: 2, 3: 4}, 'jffkflоарблід', -1, 0, 4.5, ' ', ''])
def test_fibo_wrong_value_raise(inputs):
    """Test on wrong input type."""
    f_mod.fibo(inputs)


@pytest.mark.xfail(raises=TypeError)
def test_fail1():
    """Expected fail of test when input is 46."""
    f_mod.fibo(46)


def test_fibo_o():
    """Expected None of test when input is 50."""
    assert f_mod.fibo(50) == None


def test_fibo_fail2():
    """Expected fail of test when input is 46."""
    f_mod.fibo(46)
    pytest.raises(ImportError)


@pytest.mark.parametrize("inputs, outputs", [(1, 1), (3, 1), (4, 2), (6, 4), (17, 277), (45, 12322413)])
def test_fibo_positive(inputs, outputs):
    """Test of calculating fibonacci number with different inputs."""
    assert f_mod.fibo(inputs) == outputs


@pytest.mark.parametrize("inputs, outputs", [(0, None), (-1, None), (-3, None), (-15, None)])
def test_fibo_negative(inputs, outputs):
    """Test of calculating fibonacci number with different inputs."""
    assert f_mod.fibo(inputs) == outputs


def test_error():
    """Test of raising exception."""
    pytest.raises(TypeError, f_mod.fibo(888))


@pytest.mark.xfail(raises=RecursionError)
def test_fail():
    """Expected fail of test."""
    f_mod.fibo(-1)
