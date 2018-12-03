#!/usr/bin/env python

"""
Count ways to find path without crossing.

Take integer, even, positive number
"""


def _factorial(num):
    """
    Count factorial from num.

    : Parameters
    ----------
    num : integer number

    Returns
    -------
    factorial of num

    """
    try:
        factorial = 1
        for i in range(1, num+1):
            factorial *= i
        return factorial
    except TypeError:
        print('Wrong type')


def paths_without_crossing(num):
    """Count numbers of ways to connect num points on a circle.

    : Parameters
    ----------
    num : integer  number of points on a circle

    Returns
    -------
    f(num) = num! / ((num/2)! * (num/2)!)
        total number of ways to connect num points on a circle without crossing.

    """
    try:
        if isinstance(num, int) or num.isdigit():
            num = int(num)
            if num == 1:
                return 0
            if not (num % 2) and num >= 2:
                return _factorial(num) // (_factorial((num // 2 + 1)) * _factorial(num // 2))
        print('You entered wrond value')
        return None
    except(AttributeError, TypeError):
        print('You entered wrond type')



def descr():
    """Expect input value from keyboard and call paths_without_crossing().

    Input value
    'q' - to return
    int - to use paths_without_crossing()

    :Returns:
    int
    None
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
