"""function countingSort that takes an array (of type integer slice, []int)
 as value and sorts it using "Counting Sort" algorithm"""


def counting_sort(data):
    max_number = (max(data))
    min_number = (min(data))
    n = max_number - min_number + 1
# list for counters
    counters = [0] * n
    for v in data:
        counters[v - min_number] += 1
        print(counters)
    result = []
    count = -1
    for i in counters:
        count += 1
        result.extend([count + min_number] * i)

    return result
