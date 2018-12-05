"""Tests for paths_without_crossing.py"""

import pytest
from Dynamic_Programming.code.paths_without_crossing import paths_without_crossing as pwc


@pytest.mark.parametrize('inputs, outputs',
                         [('2', 1),
                          ('1', 0),
                          ('4', 2),
                          ('4', 2),
                          ('6', 5),
                          ('8', 14),
                          ('1038', 140239043650914933309771256012337161301472611398544757325664370049865751420453458821350670408676263462548127750393958019426775488055871200139933800366329620082724993869266473333310721268298552396471937748379893211937643818403427162436366946974972682374621242035332097535261433136817732374480806452523112121550)])
def test_positive_paths_without_crossing(inputs, outputs):
    """Tests for paths_without_crossing() function with positive values."""
    assert pwc(inputs) == outputs

@pytest.mark.xfail(raises=(TypeError, ValueError, IndexError, AttributeError))
@pytest.mark.parametrize('inputs, outputs',
                         [('3', 'Error! You entered wrong value'),
                          ('7', 'Error! You entered wrong value'),
                          ('5', 'Error! You entered wrong value'),
                          ('-8', 'Error! You entered wrong value'),
                          ('-1000342', 'Error! You entered wrong value'),
                          ('0', 'Error! You entered wrong value'),])
def test_negative_paths_without_crossing(inputs, outputs):
    """Tests for paths_without_crossing() function with negative values."""
    assert pwc(inputs) == outputs

def test_empty_paths_without_crossing():
    """Tests for paths_without_crossing() function with empty values."""
    assert pwc('') == 'Error! You entered wrong value'
