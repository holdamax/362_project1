"""Implementing task 9.
Work to be with High-effort or with Low-effort.
"""


def descr():
    try:
        print("Please input number of days and two lists of affords: ")
        days_in = input("Number of days: ")
        low_in = input("Low afford: ")
        low_in = [int(i) for i in low_in.split(",")]
        high_in = input("High afford: ")
        high_in = [int(i) for i in high_in.split(",")]
        return max_afford(low_in, high_in, int(days_in))
    except:
        print("Wrong inputs. Input only positive integer numbers.")


def max_afford(low, high, days):
    """Calculate Max afford with given value of work by days."""
    try:
        if days <= 0:
            return 0
        return max(high[days-1] + max_afford(low, high, (days-2)),
                   low[days-1] + max_afford(low, high, (days-1)))
    except TypeError:
        print("Wrong inputs")