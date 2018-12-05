"""We find the longest such subsequence using dynamic programming
over intervals within the string. We define the length of the longest
 palindromic subsequence"""


def longest_pal(inp):
    """calculating longest palindrom"""
    inp_str = str(inp)
    if len(inp_str) >= 100:
        return 'String should not be longer than 100 characters.'
    if len(inp_str) == 0 or inp_str == '':
        return str(len(inp_str)) + "\n" + inp_str
    if inp_str == inp_str[::-1]:
        return str(len(inp_str)) + "\n" + inp_str
    for i in range(len(inp_str)-1, 0, -1):
        for j in range(len(inp_str)-i+1):
            temp = inp_str[j:j+i]
            if temp == temp[::-1]:
                print(str(len(temp)) + "\n" + temp)
                return str(len(temp)) + "\n" + temp


def descr():
    while True:
        inp = input("Please type something here and we will try to find the longest palindrom:")
        if inp == 'q':
            print("That's it.")
            return 'q'
        longest_pal(inp)


if __name__ == '__main__':

    descr()
