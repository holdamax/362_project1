#!/usr/bin/env python

"""
Count ways to find path without crossing.

Take integer, even, positive number
"""


def _factorial(num: int):
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


def paths_without_crossing(num: int):
    """Count numbers of ways to connect num points on a circle.

    : Parameters
    ----------
    num : integer  number of points on a circle

    Returns
    -------
    f(num) = num! / ((num/2)! * (num/2)!)
        total number of ways to connect num points on a circle without crossing.

    """
    #if num.isdigit():
    num = int(num)
    if num == 1:
        return 0
    elif not (num % 2) and num >= 2:
        return _factorial(num) // (_factorial((num // 2 + 1)) * _factorial(num // 2))
    raise ValueError
        # raise ValueError('Error! You entered wrong value')
    # raise TypeError('Error! You entered wrong value')


def descr():
    """Expect input value from keyboard and call paths_without_crossing().

    Input value
    'q' - to return
    int - to use paths_without_crossing()

    :Returns:
    int
    None
    """
    # while True:
    inpt = input('\nPlease enter positive even number'
                 ' even and integer\n'
                 'Or \'q\' to back to the menu ... \n')
    if inpt.lower() == 'q':
        print('You have finished working with the searching count ways to connect num points on a circle')
        return 'q'
    try:
        result = paths_without_crossing(inpt)
        print(result)
    except AttributeError:
        print('Error: Please enter an array')
        return None
    except TypeError:
        return None
    except ValueError:
        print('Error: Please enter only integer, even values bigger then 0')
        return None


if __name__ == '__main__':
    descr()
