"""
Given a fence with n posts and k colors, find out the number of ways of painting
the fence such that at most 2 adjacent posts have the same color.
Input: Both n and k are positive integers.
Please write first argument - number of posts, second argumet - number of colors!
"""
def descr():
    """Function for to input and verification data"""
    try:
        posts = int(input('Please, input number of posts: '))
        colors = int(input('Please, input number of colors: '))
        return find_combinations(posts, colors)
    except:
        print('Error! Please, enter correct size (etc. 2 and 3)')

def find_combinations(post: int , color: int):
    """
    param post int: number of posts in fence
    param color int: number of colors for painting
    return: number of ways for painting the fence
    """
    same = color
    diff = same * (color - 1)
    i = 3
    if post and color <= 0:
        raise TypeError('Bad param!')
    elif post in range(1, i):
        return color ** post
    elif i <= post:

        for _ in range(i, post + 1):
            prdiff = diff
            diff = (same + diff) * (color - 1)
            same = prdiff * 1
    return same + diff

if __name__ == "__main__":
    C = int(input('How much colors you have? '))
    N = int(input('How much posts you have? '))
    if find_combinations(N, C) == 0:
        print("Okay, Houston, we've had a problem here")
    else:
        print('You have %s ways of painting the fence.' %(find_combinations(N, C)))
