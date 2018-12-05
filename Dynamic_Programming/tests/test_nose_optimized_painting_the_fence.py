"""Nose paiting_the_fence.py."""
import nose
from Dynamic_Programming.code.optimized_painting_fence import find_combinations


@nose.tools.timed(0.02)
def test_func_positive():
    """Test positive cases."""
    nose.tools.assert_equal(find_combinations(1, 1), 1)
    nose.tools.assert_equal(find_combinations(2, 4), 16)
    nose.tools.assert_equal(find_combinations(7, 3), 1344)
    nose.tools.assert_equal(find_combinations(99, 99), 366123817149514516148364806310978588296555911619520763646498043556906006656302314790963459686521537709701386771477994322892424507340183779831082307535480272964631807361347419289259402291608289280000)


@nose.tools.timed(0.02)
def test_func_negative():
    """Test negative cases."""
    nose.tools.assert_equal(find_combinations('s', 'g'), 'Error! Please, enter positive numbers (etc. 2 and 3)')
    nose.tools.assert_equal(find_combinations(-5, 5), 'Error! Please, enter positive numbers (etc. 2 and 3)')
    nose.tools.assert_equal(find_combinations(-4, -4), 'Error! Please, enter positive numbers (etc. 2 and 3)')
    nose.tools.assert_equal(find_combinations(4, -10), 'Error! Please, enter positive numbers (etc. 2 and 3)')
    nose.tools.assert_equal(find_combinations(0, 5), 'Error! Please, enter positive numbers (etc. 2 and 3)')
    nose.tools.assert_equal(find_combinations(5, 0), 'Error! Please, enter positive numbers (etc. 2 and 3)')
    nose.tools.assert_equal(find_combinations(0, 0), 'Error! Please, enter positive numbers (etc. 2 and 3)')
    nose.tools.assert_equal(find_combinations(100, 100), 'please, choose lesser numm')