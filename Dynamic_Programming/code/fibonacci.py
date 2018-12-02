"""Fibonacci support for doing this and that"""
def fibord(nam):
    """Finding a Fibonacci number"""
    try:
        nam = int(nam)
        fib_sum = [0] * (nam + 2)
        fib_sum[0], fib_sum[1] = 1, 1

        for i in range(2, nam+1):
            fib_sum[i] = fib_sum[i-1] + fib_sum[i-2]
            i += 1
        print(fib_sum[nam])
        return fib_sum[nam]

    except ValueError:
        print('Error. The values entered must be greater or equal to 0')
    except IndexError:
        print('Error. The values entered must be greater or equal to 0')

def descr():
    """Reading the Fibonacci sequence number"""
    while True:
        nam = input('Which value of element of the Fibonacci '
                    'sequence do you want to know? n = ')
        nam = nam.lower()
        if nam == 'q':
            print('You have finished working with the Fibonacci function')
            return 'q'

        fibord(nam)
