"""Fibonacci support for doing this and that"""

def fibord(nam):
    """Finding a Fibonacci number"""
    if nam.isdigit():
        nam = int(nam)
        fib_sum, fib1, fib2 = 0, 1, 2

        if nam in (0, 1):
            fib_sum = fib1
        if nam == 2:
            fib_sum = fib2

        for i in range(3, nam+1):
            fib_sum = fib2 + fib1
            fib1, fib2 = fib2, fib_sum
            i += 1
        print(fib_sum)
    else:
        print('Error. The values entered must be greater than or equal to 0')
def descr():
    """Reading the Fibonacci sequence number"""
    while True:
        nam = input('Which value of element of the Fibonacci '
                    'sequence do you want to know? n = ')
        nam = nam.lower()
        if nam == 'q':
            print('B')
            break
        else:
            fibord(nam)
