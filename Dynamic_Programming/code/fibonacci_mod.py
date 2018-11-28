"""Implementing task 2.
Find which is the member of position n
 in Modification Fibonacci sequence.
"""


def descr():
    size = input("Please input position of fibonacci number: ")
    try:
        return fibo(int(size))
    except:
        print("Wrong inputs. Input one positive integer number.")


def fibo(size):
    """Calculate Modified Fibonacci number."""

    if size < 1:
        raise TypeError
    if size in (1, 2, 3):
        return 1
    return fibo(size-1) + fibo(size-3)
