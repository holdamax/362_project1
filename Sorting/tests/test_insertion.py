"""
Test for fibonacci.py
"""
import pytest
import Sorting.code.insertion as f


def test_descr_output(capsys):
    """
        Test output of func descr when input is 'q'
    """
    f.input = lambda x: 'q'
    f.descr()
    captured = capsys.readouterr()
    assert captured.out == 'You have finished working with the sorting function\n'


def test_insertion_sort_output(capsys):
    """
    Test output of func fibord(5)
    """
    f.insertion_sort('1, 2, 5, 4, 8, 9, 6')
    captured = capsys.readouterr()
    assert captured.out == '1, 2, 4, 5, 6, 8, 9\n'


@pytest.mark.parametrize("inputs, outputs", [('1, 2, 5, 4, 8, 9, 6', [1, 2, 4, 5, 6, 8, 9]), ('1, 1, 1, 2, 5, 3, 3',
                                                                                              [1, 1, 1, 2, 3, 3, 5])])
def test_insertion_sort_positive(inputs, outputs):
    """Test of insertion_sort number with different inputs."""
    assert f.insertion_sort(inputs) == outputs
