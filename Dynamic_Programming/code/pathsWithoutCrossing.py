#!/usr/bin/env python
"""Tests for friend_pairs.py"""

from math import factorial


def pathsWithoutCrossing(num):
    """
    ...
    :param num:
    :return:
    """
    try:
        if num % 2 or num < 2:
            raise ValueError
        else:
            return round(factorial(num) / (factorial((num / 2 + 1)) * factorial(num / 2)))
    except (TypeError, ValueError):
        print('You used wrong value, please use positive, even and integer value.\n')


if __name__ == '__main__':
    Catalan = int(input('Please enter positive, even and integer value... '))
    print(pathsWithoutCrossing(Catalan))
