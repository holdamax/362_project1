"""function mergeSort takes an array (of type integer slice, []int) as value and sorts it using "Merge Sort" algorithm."""


def descr():
    """Function for to input and verification data"""
    while True:
        alista = input('\nPlease, input the list of positive integers, or "q" for exit '
                       'which has to be checked (e.g. 3, 4, 5, 7, 8, 9): ')
        if alista == 'q':
            print('Bye')
            return 'q'
        print(check1(alista))


def check1(alist):
    """check inputs and call 'mergeSort' algorithm"""
    try:

        alist = [int(i) for i in alist.split(',')]
        sizealist = len(alist)
        print(f"Using list {alist}...")
        print(mergesort_16(alist, sizealist))
    except:
        print("Please enter correct input.")


def mergesort_16(alist, sizealist):
    """"
    "Merge Sort" algorithm
    """
    try:

        if len(alist)>1:
            mid = len(alist)//2
            lefthalf = alist[:mid]
            righthalf = alist[mid:]
            if sizealist <= 16:
                print('Left: ', lefthalf, ' Rigt: ', righthalf)

            mergesort_16(lefthalf, sizealist)
            mergesort_16(righthalf, sizealist)
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

    except:
        print("Please enter correct input.")


if __name__ == '__main__':

    descr()
