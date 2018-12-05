"""Testing task 14 - Optimized painting fence."""

import pytest
from Dynamic_Programming.code import optimized_painting_fence as opf


class TestPositive:
    def test_1_1(self):
        assert opf.find_combinations(1, 1) == 1

    def test_13_14(self):
        assert opf.find_combinations(13, 14) == 752711352439774

    def test_99_99(self):
        assert opf.find_combinations(99,
                                     99) == 366123817149514516148364806310978588296555911619520763646498043556906006656302314790963459686521537709701386771477994322892424507340183779831082307535480272964631807361347419289259402291608289280000
        366123817149514516148364806310978588296555911619520763646498043556906006656302314790963459686521537709701386771477994322892424507340183779831082307535480272964631807361347419289259402291608289280000


class TestNegative:
    def test_subzero(self):
        assert opf.find_combinations(-1, 3) == 'Error! Please, enter positive numbers (etc. 2 and 3)'

    def test_0_0(self):
        assert opf.find_combinations(0, 0) == 'Error! Please, enter positive numbers (etc. 2 and 3)'

    def test_100_100(self):
        assert opf.find_combinations(100, 100) == 'please, choose lesser numm'
