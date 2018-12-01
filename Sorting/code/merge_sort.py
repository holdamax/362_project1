"""function mergeSort takes an array (of type integer slice, []int) as value and sorts it using "Merge Sort" algorithm."""

def descr():
    """Function for to input and verification data"""
    while True:
        alista = input('\nPlease, input the list of positive integers, or "q" for exit '
                        'which has to be checked (e.g. 3, 4, 5, 7, 8, 9): ')
        if alista == 'q':
            print('Bye')
            return alista
        print(check(alista))

def check(alist):
    """check inputs and call 'mergeSort' algorithm"""
    try:
        if alist == '':
            alist = [3, 4, 5, 7, 8, 9]
            print(f"Using default list {alist}...")
        else:
            alist = sorted([int(i) for i in alist.split(',')])
            print(f"Using list {alist}...")
        print(mergeSort(alist))
    except:
        print("Please enter correct input.")

def mergeSort(alist):
    """"
    "Merge Sort" algorithm
    """
    try:

        if len(alist)>1:
            mid = len(alist)//2
            lefthalf = alist[:mid]
            righthalf = alist[mid:]

            print('Left: ', lefthalf, ' Rigt: ', righthalf)

            mergeSort(lefthalf)
            mergeSort(righthalf)
    except:
        print("Please enter correct input.")

if __name__ == '__main__':

    descr()


