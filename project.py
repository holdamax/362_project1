"""Main project module"""

import os

from Dynamic_Programming.code import *
from Sorting.code import *

TASKS = {'1': fibonacci,
         '2': fibonacci_mod,
         #'3': yakobstelnum,
         '4': longest_sequence,
         '5': ways_to_sum,
         '6': ways_to_write_n_as_sum_of_integers,
         '7': ways_to_cover_in_3_steps,
         '8': paths_without_crossing,
         '9': min_max_afford,
         '10': palindrom,
         '11': friend_pairs,
         '12': ways_tile_floor,
         '13': painting_the_fence,
         '14': optimized_painting_fence,
         '15': insertion,
         '16': countingsort,
         '17': quick_sort,
         '18': bucket_sorting,
         '19': merge_sort
         }

CHOOSE = "Choose task: \n"\
         "\n\tDynamic Programming\n"\
         "1:  Fibonacci\n"\
         "2:  Modified fibonacci\n"\
         "3:  Interesting row\n"\
         "4:  Longest sub-sequence with difference one\n"\
         "5:  Ways to sum to N using array elements with repetition\n"\
         "6:  Ways to write n as sum of two or more positive integers\n"\
         "7:  Ways to cover in 3 steps\n"\
         "8:  Paths without crossing\n"\
         "9:  Work to be with High-effort or with Low-effort\n"\
         "10: The longest palindromic sub-sequence\n"\
         "11: Friend pairs\n"\
         "12: Ways to tile the floor\n"\
         "13: Painting the fence\n"\
         "14: Optimized painting fence: use one variable instead of a table\n"\
         "\n\tSorting\n"\
         "15: Insertion sort\n"\
         "16: Counting sort\n"\
         "17: Quick sort\n"\
         "18: Bucket sort\n"\
         "19: Merge sort\n"\
         "\nq: back\n"


def cls(): os.system('cls')


cls()
while True:
    cls()
    print(CHOOSE)
    TASK_N = input("Input task number: ")
    if TASK_N == "q":
        cls()
        break
    try:
        while True:
            RESULT = TASKS[TASK_N].descr()
            if RESULT == 'q' or RESULT is not None:
                break

    except KeyError:
        print("Wrong task number")
