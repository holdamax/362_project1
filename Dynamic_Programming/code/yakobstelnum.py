""""count yacobstel number"""


def descr():

    num = int(input(print("Please input yacobstel number:")))
    try:
        return yakobstelelement(num)
    except:
        print("Only number inputs")


def yakobstelelement(num):
    """calculate sequence"""

    return int((2**num-(-1)**num)/3)
