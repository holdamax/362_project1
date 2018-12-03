"""Testing task 2
Find which is the member of position n
 in Modification Fibonacci sequence."""

import pytest
from Dynamic_Programming.code.fibonacci_mod import fibo

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








"""PyTest for fibonacci_mod.py."""
import pytest
import Dynamic_Programming.code.fibonacci_mod as f_mod


def test_descr_output(capsys):
    """Test output of func descr when input is 'q'."""
    f.input = lambda x: 'q'
    f.descr()
    captured = capsys.readouterr()
    assert captured.out == 'You have finished working with the Fibonacci function\n'

def test_fibord_output(capsys):
    """Test output of func fibord(5)."""
    f.fibord(5)
    captured = capsys.readouterr()
    assert captured.out == '8\n'


@pytest.mark.xfail(raises=(TypeError, ValueError, IndexError, AttributeError))
@pytest.mark.parametrize("inputs", [(1, 2, 3, 4), [1, 2, 3, 4, 5], {1: 1, 2: 2}, 'hjbjbjb', -1, 2.4])
def test_fibord_wrong_value_raise(inputs):
    """test on wrong input type."""
    f.fibord(inputs)


def test_fibord_null():
    """Test of calculating fibonacci number when input is 0."""
    assert f.fibord(0) == 1


@pytest.mark.parametrize("inputs, outputs", [(1, 1), (2, 2), (3, 3), (4, 5), (5, 8), (24, 75025)])
def test_fibord_positive(inputs, outputs):
    """Test of calculating fibonacci number with different inputs."""
    assert f.fibord(inputs) == outputs

