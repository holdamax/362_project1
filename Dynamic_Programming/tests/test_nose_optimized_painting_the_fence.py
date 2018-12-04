"""Nose paiting_the_fence.py."""
import nose
from Dynamic_Programming.code.optimized_painting_fence import find_combinations


@nose.tools.timed(0.02)
def test_func_positive():
    """Test positive cases."""
    nose.tools.assert_equals(find_combinations(2, 4), 16)
    nose.tools.assert_equals(find_combinations(7, 3), 1344)
    nose.tools.assert_equals(find_combinations(200, 10), 16133564160754703249695860213465520495925134435453257382521184041622675197165786384957745198957977610993795086651908676938671838048297132983309017576413935468343852352012119422885524187318585539773700)


@nose.tools.timed(0.02)
def test_func_negative():
    """Test negative cases."""
    nose.tools.assert_equal(find_combinations('s', 'g'), None)
    nose.tools.assert_equals(find_combinations(-5, 5), None)
    nose.tools.assert_equals(find_combinations(0, 5), None)