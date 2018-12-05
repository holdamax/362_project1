"""function countingSort that takes an array (of type integer slice, []int)
 as value and sorts it using "Counting Sort" algorithm"""


def counting_sort(data):
<<<<<<< HEAD

    member_list=[]
    for i in data.split(','):
        member_list.append(int(i))
    max_number = (max(member_list))
    min_number = (min(member_list))
    n = max_number - min_number + 1
    # list for counters
    counters = [0] * n
    for v in member_list:
=======
    dat = data.split()
    max_number = (max(dat))
    min_number = (min(dat))
    n = max_number - min_number + 1
    # list for counters
    counters = [0] * n
    for v in dat:
>>>>>>> 8c2cb2f1afad067f87023cd51510afef770cef2c
        counters[v - min_number] += 1
    result = []
    count = -1
    for i in counters:
        count += 1
        result.extend([count + min_number] * i)
    print(result)
    return result
counting_sort('1,2,3,7')
def descr():
    """Entry point function for the menu app."""
    while True:
        data = input("Please type list of integers and i sort it:")
        if data == 'q':
            print("That's it.")
            return 'q'
        counting_sort(data)
