from math import factorial


def catalanNumbrs(n):
    try:
        if not n % 2:
            return round(factorial(n)/(factorial((n/2+1))*factorial(n/2)))
    except (TypeError, ValueError):
        print('You used wrong value, please use positive, even and integer value.\n')


if __name__ == '__main__':
    catalan = int(input('Please enter positive, even and integer value... '))
    print(catalanNumbrs(catalan))
