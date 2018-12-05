"""PyTest for fibonacci.py."""
import pytest
import Dynamic_Programming.code.fibonacci as f

@pytest.mark.parametrize("inputs, outputs", [((1, 2, 3, 4),TypeError),
                                             ([1, 2, 3, 4, 5], TypeError),
                                             ('yaba-daba-dooooooo',ValueError),
                                             ('2.5',ValueError),
                                             (-5, IndexError)])
def test_fibord_wrong_value_raise(inputs, outputs):
    """test on wrong input type."""
    with pytest.raises(outputs):
        f.fibord(inputs)


def test_fibord_null():
    """Test of calculating fibonacci number when input is 0."""
    assert f.fibord(0) == 1


@pytest.mark.parametrize("inputs, outputs", [(1, 1), ('1', 1), (24, 75025)])
def test_fibord_positive(inputs, outputs):
    """Test of calculating fibonacci number with different inputs."""
    assert f.fibord(inputs) == outputs
