"""Testing task .
Paths without crossing"""

from Dynamic_Programming.code.paths_without_crossing import paths_without_crossing
import nose


def test_func():
    """Test with given input 1."""
    assert paths_without_crossing(1) == 0


def test_func_positive():
    """Test positive cases."""
    nose.tools.assert_equals(paths_without_crossing(8), 14)
    nose.tools.assert_equals(paths_without_crossing(10), 42)


def test_func_negative():
    """Test negative cases."""
    nose.tools.assert_equals(paths_without_crossing(3), None)
    nose.tools.assert_equals(paths_without_crossing(-1), None)
    nose.tools.assert_equals(paths_without_crossing("fdvdfv"), None)
    nose.tools.assert_equals(paths_without_crossing("аррвсв"), None)
    nose.tools.assert_equals(paths_without_crossing(" "), None)
    nose.tools.assert_equals(paths_without_crossing(""), None)