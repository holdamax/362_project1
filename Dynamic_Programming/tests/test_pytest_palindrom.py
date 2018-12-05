"""Test of palindrom.py"""

import pytest
from Dynamic_Programming.code.palindrom import longest_pal

                                
def test_func():
    """Test with given input"""
    assert longest_pal('Test sequence ololo') == 5


def test_error():
    """Test of raising exception."""
    pytest.raises(TypeError, "longest_pal(10)")


@pytest.mark.parametrize("string, palindrom_length", [("no palindrom", 1),
                                                      ("testset", 7),
                                                      ("lol  kekek", 5),
                                                      ("Tesing longestpalaptsegnol algoritm 12321", 21)])
def test_fibo(string, palindrom_length):
    """Test with different inputs."""
    assert longest_pal(string) == palindrom_length
