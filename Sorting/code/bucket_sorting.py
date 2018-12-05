"""Bucket Sorting.

Task: write the function bucketSort which sorts an array using "Bucket Sort" algorithm and the function ms_bits.
The function bucketSort takes an array (of type integer slice, []int) as first input value and
a function as second input value.
The function ms_bits takes an array (of type integer slice, []int) as first input value,
some element (of type int) of this array as second input value and
returns number (of type int) of bucket to put this element.

Use "Bucket Sort" to sort all buckets.
"""


def bucket_sorting(lst: (list, str)):
    """Bucket sorting.

    Functions sort list in bucket sorting

    Parameters
    ----------
    lst : list     unsorted list

    Returns
    -------
    lst : list     sorted list.

    """
    buckets = list()
    result = list()
    if isinstance(lst, str):
        lst = list(map(int, lst.split()))
    for bucket in range(len(lst)):
        buckets.append(list())
    i = 1
    for item in lst:
        if isinstance(item, float):
            raise ValueError
        num_bucket = ms_bits(lst, item)
        if ([item] in buckets) and (lst.count(item) == len(lst)):
            buckets[num_bucket + i].append(item)
            i += 1
        else:
            buckets[num_bucket].append(item)

    for bucket in buckets:
        if len(bucket) > 1:
            result.extend(bucket_sorting(bucket))
        elif len(bucket) == 1:
            result.extend(bucket)
    return result


def ms_bits(lst: list, item: int):
    """Calculate number of bucket.

    Parameters
    ----------
    lst : list     unsorted list
    item : int     Integer value from lst

    Returns
    -------
    : int     number ob bucket.

    """
    max_value = max(lst)
    min_value = min(lst)
    return int(((item - min_value) / (max_value - min_value + 1)) * len(lst))


def descr():
    """Entry point function for the menu app."""
    inpt = input('\nPlease enter array in format \"1 3 4 5 6 33 44"...\n'
                 'Or \'q\' to back to the menu ... ')
    if inpt.lower() == 'q':
        return 'q'
    try:
        result = bucket_sorting(inpt)
        print(result)
        return None
    except TypeError:
        print('Error: Please enter an array')
        return None
    except ValueError:
        print('Error: Please enter only integer values')
        return None


if __name__ == '__main__':
    descr()
