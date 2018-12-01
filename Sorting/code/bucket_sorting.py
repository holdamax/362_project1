import random

def bucket_sorting(lst):
    max_value = max(lst)
    min_value = min(lst)
    buckets = list()
    for bucket in range(len(lst)):
        buckets.append(list())

    for item in lst:
        bucket = int(((item - min_value) / (max_value - min_value + 1)) * len(lst))
        buckets[bucket].append(item)

    for bucket in buckets:
        if len(bucket) > 1:
            buckets[buckets.index(bucket)] = bucket_sorting(bucket)

    return buckets


print(bucket_sorting(random.sample(range(1, 100000), 10000)))
