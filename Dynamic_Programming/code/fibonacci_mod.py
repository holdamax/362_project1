"""Implementing task 2.
Find which is the member of position n
 in Modification Fibonacci sequence.
"""


def descr():
    """Description function for checking inputs"""
    try:
        size = input("Please input position of fibonacci number in range from 0 to 45.")
        if size == 'q':
            print("You have finished working with the Fibonacci mod function")
            return 'q'
        print(fibo(int(size)))
        return None
    except (TypeError, ValueError, RecursionError):
        print("Wrong inputs. Input one positive integer number in range from 0 to 45.")


def fibo(size: int):
    """Calculate Modified Fibonacci number."""
    if size > 45:
        print("Wrong inputs. Calculating will take too much time, input number in range from 0 to 45.")
        return None
    if size in (1, 2, 3):
        return 1
    return fibo(size-1) + fibo(size-3)

