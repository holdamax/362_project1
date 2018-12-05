"""Testing task .
Paths without crossing"""

from Dynamic_Programming.code.paths_without_crossing import paths_without_crossing, _factorial
import nose

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
def test_func_negative():
    """Test negative cases."""
    nose.tools.assert_equals(paths_without_crossing(3), None)
    nose.tools.assert_equals(paths_without_crossing(-1), None)
    nose.tools.assert_equals(paths_without_crossing(0), None)
    nose.tools.assert_equals(paths_without_crossing("fdvdfv"), None)
    nose.tools.assert_equals(paths_without_crossing("аррвсв"), None)
    nose.tools.assert_equals(paths_without_crossing(" "), None)
    nose.tools.assert_equals(paths_without_crossing(""), None)


@nose.tools.timed(0.02)
@nose.tools.raises(AttributeError, TypeError)
def test_raises_type_error():
    raise TypeError('Error! You entered wrong value')

##############################################################
@nose.tools.timed(0.02)
def test_func_factorial():
    """Test with given input 1."""
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


@nose.tools.timed(0.02)
@nose.tools.raises(TypeError)
def test_raises_type_error_factorial():
    raise TypeError('Wrong type')