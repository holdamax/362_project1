"""Insertion sort"""
def insertion_sort(array):
    """Function that is intended for sorting"""
    try:
        array = array.split(',')
        array = [(int(i)) for i in array]

        for i in range(1, len(array)):
            k = array[i]
            j = i - 1
            while j >= 0 and k < array[j]:
                array[j + 1] = array[j]
                j -= 1
            array[j + 1] = k

        for i, _ in enumerate(array):
            print(array[i])
        return array

    except (IndexError, ValueError, TypeError, AttributeError):
        print('Error. The values entered must be a integer numbers(etc. 12, 11, 13, 5, 6)')

def descr():
    """Reading a numbers for sorting"""
    while True:
        array = input('Input the array which you need to sort (etc. 12, 11, 13, 5, 6): ')

        if 'q' in array or 'Q' in array:
            print('You have finished working with the sorting function')
            return 'q'

        insertion_sort(array)
