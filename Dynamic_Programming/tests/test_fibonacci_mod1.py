"""PyTest for fibonacci_mod.py."""
import pytest
import Dynamic_Programming.code.fibonacci_mod as f_mod


# @pytest.mark.xfail(raises=(TypeError, ValueError, RecursionError))
# @pytest.mark.parametrize("inputs", [(4, 2, 3, 4), [0, 2, 1, 6, 1], {1: 2, 3: 4}, 'jffkflоарблід', -1, 0, 4.5, ' ', ''])
# def test_fibo_wrong_value_raise(inputs):
#     """Test on wrong input type."""
#     f_mod.fibo(inputs)

@pytest.mark.xfail(raises=(TypeError))
def test_fibo_wrong_value_raise():
    """Test on wrong input type."""
    f_mod.fibo([0, 2, 1, 6, 1]) != None

def test_fibo_o():
    """Test of calculating fibonacci number when input is 1."""
    assert f_mod.fibo(-1) == None


def test_fibo_null():
    """Test of calculating fibonacci number when input is 0."""
    assert f_mod.fibo(0) == None

@pytest.mark.parametrize("inputs, outputs", [(1, 1), (3, 1), (4, 2), (6, 4), (17, 277)])
def test_fibo_positive(inputs, outputs):
    """Test of calculating fibonacci number with different inputs."""
    assert f_mod.fibo(inputs) == outputs
