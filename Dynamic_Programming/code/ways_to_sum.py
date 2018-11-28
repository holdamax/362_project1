"""Python3 implementation to count
ways to sum up to a given value N"""
def descr():
    """Function for to input and verification data"""
    try:
        my_list = input('Please, input the array which has to be represented: ')
        my_list = [int(i) for i in my_list.split(',')]
        number = int(input('Please, input the number which has to be represented: '))
        return ways_to_sum(my_list, number)
    except:
        print('Error! Please, enter correct list and number (etc. 1,5,6 and 7)')

def ways_to_sum(my_list=None, number=None):
    """ Function to count the total
    number of ways to sum up to 'number'
    Keyword arguments:
            my_list -- the array which has to be represented (default None)
            number -- the number which has to be represented (default None)"""
    count = [0 for i in range(number + 1)]
    count[0] = 1
    len_my_list = len(my_list)
    for i in range(1, number + 1):
        for j in range(len_my_list):
            if i >= my_list[j]:
                count[i] += count[i - my_list[j]]

    print("Total number of ways = ", end='')
    return count[number]
