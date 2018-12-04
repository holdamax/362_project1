#!/usr/bin/env python
"""Find how many numbers we have with difference one in the sub sequence."""

import os


def cls():
    """Clear screen."""
    os.system('cls')


def descr():
    """Entry point function for the menu app."""
    cls()
    while True:
        in_list = input('\nPlease, input sequence of coma separated integers, '
                        'which has to be checked (e.g. 3, 4, 7, 8, 9): ')
        if in_list == 'q':
            print('Bye')
            return in_list
        elif in_list == 'c':
            cls()
        else:
            longest_seq_with_diff_one(in_list)


def count_it(arr) ->int or str:
    """Find how many numbers we have with difference one in the sub sequence.

    Input: coma separated integers - Sequence with integer numbers

    Returns: Number, which represents the longest sequence of integers with difference one."""
    arr = sorted(arr)
    print(f"Using list {arr}...")

    num = len(arr)
    arr_1 = [1 for _ in range(len(arr))]

    for i in range(num):
        for j in range(i):
            if (arr[i] == arr[j] + 1) or (arr[i] == arr[j] - 1):
                arr_1[i] = max(arr_1[i], arr_1[j] + 1)

    print(f"Longest sequence of numbers with difference one is: {max(arr_1)}")
    return max(arr_1)


def longest_seq_with_diff_one(arr: int or str, *args: int or str) -> int or str:

    if arr == '':
        print("Please enter correct input.")
        return "Please enter correct input."
    elif isinstance(arr, int):
        lst = []
        lst.append(arr)
        for arg in args:
            if str(arg).isdigit():
                lst.append(arg)
        count_it(lst)
    elif isinstance(arr, list):
        for arg in args:
            arr.append(arg)
        count_it(arr)
    elif isinstance(arr, str):
        try:
            arr = [int(i) for i in arr.split(',')]
            count_it(arr)
        except ValueError:
            print("Please enter correct input.")
            return "Please enter correct input."


if __name__ == '__main__':

    descr()
