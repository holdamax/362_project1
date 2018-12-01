""""count yacobstel number"""
def descr():
    try:
        print("Please input yacobstel number:")
        num = int(input())
        return yakobstelelement(num)
    except:
        print("Only number inputs")

def yakobstelelement (num):

    return int((2**num-(-1)**num)/3)

