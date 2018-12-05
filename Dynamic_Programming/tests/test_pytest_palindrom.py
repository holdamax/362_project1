"""Test of palindrom.py"""

import pytest
from Dynamic_Programming.code.palindrom import longest_pal

                                
def test_func():
    """Test with given input"""
    assert longest_pal("Test sequence qwqwq") == 5


@pytest.mark.parametrize("input, exception", [("", IndexError), (10, TypeError)])
def test_errors(input, exception):
    """Test of raising exceptions."""
    with pytest.raises(exception):
        longest_pal(input)


@pytest.mark.parametrize("input, palindrom_length", [("qwerty qwerty", 1),
                                                    ("testset", 7),
                                                    ("lol  kekek", 5),
                                                    ("Tesing longestpalaptsegnol algoritm 12321", 21)
                                                    ])
def test_fibo(input, palindrom_length):
    """Test with different inputs."""
    assert longest_pal(input) == palindrom_length
