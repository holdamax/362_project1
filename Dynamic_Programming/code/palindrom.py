"""We find the longest such subsequence using dynamic programming
over intervals within the string. We define the value Opt[i,j]
 for each interval [i,j] as the length of the longest palindromic subsequence"""
def longest_pal(str):
    n = len(str)

    # initialize Opt Table
    Opt = [[0 for i in range(n)] for j in range(n)]

    # Opt of single char is 1
    for i in range(n):
        Opt[i][i] = 1

    # Opt for adjacent chars is 2 if same, 1 otherwise
    for i in range(n - 1):
        if str[i] == str[i + 1]:
            Opt[i][i + 1] = 2
        else:
            Opt[i][i + 1] = 1

        # we now define sil as (s)substring (i)interval (l) length of the
        # interval [i,j] --- sil=(j-i +1) and j = i+sil-1

        # we compute Opt table entry for each sil length and
        # starting index i


    for sil in range(2, n + 1):
        for i in range(n - sil + 1):
            j = i + sil - 1
            if (str[i] == str[j]):
                Opt[i][j] = Opt[i + 1][j - 1] + 2;
            else:
                Opt[i][j] = max(Opt[i][j - 1], Opt[i + 1][j])

    return Opt[0][n - 1]
