"""Testing task 14 - Optimized painting fence."""

import pytest
from Dynamic_Programming.code import optimized_painting_fence as opf


@pytest.mark.parametrize('inputs, outputs',[((1, 1), 1)])
def test_itr(inputs, outputs):
    """Tests for positive results"""
    assert opf.find_combinations(inputs) == outputs

