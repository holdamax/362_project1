"""
Given a fence with n posts and k colors, find out the number of ways of painting
the fence such that at most 2 adjacent posts have the same color.
Input: Both n and k are positive integers.
Please write first argument - number of posts, second argumet - number of colors!
"""

def find_combinations(post, color):
    """
    :param post int:
    :param color int:
    :return:
    """
    i = 3
    if post <= 0:
        ans = 0
    elif post in range(1, 3):
        ans = color ** post
    elif i <= post:
        same = color
        diff = same * (color - 1)
        for i in range(i, post + 1):
            prdiff = diff
            diff = (same + diff) * (color - 1)
            same = prdiff * 1
        ans = same + diff
    if color > 0:
        pass
    else:
        ans = 0
    if ans == 0:
        raise TypeError('Bad param!')
    else:
        return ans
if __name__ == "__main__":
    C = int(input('How much colors you have? '))
    N = int(input('How much posts you have? '))
    if find_combinations(N, C) == 0:
        print("Okay, Houston, we've had a problem here")
    else:
        print('You have %s ways of painting the fence.' %(find_combinations(N, C)))
