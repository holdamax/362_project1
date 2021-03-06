"""looking for number value in yakobstel sequence"""

import pytest
from yakobstelnum import yakobstelelement


def test_func():
    """yakobstel number with input 4"""
    assert yakobstelelement(4) == 5


def test_error():
    """exception."""
    pytest.raises(AttributeError, yakobstelelement("sdfsdf"))


@pytest.mark.xfail(raises=TypeError)
def test_fail():
    """fail ?"""
    yakobstelelement('qwerty')


@pytest.mark.parametrize("inputs, outputs", [(1, 1), (2, 1), (5, 11), (7, 43), (9, 171)])
def test_yakob(inputs, outputs):
    """calculate yakobstel number with different inputs."""
    assert yakobstelelement(inputs) == outputs
