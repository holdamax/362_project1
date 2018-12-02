"""Testing task 2
"""

from Dynamic_Programming.code.fibonacci import fibord
import pytest

@pytest.mark.parametrize("input, output", [(1, 1), (2, 1), (5, 3), (10, 19), (15, 129)])
def test_fibord(input, output):
    """Test of calculating fibonacci number with different inputs."""
    assert fibord(input) == output


@pytest.mark.parametrize("input, output", [('-1', None), ('hjbjbjb', None), ('5', 3), ('10', 19), ('15', 129)])
def test_fibord_positive(input, output):
    assert fibord(input) == output

@pytest.mark.parametrize("input, output", [('1', 1), ('2', 1), ('5', 3), ('10', 19), ('15', 129)])
def test_fibord_positive(input, output):
    """Test of calculating fibonacci number with different inputs."""
    assert fibord(input) == output
