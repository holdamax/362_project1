"""Fibonacci support for doing this and that"""
def fibord(nam):
    """Finding a Fibonacci number"""
    try:
        if isinstance(nam, int) or nam.isdigit():
            nam = int(nam)
            fib_sum = [0] * (nam + 2)
            fib_sum[0], fib_sum[1] = 1, 1

            for i in range(2, nam+1):
                fib_sum[i] = fib_sum[i-1] + fib_sum[i-2]
                i += 1
            print(fib_sum[nam])
            return fib_sum[nam]
        print('Error. The values entered must be integer and greater or equal to 0')
        return None

    except (IndexError, ValueError, TypeError):
        print('Error. The values entered must be integer and greater or equal to 0')

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
