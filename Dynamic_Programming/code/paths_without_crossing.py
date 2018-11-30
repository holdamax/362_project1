#!/usr/bin/env python
"""
Count ways to find path without crossing
Take integer, even, positive number
"""


def _factorial(num):
    """
    Count factorial from num

    : Parameters
    ----------
    n : integer number

    Returns
    -------
    n!
    factorial
    """
    num = int(num)
    number = 1
    for i in range(1, num+1):
        number *= i
    return number


def _paths_without_crossing(num):
    """Counts numbers of ways to connect num points on a circle
    : Parameters
    ----------
    n : number of points on a circle
    Returns
    -------
    f(n) = num! / ((num/2)! * (num/2)!)
        total number of ways to connect num points on a circle without crossing.
    """
    return round(_factorial(num) / (_factorial((num / 2 + 1)) * _factorial(num / 2)))




def descr():
    """Check entered data for integer type and correct value
    Calls paths_without_crossing function and check type
    :Returns:


    """
    while True:

        try:
            inpt = input('Please enter number in range from 2 to 1038, positive,'
                         ' even and integer...\n'
                         'Or \'q\' to back to the menu'
                         'WARNING!!! Do not enter value BIGGER then 1038, please\n')
            if isinstance(inpt, str) and inpt.lower() == 'q':
                return 'q'
            number = int(inpt)
            if number != 0 and (not (number % 2) and number <= 1038 and number >= 2):
                return _paths_without_crossing(number)
        except(TypeError, ValueError):
            print('You used wrong value')

if __name__ == '__main__':
    print(descr())
