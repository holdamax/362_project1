"""
Test for fibonacci.py
"""
import pytest
import Dynamic_Programming.code.ways_to_cover_in_3_steps as f


def test_descr_output_q(capsys):
    f.input = lambda x: 'q'
    f.descr()
    captured = capsys.readouterr()
    assert captured.out == 'You have finished working with the searching count ways\n'

def test_count_ways_output(capsys):
    """
    Test output of func count_ways(8)
    """
    f.count_ways(8)
    captured = capsys.readouterr()
    assert captured.out == '81\n'


@pytest.mark.xfail(raises=(TypeError, ValueError, IndexError, AttributeError))
@pytest.mark.parametrize("inputs", [(1, 2, 3, 4), [1, 2, 3, 4, 5], {1: 1, 2: 2}, 'hjbjbjb', -1, 2.4])
def test_count_ways_wrong_value_raise(inputs):
    """
    test on wrong input type
    """
    f.count_ways(inputs)


def test_count_ways_null():
    """
    Test result of func count_ways(0)
    """
    assert f.count_ways(0) == 1


@pytest.mark.parametrize("inputs, outputs", [(1, 1), (5, 13), (8, 81), (24, 1389537)])
def test_count_ways_positive(inputs, outputs):
    """Test of calculating Ways to cover in 3 steps with different inputs."""
    assert f.count_ways(inputs) == outputs