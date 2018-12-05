"""We find the longest sub-sequence using dynamic programming
over intervals within the string. We define the value Opt[i,j]
 for each interval [i,j] as the length of the longest palindromic sub-sequence"""

import nose
from Dynamic_Programming.code.palindrom import longest_pal

                                
def test_func():
    """Test for positive results"""
    nose.tools.assert_equals(longest_pal(
            '1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890'),
            19)
    assert longest_pal('0') == 1
    assert longest_pal('banana') == 5
    assert longest_pal('-5-5-5') == 5
    assert longest_pal('try this one') == 1


def test_func_negative():
    """Test negative cases"""
    assert longest_pal('-9') == 1

@nose.tools.raises(IndexError)
def test_func_negative():
    """Test raise cases"""
    assert longest_pal('') == None
