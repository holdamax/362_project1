"""
Given a fence with n posts and k colors, find out the number of ways of painting
the fence such that at most 2 adjacent posts have the same color.
Input: Both n and k are positive integers.
Please write first argument - number of posts, second argumet - number of colors!
"""


def descr():
    """
    Function for to input and verification data
    """
    while True:
        posts = input('Please, input number of posts: ')
        colors = input('Please, input number of colors: ')
        if posts == 'q' or colors == 'q':
            return 'q'
        print(find_combinations(posts, colors))


def find_combinations(post: int, color: int):
    """
    param post int: number of posts in fence
    param color int: number of colors for painting
    return: number of ways for painting the fence
    """

    try:
        post, color = (int(post), int(color))
        same = color
        diff = same * (color - 1)
        i = 3
        if post > 99 or color > 99:
            return "please, choose lesser numm"
        if post <= 0 or color <= 0:
            raise TypeError

        if post in range(1, i):
            return color ** post

        if i <= post:

            for _ in range(i, post + 1):
                prdiff = diff
                diff = (same + diff) * (color - 1)
                same = prdiff

        print("total number of ways of painting the fence: %s" % (same + diff))
        return same + diff

    except (TypeError, ValueError):
        return 'Error! Please, enter positive numbers (etc. 2 and 3)'


if __name__ == '__main__':

    descr()
