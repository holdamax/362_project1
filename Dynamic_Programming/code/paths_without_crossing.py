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
    num : integer number

    Returns
    -------
    factorial of num"""
    num = int(num)
    factorial = 1
    for i in range(1, num+1):
        factorial *= i
    return factorial


def paths_without_crossing(num):
    """Counts numbers of ways to connect num points on a circle
    : Parameters
    ----------
    num : integer  number of points on a circle
    Returns
    -------
    f(num) = num! / ((num/2)! * (num/2)!)
        total number of ways to connect num points on a circle without crossing.
    """
    if isinstance(num, int) or num.isdigit():
        num = int(num)
        if num == 1:
            return 0
        if not (num % 2) and num >= 2:
            return _factorial(num) // (_factorial((num // 2 + 1)) * _factorial(num // 2))
    print('You entered wrond value')
    return None


def descr():
    """
    Input value
    Calls paths_without_crossing function
    :Returns:

    """
    inpt = input('\nPlease enter positive even number'
                 ' even and integer\n'
                 'Or \'q\' to back to the menu ... ')
    if inpt.lower() == 'q':
        return 'q'
    result = paths_without_crossing(inpt)
    print(result)
    return result


if __name__ == '__main__':
    descr()