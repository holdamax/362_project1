"""Tests for paths_without_crossing.py"""

import pytest
from Dynamic_Programming.code.paths_without_crossing import paths_without_crossing as pwc


@pytest.mark.parametrize('inputs, outputs',
                         [('2', 1),
                          ('4', 2),
                          ('4', 2),
                          ('6', 5),
                          ('8', 14),
                          ('1038', 140239043650914933309771256012337161301472611398544757325664370049865751420453458821350670408676263462548127750393958019426775488055871200139933800366329620082724993869266473333310721268298552396471937748379893211937643818403427162436366946974972682374621242035332097535261433136817732374480806452523112121550),
                          ('2000', 2046105521468021692642519982997827217179245642339057975844538099572176010191891863964968026156453752449015750569428595097318163634370154637380666882886375203359653243390929717431080443509007504772912973142253209352126946839844796747697638537600100637918819326569730982083021538057087711176285777909275869648636874856805956580057673173655666887003493944650164153396910927037406301799052584663611016897272893305532116292143271037140718751625839812072682464343153792956281748582435751481498598087586998603921577523657477775758899987954012641033870640665444651660246024318184109046864244732001962029120)])
def test_positive_paths_without_crossing(inputs, outputs):
    """Tests for paths_without_crossing() function with positive values."""
    assert pwc(inputs) == outputs


@pytest.mark.parametrize('inputs, outputs',
                         [('3', ValueError),
                          ('7', ValueError),
                          ('-8', ValueError),
                          ('saffs', ValueError),
                          ('0', ValueError),])
def test_negative_paths_without_crossing(inputs, outputs):
    """Tests for paths_without_crossing() function with negative values."""
    with pytest.raises(outputs):
        pwc(inputs)


def test_empty_paths_without_crossing():
    """Tests for paths_without_crossing() function with empty values."""
    with pytest.raises(ValueError):
        pwc('')
