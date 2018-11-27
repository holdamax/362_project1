"""Implementing task 2.
Find which is the member of position n
 in Modification Fibonacci sequence.
"""


def fibo(size):
    """Calculate Modified Fibonacci number."""
    if size in (1, 2, 3):
        return 1
    return fibo(size-1) + fibo(size-3)
