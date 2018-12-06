"""Testing task .
Nose: Paths without crossing"""
import nose
from Dynamic_Programming.code.paths_without_crossing import paths_without_crossing, _factorial


@nose.tools.timed(0.02)
def test_func():
    """Test with given input 1."""
    assert paths_without_crossing(1) == 0

@nose.tools.timed(0.02)
def test_func_positive():
    """Test positive cases."""
    nose.tools.assert_equals(paths_without_crossing(8), 14)
    nose.tools.assert_equals(paths_without_crossing(10), 42)


@nose.tools.timed(0.02)
@nose.tools.raises(ValueError)
def test_func_negative1():
    """Test negative cases."""
    nose.tools.raises(paths_without_crossing(3))


@nose.tools.timed(0.02)
@nose.tools.raises(ValueError)
def test_func_negative2():
    """Test negative cases."""
    nose.tools.raises(paths_without_crossing(-1))


@nose.tools.timed(0.02)
@nose.tools.raises(ValueError)
def test_func_negative3():
    """Test negative cases."""
    nose.tools.raises(paths_without_crossing(0))


@nose.tools.timed(0.02)
@nose.tools.raises(ValueError)
def test_func_negative4():
    """Test negative cases."""
    nose.tools.raises(paths_without_crossing("fdvdfv аррвсв"))


@nose.tools.timed(0.02)
@nose.tools.raises(ValueError)
def test_func_negative5():
    """Test negative cases."""
    nose.tools.raises(paths_without_crossing(""))


@nose.tools.timed(0.02)
@nose.tools.raises(ValueError)
def test_func_negative6():
    """Test negative cases."""
    nose.tools.raises(paths_without_crossing(" "))


##############################################################


@nose.tools.timed(0.02)
def test_func_factorial():
    """Test with given input 0."""
    assert _factorial(0) == 1

@nose.tools.timed(0.02)
def test_func_positive_factorial():
    """Test positive cases."""
    nose.tools.assert_equals(_factorial(4), 24)
    nose.tools.assert_equals(_factorial(9), 362880)

@nose.tools.timed(0.02)
def test_func_negative_factorial():
    """Test negative cases."""
    nose.tools.assert_equals(_factorial("fdvdfv"), None)
    nose.tools.assert_equals(_factorial("аррвсв"), None)
    nose.tools.assert_equals(_factorial(" "), None)
    nose.tools.assert_equals(_factorial(""), None)
