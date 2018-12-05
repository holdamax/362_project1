"""Test for fibonacci.py."""
import pytest
import Dynamic_Programming.code.ways_to_cover_in_3_steps as f


@pytest.mark.parametrize("inputs, outputs", [((1, 2, 3, 4),TypeError),
                                             ([1, 2, 3, 4, 5], TypeError),
                                             ('yaba-daba-dooooooo',ValueError),
                                             (-1, IndexError)])
def test_count_ways_wrong_value_raise(inputs, outputs):
    """Test on wrong input type."""
    with pytest.raises(outputs):
        f.count_ways(inputs)


def test_count_ways_null():
    """Test result of func count_ways(0)."""
    assert f.count_ways(0) == 1


@pytest.mark.parametrize("inputs, outputs", [(1, 1), (8, 81), (24, 1389537)])
def test_count_ways_positive(inputs, outputs):
    """Test of calculating Ways to cover in 3 steps with different inputs."""
    assert f.count_ways(inputs) == outputs
