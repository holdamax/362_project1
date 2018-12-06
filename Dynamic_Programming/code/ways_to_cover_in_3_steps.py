""" Ways to cover in 3 steps"""
def count_ways(nam):
    """Function for searching count ways"""
    nam = int(nam)
    res = [0] * (nam + 3)
    res[0], res[1], res[2] = 1, 1, 2

    for i in range(3, nam + 1):
        res[i] = res[i - 1] + res[i - 2] + res[i - 3]
        i += 1
    return res[nam]


def descr():
    """Reading a numbers for searching count ways"""
    try:
        nam = input('What distance do you want to cover '
                    'with 1, 2 and 3 steps? n = ')
        nam = nam.lower()

        if nam == 'q':
            print('You have finished working with the searching count ways')
            return 'q'

        print(count_ways(nam))
        return None

    except (IndexError, ValueError):
        print('Error. The values entered must be integer and greater or equal to 0')
