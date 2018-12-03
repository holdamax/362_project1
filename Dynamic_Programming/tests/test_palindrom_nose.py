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
