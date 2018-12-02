"""
Test for fibonacci.py
"""
import pytest
import Dynamic_Programming.code.fibonacci as f


def test_descr_output(capsys):
    f.input = lambda x: 'q'
    f.descr()
    captured = capsys.readouterr()
    assert captured.out == 'You have finished working with the Fibonacci function\n'

def test_fibord_output(capsys):
    """
    Test output of func fibord(5)
    """
    f.fibord(5)
    captured = capsys.readouterr()
    assert captured.out == '8\n'


# @pytest.mark.xfail(raises=(TypeError, ValueError, IndexError, AttributeError))
# @pytest.mark.parametrize("inputs", [(1, 2, 3, 4), [1, 2, 3, 4, 5], {1: 1, 2: 2}, 'hjbjbjb', -1, 2.4])
# def test_fibord_wrong_value_raise(inputs):
#     """
#     test on wrong input type
#     """
#     f.fibord(inputs)


def test_fibord_null():
    """

    """
    assert f.fibord(0) == 1


@pytest.mark.parametrize("inputs, outputs", [(1, 1), (2, 2), (3, 3), (4, 5), (5, 8), (24, 75025)])
def test_fibord_positive(inputs, outputs):
    """Test of calculating fibonacci number with different inputs."""
    assert f.fibord(inputs) == outputs
