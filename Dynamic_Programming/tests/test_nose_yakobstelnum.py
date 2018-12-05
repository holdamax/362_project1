"""Nose tests for task 3. Yakobstel number."""

import nose
from Dynamic_Programming.code.yakobstelnum import yakobstelelement as ytl


def test_func_positive():
    """Test positive cases"""
    assert ytl('0') == 0
    assert ytl('9') == 171


def test_func_negative():
    """Test negative cases"""
    assert ytl('-9') == 'Error. The values entered must be Positive integer.'
    assert ytl('hey') == 'Error. The values entered must be integer!'
    assert ytl('1001') == 'Error. The values entered is to large.'

@nose.tools.raises(IndexError)
def test_func_negative():
    """Test raise cases"""
    assert ytl('') == 'Error. The values entered must be integer.'

