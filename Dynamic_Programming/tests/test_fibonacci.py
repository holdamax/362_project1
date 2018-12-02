"""
Test for fibonacci.py
"""
import pytest
from Dynamic_Programming.code.fibonacci import fibord


def test_fibord_output(capsys):
    """
    Test output of func fibord(5)
    """
    fibord(5)
    captured = capsys.readouterr()
    assert captured.out == '8\n'


@pytest.mark.xfail(raises=(TypeError, ValueError, IndexError))
@pytest.mark.parametrize("inputs", [(1, 2, 3, 4), [1, 2, 3, 4, 5], {1: 1, 2: 2}, 'hjbjbjb'])
def test_fibord_wrong_types_raise(inputs):
    """
    test on wrong input type
    """
    fibord(inputs)


@pytest.mark.parametrize("inputs, outputs", [(-1, None), (2.4, None)])
def test_fibord_negativevalue_output(inputs, outputs, capsys):
    """
    test on wrong input value(negative and float number)
    """
    assert fibord(input) == outputs
    captured = capsys.readouterr()
    assert captured.out == 'Error. The values entered must be greater or equal to 0\n'


def test_fibord_null():
    """

    """
    assert fibord(0) == 1


@pytest.mark.parametrize("inputs, outputs", [(1, 1), (2, 2), (3, 3), (4, 5), (5, 8), (24, 75025)])
def test_fibord_positive(inputs, outputs):
    """Test of calculating fibonacci number with different inputs."""
    assert fibord(inputs) == outputs
