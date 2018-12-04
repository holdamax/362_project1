""""countwhich is the member of position num
         in Yacobstel sequence"""


def yakobstelelement(num):
    """calculate sequence"""
    if num.isdigit():
        num = int(num)
        print(int((2**num-(-1)**num)/3))
        return int((2**num-(-1)**num)/3)

    else:
        print('Error. The values entered must be integer')         
        return 'Error. The values entered must be integer'


def descr():
    while True:
        num = input("Please input yacobstel number:")
        if num == 'q':
            print('You have finished working with the interesting row function')
            return 'q'

        yakobstelelement(num)
