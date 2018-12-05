#!/usr/bin/env python

"""Count ways to find path without crossing.

Take integer, even, positive number
"""


def _factorial(num: int):
    """Count factorial from num.

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


def paths_without_crossing(num: (int, str)):
    """Count numbers of ways to connect num points on a circle.

    : Parameters
    ----------
    num : integer  number of points on a circle

    Returns
    -------
    f(num) = num! / ((num/2)! * (num/2)!)
        total number of ways to connect num points on a circle without crossing.

    """
    num = int(num)
    if num == 1:
        return 0
    if not (num % 2) and num >= 2:
        return _factorial(num) // (_factorial((num // 2 + 1)) * _factorial(num // 2))
    raise ValueError


def descr():
    """Entry point function for the menu app."""
    inpt = input('\nPlease enter positive even number'
                 ' even and integer\n'
                 'Or \'q\' to back to the menu ... \n')
    if inpt.lower() == 'q':
        print('You have finished working with the searching count ways to connect num points on a circle')
        return 'q'
    try:
        result = paths_without_crossing(inpt)
        print(result)
        return None
    except (AttributeError, TypeError):
        print('Error: Please enter an array')
        return None
    except ValueError:
        print('Error: Please enter only integer, even values bigger then 0')
        return None


if __name__ == '__main__':
    descr()
