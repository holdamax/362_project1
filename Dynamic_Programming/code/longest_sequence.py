#!/usr/bin/env python
"""Function to find the length of longest sequence with difference one."""


def descr():
    """Entry point function for the menu app."""
    try:
        in_list = input('Please, input the list of positive integers, '
                        'which has to be checked (e.g. 1, 5, 6 and 7): ')
        if in_list == '':
            in_list=[3, 4, 7, 8, 9]
        else:
            in_list = [int(i) for i in in_list.split(',')]
            print(in_list)
        return longest_seq_with_diff_one(in_list)
    except ValueError:
        print('Please enter correct input.')


def longest_seq_with_diff_one(arr):
    """Find longest sequence of numbers with difference one."""
    arr_1 = [1 for _ in range(len(arr))]
    arr = sorted(arr)

    for i in range(len(arr)):
        for j in range(i):
            if ((arr[i] == arr[j] + 1) or (arr[i] == arr[j] - 1)):
                arr_1[i] = max(arr_1[i], arr_1[j] + 1)

                # Longest length will be the maximum value of dp array.
    result = 1
    for i in range(len(arr)):
        if result < arr_1[i]:
            result = arr_1[i]
    print(f"Longest sequence of numbers with difference 1 is: {result}\n")
    return result


if __name__ == '__main__':

    descr()
