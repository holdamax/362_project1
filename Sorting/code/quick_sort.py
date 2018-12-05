"""Quick sorting with python """


def descr():
    """Function for to input and verification data"""
    alist = input('Please enter list of numbers to sort like: 5, 4, 3, 2, 1 \n')
    alist = list(map(int, alist.split(',')))
    if alist == 'q':
        return 'q'
    try:
        quicksort(alist)
        print("Sorted list looks like: {}".format(alist))
    except (TypeError, ValueError, IndexError):
        print('Wrong input. Please enter list of numbers like: 5, 4, 3, 2, 1 ')
    return None


def quicksort(alist: list):
    quicksort_helper(alist,0,len(alist)-1)


def quicksort_helper(alist,first,last):
    if first<last:
        splitpoint = partition(alist,first,last)
        quicksort_helper(alist,first,splitpoint-1)
        quicksort_helper(alist,splitpoint+1,last)


def partition(alist,first,last):
    pivotvalue = alist[first]

    leftmark = first+1
    rightmark = last

    done = False
    while not done:

       while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = alist[leftmark]
           alist[leftmark] = alist[rightmark]
           alist[rightmark] = temp

    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp
    return rightmark
