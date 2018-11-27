"""Implemente task 2."""


def fibo(size):
    """Calculate Modified Fibonacci."""
    if size in (1, 2, 3):
        return 1
    return fibo(size-1) + fibo(size-3)

print(fibo(22))