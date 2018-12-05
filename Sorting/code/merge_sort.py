"""
function mergeSort takes an array (of type integer slice, []int)
as value and sorts it using "Merge Sort" algorithm.
"""


def descr():

    """Function for to input and verification data"""

    while True:
        alista = input('\nPlease, input the list of positive integers, or "q" for exit '
                       'which has to be checked (e.g. 3, 4, 5, 7, 8, 9): ')
        if alista == 'q':
            print('Bye')
            return 'q'
        print(check(alista))


def check(alist):
    """check inputs and call 'mergeSort' algorithm"""

    try:
        alist = [int(i) for i in alist.split(',')]
        sizealist = len(alist)
        print(f"Using list {alist}...")
        return(mergesort(alist, sizealist))


    except(TypeError, ValueError):
        print("Please enter correct input.")


def mergesort(alist, sizealist):
    """"
    "Merge Sort" algorithm
    """
    if len(alist) > 1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]
        if sizealist <= 16:
            print('Left: ', lefthalf, ' Rigt: ', righthalf)

        mergesort(lefthalf, sizealist)
        mergesort(righthalf, sizealist)
        i = j = k = 0

        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i += 1
            else:
                alist[k] = righthalf[j]
                j += 1
            k += 1

        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i += 1
            k += 1

        while j < len(righthalf):
            alist[k] = righthalf[j]
            j += 1
            k += 1
    return alist


if __name__ == '__main__':

    descr()
