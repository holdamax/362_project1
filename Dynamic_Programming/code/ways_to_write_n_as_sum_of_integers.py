"""
This method calculates in how many ways
is possible to calculate n with positive integers
"""

def descr():
    """Function for to input and verification data"""
    my_list = input('Please enter a number (e.g. 40):')
    if my_list == 'q':
        return 'q'
    return count_ways(my_list)


def count_ways(number: int):
    """
    table[i] will be storing the number of
    solutions for value i. We need n+1 rows
    as the table is constructed in bottom up
    manner using the base case (n = 0)
    Initialize all table values as 0
    """
    try:
        number = int(number)
        if number > 0:
            table = [0] * (number + 1)
            table[0] = 1
            for i in range(1, number):
                for j in range(i, number + 1):
                    table[j] += table[j - i]
        print(table[number])
    except TypeError:
        print('Please enter positive integer > 0')
    except ValueError:
        print('Please enter positive integer > 0')
    except IndexError:
        print('Please enter positive integer > 0')
