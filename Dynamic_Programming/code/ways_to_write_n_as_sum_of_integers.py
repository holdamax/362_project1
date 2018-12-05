"""
This method calculates in how many ways
is possible to calculate n with positive integers
"""


def descr():
    """Function for to input and verification data"""
    number = input('Please enter number in range: 0 < integer number < 10000 (e.g. 40):')
    if number == 'q':
        return 'q'
    try:
        print("There are {1} ways to write {0} as "
              "sum of positive integers".format(number, count_ways(int(number))))
    except (TypeError, ValueError, IndexError):
        print('Wrong input. Please enter number in range: 0 < integer number < 10000')
    return None


def count_ways(number: int):
    """
    table[i] will be storing the number of
    solutions for value i. We need n+1 rows
    as the table is constructed in bottom up
    manner using the base case (n = 0)
    Initialize all table values as 0
    """
    if not isinstance(number, int):
        raise TypeError('Wrong input. Please enter number like: 0 < integer number < 10000')
    if 10000 > number > 0:
        table = [0] * (number + 1)
        table[0] = 1
        for i in range(1, number):
            for j in range(i, number + 1):
                table[j] += table[j - i]
        return table[number]
    raise ValueError('Wrong input. Please enter number like: 0 < integer number < 10000')

