"""
looking for number value in yakobstel sequence."""


from yakobstelnum import yakobstelelement
import pytest


def test_func():
    """yakobstel number with input 4"""
    assert yakobstelelement(4) == 5


def test_error():
    """exception."""
    pytest.raises(TypeError, "yakobstelelement('wrong_value')")


@pytest.mark.xfail(raises=RecursionError)
def test_fail():
    """fail ?"""
    yakobstelelement(-1)


@pytest.mark.parametrize("yakobstelel_num, yakobstel_val", [(1, 1), (2, 1), (5, 11), (7, 43), (9, 171)])
def test_yakob(yakobstelel_num, yakobstel_val):
    """calculate yakobstel number with different inputs."""
    assert yakobstelelement(yakobstelel_num) == yakobstel_val