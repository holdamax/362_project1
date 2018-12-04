"""PyTest for fibonacci_mod.py."""
import pytest
import Dynamic_Programming.code.fibonacci_mod as f_mod


def test_descr_output(capsys):
    """Test for function descr when input is 'q'."""
    f_mod.input = lambda x: 'q'
    f_mod.descr()
    captured = capsys.readouterr()
    assert captured.out == 'You have finished working with the Fibonacci mod function\n'


# def test_fibo_output6(capsys):
#     """Test for function fibo(6)."""
#     f_mod.fibo(6)
#     captured = capsys.readouterr()
#     assert captured.out == '4\n'
#
#
# def test_fibo_output1(capsys):
#     """Test for function fibo(1)."""
#     f_mod.fibo(1)
#     captured = capsys.readouterr()
#     assert captured.out == '1\n'


@pytest.mark.xfail(raises=(TypeError, ValueError, RecursionError))
@pytest.mark.parametrize("inputs", [(4, 2, 3, 4), [0, 2, 1, 6, 1], {1: 2, 3: 4}, 'jffkflоарблід', -1, 0, 4.5, ' ', ''])
def test_fibo_wrong_value_raise(inputs):
    """Test on wrong input type."""
    f_mod.fibo(inputs)


def test_fibo_one():
    """Test of calculating fibonacci number when input is 1."""
    assert f_mod.fibo(1) == 1

# def test_fibo_null():
#     """Test of calculating fibonacci number when input is 0."""
#     assert f_mod.fibo(0) == ''

@pytest.mark.parametrize("inputs, outputs", [(1, 1), (2, 1), (3, 1), (4, 2), (5, 3), (6, 4), (7, 6), (8, 9), (17, 277)])
def test_fibo_positive(inputs, outputs):
    """Test of calculating fibonacci number with different inputs."""
    assert f_mod.fibo(inputs) == outputs
