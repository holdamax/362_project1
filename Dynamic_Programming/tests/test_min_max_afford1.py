"""PyTest for min_max_afford.py."""
import pytest
import Dynamic_Programming.code.min_max_afford as min_max

def test_descr_output(capsys):
    """Test for function descr when input is 'q'."""
    min_max.input = lambda x: 'q'
    min_max.descr()
    captured = capsys.readouterr()
    assert captured.out == 'You have finished working with the Fibonacci mod function\n'


@pytest.mark.xfail(raises=(TypeError, ValueError, RecursionError))
@pytest.mark.parametrize("low, high, days, raises", [((4, 2), [10, 12, 11, 16, 11], -1),
                                                 ([10, 12, 11, 16, 11], (4, 2), 0),
                                                 ({1: 2, 3: 4}, 5, [2, 4, 6, 1]),
                                                 ('jffkflоарблід', -1, 0),
                                                 (4.5, 7, ' '),
                                                 ('','','')])
@pytest.mark.parametrize("low, high, days", [((4, 2), [10, 12, 11, 16, 11], -1),
                                                 ([10, 12, 11, 16, 11], (4, 2), 0),
                                                 ({1: 2, 3: 4}, 5, [2, 4, 6, 1]),
                                                 ('jffkflоарблід', -1, 0),
                                                 (4.5, 7, ' '),
                                                 ('','','')])



def test_max_afford_value_raise(low, high, days):
    """Test on wrong input type."""
    min_max.max_afford(low, high, days)


@pytest.mark.parametrize("low", "high", "days", [(([1, 5, 4, 5, 3], [3, 6, 8, 7, 6], 5), 20),
                                                 (([1, 5, 4, 5, 3], [3, 6, 8, 7, 10], 5), 22)])
def test_min_max_positive(low, high, days, outputs):
    """Test of calculating max afford number with  given inputs."""
    assert min_max.max_afford(low, high, days) == outputs


def test_func():
    """Test of calculating max afford number with  given inputs."""
    assert min_max.max_afford([1, 5, 4, 5, 3], [3, 6, 8, 7, 6], 5) == 20


def test_func_2():
    """Test of calculating max afford number with  given inputs."""
    assert min_max.max_afford([1, 5, 4, 5, 3], [3, 6, 8, 7, 10], 5) == 22
