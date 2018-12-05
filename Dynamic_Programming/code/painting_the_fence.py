"""
This method finds out the number of ways
of painting with some number of colors
the fence with some number of posts
such that at most 2 adjacent posts have the same color
"""


def descr():
    """Function for to input and verification data"""
    number_posts = input('Please enter a number of posts in range: '
                         '0 <= number < 10000 (e.g. 10): ')

    if number_posts == 'q':
        return 'q'

    try:
        number_posts = int(number_posts)
        if number_posts < 0 or number_posts >= 10000:
            print('Wrong input. Please enter number in range: 0 <= positive integer < 10000')
            return None
    except (TypeError, ValueError, IndexError):
        print('Wrong input. Please enter number in range: 0 <= positive integer < 10000')
        return None

    number_colors = input('Please enter a number of colors in range: ' +
                          '0 <= number < 10000 (e.g. 5): ')

    if number_colors == 'q':
        return 'q'

    try:
        number_colors = int(number_colors)
        print('There are {} ways to paint your fence \
                  '.format(ways_to_paint_fence(number_posts, number_colors)))
        return None
    except (TypeError, ValueError, IndexError):
        print('Wrong input. Please enter number in range: 0 <= positive integer < 10000')


def ways_to_paint_fence(number_posts: int, number_colors: int):
    """
    1) if parameters are not int and <0 raise error;
    2) if posts == 0 or colors == 0, then there are no ways to color it;
    3) if posts == 1, then ways to color it equal to number of colors
    4) if posts == 2, then ways to color it calculate like:
    Ways when both posts have same color: 4
    Ways when both posts have diff color:
    4(choices for 1st post) * 3(choices for 2nd post) = 12
    Then the output must be 4+12= 16
    5) if posts > 2 then ways to color it calculate like:
    total[i] = same[i] + diff[i]
    same[i]  = diff[i-1]
    diff[i]  = (diff[i-1] + diff[i-2]) * (k-1)= total[i-1] * (k-1)
    """
    if not isinstance(number_posts,int):
        raise TypeError('{} is wrong type. Positive int expected'.format(type(number_posts)))
    if not isinstance(number_colors,int):
        raise TypeError('{} is wrong type. Positive int expected'.format(type(number_colors)))
    if 0 <= number_posts < 10000 and 0 <= number_colors < 10000:

        if number_posts == 0:
            return 0

        if number_posts == 1:
            return number_colors

        same = number_colors
        diff = number_colors * (number_colors - 1)

        for _ in range(3, number_posts + 1):
            prev_diff = diff
            diff = (same + diff) * (number_colors - 1)
            same = prev_diff
        return same + diff

    raise ValueError('Wrong value. Please enter number in range: 0 <= positive integer < 10000')
