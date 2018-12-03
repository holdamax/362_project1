"""We find the longest sub-sequence using dynamic programming
over intervals within the string. We define the value Opt[i,j]
 for each interval [i,j] as the length of the longest palindromic sub-sequence"""

from nose.tools import assert_equals
from palindrom import longest_pal

                                
def test_func():
    """Test of calculating palindrom number with input 'banana'"""
    assert longest_pal('banana') == 5


def test_error():
    """Test of raising exception."""
    pytest.raises(TypeError, longest_pal(12345))


@pytest.mark.xfail(raises=NameError)
def test_fail():
    """Expected fail of test."""
    longest_pal(asdfg)


@pytest.mark.parametrize("pal_number, pal_value", [('123qQq', 3), ('123aafaafaa456', 8), ('12345abba', 4)])
def test_pal(pal_number, pal_value):
    """Test of calculating pakindrom number with different inputs."""
    assert longest_pal(pal_number) == pal_value
