#!/usr/bin/env python
"""Friend pairs.

For a group of n friends, let f(n) be the number of ways how they can be paired up or remain single.
Then either the n-th person remains single, or paired up.
If the n-th person is single, then we recur for (n - 1) friends.
If the n-th person is paired up with any of the remaining (n-1) person, then, we recur (n-1)*f(n-2).
"""
import os


def cls():
    """Clear screen."""
    os.system('cls')


def descr():
    """Entry point function for the menu app."""
    cls()
    while True:
        choice = input(
            '\n>>> Please enter integer positive number of friends or X, if you want to exit: ')
        choice = choice.lower()

        if choice == 'q':
            print('Bye\n')
            cls()
            return choice
        if choice == 'c':
            cls()
        else:
            itr(choice)


def itr(n: str):
    """Count all possible pairings.

    Function takes in number of friends and outputs the total number of ways in which friends
    can remain single or can be paired up.

    Parameters
    ----------
    n : str     number of friends

    Returns
    -------
    f(n) = f(n-1) + (n-1) * f(n-2)
        total number of ways in which friends can remain single or can be paired up.

    """
    if n.isdigit():
        n = int(n)
        if n == 0:
            result = 0
        elif n == 1:
            result = 1
        elif n >= 2:
            result, f_1, f_2 = 0, 1, 1

            for i in range(2, n + 1):
                result = f_1 + (i - 1) * f_2
                f_2, f_1 = f_1, result
        cls()
        print(f"Number of ways to pair {n} friends is:\t {result}")
        return result
    else:
        return "You gave wrong input. Try again."


if __name__ == '__main__':

    descr()
