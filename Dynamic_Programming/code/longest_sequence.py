#!/usr/bin/env python
"""Find how many numbers we have with difference one in the sub sequence."""


def descr():
    """Entry point function for the menu app."""
    while True:
        in_list = input('\nPlease, input the list of positive integers, '
                        'which has to be checked (e.g. 3, 4, 7, 8, 9): ')
        if in_list == 'q':
            print('Bye')
            return in_list
        longest_seq_with_diff_one(in_list)


def longest_seq_with_diff_one(arr):
    """Find how many numbers we have with difference one in the sub sequence.
<<<<<<< HEAD
    Input: list of strings - Sequence with integer numbers
=======

    Input: list of strings - Sequence with integer numbers

>>>>>>> origin
    Returns
    -------
    Number, which represents the longest sequence of integers with difference one.
    """
    try:
        if arr == '':
            arr = [3, 4, 7, 8, 9]
            print(f"Using default list {arr}...")
        else:
            arr = sorted([int(i) for i in arr.split(',')])
            print(f"Using list {arr}...")

        num = len(arr)
        arr_1 = [1 for _ in range(len(arr))]

        for i in range(num):
            for j in range(i):
                if (arr[i] == arr[j] + 1) or (arr[i] == arr[j] - 1):
                    arr_1[i] = max(arr_1[i], arr_1[j] + 1)

        print(f"Longest sequence of numbers with difference one is: {max(arr_1)}")
        return max(arr_1)
    except ValueError:
        print('Please enter correct input.')


if __name__ == '__main__':

    descr()