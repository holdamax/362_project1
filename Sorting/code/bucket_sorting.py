import random
"""
Task: write the function bucketSort which sorts an array using "Bucket Sort" algorithm and the function msBits.
The function bucketSort takes an array (of type integer slice, []int) as first input value and 
a function as second input value.
The function msBits takes an array (of type integer slice, []int) as first input value, 
some element (of type int) of this array as second input value and 
returns number (of type int) of bucket to put this element.

Use "Bucket Sort" to sort all buckets.
"""
def bucket_sorting(lst):
    if isinstance(lst, list):
        buckets = list()
        result = list()
        for bucket in range(len(lst)):
            buckets.append(list())
        i = 1
        for item in lst:
            num_bucket = msBits(lst, item)
        #     num_bucket = int(((item - min_value) / (max_value - min_value + 1)) * len(lst))
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
    print('Please enter an array of integer numbers')

def msBits(lst, item):
    """

    :param lst: List of integer values
    :param item: Integer value from lst
    :return: Integer number ob bucket
    """
    try:
        if item in lst:
            max_value = max(lst)
            min_value = min(lst)
            return int(((item - min_value) / (max_value - min_value + 1)) * len(lst))
        print('value should be in the list')
    except TypeError:
        print('Type error')



def descr():
    """
    Input list
    Calls paths_without_crossing function
    :Returns:
    Sorted list
    """
    inpt = input('\nPlease enter array in format \"1 3 4 5 6 33 44"...\n'
                 'Or \'q\' to back to the menu ... ')
    if inpt.lower() == 'q':
        return 'q'

    inpt = inpt.split()
    lst = list(map(int,inpt))
    result = bucket_sorting(lst)
    print(result)
    return result


if __name__ == '__main__':
    descr()
