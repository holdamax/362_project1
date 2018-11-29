"""
This method finds out the number of ways
of painting with some number of colors
the fence with some number of posts
such that at most 2 adjacent posts have the same color
"""


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
    if isinstance(number_posts, int) and isinstance(number_colors, int) \
            and number_posts >= 0 and number_colors >= 0:

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

    return 'Please enter data like (posts, colors). E.g. (5,2)'


def descr(posts, colors):
    try:
        print(ways_to_paint_fence(int(posts), int(colors)))
    except TypeError:
        print('Please enter positive integer > 0')
    except ValueError:
        print('Please enter positive integer > 0')


descr(input('Please enter a number of posts (e.g. 40):'), input('Please enter a number of colors (e.g. 40):'))