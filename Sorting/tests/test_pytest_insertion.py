"""PyTest for insertion.py
"""
import pytest
import Sorting.code.insertion as f


@pytest.mark.parametrize("inputs, outputs", [('-1, -2, -5, -4, -8, -9, -6', [-9, -8, -6, -5, -4, -2, -1]),
                                             ('1, 1, 1, 2, 5, 3, 10', [1, 1, 1, 2, 3, 5, 10]),
                                             ('1, -1, 0', [-1, 0, 1])])
def test_insertion_sort_positive(inputs, outputs):
    """Test of insertion_sort number with different inputs."""
    assert f.insertion_sort(inputs) == outputs

def test_insertion_sort_empty_string():
    """Test of insertion_sort number with different inputs."""
    with pytest.raises(ValueError):
        f.insertion_sort('')

@pytest.mark.parametrize("inputs", [[-1, -2, -5, -4, -8, -9, -6], (1, 1, 1, 2, 5, 3, 10), 8])
def test_insertion_sort_whrong_types(inputs):
    """Test of insertion_sort number with different inputs."""
    with pytest.raises(AttributeError):
        f.insertion_sort(inputs)

def test_insertion_sort_string():
    """Test of insertion_sort number with different inputs."""
    with pytest.raises(ValueError):
        f.insertion_sort('yaba-daba-dooooooo')
