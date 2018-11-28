#!/usr/bin/env python
"""Friend pairs.

For a group of n friends, let f(n) be the number of ways how they can be paired up or remain single.
Then either the n-th person remains single, or paired up.
If the n-th person is single, then we recur for (n - 1) friends.
If the n-th person is paired up with any of the remaining (n-1) person, then, we recur (n-1)*f(n-2).
"""

def itr(n):
    """Count all possible pairings.

    Funtion takes in number of friends and outputs the total number of ways in which friends
    can remain single or can be paired up.

    Parameters
    ----------
    n : number of friends

    Returns
    -------
    f(n) = f(n-1) + (n-1) * f(n-2)
        total number of ways in which friends can remain single or can be paired up.

    """
    if n.isdigit() and int(n) >= 0:
        n = int(n)
        if n == 0:
            fn = 0
        elif n == 1:
            fn = 1
        elif n >= 2:
            fn, f1, f2 = 0, 1, 1

            for i in range(2, n + 1):
                fn = f1 + (i - 1) * f2
                f2, f1 = f1, fn

        print("Number of ways to pair {0} friends is: {1}\n".format(n, fn))
        return fn
    else:
        print("You gave wrong input. Try again.\n")
        return None


if __name__ == '__main__':

    while True:
        choice = input(
            '>>> Please enter integer positive number of friends or X, if you want to exit: ')

        if choice == 'x':
            print('Bye')
            break
        else:
            itr(choice)
