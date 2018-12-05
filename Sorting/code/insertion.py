"""Insertion sort"""
def insertion_sort(array):
    """Function that is intended for sorting"""
    array = array.split(',')
    array = [(int(i)) for i in array]

    for i in range(1, len(array)):
        k = array[i]
        j = i - 1
        while j >= 0 and k < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = k

    return array


def descr():
    """Reading a numbers for sorting"""
    try:
        array = input('Input the array which you need to sort (etc. 12, 11, 13, 5, 6): ')

        if 'q' in array or 'Q' in array:
            print('You have finished working with the sorting function')
            return 'q'

        print(insertion_sort(array))
        return None

    except (ValueError, TypeError, AttributeError):
        print('Error. The values entered must be a integer numbers(etc. 12, 11, 13, 5, 6)')
