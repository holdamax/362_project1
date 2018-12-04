"""Nose paiting_the_fence.py."""
import nose
from Dynamic_Programming.code.painting_the_fence import ways_to_paint_fence


@nose.tools.timed(0.02)
def test_func_positive():
    """Test positive cases."""
    nose.tools.assert_equals(ways_to_paint_fence(2, 4), 16)
    nose.tools.assert_equals(ways_to_paint_fence(7, 3), 1344)
    nose.tools.assert_equals(ways_to_paint_fence(0, 3), 0)
    nose.tools.assert_equals(ways_to_paint_fence(456, 2), 287671334303350962667238206909904017415460679837731762973746718169531793949268137295281753099874)


@nose.tools.timed(0.02)
@nose.tools.raises(TypeError)
def test_func_negative():
    """Test negative cases."""
    nose.tools.raises(ways_to_paint_fence('s', 'g'))
    nose.tools.raises(ways_to_paint_fence(-5, 5))
    nose.tools.raises(ways_to_paint_fence(-5, 5))

