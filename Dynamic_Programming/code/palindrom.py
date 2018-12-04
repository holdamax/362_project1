"""We find the longest such subsequence using dynamic programming
over intervals within the string. We define the value Opt[i,j]
 for each interval [i,j] as the length of the longest palindromic subsequence"""


def longest_pal(inp_str):
    """calculate longest palindrom"""
    len_inp_str = len(inp_str)
    if len_inp_str > 100:
        return "String not more than 100 symbols !"

    # initialize opt Table
    opt = [[0 for i in range(len_inp_str)] for j in range(len_inp_str)]

    # opt of single char is 1
    for i in range(len_inp_str):
        opt[i][i] = 1

    # opt for adjacent chars is 2 if same, 1 otherwise
    for i in range(len_inp_str - 1):
        if inp_str[i] == inp_str[i + 1]:
            opt[i][i + 1] = 2
        else:
            opt[i][i + 1] = 1

        # we now define sil as (s)substring (i)interval (l) length of the
        # interval [i,j] --- sil=(j-i +1) and j = i+sil-1
        # we compute opt table entry for each sil length and
        # starting index i

    for sil in range(2, len_inp_str + 1):
        for i in range(len_inp_str - sil + 1):
            j = i + sil - 1
            if inp_str[i] == inp_str[j]:
                opt[i][j] = opt[i + 1][j - 1] + 2
            else:
                opt[i][j] = max(opt[i][j - 1], opt[i + 1][j])
    print(opt[0][len_inp_str - 1])
    return opt[0][len_inp_str - 1]


def descr():
    while True:
        inp_str = input("Please type something here and we will try to find the longest palindrom:")
        if inp_str == 'q':
            print("That's it.")
            return 'q'
        longest_pal(inp_str)
