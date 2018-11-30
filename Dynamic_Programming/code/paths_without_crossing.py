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


def paths_without_crossing(num):
    """Counts numbers of ways to connect num points on a circle
    : Parameters
    ----------
    n : number of points on a circle
    Returns
    -------
    f(n) = num! / ((num/2)! * (num/2)!)
        total number of ways to connect num points on a circle without crossing.
    """
    if num.isdigit():
        num = int(num)
        if not (num % 2) and num >= 2:
            return _factorial(num) // (_factorial((num // 2 + 1)) * _factorial(num // 2))
    print('You entered wrond value')



def descr():
    """Check entered data for integer type and correct value
    Calls paths_without_crossing function and check type
    :Returns:

    """
    inpt = input('\nPlease enter positive even number'
                 ' even and integer...\n'
                 'Or \'q\' to back to the menu ... ')
    if inpt.lower() == 'q':
        return 'q'
    result = paths_without_crossing(inpt)
    print(result)
    return result

if __name__ == '__main__':
   descr()
