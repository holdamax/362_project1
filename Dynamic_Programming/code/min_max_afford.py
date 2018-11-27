"""Implementing task 9.
Work to be with High-effort or with Low-effort.
"""


def max_afford(low, high, days):
    """Calculate Max afford with given value of work by days."""
    if days <= 0:
        return 0
    return max(high[days-1] + max_afford(low, high, (days-2)),
               low[days-1] + max_afford(low, high, (days-1)))
