"""Testing task 9.
Work to be with High-effort or with Low-effort."""
from min_max_afford import max_afford
import pytest


def test_func():
    """Test of calculating max afford number with  given inputs."""
    assert max_afford([1, 5, 4, 5, 3], [3, 6, 8, 7, 6], 5) == 20


def test_func_2():
    """Test of calculating max afford number with  given inputs."""
    assert max_afford([1, 5, 4, 5, 3], [3, 6, 8, 7, 10], 5) == 22


def test_error():
    """Test of raising exception."""
    pytest.raises(TypeError, "max_afford(1)")
