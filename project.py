"""Main project module"""
from Dynamic_Programming.code import *

TASKS = {'2': fibonacci_mod,
         '5': ways_to_sum,
         '8': paths_without_crossing,
         '9': min_max_afford,
         '14': optimized_painting_fence}

print("Choose task: \n"
      "1:  Fibonacci\n"
      "2:  Modified fibonacci\n"
      "3:  Intresting row\n"
      "4:  Longest subsequence with difference one\n"
      "5:  Ways to sum to N using array elements with repetition\n"
      "6:  Ways to write n as sum of two or more positive integers\n"
      "7:  Ways to cover in 3 steps\n"
      "8:  Paths without crossing\n"
      "9:  Work to be with High-effort or with Low-effort\n"
      "10: The longest palindromic subsequence\n"
      "11: Friend pairs\n"
      "12: Ways to tile the floor\n"
      "13: Painting the fence\n"
      "14: Optimized painting fence: use one variable instead of a table\n"
      "q: back")
while True:
    TASK_N = input("Input task number: ")
    if TASK_N == "q":
        break
    try:
        while True:
            RESULT = TASKS[TASK_N].descr()
            if RESULT == 'q' or RESULT is not None:
                break

    except KeyError:
        print("Wrong task number")
