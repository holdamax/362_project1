# Function to find the length of longest subsequence

def longestSubseqWithDiffOne(arr, n):
    dp = [1 for i in range(n)]
    arr = sorted(arr)

    for i in range(n):
        for j in range(i):
            if ((arr[i] == arr[j] + 1) or (arr[i] == arr[j] - 1)):
                dp[i] = max(dp[i], dp[j] + 1)

                # Longest length will be the maximum value of dp array.
    result = 1
    for i in range(n):
        if (result < dp[i]):
            result = dp[i]
    print(result)
    return result


if __name__ == '__main__':
    # Driver code
    arr = [3, 4, 5, 6, 7, 8, 9]
    # Longest subsequence with one difference is
    # {1, 2, 3, 4, 3, 2}
    n = len(arr)
    print
    longestSubseqWithDiffOne(arr, n)
