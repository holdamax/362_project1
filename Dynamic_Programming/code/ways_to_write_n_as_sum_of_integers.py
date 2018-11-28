"""
This method calculates in how many ways
is possible to calculate n with positive integers
"""

print('Please enter a number (e.g. 40)')


def count_ways(number: int):
    """
    table[i] will be storing the number of
    solutions for value i. We need n+1 rows
    as the table is constructed in bottom up
    manner using the base case (n = 0)
    Initialize all table values as 0
    """
    if isinstance(number, int) and number > 0:
        table = [0] * (number + 1)
        table[0] = 1
        for i in range(1, number):
            for j in range(i, number + 1):
                table[j] += table[j - i]
        return table[number]
    else:
        return 'Please enter integer number > 0'

print(count_ways(2))