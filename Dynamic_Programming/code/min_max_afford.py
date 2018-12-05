"""Implementing task 9.
Work to be with High-effort or with Low-effort.
"""


def descr():
    """Description function for checking inputs"""
    while True:
        try:
            print("Please input number of days and two lists of affords: ")
            days_in = input("Number of days: ")
            if days_in == 'q':
                print('You have finished working with the Fibonacci mod function')
                return 'q'
            days_in = int(days_in)
            if days_in > 45:
                print("Sorry, number is too big. Calculating will take too much time.")
                continue
            if days_in <= 0:
                raise TypeError
            low_in = input("Low afford: ")
            low_in = [int(i) for i in low_in.split(",")]
            high_in = input("High afford: ")
            high_in = [int(i) for i in high_in.split(",")]
            if len(low_in) != days_in or len(high_in) != days_in:
                raise IndexError
            print(max_afford(low_in, high_in, days_in))
        except (TypeError, ValueError):
            print("Wrong inputs. Input only positive integer numbers.")
        except IndexError:
            print("Wrong inputs. Number of affords should be equal to number of days.")


def max_afford(low: list, high: list, days: int):
    """Calculate Max afford with given value of work by days."""
    try:
        if days <= 0:
            return 0
        if len(low) != days or len(high) != days:
            raise IndexError
        return max(high[days-1] + max_afford(low, high, (days-2)),
                   low[days-1] + max_afford(low, high, (days-1)))
    except (TypeError, ValueError):
        print("Wrong inputs. Input only positive integer numbers.")
    except IndexError:
        print("Wrong inputs. Number of affords should be equal to number of days.")
