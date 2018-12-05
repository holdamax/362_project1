"""PyTest for fibonacci.py."""
import pytest
import Dynamic_Programming.code.fibonacci as f

@pytest.mark.parametrize("inputs", [(1, 2, 3, 4), [1, 2, 3, 4, 5], {1: 1, 2: 2}, 2.4])
def test_fibord_wrong_value_raise(inputs):
    """test on wrong input type."""
    with pytest.raises((AttributeError, TypeError, ValueError)):
        f.fibord(inputs)


def test_fibord_null():
    """Test of calculating fibonacci number when input is 0."""
    assert f.fibord(0) == 1


def test_fibord_negative():
    """Test of calculating fibonacci number when input is negative number."""
    assert f.fibord(-4) is None


@pytest.mark.parametrize("inputs, outputs", [(1, 1), (2, 2), (3, 3), (4, 5), (5, 8), (24, 75025)])
def test_fibord_positive(inputs, outputs):
    """Test of calculating fibonacci number with different inputs."""
    assert f.fibord(inputs) == outputs
