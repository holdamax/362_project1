"""Test of yakobstelnum.py"""

import pytest
from Dynamic_Programming.code.yakobstelnum import yakobstelelement


@pytest.mark.parametrize("input, exception", [("", IndexError), (10, TypeError)])
def test_errors(input, exception):
    """Test of raising exceptions."""
    with pytest.raises(exception):
        yakobstelelement(input)


@pytest.mark.parametrize("input, yakobstelnum", [("1", 1),
                                                 ("3", 3),
                                                 ("4", 5),
                                                 ("5", 11)
                                                ])
def test_fibo(input, yakobstelnum):
    """Test with different inputs."""
    assert yakobstelelement(input) == yakobstelnum