"""Python3 implementation to count
ways to sum up to a given value number"""
def descr():
    """Function for to input and verification data"""
    my_list = input('Please, input the array which has to be represented (etc. 1,5,6): ')
    number = input('Please, input the number which has to be represented (etc. 7): ')
    if my_list == 'q' or number == 'q':
        return 'q'
    return ways_to_sum(my_list, number)

def ways_to_sum(my_list=None, number=None):
    """ Function to count the total
    number of ways to sum up to 'number'
    Keyword arguments:
            my_list -- the array which has to be represented (default None)
            number -- the number which has to be represented (default None)"""
    try:
        number = abs(int(number))
        my_list = [abs(int(i)) for i in my_list.split(',')]
        count = [0 for i in range(number + 1)]
        count[0] = 1
        len_my_list = len(my_list)
        for i in range(1, number + 1):
            for j in range(len_my_list):
                if i >= my_list[j]:
                    count[i] += count[i - my_list[j]]

        print("Total number of ways = {}".format(count[number]))
        return count[number]
    except TypeError:
        print('Error! Please, enter correct list and number (etc. 1,5,6 and 7)')
    except ValueError:
        print('Error! Please, enter correct list and number (etc. 1,5,6 and 7)')
    except IndexError:
        print('Error! Please, enter correct list and number (etc. 1,5,6 and 7)')

