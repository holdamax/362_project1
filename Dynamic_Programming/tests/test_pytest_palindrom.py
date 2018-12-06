"""Test of palindrom.py"""

import pytest
from Dynamic_Programming.code.palindrom import longest_pal

                                
def test_func():
    """Test with given input"""
    assert longest_pal("Test sequence qwqwq") == "5"


@pytest.mark.parametrize("inputs, ouputs", [("123456789012345678901234567890123456789012345678901"
                                             "23456789012345678901234567890123456789012345678901",
                                             'String should not be longer than 100 characters.')])
def test_errors(inputs, ouputs):
    """Test of raising exceptions."""
    assert longest_pal(inputs) == ouputs


@pytest.mark.parametrize("inputs, palindrom_length", [("qwerty qwerty", "1"),
                                                    ("testset", "7"),
                                                    ("lol  kekek", "5"),
                                                    ("Tesing longestpalaptsegnol algoritm 12321", "21")
                                                    ])
def test_fibo(inputs, palindrom_length):
    """Test with different inputs."""
    assert longest_pal(inputs) == palindrom_length
