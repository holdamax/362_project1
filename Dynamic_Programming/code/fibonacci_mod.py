"""Implementing task 2.
Find which is the member of position n
 in Modification Fibonacci sequence.
"""


def descr():
    """Description function for checking inputs"""
    while True:
        try:
            size = input("Please input position of fibonacci number: ")
            if size == 'q':
                print('You have finished working with the Fibonacci mod function')
                return 'q'
            print(fibo(int(size)))
        except (TypeError, ValueError, RecursionError):
            print("Wrong inputs. Input one positive integer number.")


def fibo(size):
    """Calculate Modified Fibonacci number."""
    if size in (1, 2, 3):
        return 1
    return fibo(size-1) + fibo(size-3)
