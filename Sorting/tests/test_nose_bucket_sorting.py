"""Testing task .
Nose: Bucket sorting"""
import nose
from Sorting.code.bucket_sorting import bucket_sorting


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
@nose.tools.raises(ValueError)
def test_func_negative4():
    """Test negative cases."""
    nose.tools.raises(bucket_sorting("fdvdfv аррвсв"))


@nose.tools.timed(0.02)
@nose.tools.raises(AttributeError)
def test_func_negative5():
    """Test negative cases."""
    nose.tools.raises(bucket_sorting(""))


@nose.tools.timed(0.02)
@nose.tools.raises(AttributeError)
def test_func_negative6():
    """Test negative cases."""
    nose.tools.raises(bucket_sorting(" "))
