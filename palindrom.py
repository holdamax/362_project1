def palindrommax(string):
    n = len(string)
    arr = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        arr[i][i] = 1
    for length in range(2, n + 1):
        for i in range(0, n - length + 1):
            j = i + length - 1
            if string[i] == string[j] and length == 2:
                arr[i][j] = 2
            elif string[i] == string[j]:
                arr[i][j] = 2 + arr[i + 1][j - 1]
            else:
                arr[i][j] = max(arr[i + 1][j], arr[i][j - 1])

    return arr[0][n - 1]

