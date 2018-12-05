"""Testing task .
Paths without crossing"""

from Sorting.code.bucket_sorting import bucket_sorting, msBits
import nose

@nose.tools.timed(0.02)
def test_func():
    """Test with given input 1."""
    assert bucket_sorting([1]) == [1]

@nose.tools.timed(0.02)
def test_func_positive():
    """Test positive cases."""
    nose.tools.assert_equals(bucket_sorting([1, 4, 6, 0, -1]), [-1, 0, 1, 4, 6])
    nose.tools.assert_equals(bucket_sorting([10, -2, 5]), [-2, 5, 10])

@nose.tools.timed(0.02)
def test_func_negative():
    """Test negative cases."""
    nose.tools.assert_equals(bucket_sorting("fdvdfv"), None)
    nose.tools.assert_equals(bucket_sorting("аррвсв"), None)
    nose.tools.assert_equals(bucket_sorting(" "), None)
    nose.tools.assert_equals(bucket_sorting(""), None)


@nose.tools.timed(0.02)
@nose.tools.raises(IndexError, TypeError)
def test_raises_type_error():
    raise TypeError('Please enter an array of integer numbers')
